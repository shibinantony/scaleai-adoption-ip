# Should we fund this workflow?

For an invoice-exception pilot, ask Finance to bring the cost of resolving a disputed invoice today and Operations to bring a case an analyst recently had to finish by hand. Walk through that case together. Where would a draft have saved time? Which checks would the analyst still have had to do? Those answers determine what belongs in the business case.

## What the board should see

Choose one service and tenant, and report the number and types of cases over the same period. Otherwise a queue of simple invoices can make one model look faster or cheaper than another. The table shows what each executive should be able to measure.

| Pillar | CIO · service delivery | CISO · exposure | COO · operations | CFO · cost |
| --- | --- | --- | --- | --- |
| Process | % of eligible cases traceable from intake to close | % of final actions linked to an authorized reviewer | Cases where a reviewer accepted the assisted outcome, out of all eligible cases. Reopen rate and age of oldest pending case | Full cost per accepted outcome against comparable manual cases |
| Technology | 95th-percentile time from request to draft, by model route | Number of routes using an unapproved processor | Reviewed drafts with an unsupported material claim, out of all substantive drafts reviewed | Model, retrieval and reviewer cost by route |
| Tools | % of gateway requests with a complete decision record | Restricted fields found in exported logs | % of rejected or timed-out cases that reach the manual queue | Cost of retries and cache misses per 1,000 eligible requests |
| Architecture | Time to restore an approved deployment | Cross-tenant reads and connections to unapproved destinations | Open cases accounted for after failover, out of all open cases | Private infrastructure cost per active tenant and per accepted case |
| Trust and assurance | % of proposed releases with current evidence for that exact version | Open critical failures and time taken to suspend service | Decisions an independent reviewer can reconstruct, out of those sampled | Outstanding assurance actions by due date and the cost of fixing them |

## Who can say yes, and who can stop the work?

**Discovery.** The business sponsor and finance partner may fund a capped investigation once they can name the owner, the queue and a way to measure current costs. They can decide on production funding after Finance has measured that baseline.

**First live cases.** The COO can open a small supervised rollout (a canary) for one tenant and one staffed review queue. The service may draft. A person releases the result. Independent assurance verifies the tests, the CISO signs off on data access, and the CIO accepts operational support. All mandatory release checks must pass. Operations must show it can switch open cases to a safe route within 15 minutes.

**An incident during a shift.** On-call operations can suspend the service immediately. One confirmed data-boundary breach or unauthorized write is enough. Security leads containment, and the workflow owner gets the open cases back to analysts. Retain the evidence in client custody and reconcile each case ID.

**More funding.** For the invoice pilot, the board needs at least 200 eligible cases past the seven-day reopen window. Analysts must have accepted at least 85% through the assisted route, and full cost per accepted outcome must be at most 80% of the manual baseline. Quality and access checks must also pass. The sponsor accepts the remaining business risk for one named expansion, and Finance approves its budget.

**Retirement.** The process owner accounts for all open cases. The platform owner revokes credentials and applies the agreed retention schedule to tenant data and records. Keep the joint closure decision.

Finance should distinguish a gain in capacity from a reduction in spending. In the worked example, $6 per accepted assisted case clears the $6.40 ceiling. If the same people are still on payroll, record where their time went. Recognize cash savings when a budget line actually falls. [Worked release decision](../03-client-execution-kit/worked-release-decision.md) · [Cost calculation](../01-pillar-blueprints/01-process-and-finops.md)
