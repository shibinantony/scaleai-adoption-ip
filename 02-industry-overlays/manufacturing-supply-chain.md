# Manufacturing and supply chain

Which asset warrants inspection on the next shift? Start with one asset family. Send proposals to the existing computerized maintenance management system (CMMS), where a planner can accept or dismiss each one. Compare the proposals against the alarms the site already uses before connecting the service to purchasing.

## Day 0–90 · Commission a read-only advisory

Start at the plant drawing. The operational technology (OT) owner marks the historian, the industrial demilitarized zone (DMZ) and the client’s analytics enclave. Export only the historian fields approved for that site, tenant and asset, using a one-way transfer where the site design requires it. Keep inference, keys and access logs in the enclave. Disable external egress and third-party training.

Before connection, the OT owner checks effective firewall rules, service identities and recorded flows offline. Require **zero reachable controller, safety or engineering interfaces**, zero control credentials in analytics and a match to the approved manifest for every transfer. This boundary keeps an incident in corporate analytics from reaching equipment that controls the process. [NIST SP 800-82 Rev. 3, OT security](https://csrc.nist.gov/pubs/sp/800/82/r3/final)

The safety manager determines where US hazardous-energy requirements apply to servicing and maintenance. A proposal can cite an approved procedure identifier. Authorized personnel select and carry out the procedure. Keep existing alarms, interlocks and maintenance authorization in service throughout the trial. [OSHA 29 CFR 1910.147](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.147)

### What earns a place in the planner’s queue?

Use a site with independent alarms, labeled maintenance history and an established manual queue. The plant manager, safety manager and OT owner agree the thresholds for the selected asset family before the trial.

| On the commissioning sheet | Evidence required |
| --- | --- |
| Correct machine and reading | Match serial number, sensor revision, units and timestamp. Reject missing, duplicate or out-of-order intervals. The pilot feed arrives every five minutes. Suppress proposals when the newest reading is over ten minutes old. All 60 stale, wrong-unit or cross-asset cases must be suppressed. A work request on the wrong machine wastes an inspection. |
| Enough time to act | Across at least 200 valid intervals, p95 time from batch arrival to proposal must be at most 60 seconds. Count overdue work as a breach. Agree the useful warning interval for each operating regime before scoring alerts. |
| Enough signal to justify the inspections | Reliability engineers replay histories held out by asset and date, in time order. Detect at least 90% of 50 or more labeled inspection events within the agreed warning interval. Of at least 100 issued proposals, 80% or more must warrant inspection. Record zero suppressed existing alarms and zero generated substitutes for approved work instructions. |

The OT owner signs the topology and the reliability engineer signs the replay. The planner takes accepted proposals through the CMMS. If the boundary fails or stale or wrong-asset advice gets through, close the analytics feed and withdraw unreviewed drafts. Existing monitoring and maintenance planning continue. [First-release runbook](../03-client-execution-kit/day-0-90-immediate-runbook.md)

## Day 90+ · Add a plant or a purchasing step

**Another plant needs its own replay.** Review performance monthly by asset family and operating regime. Sensor replacements and maintenance-policy changes trigger a fresh replay. Apply the original precision, recall and sample-size requirements to each new regime. Keep undersampled regimes in shadow. Compare proposal volume with the planner’s signed shift capacity. Five consecutive shifts over capacity suspend new proposals before the backlog masks urgent work.

**A work order can justify a draft requisition.** A restricted service reads the authorized work order, then checks plant, supplier, part and quantity against the controlled catalog. Deduplicate on work-order and line-item IDs. Across 100 simulated retries and supplier or part substitutions, require zero duplicate or unauthorized requisitions. The buyer approves every commitment through procurement. A repeated reservation can tie up the last spare even if no purchase order has been sent.

**Price the proposal.** Finance counts monthly historian replication, secure infrastructure, inference, planner review and time spent on rejected suggestions. For example, **$1,800 / 120 unique planner-accepted proposals = $15 per proposal**. Report verified findings per inspection and observed downtime against comparable assets. The plant controller signs off any claim of avoided downtime. With no accepted proposals or a failed quality test, defer the next site. [Ongoing runbook](../03-client-execution-kit/day-90-plus-ongoing-runbook.md)
