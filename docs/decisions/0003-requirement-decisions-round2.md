---
doc_id: DLT-DDR-003
title: DoliTrail requirement decisions, round 2
project: DoliTrail
doc_type: Design decision record
version: "0.1"
status: Draft
date: '2026-10-03'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-03'
  author: Amish Chadha
  change: Decisions O1 to O4 on R3, R5, R7 and R8, decided by Amish on 2026-10-03 and carried into the model, calculations, BOM and build plan
---

# 0003: Requirement decisions, round 2

- **Date:** 2026-10-03
- **Status:** Decided. Decided by Amish Chadha, 2026-10-03: "i approve all of the 47 recommendations provided by you. Execute them." Each decision below is the recommendation as worded in `docs/06-design-decisions.md` (DLT-DEC-001 v0.1), including its conditions.

> **Safety:** Three of these decisions (O1, O2 and O4) concern carrying a person. Each is the conservative option and puts a person, a proof load or a rule between the patient and the shortfall. None of them is a test: no person is carried until the TRL 4 proof loads, including the 285 kg static proof load of the wheel and tyre, and the wet ramp test have passed (DLT-BLD-001, sections 5 and 6). DoliTrail is not certified medical or rescue equipment.

## Context

DLT-CAL-001 v0.1 left R3 (carry load) and R5 (brake holds on descents) at risk, and R7 (portable) and R8 (lift over obstacles) not met. Each was posed as Proposed, awaiting Amish, with options and a recommendation.

## Decision

Table 1. Decisions

| # | Requirement | Option chosen | Effect (DLT-CAL-001 v0.2) | Condition |
| --- | --- | --- | --- | --- |
| O1 | R3, wheel and tyre margin | **A:** keep the 20 inch cargo wheel and prove it with a 285 kg static proof load before any person is carried | No change to the wheel, cost or mass. R3 met if the proof load holds; until then the wheel (0.70) and tyre (0.53 of twice the wheel load on their ratings) are unproven. The proof load is a TRL 4 step, written into the build plan's first checks and safety stops S4 and S5 | Moving to B, a heavier 20 inch tricycle wheel and a 20 x 2.4 cargo tyre (about USD 30 more, 0.6 kg heavier), only if the proof load fails; the proof load is then repeated |
| O2 | R5, grip on a wet descent | **A:** a hold-back strap from the rear bearer's hip belt to the rear pole ends, plus a rule to lift and carry on wet clay steeper than 20 per cent | BOM line 17 (USD 6, 0.2 kg) and a D-ring on the rear bearer's hip belt; hold-back loops on the rear pole ends in the model. The rear bearer holds the shortfall of about 7 kg-force on wet clay at 30 per cent; worst case 402 N if the wheel slides fully, a factor of 12 on the webbing's assumed 5 kN. Tyre grip factor at 20 per cent on wet clay is 1.37. R5 met with the bearer's help, not by the kit alone | The rule is on the fitting card and in safety stop S5 |
| O3 | R7, kit mass | **A:** two bags carried by the two bearers | BOM line 12 becomes two bags (USD 15 more, 0.3 kg). Kit 15.5 kg (with the O2 and O4 parts) in bags of about 6.9 kg and 8.7 kg, each within R7, but not one load for one person | None |
| O4 | R8, lifting over a 400 mm step | **A:** four bearers at steps over about 250 mm, the two helpers lifting at webbing handles on the cross stubs | BOM line 16 (two handles, USD 6, 0.2 kg); handles wrapped round the cross stubs in the model, checked clear of the struts, set screws, wheel and brake. About 36 kg per person at a 400 mm step. R8 met with four people, not two | The rule is on the fitting card and in safety stop S5 |

## Consequences

- Requirement status (DLT-REQ-001 v0.3): R3 at risk to met if the proof load holds; R5 at risk to met with the bearer's help; R7 not met to each load met, not one load for one person; R8 not met to met with four people. No requirement was restated.
- Estimated cost: USD 455 to USD 482 against the USD 1,500 value-engineering target (USD 1,018 under). Kit 14.8 to 15.5 kg; fitted 12.3 to 12.5 kg; rolling weight 142.5 kg, so twice the wheel load is still 285 kg.
- Model: 83 of 83 constructability checks pass (75 before; eight new checks for the lift handles and hold-back loops). STEP and STL, general arrangement DLT-DWG-001 Rev P3, the concept media with blueprint DLT-DWG-010 Rev P2, the build plan pictures (two new joint close-ups) and `media/model.glb` are regenerated.
- New open decision O5 in `docs/06-design-decisions.md`: below the 250 mm threshold two bearers still lift about 71 kg each, by up to 300 mm.
