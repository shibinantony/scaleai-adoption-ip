# Banking and insurance

The first reader of a dispute chronology is the investigator. The second may be a complaints officer, months after the case closed. Both need to see the receipt, the amount and the document the investigator relied on. A claims examiner needs the same traceability when reviewing a coverage decision.

Choose one queue in one legal entity. For a bank, commission a dated chronology of a disputed transaction. For an insurer, commission a document index for an open claim. Give the service access to the assigned case and its draft queue. Existing staff and systems retain authority over settlement, coverage, credit and payment.

## Day 0–90 · Qualify one case queue

Agree the following acceptance tests with the risk owner before testing. Run inference privately, keep logs under client-controlled keys and disable third-party training.

1. **Follow an attachment.** Allowlist the adapter’s fields, replace personal identifiers with case-specific tokens and hold free text until redaction succeeds. Inspect the model input, cache and logs across 200 synthetic cases seeded with identifiers. Require zero raw primary account numbers (PANs), card security codes or prohibited identifiers at all three destinations. A missed attachment can put card data into searchable logs for their full retention period.
2. **Reassign a case.** On every document fetch, check the tenant, legal entity, assigned case and staff entitlement. Include closed files in the tests. Require zero unauthorized reads across 100 denial cases. For all 20 revoked assignments, the *next fetch* must fail. Otherwise a former handler could still read a claimant’s medical or financial records.
3. **Hand the file to another examiner.** Link each material assertion to a document version and location, hash the source manifest, and retain the signed disposition in the case system. Across 200 independently reviewed substantive drafts, allow zero wrong parties, amounts or coverage assertions and at most two drafts with any unsupported material claim. Every completed case needs its manifest and approval. Measure draft latency across all requests. The p95 limit is 10 seconds. Count timeouts as breaches and send those cases to manual review.

The operations owner and independent risk reviewer sign the queue mandate, redaction results, examiner findings and fallback drill. A privacy breach or material decision error stops drafting in that queue. Preserve the manifest, reopen affected cases from the last verified release and assign pending cases to the manual queue. [First-release runbook](../03-client-execution-kit/day-0-90-immediate-runbook.md)

**Which US rules apply?** For a bank, the model risk officer records whether a separate conventional predictive component falls under SR 26-2. The April 17, 2026 guidance supersedes SR 11-7, excludes generative and agentic AI, and is most relevant to Federal Reserve-supervised banks above $30 billion in assets. Apply the bank’s own AI governance to the drafting service. Card operations maps the PCI DSS boundary, including connected systems. Stored PANs remain subject to protection upstream even when inference receives tokens. [Federal Reserve letter](https://www.federalreserve.gov/supervisionreg/srletters/sr2602.htm) · [Guidance, footnote 3](https://www.federalreserve.gov/frrs/guidance/supervisory-guidance-on-model-risk-management.htm) · [PCI SSC account-data guidance](https://www.pcisecuritystandards.org/faqs/1222/)

For an insurer, compliance records the state regulator, applicable bulletin and effective date. The NAIC model bulletin sets out a risk-proportionate written AI systems program for insurers using AI in decisions affecting consumers. Confirm what the state has adopted before extending the pilot there. [NAIC bulletin background](https://content.naic.org/article/naic-members-approve-model-bulletin-use-ai-insurers)

## Day 90+ · Reopen the file before opening another queue

At the quarterly review, give an examiner 30 sampled files. All 30 must reproduce the source bundle, recorded draft, reviewer edits and final disposition. Preserve source and route versions and authorized token lookup under the retention schedule and legal holds. One missing bundle holds expansion until staff can recover it.

Reviewers also sample weekly by product, language and complexity. Record the lawful basis for subgroup selection. Independently adjudicate material errors and escalations against matched manual cases. For each group proposed for expansion, require at least 100 reviewed cases in each arm, zero wrong parties or amounts and an absolute escalation-rate gap of at most five percentage points. A low-volume language queue stays at its current scope until it has evidence of its own.

Finance counts unique reviewer-accepted evidence packets. Include inference, retrieval, platform allocation, review, exceptions and rework. An illustrative month at **$4,200 for 700 accepted packets costs $6 per packet**. Track cases reopened within 30 days. Expand one queue after two successive monthly cohorts beat the signed manual cost baseline and both quarterly checks pass. With zero accepted packets, finance holds the decision. [Operating cadence](../03-client-execution-kit/day-90-plus-ongoing-runbook.md)
