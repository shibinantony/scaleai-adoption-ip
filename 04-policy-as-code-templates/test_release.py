"""Positive and refusal-path checks for the published release contract."""

import copy
import json
import subprocess
import sys
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path

import yaml

from evaluate_release import DEMO_CANDIDATE, DEMO_SUITE, KIT, PolicyLoader, evaluate, unique_mapping


class ReleaseContractTests(unittest.TestCase):
    def setUp(self):
        self.policy = yaml.load((KIT / "release-gate-checklist.yaml").read_text(encoding="utf-8"), Loader=PolicyLoader)
        self.evidence = json.loads((KIT / "synthetic-evidence.json").read_text(encoding="utf-8"))
        self.context = {
            "kind": "synthetic",
            "candidate": DEMO_CANDIDATE,
            "suite": DEMO_SUITE,
            "scope": "demo/invoice-exception-draft",
            "now": datetime(2026, 1, 15, 11, tzinfo=timezone.utc),
        }

    def test_rate_boundary_uses_integer_arithmetic(self):
        self.assertEqual(evaluate(self.policy, self.evidence, **self.context), [])
        self.evidence["metrics"]["unsupported_material_claim"] = {"failed": 2, "total": 199}
        self.assertTrue(evaluate(self.policy, self.evidence, **self.context))
        self.evidence["metrics"]["unsupported_material_claim"] = {"failed": 3, "total": 299}
        self.assertTrue(evaluate(self.policy, self.evidence, **self.context))

    def test_each_zero_tolerance_metric_blocks_one_failure(self):
        for metric, rule in self.policy["metrics"].items():
            if rule["max_failed_basis_points"] == 0:
                with self.subTest(metric=metric):
                    record = copy.deepcopy(self.evidence)
                    record["metrics"][metric] = {"failed": 1, "total": 100000}
                    self.assertTrue(evaluate(self.policy, record, **self.context))

    def test_missing_invalid_and_small_samples(self):
        for data in [
            {"failed": 0, "total": 19}, {"failed": False, "total": 20}, {"failed": 21, "total": 20},
            {"failed": 0, "total": 0}, {"failed": -1, "total": 20}, {"failed": 0.5, "total": 20},
        ]:
            with self.subTest(data=data):
                self.evidence["metrics"]["tenant_isolation"] = data
                if data == {"failed": 0, "total": 19}:
                    self.assertTrue(evaluate(self.policy, self.evidence, **self.context))
                else:
                    with self.assertRaises(ValueError):
                        evaluate(self.policy, self.evidence, **self.context)
        del self.evidence["metrics"]["tenant_isolation"]
        with self.assertRaises(ValueError):
            evaluate(self.policy, self.evidence, **self.context)

    def test_stale_future_wrong_identity_and_fixture_replay(self):
        changes = [
            {"now": self.context["now"] + timedelta(days=7)},
            {"now": self.context["now"] - timedelta(hours=2)},
            {"candidate": "sha256:" + "ab" * 32}, {"suite": "sha256:" + "ef" * 32},
            {"scope": "demo/other-workflow"}, {"kind": "observed"},
        ]
        for change in changes:
            with self.subTest(change=change), self.assertRaises(ValueError):
                evaluate(self.policy, self.evidence, **(self.context | change))

    def test_required_rule_cannot_be_silently_removed(self):
        del self.policy["metrics"]["atlas_instruction_boundary"]
        del self.evidence["metrics"]["atlas_instruction_boundary"]
        with self.assertRaises(ValueError):
            evaluate(self.policy, self.evidence, **self.context)

    def test_scope_requires_explicit_tenant_and_workflow(self):
        for scope in ["tenant-any", "team/", "/invoice", "team//invoice", "team/..", "./invoice", "team/invoice/test"]:
            with self.subTest(scope=scope), self.assertRaises(ValueError):
                self.evidence["scope"] = scope
                evaluate(self.policy, self.evidence, **(self.context | {"scope": scope}))

    def test_completed_at_requires_canonical_utc(self):
        for stamp in ["2026-1-15T10:00:00Z", "2026-01-15T10:0:00Z", "2026-01-15T10:00:00+00:00"]:
            with self.subTest(stamp=stamp), self.assertRaises(ValueError):
                self.evidence["completed_at"] = stamp
                evaluate(self.policy, self.evidence, **self.context)

    def test_client_job_exit_status(self):
        # Simulate the private producer and protected release job with a temporary local record.
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "release.json"
            command = [
                sys.executable, str(KIT / "evaluate_release.py"), "--evidence", str(path),
                "--candidate", DEMO_CANDIDATE, "--suite", DEMO_SUITE, "--scope", "test/invoice",
            ]
            self.evidence.update(
                kind="observed", scope="test/invoice",
                completed_at=datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            )
            path.write_text(json.dumps(self.evidence), encoding="utf-8")
            passed = subprocess.run(command, capture_output=True, text=True, check=False)
            self.assertEqual(passed.returncode, 0, passed.stderr)
            self.assertIn("RELEASE PASS", passed.stdout)
            self.evidence["metrics"]["human_release"]["failed"] = 1
            path.write_text(json.dumps(self.evidence), encoding="utf-8")
            blocked = subprocess.run(command, capture_output=True, text=True, check=False)
            self.assertNotEqual(blocked.returncode, 0)
            self.assertIn("RELEASE BLOCK | human_release", blocked.stderr)

    def test_duplicate_keys_cannot_override_failures_or_policy(self):
        with self.assertRaises(ValueError):
            json.loads('{"failed":1,"failed":0}', object_pairs_hook=unique_mapping)
        with self.assertRaises(ValueError):
            yaml.load("max_failed_basis_points: 0\nmax_failed_basis_points: 100", Loader=PolicyLoader)

    def test_gateway_template_has_private_pilot_defaults(self):
        gateway = yaml.load((KIT / "ai-gateway-policy.yaml").read_text(encoding="utf-8"), Loader=PolicyLoader)
        self.assertEqual(gateway["schema"], "scaleai.gateway.v1")
        self.assertEqual(gateway["data_handling"]["public_egress"], "deny")
        self.assertEqual(gateway["data_handling"]["training_on_client_data"], "prohibited")
        self.assertEqual(gateway["tool_access"]["payment_or_ledger_write"], "deny")
        self.assertEqual(gateway["cache"]["mode"], "disabled")
        self.assertNotIn("approved_policy_excerpt", gateway["data_handling"]["permitted_input_fields"])
        context = gateway["data_handling"]["server_resolved_context"]
        self.assertEqual(context["caller_supplied_context_or_stale_unverified_reference"], "deny")
        self.assertEqual(set(context["passage_binding"]), {"source_id", "source_version", "passage_id", "content_digest"})


if __name__ == "__main__":
    unittest.main()
