# Technology stack and model routing

The invoice-exception service can classify a discrepancy and draft an explanation. An accounts-payable reviewer decides what to release. Ledger entries, supplier changes and payments stay in the existing business process.

The head of AI engineering approves each route for a specific workflow, data class and model revision. Run inference, retrieval, evaluation and the models that encode text for search (embeddings) inside the client's virtual private cloud (VPC) or disconnected enclave. Exclude any route that permits third-party training on client inputs or outputs.

## Immediate priority · Day 0–90

### TECH-01 · Choose the least complex qualified route

Suppose the invoice is 1,075.00 and the purchase order is 1,000.00 in the same currency. Decimal arithmetic on the authorized records gives a variance of 75.00. A private small language model (SLM) can classify the exception. A fixed template can show the variance and policy citation. If the currencies differ and the case lacks an approved exchange-rate source, send the records and reason to the reviewer. Greater model capacity cannot supply the missing authority.

| What is known about the case? | Permitted route |
| --- | --- |
| The business rule and source values settle the question. | Calculate against the system of record. Return the verified values. |
| A required source is missing or revoked, or two effective policies conflict. | Stop drafting and place the case in the manual queue. |
| The exception type and language are covered by the SLM qualification report. | Classify with the domain-tuned SLM. Use the verified class, values and evidence to render the routine draft. |
| Several compatible policy clauses require interpretation, and the class was separately qualified. | Use the approved private larger or frontier language model within the same tenant boundary, budget and review path. An unavailable route goes to a human. |

The platform lead signs a route manifest recording the workflow, exception class, residency, resource cap and cryptographic fingerprints of the model and prompt. Use a fixed set of cases withheld from development to exercise each rule, default and disabled route, including cases that must abstain. Keep the decision log by exception type. Every enabled route must have current approval and a matching model digest. Every unlisted class or unavailable route must land in the manual queue, with zero calls to unapproved endpoints. Otherwise a difficult case can move silently to a different processing boundary.

### TECH-02 · Check what the cited passage actually supports

For retrieval-augmented generation (RAG), the service supplies relevant source passages to the model. The knowledge owner records the owner, version, access policy and effective dates for each passage. Filter by authenticated tenant, case permissions and effective date before search and again before assembling the prompt. Both model routes must emit the approved output structure. For each material claim, verify the cited source ID, version and passage mechanically. A reviewer then checks whether that passage supports the claim.

Every citation must resolve under the original entitlements. All test cases with missing authority must abstain. Of **at least 200 substantive drafts**, **at most 1%** may contain an unsupported material claim. Count a draft once even if several claims fail. Report by route and exception type, along with abstentions divided by all eligible cases. Otherwise the result can improve simply by deferring the hardest invoices. The purchasing-policy owner and controller settle disputed labels and sign the results. An unchecked citation can point to a different customer's record or a policy that took effect too late. [NIST Generative AI Profile](https://doi.org/10.6028/NIST.AI.600-1)

### TECH-03 · Bind approval to the draft the reviewer saw

The accounts-payable controller keeps the model's access read-only. Show the reviewer the original amounts, cited passages, proposed text and unresolved questions. Store the reviewer, case revision and disposition in the approval system. Every released draft needs a human decision for that exact revision, and editing a draft invalidates prior approval. Verify that zero model identities can post, pay or change a supplier. A stale approval can turn a corrected explanation into an unintended financial action.

## Ongoing priority · Day 90+

### TECH-04 · Compare a replacement on the same invoices

The evaluation lead runs the candidate alongside the incumbent inside the same boundary. Give both the same labeled cases and hide model identity from the reviewers. Both must independently pass the release gate. On **at least 200 paired eligible cases**, the candidate's acceptance rate per eligible case can fall by **at most two percentage points** from the incumbent. Break out errors, acceptance, abstentions, latency and full cost per accepted outcome by exception class. A lower overall cost can mask growing rework in a small class. Archive both manifests and the paired results. The workflow owner signs the cost and capacity trade-off.

### TECH-05 · Give cooperating agents a single spending limit

The orchestration lead gives retrieval and drafting separate identities and fixed read permissions. Record which step may follow which and have the coordinator validate each result. One call budget and one deadline cover both agents, including retries. In the exhaustion drill, the next call must be denied and exactly one manual case created. Every transition must appear in the approved table and no delegated identity may widen the parent's permissions. Otherwise a handoff can grant extra access or restart an exhausted budget.

### TECH-06 · Roll back the components that produced the error

Each week the service owner compares reviewer labels, abstentions and the mix of exceptions against the signed baseline. Make a quality decision once at least **200 substantive drafts** have accumulated. With fewer than 200, keep collecting and hold expansion. Breaching the approved error ceiling freezes the affected route. Confirmed cross-tenant exposure or an unauthorized action suspends it immediately at any volume.

Roll back the model, prompt, index, rules and route as one compatible release, or restore manual handling. Rehearse this within **15 minutes**. Reprocess affected open drafts and record denominators, baseline, route changes and recovery times in the private release record. Restoring only the model leaves a stale index free to produce the same error. Finance and engineering use the same case ledger when they compare costs and reviewer acceptance. [Process and FinOps](01-process-and-finops.md) · [Release criteria](../04-policy-as-code-templates/release-gate-checklist.yaml) · [Ongoing delivery runbook](../03-client-execution-kit/day-90-plus-ongoing-runbook.md)
