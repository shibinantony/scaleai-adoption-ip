# Trust and assurance

An invoice reviewer challenges a draft after discovering that its cited policy had expired. The team needs to identify the policy and model used, find the cases exposed to the error, and give the reviewer a way to correct the record. Those are different responsibilities. Operations can suspend traffic immediately. Independent assurance verifies the evidence, Legal determines which obligations apply, and the accountable business executive decides whether to accept the remaining risk. All case evidence stays in the client's private environment.

## Immediate priority · Day 0–90

### TRUST-01 · Put the limits of the approved use on record

Legal and the business owner record the intended purpose, excluded uses, affected people, jurisdictions, data classes, provider and deployer roles, legal rationale, human oversight and next review date. Bind each enabled route to that signed register entry. **Every enabled route must have a current entry.** A prohibited use or missing classification blocks activation. Without this link, approval for internal drafting can be reused to justify a consequential decision no one assessed.

### TRUST-02 · Evaluate the version the team plans to release

Independent assurance approves the evaluation suite. Test the proposed release in the client boundary with a manifest covering the model, prompt, retrieval index, permitted tools and gateway configuration. Verify the origin of the evidence and the cryptographic digest that identifies each version before evaluating the counts. Keep the manifest, adjudication references, raw counts and gate result.

Every mandatory metric must clear both the baseline release policy and any tighter applicable sector threshold. Expired evidence, a different digest or a missing test population blocks release. A real evaluation of yesterday's prompt tells the release manager little about today's changed authorization rules.

### TRUST-03 · Follow a challenge back to the original decision

Keep case ID, source references and the reviewer's disposition in the access-controlled business journal. A client-owned opaque trace ID joins that journal to the permitted route, policy and timing records at the gateway. Give the reviewer a correction route from the case record itself.

For each release, independently select **20 decisions, or all decisions if fewer than 20**. Reconstruct every one and demonstrate that a contested case reaches a reviewer **by the next business day**. Retain the access and reconciliation receipts. A complete log entry alone cannot correct a material error on someone's case.

### What each assurance source asks the team to show

