# The investment decision

Fund one workflow whose owner controls the queue, the reviewer roster and the outcome measure. Release funding in stages. Extend the deployment only when the sponsor can name what improved, who can stop the service and what a second tenant would cost to serve.

## Board scorecard

Each cell is a question the named executive can answer from the evidence pack. Set targets against one service, tenant, population and observation window. Break down measures by material case type before comparing results.

| Pillar | CIO · service delivery | CISO · exposure | COO · operating result | CFO · economics |
| --- | --- | --- | --- | --- |
| Process | Share of eligible cases linked to one end-to-end trace | Share of final actions attributed to an authorized reviewer | Accepted cases / eligible cases, reopen rate and queue age | Fully loaded cost per accepted outcome vs. matched manual baseline |
| Technology | p95 time from request to draft, by model route | Number of routes with unapproved data processing | Drafts with unsupported material claims / reviewed substantive drafts | Separate inference, retrieval and reviewer costs per route |
| Tools | Requests with complete decision telemetry / total gateway requests | Unredacted restricted fields found in exported telemetry | Share of rejected or timed-out drafts delivered to the manual queue | Spend consumed by retries and cache misses per 1,000 eligible requests |
| Architecture | Time to restore a signed, known-good deployment | Observed cross-tenant reads and unapproved egress events | Open case IDs successfully reconciled during failover / open cases | Private infrastructure allocation per active tenant and accepted case |
| Trust and assurance | Candidate releases with current, bound evidence / all release candidates | Open critical control failures and time to suspension | Decisions that can be reconstructed from evidence / sampled decisions | Unclosed assurance actions by due date and funded remediation cost |

## Decisions and delegated authority

| Decision | Decision right | Evidence and rule for the invoice pilot |
| --- | --- | --- |
| Fund discovery | Business sponsor and finance partner | Approve a capped discovery allocation when an accountable owner, eligible queue and manual baseline can be identified. Defer a production commitment until the baseline is measured. |
| Open a canary | COO authorizes scope after independent assurance, CISO boundary sign-off and CIO operational acceptance | Restrict the first cohort to one tenant, draft-only use and a staffed review queue. Each required automated gate must pass, and operations must demonstrate rollback in ≤15 minutes. |
| Suspend service | On-call operations may stop traffic immediately. Security leads containment for data events. | One confirmed boundary breach or unauthorized write disables the route. Continue the manual queue, preserve client-owned evidence and reconcile case IDs. |
| Expand funding | Sponsor accepts residual business risk and finance approves the next tranche | Pilot target is ≥85% assisted acceptance and ≤80% of manual unit cost on ≥200 settled eligible cases, with quality and boundary gates passing. Approve one named new scope and a fresh budget. |
| Retire | Process owner and platform owner | Route outstanding cases to people, reconcile outcomes, revoke credentials and remove tenant artifacts according to the approved retention schedule. Retain the closure decision. |

The example pilot's USD 6.00 per accepted assisted outcome clears a USD 6.40 ceiling. Its finance partner would still need evidence of an actual budget reduction to recognize cash savings. A low unit cost cannot authorize data access or override the CISO's boundary decision. [Worked release decision](../03-client-execution-kit/worked-release-decision.md) · [Cost definition](../01-pillar-blueprints/01-process-and-finops.md)
