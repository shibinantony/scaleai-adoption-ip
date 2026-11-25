# Day 0–90 · Deliver the first controlled workflow

Over 13 weeks, the team decides whether one named tenant can use AI to draft explanations for invoice exceptions. An accounts-payable analyst still decides each case. Only an authorized human can initiate a payment or ledger action. If a checkpoint slips, keep the last approved operating mode. A second workflow needs its own purpose, business case and release evidence.

## Weeks 1–3 · Choose the work and establish the boundary

**Week 1 · days 0–6.** The sponsor and Finance rank the candidate queues and identify who would be affected. Run the [five-pillar diagnostic](day-0-discovery-diagnostic.md) on the proposed workflow. Sign a charter with an accountable owner, scope, spending cap and manual fallback. Hold candidates that lack permission to use the data.

**Week 2 · days 7–13.** The process owner brings four historical weeks of comparable cases and traces where duplicate entry or rework begins. Agree what counts as an accepted outcome and how long it takes to settle. The CFO signs the baseline volume, groups of comparable cases, cost categories and reviewer capacity. Extend discovery if history is missing or the team cannot measure the unit of value.

**Week 3 · days 14–20.** Security and Legal establish which data the workflow may handle, where processing may occur, and which provider terms and obligations apply. The CISO signs the data-flow map, outbound network rules, no-training condition, key custody and client log ownership. Engineers work with synthetic records.

## Weeks 4–8 · Rehearse before taking live work

**Week 4 · days 21–27.** The platform lead puts the private gateway, caller identity, token reservations, outbound restrictions and client audit store in place. Run allowed and denied requests for two synthetic tenants. Inspect every permitted destination for the restricted values seeded in those cases. Live data can enter only after these boundary checks pass.

**Week 5 · days 28–34.** The data owner limits each lookup by user, tenant, case and effective date. Revoke a reader's access, then show that retrieval denies the next lookup. An authorized reviewer must still be able to open each source link. The Finance systems team removes agent write access and demonstrates a forbidden tool call leaves an audit record and changes no financial record.

**Week 6 · days 35–41.** The model lead tests small and larger private models on comparable invoice exceptions. Select the least expensive route that meets each task's quality and latency limits. Freeze the selected versions together. When sources cannot support a draft, the service abstains and sends the original case to an analyst.

**Week 7 · days 42–48.** The assurance lead and domain reviewers agree on material errors, severe harm, sector-specific case groups and minimum sample sizes. Keep tuning cases separate. Before scoring the candidate, independent reviewers resolve label disagreements, record why the thresholds apply and approve the evaluation suite's digest, its cryptographic identifier.

**Week 8 · days 49–55.** The release engineer runs the [policy gate](../04-policy-as-code-templates/README.md) on authenticated evidence. Operations rehearses a model failure, an unavailable audit store and transfer to the manual queue. Save the gate result, reconcile every case and demonstrate rollback in **15 minutes or less**. A failed required control blocks progression beyond shadow.

## Weeks 9–11 · Compare alongside staff, then limit live traffic

**Week 9 · days 56–62.** In shadow mode, the service owner generates private drafts under the approved data terms while staff independently complete the cases. Account for arrivals, timeouts, abstentions, completed drafts and reviewer cost. Independent assurance and the CISO sign the evidence for this candidate.

**Week 10 · days 63–69.** A canary is a small supervised live rollout. The COO can open one after release approval. Rerun the gate at promotion using evidence for this candidate and tenant/workflow scope. The starter policy allows up to **168 hours** from evaluation completion. Replace expired evidence before running the gate.

Start with **one staffed shift, one tenant, at most 5% of eligible cases and 50 cases/day**. Both caps apply. Require a human decision for every release. Review all decision records, guardrail results, arrivals, backlog and spend daily. A hard stop sends the affected cases back to people immediately.

**Week 11 · days 70–76.** Operations waits for the first cases to complete their seven-day reopen window. Report the sample size, error severity, reopen rate and oldest waiting case by type. Before increasing traffic, rerun the gate with current evidence. If the controls hold and the sample is sufficient, seek a signed increase in the same scope to **at most 25% and 200 cases/day**. Keep the existing caps while evidence is insufficient.

## Weeks 12–13 · Decide what the business will fund

**Week 12 · days 77–83.** Finance prices the entire path, including failed attempts and cases completed manually. Bring the settled-case ledger, forecast, incidents and exact deployment version. Independent assurance verifies the evidence for the proposed operating scope. Compare actual acceptance and cost per accepted outcome with the signed business thresholds.

**Week 13 · days 84–90.** The director convenes the COO, CIO, CISO, Finance and independent assurance. Confirm who supports the service and who can suspend it. Choose release, continued canary, hold or retirement. Sign the scope, budget, case cap, residual risk, expiry and next review date. If too few cases have settled, the group can extend the canary within its existing limits. [Worked decision record](worked-release-decision.md)

## If the service must stop

A confirmed data-boundary breach or unauthorized action suspends the affected route. Quarantine its drafts and preserve the incident evidence in restricted storage. Assign every open case ID to the existing manual queue. The CISO and workflow owner verify the fix and commission a fresh evaluation before reopening. If the service misses its financial target, hold expansion and return the cost model to Finance. [Ongoing runbook](day-90-plus-ongoing-runbook.md)

## File the release record

| Record owner | What the reviewer should be able to find |
| --- | --- |
| Delivery lead and Finance | Named scope, legal decision, dated diagnostic, baseline ledger and business authorization. |
| Platform and release leads | Route and artifact digests, every required failure or denial record, timed rollback drill and manual case reconciliation. |
| Independent assurance | Synthetic or client-controlled evaluation results, signed evaluator identity, pre-approved suite digest and the decision for this candidate. |

Link each item to the workflow, candidate and person responsible for the evidence. Keep real case data in the client environment. Public examples use synthetic information.
