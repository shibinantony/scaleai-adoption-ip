# ScaleAI Enterprise Adoption Framework

**A director’s field guide to onboarding enterprise AI responsibly and deciding when it is ready to scale.**

Consider an invoice that fails a three-way match. A private AI service retrieves the purchase order and receipt, checks the variance and drafts an explanation. An accounts-payable analyst decides what happens to the invoice. This framework shows the director funding that service how to measure the cost of an accepted outcome, limit what the system can do and decide whether to expand or stop it.

Version **1.0.0** · Published by **Shibin Antony** · Independent, vendor-neutral framework for enterprise AI adoption. [Citation](CITATION.cff) · [Licence and attribution](NOTICE.md)

## Start with the decision in front of you

| If you are deciding… | Open this first | Leave with |
| --- | --- | --- |
| Which workflow deserves funding? | [Executive scorecard](00-executive-overview/cxo-value-proposition.md) and [Day 0 diagnostic](03-client-execution-kit/day-0-discovery-diagnostic.md) | A ranked use case, a named risk owner, the manual baseline and the gaps that block a pilot. |
| What must be ready for the first release? | [Five-pillar operating matrix](00-executive-overview/5x2-master-matrix.md) and [Day 0–90 runbook](03-client-execution-kit/day-0-90-immediate-runbook.md) | A private deployment boundary, a staffed review queue, a tested fallback and an evidence-backed release decision. |
| Can we expand to another team, model or tenant? | [Worked director decision](03-client-execution-kit/worked-release-decision.md) and [Day 90+ runbook](03-client-execution-kit/day-90-plus-ongoing-runbook.md) | A scoped authorization with unit-cost and quality limits, a rollback owner and an expiry date. |
| How do I test the release rules? | [Runnable policy kit](04-policy-as-code-templates/README.md) | A reproducible pass/fail decision on synthetic evidence and an integration contract for a private client runner. |

## What changes between onboarding and scale

**Day 0–90.** Select one or two high-value workflows. Redesign the handoff to a human, establish the tenant boundary, deploy a private gateway and qualify a single bounded release. Fund a supervised canary only when the team can show what happens when a model, reviewer or audit dependency is unavailable.

**Day 90+.** Compare production quality and cost against the signed baseline. A new tenant, model or agent permission creates a new decision. Run regression checks, rehearse tenant-specific rollback and bring unresolved risk, margin and audit findings back to management.

| Pillar | Question the owner must answer |
| --- | --- |
| [Process and FinOps](01-pillar-blueprints/01-process-and-finops.md) | What counts as an accepted outcome, and what does it cost after human review, retries and fallback? |
| [Technology](01-pillar-blueprints/02-technology-stack.md) | When should a rule, a private small model or a larger model handle a case, and when should the system abstain? |
| [Tools](01-pillar-blueprints/03-tooling-ecosystem.md) | Where are authentication, guardrails, evaluation, budget checks and audit receipts enforced? |
| [Architecture](01-pillar-blueprints/04-reference-architecture.md) | Which components can read this tenant’s data or invoke a tool, and how can those rights be revoked? |
| [Trust and assurance](01-pillar-blueprints/05-trust-and-assurance.md) | Which evidence supports the release, which obligations apply, and who can suspend it? |

### A worked funding decision

In the synthetic finance case, **900 of 1,000 eligible cases** reach a reviewer-accepted assisted outcome. Total operating cost is **USD 5,400**, including the 100 cases handled manually. That gives **USD 6.00 per accepted assisted outcome** against a manual baseline of **USD 8.00**. The director can continue the authorized queue. A new tenant still needs its own evidence. Moving from two to three unsupported drafts in a sample of 200 would block release even at the same cost. [See the decision, cost calculation and stop conditions](03-client-execution-kit/worked-release-decision.md)

## Adapt the controls to the sector

| Operating context | Decision the sector guide addresses |
| --- | --- |
| [Banking and insurance](02-industry-overlays/bfsi-banking-insurance.md) | Can an investigator or examiner rely on a draft evidence packet without exposing card or case data? |
| [Healthcare and life sciences](02-industry-overlays/healthcare-life-sciences.md) | Can clinical and quality teams verify a draft against the authorized record before it affects a patient or a regulated record? |
| [Manufacturing and supply chain](02-industry-overlays/manufacturing-supply-chain.md) | Can maintenance teams act on an advisory while keeping plant controls and safety functions isolated? |
| [Retail and telecom](02-industry-overlays/retail-telecom.md) | Can a high-volume service preserve offer accuracy, subscriber privacy and margin at peak traffic? |

## Run the release example

From the repository root with Python 3.11 and a virtual environment active, run these commands. The fixture includes only invented records.

```sh
python -m pip install -r 04-policy-as-code-templates/requirements.txt
python 04-policy-as-code-templates/evaluate_release.py --demo
```

A `DEMO PASS` checks the sample against the release thresholds. For deployment, integrate the gateway policy with the client’s enforcement points, produce authenticated evidence inside the client boundary and obtain the operating owner's sign-off. The private design keeps inference, retrieval, telemetry and audit records under client control and prohibits third-party training on client data. [Gateway policy](04-policy-as-code-templates/ai-gateway-policy.yaml) · [Release gate](04-policy-as-code-templates/release-gate-checklist.yaml) · [Integration and test instructions](04-policy-as-code-templates/README.md)

## Reusing the IP

Original documents and diagrams are available under **CC BY 4.0**. Original code, workflow definitions, YAML policies and synthetic machine-readable examples are available under **Apache 2.0**. Both permit commercial adaptation subject to their terms. An adopter owns its risk decisions, implementation and evidence. The framework is published independently of Scale AI, Inc. [Licence scope](LICENSE) · [Documentation licence](LICENSE-DOCS) · [Code licence](LICENSE-CODE) · [Notices](NOTICE.md) · [Contributing](CONTRIBUTING.md)
