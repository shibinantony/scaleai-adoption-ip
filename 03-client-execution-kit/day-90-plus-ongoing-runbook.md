# Day 90+ · Operate and expand

The service owner runs the operating review for the approved tenant and workflow. The sponsor funds staff time for review, fallback and assurance alongside inference. A new tenant, data source, agent capability or decision right changes what can go wrong. Assess that change and obtain approval before extending the service.

## During a shift

**On every request, the platform on-call owns the checks.** Verify the tenant's identity, current access rights, permitted route, remaining budget and working audit path. If a prerequisite fails, deny the request, prevent side effects and send recoverable cases to the manual queue. Write the decision to client-owned storage. If that storage is down, hold the draft and reconcile the missing event when the store recovers. A confirmed boundary breach or unauthorized action suspends the affected path immediately.

**Once a day, the workflow owner accounts for the queue.** Match every eligible case ID to a pending, assisted or manual disposition. Investigate unexplained IDs and repeated breaches of the approved queue-age target before adding traffic. On replay, reuse the original case ID so one invoice cannot become two cases. Keep the counts, oldest case age and available reviewer capacity at shift handoff.

## At the weekly review

Bring quality and cost to the same meeting. The quality sample counts substantive drafts. The financial sample counts eligible cases that have completed the seven-day reopen window. Use each denominator for its own decision.

| Owner | What to measure | When to intervene |
| --- | --- | --- |
| Independent quality lead | Compare unsupported material claims and abstentions with the baseline for each affected route and material case group. Accumulate at least **200 substantive drafts** per quality decision. Show all eligible cases, exclusions and severity alongside the sample. | A confirmed critical error starts incident review immediately. Above **1%** unsupported material claims, or above a tighter sector limit, hold the route. Use a verified compatible version or manual review and repeat the release gate. Low volume holds expansion. |
| Finance partner | Reconcile actual spend and accepted outcomes for settled cohorts. Recheck model mix and seven-day reopens against comparable manual work. | Freeze new allocation when cost per accepted outcome is **above 80%** of the matched manual cost or acceptance is **below 85%** for two consecutive eligible weekly windows. The invoice example uses at least 50 eligible cases per window. Pool smaller samples and keep their counts visible. |

When cost breaches a limit, Finance separates price changes, volume, case mix, repeat requests and reviewer time. Keep the signed explanation of the variance. A lower-cost model must pass the same quality floor before it can take traffic.

## At change, recovery and investment reviews

**For each material change, the release manager qualifies the exact deployment.** Build a fresh evidence manifest that identifies the model, prompt, policy, retrieval index, tool permissions and deployment scope. Test changed behavior alongside prior regression cases. An independent assessor checks who produced the evidence and the decision it supports. Promote the approved candidate, revoke the old manifest after switching traffic and retain a compatible rollback bundle.

**Monthly, the platform lead runs a recovery drill.** Revoke a synthetic tenant's access, simulate unavailable dependencies, restore service and exercise the on-call handoff. Every open case ID must reach its owner exactly once, and the service must reach an authorized route within **15 minutes**. A failed restoration freezes expansion. Record the drill result and the person responsible for the correction.

**Quarterly, the accountable executive decides whether to continue, expand within a cap, reduce or retire.** Review service value, complaints, subgroup outcomes where appropriate, legal changes and material incidents. Independent internal audit traces a sample from release to human action. Record the audit scope, open risks, resources, owners and deadlines. Close overdue critical actions before an ISO/IEC 42001 readiness decision.

## When the inputs change or a boundary fails

1. **Size the change.** Break down input class, language, abstentions and source freshness by tenant and route. For the invoice pilot, a shift of **at least 10 percentage points** in a case type's share compared with the previous four weeks starts analyst review. If the denominator is unknown, report quality as undetermined.
2. **Contain a boundary failure immediately.** Disable the affected route, revoke its tool grant and page Security and the workflow owner. Quarantine drafts, preserve a restricted incident snapshot and hand every open case to a person. Consult counsel about notification duties and deadlines.
3. **Find the cause.** Compare the deployed versions with the last working bundle. Check corpus membership, entitlements, prompt and model versions, the evaluator, traffic mix and reviewer labels. Record the affected period and potentially affected case IDs inside the client environment.
4. **Verify the repair.** Have reviewers score the affected cases again. Replay both the regression cases and the boundary checks. Independent assurance verifies fresh, authenticated gate evidence and a successful timed restoration.
5. **Restart under supervision.** Security and the workflow owner authorize a small cohort. The service owner confirms staffing and Finance confirms budget. Wait until the signed observation window settles before expanding. Link the incident, affected decisions, corrective action and new release record.

## When a second tenant or agent is proposed

Run the proposed scope in shadow on an authorized group of comparable cases. For an agent chain, set a single ceiling for total steps, tokens and elapsed time and give each step only the permissions it needs. A human retains every final business action. The architecture owner demonstrates that one tenant can be suspended independently. Bring the steering group the independent release decision, incremental budget and comparisons of accepted outcomes, unsupported claims, subgroup effects, latency and fully loaded cost.

If the board retires the workflow, send open cases to the manual team, revoke secrets and tool grants, and stop billing reservations. Expire tenant artifacts under the approved records schedule and any legal holds. The accountable owner signs off on all cases and the final cost statement. [Assurance blueprint](../01-pillar-blueprints/05-trust-and-assurance.md) · [Policy kit](../04-policy-as-code-templates/README.md) · [Worked decision](worked-release-decision.md)
