# Day 0 discovery diagnostic

**Use in a 90-minute intake.** The delivery lead brings the process owner, platform engineer, security architect, finance partner and independent risk reviewer together around one named workflow and tenant. Start with a real queue and aggregate baseline counts. Keep client evidence in the client environment. Output a five-pillar profile, a list of blocking gaps with named owners and a decision on the next tranche of work.

## How to score a workflow

Each row has five cumulative evidence checks in increasing order of maturity. Mark each check **verified** only when a reviewer can locate a dated artifact for this scope and its owner. A verbal commitment earns no credit. Count the consecutive verified checks from the left, stopping at the first gap. Record that count as evidence depth (0–5). The pillar score is the higher of 1 and evidence depth. Flag a depth of zero as **unverified**. Record later verified checks as strengths even when an earlier gap caps the score.

| Pillar | 1 · Identify | 2 · Design | 3 · Demonstrate | 4 · Operate | 5 · Expand |
| --- | --- | --- | --- | --- | --- |
| Process | Can the owner show the existing case queue and decision right? | Are the baseline, eligible cohort, acceptance definition and budget recorded? | Does a sampled case show human disposition and manual fallback? | Do two settled cohorts reconcile cost, acceptance and reopens? | Has finance checked realized capacity or margin after a scope expansion? |
| Technology | Is the inference and retrieval inventory versioned? | Does the route specify data class, authorized sources and budget? | Does a frozen test set demonstrate grounding, abstention and routing? | Can the owner show monitored drift and a tested rollback bundle? | Has a replacement model or bounded agent step passed a paired evaluation? |
| Tools | Can operators locate the gateway and the client-owned event sink? | Are identity, redaction, rate and cost rules configured with owners? | Has a private rehearsal shown fail-closed rules and delivery of audit events? | Can on-call staff reconcile dropped events and repeat a guardrail drill? | Are evaluations, configuration changes and incident receipts linked across two approved scopes? |
| Architecture | Is the tenant boundary and each data flow recorded? | Are keys, retrieval, cache, identities, egress and tools restricted by design? | Do private tests deny disallowed access and preserve the first tenant’s manual route? | Has the team restored an approved deployment with its policies and records? | Has an isolation and revocation drill passed with a second synthetic tenant? |
| Trust and assurance | Are the intended use, accountable executive and assessor named? | Is there a signed risk and obligation register with applicable controls? | Has an independent reviewer verified candidate-bound evidence and the stop procedure? | Are incidents, changes, overrides and due corrective actions reviewed on schedule? | Can an internal auditor reconstruct an outcome and verify closure of a corrective action? |

There are 25 checks. Report the five pillar scores separately and their sum (5–25). The total helps allocate discovery effort. A single hard stop below holds the affected release at any score.

| Diagnostic disposition | Decision and owner |
| --- | --- |
| Total 5–12 or any pillar unverified | Sponsor funds scoped discovery and control design. Keep production traffic on the manual route. |
| Total 13–19 and all pillars have evidence | Delivery lead may request shadow evaluation in the approved environment. A supervised canary requires every pillar ≥3, all release gates passing and the named approvals. |
| Total 20–25 with a pillar below 3 | Delivery lead keeps work in shadow until each lagging pillar demonstrates its controls. An unverified pillar returns the workflow to discovery. |
| Total 20–25 and no pillar below 3 | Steering group can consider expansion after two settled weekly cohorts, verified capacity and fresh scope-specific evidence. |
| Missing lawful purpose or data permission, unbounded egress, cross-tenant disclosure, unauthorized action, third-party training, missing client audit custody, missing human or manual fallback | Security or the process owner blocks production use, names a remediator, records a due date and retests the specific boundary. The score cannot override this decision. |

**Worked intake.** A synthetic invoice workflow verifies four, three, two, three and three consecutive checks respectively. Record **4 / 3 / 2 / 3 / 3 = 15/25**. Tools has a design record but lacks an observed deny-and-audit receipt. The delivery lead can schedule shadow evaluation after environment approval. The platform owner must demonstrate the receipt before the COO can consider a canary.

**Meeting close.** For each failed check, record workflow, check number, finding, artifact reference, accountable individual, due date, retest and decision. For example, the invoice pilot’s Tools 3 finding links the missing audit receipt to design record GW-07. The platform lead owns a day 14 retest with the sink disabled. The delivery lead keeps the canary on hold. Publish the profile, decision and next review date in the client risk register. [Master matrix](../00-executive-overview/5x2-master-matrix.md) · [Immediate runbook](day-0-90-immediate-runbook.md)
