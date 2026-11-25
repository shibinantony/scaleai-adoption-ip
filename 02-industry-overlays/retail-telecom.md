# Retail and telecom

“Does this plan include roaming?” belongs on a public help page. “Why did you charge me for roaming yesterday?” needs an authenticated billing agent. A retailer faces the same split between publishing a return policy and disclosing the status of someone’s refund. Separate those routes before opening a single storefront or carrier brand to traffic.

## Day 0–90 · Open the public help page

Start in one market and language. Fetch the current price, currency, eligibility, expiry and exclusions from the approved offer service at request time. The assistant can explain approved terms. Account-specific billing, disputed charges and changes to service stay with authenticated support. Serving, telemetry and cache remain within the client tenant, with third-party prompt training disabled.

**Merchandising or carrier compliance checks what the customer will see.** Across at least 200 substantive conversations per market and language, require zero wrong prices, unsupported material product claims, disallowed brand language or missing mandatory disclosures. All 40 cases with expired or conflicting terms must produce an explicit abstention or a handoff to support with the source reference. A single outdated promotion can mislead everyone arriving from the same campaign. US retail marketing owns the supporting evidence for objective advertising claims. [FTC advertising guidance](https://www.ftc.gov/business-guidance/resources/advertising-faqs-guide-small-business)

**The contact-center owner tests the transfer to an agent.** The public service has no access to individual accounts. At handoff, reauthenticate through the approved channel, verify the account and tenant again, and log only the decision. Personalized requests and responses bypass shared caches. Across 100 anonymous, wrong-account or expired-session cases, require zero shared-cache reads or writes for personal data and zero disclosures of orders, usage or customer proprietary network information (CPNI). Carrier privacy counsel identifies the covered data and approves the channel’s authentication and disclosure process under applicable US CPNI rules. [47 CFR §64.2010](https://www.ecfr.gov/current/title-47/chapter-I/subchapter-B/part-64/subpart-U/section-64.2010)

### Rehearse a promotion or service outage

Customer care and site reliability engineering agree the traffic mix, per-tenant inference limit and staffed overflow capacity. Rehearse with both warm and cold caches. When capacity runs out, serve approved static terms or send the customer to a person. Without a limit, a slow model can build both an online queue and a contact-center backlog.

| Pilot load | Pass at that load |
| --- | --- |
| 80 requests/second for 20 minutes, up to 250 concurrent sessions | p95 first visible answer ≤2 seconds. p95 complete answer or handoff ≤6 seconds. Count timeouts as breaches. |
| All arrivals during the rehearsal | Technical errors ≤0.5% of arrivals. Overload handoffs ≤5% of arrivals. |

Marketing or carrier compliance signs the claims and access tests. Customer care signs the rehearsal and confirms staffing. A wrong active offer, an account disclosure or a cross-customer cache hit closes the affected route. Evict its cache, switch to approved static terms or staffed service, and retain the campaign version, trace and affected-session list in the client environment. [First-release plan](../03-client-execution-kit/day-0-90-immediate-runbook.md)

## Day 90+ · Decide which answers are worth caching

Cache only approved public explanations. Match tenant, brand, market, language, intent, policy version and disclosure version before considering a semantic match. Look up prices, eligibility and personal details separately. Invalidate on catalog or policy publication, with a five-minute expiry as a backstop. Route unresolved versions to an agent. In 200 same-intent cases across markets, brands and revisions, permit zero cross-scope hits or superseded claims. Changed entries must stop serving within 60 seconds of publication.

A closed chat can still produce a second call. Join corrections, upheld complaints and repeat contacts to the original tenant-scoped session. Each week, sample promotions and outages as well as ordinary traffic in each market. Before expanding, require two consecutive weekly cohorts that have completed the seven-day follow-up. Each needs at least 200 audited substantive responses, zero material brand or price errors and a same-intent recontact rate no higher than its matched manual cohort.

Count a resolution once, after confirmation or a verified completed outcome and seven days without a same-intent reopening. Include tokens, cache, infrastructure, handoffs, support labor and refunds attributable to errors. An illustrative **$2,100 for 1,400 accepted resolutions is $1.50 per resolution**. Compare that figure to the matched manual channel alongside the cache hit and recontact rates. Defer the margin decision until the cohort matures and has at least one accepted resolution. [Ongoing runbook](../03-client-execution-kit/day-90-plus-ongoing-runbook.md)
