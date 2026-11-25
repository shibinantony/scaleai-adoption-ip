# ScaleAI Enterprise Adoption Framework

A guide for directors deciding where to use AI, when to put it into production and what would justify a wider rollout.

Suppose a supplier invoices $1,075 against a $1,000 purchase order. The $75 difference is easy to calculate. The harder question is whether the order and delivery receipt support an explanation. A private AI service can pull those records together and draft a note for accounts payable. If a record is missing, the case goes back to an analyst. Only an authorized employee can release a payment.

That invoice is the running example in this framework. It shows where AI can save a person time, which decisions the person keeps, and what a director should ask to see before funding the next team.

## Start here

**For a first funding meeting**, bring the process owner, a finance partner and someone who actually handles the work. Agree on what counts as a completed case and what it costs today. The diagnostic has 25 questions. A missing permission or an unstaffed fallback can hold the pilot even when the overall score looks good. [Executive scorecard](00-executive-overview/cxo-value-proposition.md) · [Day 0 diagnostic](03-client-execution-kit/day-0-discovery-diagnostic.md)

**During the first 90 days**, qualify one or two workflows for a supervised rollout. Before the invoice pilot takes a live case, the team has to show that unauthorized records stay private, an analyst can take over and an operator can account for every open invoice after a failure. [Week-by-week rollout plan](03-client-execution-kit/day-0-90-immediate-runbook.md)

**At the expansion review**, ask what changed for the people doing the work. In the synthetic invoice pilot, analysts accept a draft in 900 of 1,000 eligible cases. Including the 100 cases finished manually, the service costs $6 per accepted assisted case against an $8 manual baseline. The economics support continuing the current queue. In a separate quality sample, two of 200 drafts contain a material claim their sources cannot support. A third would exceed the pilot’s 1% limit and hold the release. [Worked director decision](03-client-execution-kit/worked-release-decision.md) · [Day 90+ operating guide](03-client-execution-kit/day-90-plus-ongoing-runbook.md)

## The five pillars

| Area | What the guide helps you settle |
| --- | --- |
| [Process and FinOps](01-pillar-blueprints/01-process-and-finops.md) | Which work to redesign and how to price a case after review, rework and fallback. |
| [Technology](01-pillar-blueprints/02-technology-stack.md) | When a rule is enough, where a model helps, and which source records a draft needs. |
| [Tools](01-pillar-blueprints/03-tooling-ecosystem.md) | How to enforce access and spending limits, check a draft and trace what happened. |
| [Architecture](01-pillar-blueprints/04-reference-architecture.md) | Where client data goes, which tools can read it, and how to withdraw access for one tenant. |
| [Trust and assurance](01-pillar-blueprints/05-trust-and-assurance.md) | Which obligations apply, what evidence a reviewer can rely on and who can stop the service. |

The steering group can use the [five-pillar matrix](00-executive-overview/5x2-master-matrix.md) to assign the work for the first release and the next expansion.

## Industry guides

Each guide starts with a decision someone in that industry already owns.

- An investigator checks a disputed payment or an examiner reviews a claim. [Banking and insurance](02-industry-overlays/bfsi-banking-insurance.md)
- A clinician signs a handoff or a study coordinator verifies which protocol applies at a site. [Healthcare and life sciences](02-industry-overlays/healthcare-life-sciences.md)
- A maintenance planner decides whether a machine needs inspection. [Manufacturing and supply chain](02-industry-overlays/manufacturing-supply-chain.md)
- A customer asks which offer is valid during a promotion or a service outage. [Retail and telecom](02-industry-overlays/retail-telecom.md)

## Try the release check

From the repository root, run this in a Python 3.11 virtual environment.

```sh
python -m pip install -r 04-policy-as-code-templates/requirements.txt
python 04-policy-as-code-templates/evaluate_release.py --demo
```

`DEMO PASS` means the synthetic sample meets the example thresholds. For a live service, the client connects the gateway to its own systems, verifies who produced the evidence and assigns a person to approve rollout. Inference, retrieval and audit logs stay under client control. Third-party training on client data is prohibited. [Gateway rules](04-policy-as-code-templates/ai-gateway-policy.yaml) · [Release thresholds](04-policy-as-code-templates/release-gate-checklist.yaml) · [Integration instructions](04-policy-as-code-templates/README.md)

## Reuse and attribution

Shibin Antony publishes this vendor-neutral framework independently of Scale AI, Inc. Original documentation and diagrams use CC BY 4.0. Code, configuration and synthetic machine-readable examples use Apache 2.0. Both licences permit commercial use under their terms. [Licence scope](LICENSE) · [Documentation licence](LICENSE-DOCS) · [Code licence](LICENSE-CODE) · [Attribution](NOTICE.md) · [Citation](CITATION.cff) · [Contributing](CONTRIBUTING.md)
