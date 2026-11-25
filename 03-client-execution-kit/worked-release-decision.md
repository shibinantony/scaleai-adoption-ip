# Decision memo · Keep invoice drafting in the current finance queue

**Approve a further 30 days for one finance tenant, one currency and one staffed English-language queue.** The service may draft an explanation for an invoice exception. An accounts-payable analyst checks the sources. Only an authorized employee may close the case or authorize a ledger action. Keep the limits at 200 cases a day and $6,000 in total operating cost for the period.

This is an illustrative decision using synthetic data. All amounts are in US dollars.

## What Finance can support

Of 1,000 eligible cases, analysts accepted the draft in 900. They finished the other 100 manually. All 1,000 cases cleared the seven-day window for reopening. Two consecutive weekly groups within that total each had 250 eligible cases, 225 accepted drafts and $1,350 in costs.

| What Finance measured | Result |
| --- | --- |
| Cost of an accepted assisted case, including the work spent on the 100 manual cases | $5,400 ÷ 900 = **$6.00**. Finance set the ceiling at $6.40, or 80% of the $8.00 manual baseline. |
| Cost of closing a case by either route | $5,400 ÷ 1,000 = **$5.40**. Every eligible case closed. |
| Cost difference at 1,000 comparable cases a month | $8,000 manual cost less $5,400 operating cost = **$2,600 per month** before setup costs. Record where the released hours go. Finance can recognize a cash saving once spending actually falls. |

The 90% acceptance rate and the $6.00 unit cost support keeping this queue open. [Cost definition and ledger](../01-pillar-blueprints/01-process-and-finops.md)

## Why the approval stays narrow

Two of 200 substantive drafts contained a material claim that their sources did not support. That is exactly the 1% limit. A real citation can lead to the correct document and still misrepresent what it says. Keep human review on every case and have independent reviewers sample drafts weekly. Three such drafts out of 200 would take the error rate to 1.5% and hold the release. The workflow owner would send cases through the manual queue while the team investigated. Reopening would require fresh evidence and a new human decision.

The qualification sample recorded no severe toxicity in 200 reviewed outputs. Each of the eight other required checks, including tenant isolation and human approval, recorded zero failures in 20 cases. During the fallback drill, all 40 open cases reached the manual queue exactly once in 12 minutes, inside the 15-minute limit. In a separate review of 20 cases, all 20 could be traced from the original source version to the analyst’s final decision. [Release checks and synthetic evidence](../04-policy-as-code-templates/README.md)

## Terms for the next shift

The accounts-payable supervisor checks the oldest pending case daily. The supervisor and the incident commander can each suspend drafting. Confirmed unauthorized access, an unauthorized action or a critical material error stops the service for the affected queue. An additional tenant or language needs its own risk assessment, evidence and budget.

**Approval record FIN-EX-01, revision 7.** The scope is `demo/invoice-exception-draft`. In a client deployment, the controller identifies the exact candidate by its cryptographic digest and independent assurance supplies the digest of the approved test suite. Finance validates the cost, the platform owner accepts support, the CISO verifies isolation, and independent assurance signs off on the evidence. The COO accepts the remaining business risk for this scope. File the names, signatures, decision date and expiry in the client’s private record.
