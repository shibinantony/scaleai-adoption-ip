# Healthcare and life sciences

At shift change, a clinician needs to know which encounter an allergy entry came from. At a study site, a coordinator preparing the next visit needs the protocol amendment in force *at that site today*. Choose one of these uses for the first release. The medical director owns the ward pilot. The head of study quality owns the protocol pilot.

## Day 0–90 · Put the source beside the answer

### On the ward

Show the patient, encounter, original note and cited facts together. Link identity, active allergies and medication statements to their locations in the note. Send conflicting facts or missing critical fields to the clinician with the issue marked. Only a named clinician signs the final entry in the electronic health record (EHR).

Two clinicians resolve disputed findings against the source encounter. Require zero unsupported material clinical claims across at least 200 substantive drafts. Separately, test at least 50 cases with a wrong encounter, contradictory evidence or a missing critical field. Every one must reach a clinician with the correct issue flagged. A missed allergy can follow the patient into the next shift even when most of the summary is accurate.

### At the study site

Resolve the study, site, country, effective date and amendment in the controlled document repository. Show the coordinator the approved revision, document identifier and section. Send ambiguous cases to study quality. A superseded copy can give staff the wrong visit schedule and undermine both participant protection and study records.

Across at least 200 substantive responses, require zero wrong-site or superseded citations and zero unsupported material instructions. Send all 30 test cases with ambiguous applicability to study quality. The coordinator verifies the version before using the answer.

### Before either service goes live

The privacy officer restricts retrieval by tenant, encounter or site, and current staff role. Keep inference, audit logs and test material in the client enclave. Disable third-party training, outbound telemetry and payload logging. An air-gapped installation receives signed updates through approved offline import. In 200 synthetic boundary cases, require zero unauthorized reads and zero seeded identifiers at unauthorized destinations. Use synthetic records for public demonstrations.

For US HIPAA deployments, document the risk analysis and the role of each processor. A cloud provider maintaining electronic protected health information (ePHI) on behalf of a covered entity or business associate generally needs a business associate agreement, even if it cannot decrypt that information. Verify required agreements and document the client’s choice of a private VPC or air-gapped enclave. [HHS cloud computing guidance](https://www.hhs.gov/hipaa/for-professionals/special-topics/health-information-technology/cloud-computing/index.html)

Regulatory affairs reassesses intended use before adding patient-specific recommendations. FDA sets out the criteria for non-device clinical decision support. For a study, quality assurance identifies electronic records required by an applicable FDA predicate rule and documents its Part 11 assessment. The official record and required signatures stay in the approved records system. [FDA clinical decision support guidance](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/clinical-decision-support-software) · [FDA Part 11 scope guidance](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/part-11-electronic-records-electronic-signatures-scope-and-application)

The responsible clinical or quality lead signs the thresholds before testing, then reviews the blinded findings, version manifest, access tests and fallback drill. At the observed peak concurrency, p95 time to a usable draft or explicit handoff must be **15 seconds or less over at least 200 requests**. Count timeouts as breaches. One critical error, disclosure, false chart entry or wrong-site instruction stops the affected service. Return open work to the EHR inbox or study quality queue and notify its owner. [Discovery diagnostic](../03-client-execution-kit/day-0-discovery-diagnostic.md)

## Day 90+ · Recheck what changed

- **When an EHR template changes**, rerun the flagged cases. Do the same after a model or terminology change. A renamed field can hide an allergy across a whole service. Each month audit at least 200 substantive drafts per service by note template, record abstentions separately and require zero unsupported material clinical claims. All flagged cases must route correctly. Low-volume services accumulate cases under clinician review before expansion.
- **When study quality approves an amendment**, invalidate the affected site indexes and cached answers. Keep the route closed until every affected site acknowledges the new signed revision. Check 50 version switches per amendment. Every result must match the approved copy, with zero stale answers.

Finance prices the signed handoff or the verified protocol lookup. Count each accepted encounter or lookup once. Include staff time, exceptions, secure compute, validation, quality review and corrections. For example, **$3,600 / 600 accepted handoffs = $6 per handoff**. Compare with matched manual work and track corrections for seven days. With zero accepted outputs, hold expansion. Add a ward or site only after two passing review windows and sign-off from that unit’s clinical or quality owner. [Ongoing runbook](../03-client-execution-kit/day-90-plus-ongoing-runbook.md)
