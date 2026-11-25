"""Evaluate a trusted release policy against a count-only evidence record."""

import argparse
import json
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

import yaml


KIT = Path(__file__).resolve().parent
BASE_METRICS = {
    "severe_toxicity", "unsupported_material_claim", "atlas_instruction_boundary",
    "atlas_tool_authorization", "atlas_retrieval_access", "tenant_isolation",
    "egress_containment", "audit_delivery", "human_release", "perimeter_controls",
}
DEMO_CANDIDATE = "sha256:" + "cd" * 32
DEMO_SUITE = "sha256:" + "babe" * 16


def unique_mapping(pairs):
    result = {}
    for key, value in pairs:
        if not isinstance(key, str) or key in result:
            raise ValueError("expected unique string keys")
        result[key] = value
    return result


class PolicyLoader(yaml.SafeLoader):
    """Reject duplicate mapping keys in a protected YAML configuration."""


def yaml_mapping(loader, node):
    return unique_mapping(loader.construct_pairs(node, deep=True))


PolicyLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, yaml_mapping)


def read_record(path):
    with path.open("rb") as source:
        data = source.read(65537)
    if len(data) > 65536:
        raise ValueError("input exceeds the 64 KiB aggregate-record limit")
    return data.decode("utf-8")


def fields(record, required, where):
    if not isinstance(record, dict) or set(record) != set(required):
        raise ValueError(f"{where} has missing or unexpected fields")


def whole(value, minimum, maximum, where):
    if type(value) is not int or not minimum <= value <= maximum:
        raise ValueError(f"{where} must be a whole number between {minimum} and {maximum}")
    return value


def evaluate(policy, evidence, *, kind, candidate, suite, scope, now):
    fields(policy, ["schema", "policy_id", "max_evidence_age_hours", "metrics"], "release policy")
    if policy["schema"] != "scaleai.release-policy.v1" or not isinstance(policy["policy_id"], str) or not policy["policy_id"]:
        raise ValueError("invalid release policy version or identifier")
    hours = whole(policy["max_evidence_age_hours"], 1, 8760, "policy evidence age in hours")
    rules = policy["metrics"]
    if not isinstance(rules, dict) or not BASE_METRICS.issubset(rules):
        raise ValueError("release policy omits a mandatory metric")

    fields(evidence, ["schema", "kind", "scope", "candidate_digest", "suite_digest", "completed_at", "metrics"], "evidence")
    if evidence["schema"] != "scaleai.release-evidence.v1" or evidence["kind"] != kind:
        raise ValueError("wrong evidence version or kind")
    for field, expected in [("candidate_digest", candidate), ("suite_digest", suite)]:
        if not re.fullmatch(r"sha256:[0-9a-f]{64}", expected) or evidence[field] != expected:
            raise ValueError(f"{field} differs from the expected SHA-256 identity or has an invalid format")
    scope_segment = r"[A-Za-z0-9][A-Za-z0-9._-]{0,62}"
    if not re.fullmatch(f"{scope_segment}/{scope_segment}", scope) or evidence["scope"] != scope:
        raise ValueError("deployment scope is invalid or differs from the requested scope")
    stamp = evidence["completed_at"]
    if not isinstance(stamp, str) or not re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z", stamp):
        raise ValueError("completed_at must use zero-padded UTC YYYY-MM-DDTHH:MM:SSZ")
    completed = datetime.strptime(stamp, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
    if not timedelta(0) <= now - completed <= timedelta(hours=hours):
        raise ValueError("evaluation timestamp falls outside the approved evidence window")

    fields(evidence["metrics"], rules, "evidence metrics")
    failures = []
    for name, rule in rules.items():
        fields(rule, ["min_total", "max_failed_basis_points"], f"{name} policy")
        minimum = whole(rule["min_total"], 1, 2**63 - 1, f"{name} minimum")
        cap = whole(rule["max_failed_basis_points"], 0, 10000, f"{name} basis-point limit")
        data = evidence["metrics"][name]
        fields(data, ["failed", "total"], f"{name} result")
        total = whole(data["total"], 1, 2**63 - 1, f"{name} sample count")
        failed = whole(data["failed"], 0, total, f"{name} failure count")
        if total < minimum or failed * 10000 > cap * total:
            failures.append(f"{name} failed {failed}/{total} (minimum {minimum}, limit {cap} basis points)")
    return failures


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--demo", action="store_true", help="run the bundled fixture at its fixed reference time")
    parser.add_argument("--evidence", type=Path, help="trusted producer's JSON aggregate record")
    parser.add_argument("--candidate", help="expected release-manifest digest")
    parser.add_argument("--suite", help="expected approved evaluation-suite digest")
    parser.add_argument("--scope", help="expected tenant/workflow deployment scope")
    args = parser.parse_args()
    production_args = (args.evidence, args.candidate, args.suite, args.scope)
    if args.demo:
        if any(value is not None for value in production_args):
            parser.error("--demo takes no production arguments")
        path = KIT / "synthetic-evidence.json"
        candidate, suite, scope = DEMO_CANDIDATE, DEMO_SUITE, "demo/invoice-exception-draft"
        now = datetime(2026, 1, 15, 11, tzinfo=timezone.utc)
        kind = "synthetic"
    else:
        if not all(production_args):
            parser.error("production requires --evidence, --candidate, --suite and --scope")
        path, candidate, suite, scope = production_args
        now = datetime.now(timezone.utc)
        kind = "observed"
    mode = "DEMO" if args.demo else "RELEASE"

    try:
        policy = yaml.load(read_record(KIT / "release-gate-checklist.yaml"), Loader=PolicyLoader)
        evidence = json.loads(read_record(path), object_pairs_hook=unique_mapping)
        failures = evaluate(policy, evidence, kind=kind, candidate=candidate, suite=suite, scope=scope, now=now)
    except (OSError, ValueError, yaml.YAMLError, RecursionError) as error:
        print(f"{mode} BLOCK | {error}", file=sys.stderr)
        return 1
    if failures:
        for failure in failures:
            print(f"{mode} BLOCK | {failure}", file=sys.stderr)
        return 1
    print(f"{mode} PASS | {scope} | {policy['policy_id']} | {len(policy['metrics'])} metrics | {candidate}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
