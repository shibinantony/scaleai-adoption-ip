# Gateway, evaluations and runtime evidence

When an invoice draft is challenged, the platform team needs to identify the submitting workload, the policy and model that allowed the draft, and the reviewer's decision. The first two belong in operational telemetry. The review decision belongs in the client’s business record. Join them by trace ID.

The platform director owns the private gateway. Security Engineering sets the deny rules, and the workflow owner owns the acceptance sample and manual queue. Give inference, evaluation and policy publication distinct service identities. Only the gateway identity can reach runtime inference.

## Immediate priority · Day 0–90

### TOOL-01 · Reserve capacity before dispatch

The gateway owner derives the tenant and workload from validated identity, then applies the rate limit, redaction rules and token ceiling. Two gateway replicas can receive requests at the same instant when only one request's budget remains. Reserve the maximum billable units in one atomic operation shared by all replicas. Reconcile to actual usage after completion. If the call times out before usage is known, keep the reservation open. Record its ID and the rule version in the accounting ledger.

Deny every missing or mismatched identity before inference. In the concurrency test the sum of authorized reservations must stay within the cap. Budget exhaustion must produce a controlled hold. Otherwise one tenant can exhaust shared capacity or an unverified caller can send sensitive fields downstream.

### TOOL-02 · Check the whole draft before showing it

The application security lead uses NeMo Guardrails flows to call local functions that validate required fields, allowed actions and references against the authorized source set. Buffer the full draft until the checks complete. A model-based screen may flag a case for review. Enforce permissions separately at the tool server.

Test an invalid schema, an invalid citation, a prohibited action and an unavailable check. In each case **zero draft bytes** may reach the user. The same test input and rule version must yield the same allow or deny decision. Send failures and timeouts to manual review with a reason code. Once an unchecked partial answer has streamed to a reviewer, a later refusal cannot withdraw it. [NeMo Guardrails developer guide](https://docs.nvidia.com/nemo/guardrails/about-nemo-guardrails-library/overview)

### TOOL-03 · Keep evaluation cases replayable

The assurance lead runs fixed synthetic transcripts through Microsoft's Python Risk Identification Tool (PyRIT) for scoring and uses Giskard to assess retrieval and answers. For an outdated-policy test, give the suite two versions with different effective dates. Specify the permitted citation and the acceptable manual disposition. Record the expected and observed source version separately from the reviewer's judgment about the answer. [Giskard RAG evaluation](https://docs.giskard.ai/oss/checks/use-cases/rag-evaluation) · [Microsoft PyRIT](https://microsoft.github.io/PyRIT/)

Keep the fixtures, scoring software, any model used as a judge, endpoints and reports inside the client boundary. An independent reviewer resolves label disputes. Attach counts by suite, case IDs, and the fixture and build hashes to the release. Every metric in the versioned checklist must meet its minimum coverage and quality threshold, including severe toxicity, unsupported claims and defensive scenarios. A skipped case, missing evidence or scorer error blocks promotion. Losing a difficult class of cases can make a weaker release appear to improve.

### Reconstruct a decision without logging the invoice

At ingress, issue an opaque trace ID. Record the tenant pseudonym, workflow, allow or deny result, policy digest and route. Add the model digest, latency and token counts after inference. Keep case revision and reviewer disposition in the access-controlled business record. Only authorized incident personnel may resolve pseudonyms to identities.

Export only permitted attributes through a private OpenTelemetry collector to the client-owned security information and event management (SIEM) system. Strip prompt bodies, document passages, tool arguments, raw supplier IDs, authorization headers and exception text before export. [OpenTelemetry guidance on sensitive data](https://opentelemetry.io/docs/security/handling-sensitive-data/)

Security operations replays a synthetic approval, denial and timeout. All three decisions must be retrievable by trace ID **within five minutes**, with **zero** seeded sensitive markers in runtime, collector and SIEM output. Keep the reconciliation and scan results. A missing denial hides an access-control failure. A surviving marker means the logging stack now holds a second copy of sensitive material.

## Ongoing priority · Day 90+

### TOOL-04 · Decide which answers can be reused

A semantic cache reuses an answer for a question judged sufficiently similar to an earlier one. Leave it off for invoices, personal content, mutable balances, approvals and tool results. The knowledge owner may approve static policy FAQs for a named tenant. Partition those entries by tenant and bind each to entitlements, locale, effective policy version, model and prompt. Reauthorize a hit, enforce expiry, and invalidate on source or access changes.

Denied or ineligible test cases must produce zero hits. Revocation must stop reuse immediately. Before enabling a similarity threshold, review at least **200 pairs of closely worded questions per enabled language** and require **zero materially wrong matches**. A small change in wording can change which policy applies. Compare cache savings with source validity, acceptance, abstentions, unsupported drafts, latency and budget denials.

### TOOL-05 · Find decisions lost during a telemetry outage

Security operations reconciles the ingress count to one terminal decision per admitted trace. Deduplicate repeated deliveries by the opaque trace ID. Two conflicting final decisions for the same trace fail reconciliation. Buffer events in encrypted local storage, alarm on remaining capacity and hold the affected draft on the first failed durable write. A collector outage can otherwise leave reviewers with drafts no one can account for.

During the outage drill, reconcile every admitted request to exactly one terminal decision within **five minutes**. The tenant-level alert must reach the on-call lead within **five minutes** of an evidence gap.

### TOOL-06 · Let a failed comparison stop rollout

The release manager tests the current and candidate bundles on the same frozen suite in a private runner. Bind the signed results to the model, rules, code, dataset and scorer digests. Before opening a limited one-tenant rollout, prove that the deployment adapter rejects both an incomplete scorecard and a valid report for a different candidate. Stale evidence is an easy way to approve a build that nobody tested.

If the limited rollout fails, close the route and restore the approved bundle or manual review within **15 minutes**. Keep the promotion decision for each model or policy change. Exercise the client’s gateway and deployment adapters with the same cases used for release. [Gateway policy](../04-policy-as-code-templates/ai-gateway-policy.yaml) · [Release criteria](../04-policy-as-code-templates/release-gate-checklist.yaml) · [Immediate delivery runbook](../03-client-execution-kit/day-0-90-immediate-runbook.md)
