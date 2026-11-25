# Day 0 discovery diagnostic

Use this 90-minute meeting to decide how far one tenant's workflow can proceed. The delivery lead facilitates. Invite the process owner, a platform engineer, a security architect, a finance partner and an independent risk reviewer. Ask them to bring the existing case queue, aggregate baseline counts and links to evidence in the client environment.

## Open with one case

Ask the process owner to trace a recent case from arrival to final decision. Establish who can see it, who decides it and where it goes when the service is unavailable. Write the tenant, workflow and intended use at the top of the meeting record. Score only what the group can verify for that scope.

## Ask the 25 questions

Read each pillar in order. Question 1 asks the team to identify what exists. Questions 2 through 5 cover design, demonstration, operation and expansion. For each answer, record the owner and a dated artifact that the reviewer can open. Leave an unsupported answer unverified.

### Process

1. Can the owner show the current case queue and identify who can make the final decision?
2. Where are the baseline, eligible cases, acceptance definition and budget recorded?
3. Does a sampled case show how a human makes the decision and how the team falls back to manual handling?
4. Can Finance reconcile costs, accepted cases and reopens for two groups of cases whose reopen windows have closed?
5. After an expansion, has Finance checked where released capacity went or how much margin improved?

### Technology

1. Can the engineer identify the versions of the models and retrieval systems in use?
2. For each route, where are the permitted data class, authorized sources and budget recorded?
3. Does a frozen test set show when the service can ground an answer in its sources, when it should abstain and which model it selects?
4. Can the owner show drift monitoring and a tested set of versions and policies to restore?
5. Has a replacement model or a bounded agent step passed a comparison on the same cases as the approved version?

### Tools

1. Can operators locate the gateway and the client-owned store for audit events?
2. Are identity, redaction, rate and cost rules configured, each with an owner?
3. Has a private rehearsal shown that a failed check blocks the request and delivers its audit event?
4. Can on-call staff account for dropped events and repeat a guardrail drill?
5. Can the reviewer trace evaluations, configuration changes and incident records across two approved scopes?

### Architecture

1. Is the tenant boundary documented, including each flow of data across it?
2. Does the design restrict keys, retrieval, cache access, identities, outbound connections and tools?
3. Do private tests deny disallowed access while keeping the first tenant's manual route available?
4. Has the team restored an approved deployment together with its policies and records?
5. Has the team passed an isolation and access-revocation drill with a second synthetic tenant?

### Trust and assurance

1. Are the intended use, accountable executive and assessor named?
2. Is there a signed register of risks, applicable obligations and controls?
3. Has an independent reviewer verified that the evidence belongs to the candidate under review and that the stop procedure works?
4. Does the team review incidents, changes, overrides and due corrective actions on schedule?
5. Can an internal auditor trace one outcome back to its evidence and verify that a corrective action was closed?

## Score each pillar

Count consecutive verified answers starting at question 1. Stop at the first gap. This count, from 0 to 5, is the **evidence depth**. Use the depth as the pillar score, with a minimum score of 1. At depth zero, write **1, unverified** so that nobody mistakes the scoring floor for evidence. Note any later verified answers as strengths to revisit after the gap closes.

Record all five pillar scores and their sum, from 5 to 25. Before considering the total, check for a production stop. Security or the process owner blocks production on any of these findings.

- A missing lawful purpose or data permission, unbounded outbound access or confirmed cross-tenant disclosure.
- An unauthorized action, third-party training on client data or missing client custody of audit records.
- No human decision-maker or no working manual fallback.

Name a person to correct the finding, give it a due date and retest the affected boundary. A high total cannot clear it.

| Result after the stop check | Decision |
| --- | --- |
| Any unverified pillar, or total 5–12 | The sponsor funds discovery and control design. Production stays with the manual team. |
| Total 13–19, with evidence for every pillar | The delivery lead may request an approved shadow comparison, where the team generates drafts while staff complete the real cases. A supervised canary can be considered only when every pillar scores at least 3, all release gates pass and the named approvers sign. |
| Total 20–25, with a verified pillar below 3 | Stay in shadow while the owner demonstrates the missing controls. |
| Total 20–25, every pillar at least 3 | The steering group may consider expansion after two settled weekly cohorts, verified capacity and fresh evidence for the proposed scope. |

## Close with a decision someone can act on

In the synthetic invoice pilot, the scores are **4 / 3 / 2 / 3 / 3 = 15/25**. Tools has a design record, GW-07, but nobody has seen the gateway deny a request and account for it. The delivery lead can schedule an approved shadow comparison. The platform lead owns a day 14 retest with the audit sink disabled. The COO's canary decision waits for that evidence.

For each open check, record the workflow, pillar and question number, finding, artifact reference, accountable individual, due date, retest and release decision. Put the five scores, today's decision and the next review date in the client risk register. [Master matrix](../00-executive-overview/5x2-master-matrix.md) · [Immediate runbook](day-0-90-immediate-runbook.md)
