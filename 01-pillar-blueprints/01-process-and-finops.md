# Process design and financial operations (FinOps)

A supplier invoice fails a three-way match when the invoice, purchase order and goods receipt disagree. Today an analyst retrieves the records, checks the amounts and decides who can resolve the discrepancy. Keep the case ID and that analyst's authority. Have the service do the authorized lookup once, calculate the difference in decimal arithmetic and draft a cited explanation. The analyst can accept, edit, reject or return the case to the manual queue. Payment stays in the existing accounts-payable system under human control.

The COO owns the queue and its staffing. The CFO validates the manual baseline and any benefit claimed on the profit and loss statement. The amounts and thresholds below are illustrative terms for this workflow.

## Immediate priority · Day 0–90

### PROC-01 · Decide which queue to fund

Finance joins four complete weeks of case timestamps, dispositions and fully loaded analyst costs. Break out exception type and complexity. An undifferentiated average makes a busy, easy queue look like a better investment than a smaller queue that ties up senior analysts.

Set the local materiality unit before ranking candidates. Here it is USD 25,000 of annual **net** operating benefit, after recurring costs, at comparable case volume. Score each dimension from 1 to 5. Use the lower score when an estimate spans two bands.

| Dimension and weight | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- |
| Annual net benefit in materiality units · 40% | ≤0 | >0 to <0.5 | 0.5 to <1 | 1 to <2 | ≥2 |
| Cases with both source and reviewed outcome · 25% | <40% | 40–<60% | 60–<80% | 80–<95% | ≥95% |
| Reversibility · 20% | Irreversible external action | Counterparty must correct it | Internal approval to undo | Restricted internal draft | Isolated draft and tested manual route |
| Readiness · 15% | 0 items | 1 item | 2 items | 3 items | All 4 items |

The four readiness items are a process owner, data permission, a baseline and a staffed fallback. Multiply each rating by its weight and add. At USD 31,200 annual net benefit, 96% matched evidence, an isolated draft with a tested fallback and all four readiness items, the example scores **4.6/5**. Its ratings are 4, 5, 5 and 5.

Fund a candidate only with a score of **at least 4.0/5**, four complete baseline weeks, a named baseline owner, an agreed acceptance definition and an approved spending cap. Lawful access, a permitted purpose and a safe manual route are prerequisites at any score. Keep the dated selection sheet.

### PROC-02 · Give each invoice one human disposition

Bind every submission and retry to the original case ID. Send missing evidence, disputed amounts and restricted cases to a named human queue. Record reviewer identity and disposition. An unowned queue strands the case. A retry with a new ID can release it twice.

Use 20 duplicate submissions to demonstrate exactly one disposition per case. Reconcile every released case to a human decision and require zero ledger or payment writes by an agent. Keep the reviewer drill, the revised workflow diagram and the staffing roster.

### PROC-03 · Measure cost after the case settles

Cost per accepted outcome is **all operating cost for the cohort divided by the number of distinct AI-assisted cases accepted by an authorized reviewer and still settled after seven days**. Count an edited draft if it meets the agreed rubric and the source-backed work remains usable. A full rewrite goes to manual fallback. A reopened case loses its accepted status until it settles again.

Tag the compute, allocated platform, assurance and labor costs by workflow and month. Rejected attempts, retries, rework and manual fallback all cost money even when they add nothing to the denominator. Track acceptance among *all eligible cases*, queue age and material corrections. Keep one-time implementation costs separate for payback.

| Synthetic monthly ledger | Amount or calculation |
| --- | --- |
| Matched manual baseline | USD 8,000 for 1,000 completed cases = USD 8.00 per accepted manual outcome |
| Assisted operating cost | USD 600 inference + 300 retrieval and platform + 300 assurance + 2,700 review + 700 rework + 800 manual fallback = USD 5,400. Each expense appears once. |
| Cost per accepted assisted outcome | 900 of 1,000 accepted. The other 100 close manually. USD 5,400 / 900 = **USD 6.00**. |
| Total cost per closed case | USD 5,400 / 1,000 = **USD 5.40** across both paths. At this volume the monthly operating difference is USD 2,600. A USD 7,800 setup cost pays back in three steady months if Finance can realize the difference. |

Reconcile the cohort ledger to within **2%** of actual cost and explain the variance. Expansion requires at least **200 eligible settled cases**, acceptance of **85% or higher** and cost per accepted assisted outcome at or below **80%** of the matched manual baseline. Zero accepted cases leaves the unit cost undefined and expansion on hold. Otherwise cheap drafts can hide a costly manual backlog.

## Ongoing priority · Day 90+

### PROC-04 · Look for the exception type that lost money

Finance reviews a weekly ledger by route and complexity with the operations owner. Compare like case types, loaded labor rates and reopen windows. Include retries, idle reserved capacity and analyst time. If a segment costs more than 80% of its manual baseline **or** acceptance falls below 85% for two consecutive settled weekly windows of at least 50 eligible cases each, freeze expansion pending owner action. Pool smaller samples and show the counts. A change in case mix can conceal a failing route even when the portfolio average improves.

### PROC-05 · Prove the manual team can absorb a busy hour

Once a month the staffing owner sends synthetic cases representing the last busy hour to the manual queue, with surge coverage on the roster. Every open case ID must reach an owner exactly once and rerouting must finish within **15 minutes**. Record queue age and the staffing decision after the drill. A switch that stops AI traffic but leaves invoices without an analyst does little for a supplier waiting on payment.

### PROC-06 · Put a budget owner behind the next expansion

Finance and operations compare matched volumes, service quality and labor actually released before adding a route. Every new cohort needs a signed spending cap, named owner, unit-cost ceiling and stop rule. If analysts remain on payroll, show the hours released and which queue received them. Recognize a bookable benefit only against an actual budget change approved by Finance. Otherwise a capacity gain can be counted twice, once as removed cost and again as redeployed staff. [Completed director decision](../03-client-execution-kit/worked-release-decision.md) · [Ongoing runbook](../03-client-execution-kit/day-90-plus-ongoing-runbook.md)
