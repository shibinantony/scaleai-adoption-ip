# Process and FinOps

**Decision owner** — The COO owns the workflow and reviewer capacity. The CFO validates the baseline and any claim on the P&L. This blueprint uses internal accounts-payable invoice exceptions as a worked example. All amounts and thresholds below are illustrative starting terms for that workload.

## Immediate priority · Day 0–90

A supplier invoice that fails a three-way match already has a case ID and a responsible analyst. Preserve both. The existing route asks an analyst to find the order, find the receipt, explain the mismatch and decide where to send it. The redesigned route performs the authorized lookup once, checks amounts in deterministic code, and drafts an explanation with source references. An analyst can accept, edit, reject or return the case to the manual queue. Only the existing accounts-payable service and its human operator can release a payment.

| ID and objective | Technical implementation | Pass/fail and evidence | Impact if omitted |
| --- | --- | --- | --- |
| PROC-01 · Fund a measurable problem | Finance joins case timestamps, disposition and loaded analyst cost for a representative four-week baseline. Segment by case type and complexity. Score candidates using the method below. | Every funded candidate has four complete weeks, a named baseline owner, an agreed acceptance definition, an approved spending cap and a score ≥4.0/5. Retain the dated selection sheet. | A fast demo consumes capacity while a higher-value bottleneck persists. |
| PROC-02 · Preserve decision authority | Accept submissions only on the canonical case ID. Route missing evidence, amount disagreements and restricted cases to a named human queue. Store reviewer identity and disposition. Deduplicate retries. | Across all released cases, 100% have a human decision and zero agent-initiated ledger/payment writes. On 20 duplicated submissions, exactly one disposition per case. Save reconciliation and reviewer drill. | Duplicate processing or an unapproved payment can reach the ledger. |
| PROC-03 · Price the whole workflow | Tag invoices for compute, allocated platform, labor and fallback by workflow and month. Join spend to deduplicated outcomes settled after a seven-day reopen window. | Reconcile to finance ledger within 2% of actual cost and explain the variance. For expansion require ≥200 eligible settled cases, acceptance ≥85% and cost per accepted outcome ≤80% of matched manual baseline. With zero accepted outcomes the metric is undefined and expansion is held. | Cheap drafts hide the labor of review, retries or rework. |

**Candidate selection.** Rate each dimension from 1 to 5 using the bands below. Use the conservative band if an estimate crosses a boundary. Weighted score = 0.40 × value + 0.25 × evidence + 0.20 × reversibility + 0.15 × readiness. Finance estimates annual net operating benefit at comparable case volume after recurring costs. The sponsor sets a local materiality unit before ranking, USD 25,000 in this example.

| Dimension | Anchors for ratings 1 / 2 / 3 / 4 / 5 |
| --- | --- |
| P&L value | Estimated annual net benefit in materiality units is ≤0 / >0 to <0.5 / 0.5 to <1 / 1 to <2 / ≥2. |
| Evidence availability | Share of cases with matched source and adjudicated outcome is <40% / 40–<60% / 60–<80% / 80–<95% / ≥95%. |
| Reversibility | Unrecoverable external action / correction requires counterparty / internal change needs approval to undo / internal draft with restricted distribution / isolated draft plus tested manual route. |
| Readiness | Count the available items: process owner, data permission, baseline, staffed fallback. A count of 0 / 1 / 2 / 3 / 4 yields rating 1 / 2 / 3 / 4 / 5. |

A synthetic invoice pilot with annual net benefit of USD 31,200, matched evidence on 96% of cases, isolated drafting and all four readiness items scores **4.6/5** (4, 5, 5, 5). A candidate without lawful data access, a permitted purpose or a safe manual route stops before ranking can authorize spend. Day 90 deliverables are the signed selection sheet, revised swimlane, reviewer roster and reconciled cohort ledger.

## Ongoing priority · Day 90+

| ID and objective | Technical implementation | Pass/fail and evidence | Impact if omitted |
| --- | --- | --- | --- |
| PROC-04 · Protect margin as mix changes | Produce a weekly cohort ledger by route and complexity. Compare identical case types, loaded rates and reopen windows. Include retries, idle reserved capacity and analyst time. | Review any segment at >80% of baseline cost or <85% acceptance for two settled weekly windows with ≥50 eligible cases each. Freeze expansion pending owner action. Pool smaller samples and show counts. | Easy cases can conceal an unprofitable route or a growing manual backlog. |
| PROC-05 · Maintain fallback capacity | Replay the last busy hour into the manual queue using synthetic cases. Staffing owner schedules surge coverage and tests rerouting monthly. | 100% of open case IDs reach a queue owner exactly once and rerouting completes in ≤15 minutes. Record queue age and a staffing decision after each drill. | Pausing the model strands regulated or time-sensitive work. |
| PROC-06 · Release further investment | Before adding a route, finance and operations compare matched volumes, labor realization and service quality, then approve a capped expansion cohort. | Every new scope has a signed budget, named owner, unit-cost ceiling and stop rule. Any bookable benefit reconciles to an actual budget change approved by finance. | Reported savings become a target without an accountable budget owner. |

### Cost per accepted outcome

For one settled cohort, divide **all in-scope operating cost** by **distinct cases whose AI-assisted outcome was accepted by the authorized reviewer and survived the reopen window**. Charge rejected attempts, retries and manual fallback to the numerator. An edit counts if the source-backed draft remains usable under the pre-agreed rubric. A full rewrite is manual fallback. A reopened case loses acceptance until it settles. Track accepted share against *all eligible cases*, queue age and material correction rate alongside cost. Separate one-time implementation spend for payback analysis.

| Synthetic monthly cohort | Calculation |
| --- | --- |
| Manual comparator | USD 8,000 for 1,000 matched completed cases = USD 8.00 per accepted manual outcome. |
| Assisted pathway | USD 600 inference + 300 retrieval/platform + 300 assurance + 2,700 review + 700 rework + 800 manual fallback = USD 5,400. Cost buckets are mutually exclusive. |
| Acceptance and cost | 900 of 1,000 eligible cases accepted through the assisted path. The other 100 close manually. USD 5,400 / 900 = **USD 6.00 per accepted assisted outcome**. |
| Portfolio and payback | USD 5,400 / 1,000 = USD 5.40 per closed case across both paths. At matched volumes the operating cost difference is USD 2,600/month. A USD 7,800 setup cost breaks even in three steady months if finance can realize that difference. |

If manual labor remains on payroll, show hours released and the receiving queue. Recognize cash savings only when finance can identify where spending fell. [Completed director decision](../03-client-execution-kit/worked-release-decision.md) · [Ongoing runbook](../03-client-execution-kit/day-90-plus-ongoing-runbook.md)