These mappings distinguish evidence about a workload from obligations that apply to a particular organization. In the EU, Legal records the relevant text, role, intended purpose and effective date for each duty at intake and after a material change. [EU AI Act Explorer, including the 2026 amendment](https://ai-act-service-desk.ec.europa.eu/en/ai-act-explorer) · [Commission implementation timeline](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)

- **NIST AI Risk Management Framework 1.0.** For *Govern* and *Map*, an independent reviewer checks whether TRUST-01 covers affected people, foreseeable reuse and fallback conditions. Hold intake until scope, impact and owners are signed. For *Measure* and *Manage*, use the version-specific TRUST-02 results and the TRUST-04 correction, rollback and retest record to authorize or suspend a defined cohort. [NIST AI 100-1](https://doi.org/10.6028/NIST.AI.100-1) · [NIST AI RMF Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/)
- **ISO/IEC 42001:2023.** Map TRUST-01 scope, impacts and ownership and TRUST-05 audit findings, management review and corrective-action records to the organization's licensed standard and statement of applicability. Management uses this evidence to decide when to commission an independent assessment. [ISO standard](https://www.iso.org/standard/42001)
- **MITRE ATLAS, October 2026 catalog.** Count distinct test cases and failures for instruction boundaries (AML.T0051), denial of unauthorized tool calls (AML.T0053) and retrieval access (AML.T0085.000). Signed model admission also addresses model repository risk (AML.T0010.003). Security reviews behaviors the suite did not cover and the remaining exposure of each authorized route. [Pinned MITRE dataset](https://github.com/mitre-atlas/atlas-data/blob/f56c1468731d6428e5bf875263b4643b46d67437/dist/v6/ATLAS-2026.10.yaml)
- **EU AI Act.** Screen for prohibited uses and classify the system under TRUST-01. For an in-scope high-risk deployment, map the deployer's duties to instructions for use, named human oversight, monitoring, logs and escalation. Assess impact-assessment duties separately. For an applicable direct interaction, retain the notice and evidence that users saw it. Legal records the role, trigger, due date, evidence owner and open actions for each duty. Unresolved applicable requirements block the affected scope. [Article 26](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26) · [Article 50](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-50)

### OWASP Top 10 for large language model applications

Use the 2025 risk list to choose acceptance tests. The verifier must be able to retrieve an observed result for each applicable boundary. [OWASP 2025 risk index](https://genai.owasp.org/llm-top-10/)

| Risk | What the verifier checks | What a failure exposes |
| --- | --- | --- |
| LLM01 · Prompt injection | Mark retrieved text as untrusted data. Authorize tools in a separate broker. Across the boundary tests, no instruction in retrieved text changes scope or causes an unauthorized effect. | A document can direct a privileged action. |
| LLM02 · Sensitive information disclosure | Redact restricted fields before inference and telemetry. Seed privacy tests with recognizable values and require zero occurrences in unauthorized outputs or logs. | Client records leave the approved purpose or environment. |
| LLM03 · Supply chain | Pin model, container and dependency versions. Verify signed manifests and reject every unapproved test artifact. | An unreviewed build enters production. |
| LLM04 · Data and model poisoning | Limit corpus imports and tuning jobs to approved source revisions. Quarantine every unsigned test revision. | One altered source can influence an entire caseload. |
| LLM05 · Improper output handling | Validate the business schema and encode fields for the destination. All malformed drafts must reach human review without side effects. | A downstream service can interpret generated text as a command. |
| LLM06 · Excessive agency | Issue short-lived, tenant-bound tool permissions. No denied call or expired approval may change business state. | A drafting service can act for the customer. |
| LLM07 · System prompt leakage | Keep secrets and authorization decisions in separate services. Scan the prompt bundle at release. It must contain zero credentials, and no authorization decision can depend on keeping prompt text secret. | Disclosed instructions can reveal a credential or grant access. |
| LLM08 · Vector and embedding weaknesses | Apply tenant and document access rules before ranking search results and again before display. Return zero inaccessible passages in every forbidden-retrieval case. | Another tenant's content enters an answer or citation. |
| LLM09 · Misinformation | Review claims against authorized source passages. Count any draft with an unsupported material claim once, enforce the release ceiling in each required population and escalate critical errors. | A plausible unsupported claim can change a decision. |
| LLM10 · Unbounded consumption | Reserve tenant tokens and cap concurrency, retries and agent steps. Each over-budget test must stop at the configured limit. | One tenant can exhaust the shared budget or capacity. |

## Ongoing priority · Day 90+

### TRUST-04 · Act when production quality changes

Each week compare adjudicated production cases with the approved baseline by route and affected population. Record severity, reviewer disagreement and reopening rate. Assess **at least 200 substantive drafts** when available. If more than **1%** contain an unsupported material claim, hold the route, use the verified fallback and start the quality incident procedure. Apply tighter limits to sector-critical harms. A confirmed boundary breach or unauthorized action suspends the affected path immediately. Keep the authenticated rollback receipt and case reconciliation. A change in the mix of customers or exceptions can invalidate a pre-release result while the model itself stays unchanged.

### TRUST-05 · Check whether corrective actions worked

Every quarter, an internal auditor independent of implementation selects one live workflow and a closed incident or drill. Follow both through the evidence to verify that corrective actions took effect. Management records its decisions about scope, resources and risk. Require **100% of sampled decisions** to trace to an approved scope, artifact and accountable person, with **zero overdue critical corrective actions** at the readiness review. Retain findings, management minutes and verified closure. A ticket marked closed can otherwise hide an unresolved nonconformity.

### TRUST-06 · Examine the people behind the average

Changes to model, data source, geography or agent authority require fresh scope, evidence and approval. Where lawful and meaningful, compare reviewer acceptance and material errors across comparable affected groups. For this pilot, an absolute acceptance gap **greater than 10 percentage points**, with **at least 100 cases per group**, opens an investigation and holds expansion. Identify smaller groups as unassessed. When the relevant attributes cannot be used, record why and agree an alternative such as reviewed scenario tests. A portfolio average can conceal a service that works poorly for one group.

Record the numerator, denominator, severity, sample selection, reviewer disagreements, proposer, separate verifier and expiry with the decision. Zero observed failures describes the tested sample. Use an authorized client runner to publish the signed evidence index and digests to a write-protected store inside the client virtual private cloud or disconnected enclave. Public continuous integration checks use synthetic cases. [Runnable policy kit](../04-policy-as-code-templates/README.md) · [Operating cadence](../03-client-execution-kit/day-90-plus-ongoing-runbook.md)
