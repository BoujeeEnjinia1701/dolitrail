---
doc_id: DLT-REQ-001
title: DoliTrail requirements
project: DoliTrail
doc_type: Requirements
version: "0.4"
status: Draft
date: '2026-10-04'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-09-30'
  author: Amish Chadha
  change: Initial scaffold
- version: "0.2"
  date: '2026-10-03'
  author: Amish Chadha
  change: TRL 3 status from DLT-CAL-001 on the constructable design; R10 and R11 added (DLT-DDR-001); targets R1 to R9 unchanged
- version: "0.3"
  date: '2026-10-03'
  author: Amish Chadha
  change: "Status of R3, R5, R7, R8 and R9 after Amish's round-2 decisions 6A to 9A (DLT-DDR-003); targets unchanged; wording of R7 and R8 posed to Amish (DLT-DEC-001, O5)"
- version: "0.4"
  date: '2026-10-04'
  author: Amish Chadha
  change: "R7 and R8 restated by Amish's round-3 decision 1A (DLT-DDR-004): R7 as two bags of 10 kg or less, one per bearer; R8 as four people at steps, two at the lift handles; both met as designed"
---

# DoliTrail requirements

Requirements for the kit fitted to the reference doli (two 60 mm bamboo poles, 2.55 m long, at 550 mm centres) carrying the rated patient. R1 to R9 keep the targets set at TRL 1; R10 and R11 were added at TRL 2 (DLT-DDR-001). Status is the paper result at TRL 3 from DLT-CAL-001; every requirement is verified by test at TRL 4. Requirements not met or at risk are posed to Amish as decisions in `docs/REVIEW.md` and `docs/06-design-decisions.md`.

On 2026-10-03 Amish decided the four requirement decisions on R3, R5, R7 and R8 as recommended: "i agree with all the 46 recommendations you provided. please proceed." (decisions 6A to 9A, DLT-DDR-003). The targets are unchanged. R7 and R8 are met only in the way those decisions set out (two bags; four people at steps). On 2026-10-04 Amish decided option 1A on their wording: "For round 3, I agree with all your proposed recommendations". R7 is now restated as "two bags of 10 kg or less, one per bearer" and R8 as "four people at steps, two at the lift handles" (DLT-DDR-004). Both are met as designed.

*Table 1. Requirements.*

| ID | Requirement | Target | Verification (TRL 3 or later) | TRL 3 status |
| --- | --- | --- | --- | --- |
| R1 | Fits real dolis | Clamps grip poles of 40 to 80 mm diameter and hold without slipping under a 1.5 kN load (target) | Fit trials on 10 field-made dolis and CalRig pull tests | Met on paper: the clamps close on 40 and 80 mm poles in the model; two clamps on one pole resist 3.96 kN wet (factor 2.6); bamboo crushing factor 2.0 to confirm on real poles |
| R2 | Quick to fit | Two people fit the kit to a doli in under 5 minutes | Timed trials using only the fitting card | Met on paper (estimate): about 4.7 min, with the wheel carried fitted in the fork unit |
| R3 | Carry load | Rated for a 120 kg (265 lb) patient plus doli, with a 2 to 1 safety margin on the wheel, fork and clamps | CalRig proof-load test | Met on paper for the fork, arms and clamps (lowest factor 2.01 on yield at twice the rated load). The wheel and tyre are not catalogue-rated for twice the wheel load, so each bought wheel is proof-loaded to 285 kg before use, with the heavier tricycle wheel if it fails (decision 6A) |
| R4 | Reduce bearer load | Average vertical load per bearer reduced by at least 60 per cent on level trail compared with carrying | Load cells in the harness cups during trail trials | Met on paper (estimate): 79 per cent (about 14 kg per bearer against 65 kg) |
| R5 | Brake holds on descents | Holds the rated load stationary on a 30 per cent grade, wet | Wet ramp test | Met on paper on the wet test ramp: brake factor 1.23, tyre grip factor 1.44. On wet clay the grip factor on 30 per cent is 0.84, so the bearers lift and carry on wet clay steeper than 20 per cent (grip factor 1.37 there), and a hold-back strap ties the uphill bearer to the rear pole ends (decision 7A) |
| R6 | Narrow trails | Overall width with wheel at or below 700 mm (28 in) | Measure; walk a marked 0.8 m trail course | Met on the reference doli: 680 mm; any doli with poles at more than 570 mm centres is wider than 700 mm by itself |
| R7 | Portable | Two bags of 10 kg (22 lb) or less, one per bearer | Weigh; timed carry of the bagged kit | Met as designed (decisions 8A and 1A): two bags of 7.2 and 8.3 kg, one carried by each bearer; the whole kit is 15.5 kg |
| R8 | Lift over obstacles | Four people at steps, two at the lift handles: the fitted doli goes over a 400 mm step without removing the wheel | Obstacle course trial | Met as designed (decisions 9A and 1A): the two bearers and two helpers at lift handles on the cross stubs, about 36 kg each. Two bearers alone would each lift about 71 kg to chest height, so the drill rules that out |
| R9 | Low cost | Parts cost at or below $1,500 USD for the kit | Costed bill of materials | Value-engineering target: USD 1,500. Estimated cost of the constructable design: USD 482 (USD 1,018 under the target) |
| R10 | Patient release | Each patient strap frees with one pull of one hand in 3 s or less | Timed trial, gloved hand | Met by design: cam buckles with a pull tab |
| R11 | Brake within reach | The front bearer works the brake and its parking lock without letting go of the poles | Trial with bearers of 1.5 to 1.8 m | Met on paper: lever on the front right pole about 100 to 150 mm behind the pole loop |

## Assumptions

- Rated load: a 120 kg patient on a 10 kg doli; with the 12.5 kg fitted kit the rolling weight is 142.5 kg (DLT-CAL-001, A1).
- The wheel is placed under the patient's hips to within 100 mm; bearers steady the doli with about 5 per cent of the rolling weight each.
- Typical routes roll on level ground and moderate grades; bearers lift and carry at rocks, water and wet clay steeper than 20 per cent, and four people lift at steps (decisions 7A and 9A).
- Bamboo poles carry the patient through four clamps at about 600 mm spacing near mid-span.
- Ambulance services and health committees would keep and maintain kits.

> **Safety:** These requirements describe equipment that carries a person over dangerous ground. A paper result is not a test. No patient is carried until the TRL 4 proof loads and first checks in DLT-BLD-001 pass.
