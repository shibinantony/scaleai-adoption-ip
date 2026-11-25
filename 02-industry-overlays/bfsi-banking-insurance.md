# Banking and insurance

A head of operations can sponsor one of two limited releases. A bank investigator receives a draft evidence chronology for a disputed transaction. A claims examiner receives an indexed list of documents for an open claim. The employee owns the disposition. The service identity can read the assigned case and write to a draft queue. Settlement, coverage, credit and payment systems accept writes only from the existing authorized process.

## Scope in the United States

On April 17, 2026, the US banking agencies issued revised model risk guidance. The Federal Reserve’s SR 26-2 supersedes SR 11-7 and is most relevant to Federal Reserve-supervised banking organizations above $30 billion in total assets. The guidance excludes generative and agentic AI. The bank’s model risk officer classifies any separate conventional predictive component, records the rationale and applies the bank’s own AI governance to the drafting service. [Federal Reserve letter](https://www.federalreserve.gov/supervisionreg/srletters/sr2602.htm) · [Guidance and scope, footnote 3](https://www.federalreserve.gov/frrs/guidance/supervisory-guidance-on-model-risk-management.htm)

For insurance, compliance records the issuing jurisdiction, regulator, applicable state bulletin and effective date for each pilot. The NAIC model bulletin describes a written AI systems program proportionate to risk and addresses decisions affecting consumers. Card operations separately establish the PCI DSS boundary, including systems connected to the cardholder data environment. This pilot keeps account numbers out of the inference path. PCI’s protection requirements for stored primary account numbers still apply to the upstream environment. [NAIC model bulletin background](https://content.naic.org/article/naic-members-approve-model-bulletin-use-ai-insurers) · [PCI SSC account-data guidance](https://www.pcisecuritystandards.org/faqs/1222/)

## Immediate priority · Day 0–90

The pilot covers one queue and one legal entity. Use approved, case-linked source documents within the client’s private environment. Resolve personal identifiers upstream to case-scoped tokens. Keep logs under the client’s keys and disable provider training and external inference. The figures below are proposed pilot acceptance criteria. The risk owner signs them before baseline testing.

| Control objective | Implementation and evidence | Pass threshold | Blast radius if omitted |
| --- | --- | --- | --- |
| Keep card and personal identifiers inside the system of record | The case adapter allowlists fields, tokenizes identifiers and rejects unstructured attachments until the approved redaction service clears them. Inspect inference input, cache and logs with seeded synthetic identifiers. | All 200 seeded cases pass inspection with zero raw PANs, security codes or prohibited identifiers at any of the three sinks. | One attachment can place card or personal data in searchable model logs across the retention period. |
| Enforce the investigator’s case boundary | Intersect tenant, legal entity, assigned case and staff entitlement on every document fetch. Test reassignment and closed cases. | Zero unauthorized reads in 100 denied-access fixtures. All 20 revoked assignments lose access before the next fetch. | A claims examiner can see another claimant’s medical or financial file. |
| Preserve a defensible disposition | Link each material claim to a document version and location. Hash the evidence manifest. The reviewer signs the disposition in the case system. Timeouts return the case to manual review. | In 200 independently reviewed substantive drafts, zero wrong-party, amount or coverage assertions and ≤2 drafts with any unsupported material claim. Approval and manifest present on every completed case. Draft p95 ≤10 seconds across all issued requests, counting timeouts as breaches. | Incorrect evidence can drive a payment dispute or denial that the institution cannot reconstruct. |

**Release decision.** The operations owner and independent risk reviewer sign the queue mandate, redaction report, reviewer findings and manual-fallback drill. Any privacy breach or material decision error disables drafting for the queue. Preserve the manifest and reopen affected cases from the last verified release. The existing manual queue owns pending cases.

## Ongoing priority · Day 90+

| Control objective | Implementation and evidence | Pass threshold | Blast radius if omitted |
| --- | --- | --- | --- |
| Detect selective degradation before adding a product or jurisdiction | Sample weekly by product, document language and claim complexity. Compare material-error and escalation rates with a matched manual sample. Document lawful subgroup selection and independent reviewer adjudication. | Quarterly expansion requires ≥100 reviewed cases per proposed slice in each arm, zero wrong-party or wrong-amount errors and an escalation-rate gap ≤5 percentage points versus the matched manual arm in each slice. Hold undersampled slices. | An acceptable portfolio average can conceal a failing product line or language queue. |
| Reconstruct challenged cases after model or policy changes | Retain source versions, token lookup rights, reviewer edits and route version under records schedules and legal holds. Replay a restricted evidence snapshot in the client environment. | Quarterly, all 30 sampled files reproduce the exact source bundle, recorded draft and final human disposition. One missing bundle freezes expansion until restored. | An examiner or complaints team cannot explain an individual decision months later. |

Finance measures cost per **reviewer-accepted evidence packet** by queue. Divide total inference, review, retrieval, exceptions, rework and allocated platform cost by unique accepted cases for the same monthly cohort. For example, $4,200 / 700 accepted packets = $6 per packet. Compare with the matched manual queue and track reopened cases at 30 days. A zero denominator suspends the economic decision. Expand one queue only when two successive cohorts beat the signed manual cost baseline and both control gates pass.

Use the [first-release runbook](../03-client-execution-kit/day-0-90-immediate-runbook.md) to assemble the approval pack and the [operating cadence](../03-client-execution-kit/day-90-plus-ongoing-runbook.md) to assign repeat reviews.
