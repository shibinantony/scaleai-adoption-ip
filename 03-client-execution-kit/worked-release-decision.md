# Worked director decision · Finance operations

**Decision: continue the internal invoice-exception service for one tenant.** This synthetic record shows how a steering group can approve a bounded service and decline a wider rollout at the same meeting. Figures illustrate the framework and do not describe a client deployment.

| Decision field | Example entry |
| --- | --- |
| Purpose and authority | Draft a cited explanation of an invoice/order/receipt mismatch for an accounts-payable analyst. One finance tenant, one currency and one staffed English-language queue. Only an authorized employee can close a case or authorize a ledger action. |
| Candidate and scope | Record FIN-EX-01, revision 7, scope `demo/invoice-exception-draft`. In implementation the controller supplies the immutable candidate digest and the assurance lead supplies the approved suite digest. The public fixture demonstrates this join. |
| Economic question | Can the team resolve the same case mix with less operating cost while maintaining the approved quality and service levels? Finance sets a ceiling of USD 6.40 per accepted assisted outcome (80% of the USD 8.00 manual baseline). |
| Cohort | 1,000 eligible cases settled after a seven-day reopen window. 900 assisted drafts accepted, 100 cases closed by the manual route, zero unresolved cases. Two consecutive settled weekly slices included 250 eligible cases each, with 225 accepted in each and USD 1,350 spent in each. |
| Economics | USD 5,400 total / 900 distinct accepted assisted outcomes = USD 6.00. The full pathway cost per closed case is USD 5.40. Acceptance is 90%. At 1,000 cases/month the difference from the USD 8,000 manual comparator is USD 2,600/month before one-time cost. Finance records released capacity until budget realization is evidenced. |
| Quality and containment | In the illustrative qualification set, 2/200 substantive drafts contain an unsupported material claim, 0/200 outputs contain severe toxicity, and each of the eight mandatory defensive or operational metrics has 0/20 failures. Boundary and human-approval drills pass. Public CI uses synthetic data to demonstrate the arithmetic. |
| Operational receipts | A rehearsal redirected all 40 open case IDs exactly once in 12 minutes against a 15-minute limit. In the illustrative review sample, 20/20 cases link the original source version to the reviewer disposition. The incident commander and accounts-payable supervisor can each suspend traffic. |
| Conditions and expiry | Authorize the same operating scope for 30 days at up to 200 cases/day and USD 6,000 total operating cost for the period. Review the oldest pending case daily. Stop automated drafting on confirmed unauthorized access, an unauthorized action or a critical material error. |
| Residual risk and next decision | Source citations can be valid while their interpretation is wrong. Two observed unsupported drafts place this sample at the ceiling. Keep full human review and weekly independent sampling. An additional tenant or language returns for its own classification, evidence and budget. |
| Decision rights exercised | Finance validates cost, the platform owner accepts support, CISO verifies isolation, independent assurance signs evidence sufficiency and the COO accepts residual risk for the stated scope. Record actual names, dates, signature references and decision expiry in the private deployment. |

### How to read the two unit costs

USD 6.00 answers what the organization spent to obtain one accepted AI-assisted case, including the cost of rejects and fallback. USD 5.40 answers what it spent per closed case across both routes. A director comparing another pilot needs both denominators, plus manual cost for a matched population. [Full cost ledger](../01-pillar-blueprints/01-process-and-finops.md)

### If one number changes

Three unsupported drafts in 200 would give **1.5%**, above the approved 1% ceiling. The release manager would hold promotion even at USD 6.00 per accepted outcome. The workflow owner would retain the manual path while the team investigates source selection and reviewer adjudication. A successful rerun still needs a new human decision. [Runnable gate and evidence fixture](../04-policy-as-code-templates/README.md)
