---
doc_id: DLT-REQ-001
title: DoliTrail requirements
project: DoliTrail
doc_type: Requirements
version: "0.3"
status: Draft
date: '2026-10-03'
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
  change: "Status after the round 2 requirement decisions (DLT-DDR-003), from DLT-CAL-001 v0.2; targets unchanged"
---

# DoliTrail requirements

Requirements for the kit fitted to the reference doli (two 60 mm bamboo poles, 2.55 m long, at 550 mm centres) carrying the rated patient. R1 to R9 keep the targets set at TRL 1; R10 and R11 were added at TRL 2 (DLT-DDR-001). Status is the paper result at TRL 3 from DLT-CAL-001; every requirement is verified by test at TRL 4. Amish decided the four requirements not met or at risk on 2026-10-03 (DLT-DDR-003); none was restated. R3 now rests on a 285 kg static proof load at TRL 4; R5, R7 and R8 are met only with the bearers' help, two bags and four people at steps, as the decisions say.

*Table 1. Requirements.*

| ID | Requirement | Target | Verification (TRL 3 or later) | TRL 3 status |
| --- | --- | --- | --- | --- |
| R1 | Fits real dolis | Clamps grip poles of 40 to 80 mm diameter and hold without slipping under a 1.5 kN load (target) | Fit trials on 10 field-made dolis and CalRig pull tests | Met on paper: the clamps close on 40 and 80 mm poles in the model; two clamps on one pole resist 3.96 kN wet (factor 2.6); bamboo crushing factor 2.0 to confirm on real poles |
| R2 | Quick to fit | Two people fit the kit to a doli in under 5 minutes | Timed trials using only the fitting card | Met on paper (estimate): about 4.7 min, with the wheel carried fitted in the fork unit |
| R3 | Carry load | Rated for a 120 kg (265 lb) patient plus doli, with a 2 to 1 safety margin on the wheel, fork and clamps | CalRig proof-load test | Met if the proof load holds (decided, DLT-DDR-003): fork, arms and clamps 2.01 on yield at twice the rated load; the wheel (0.70) and tyre (0.53) are not catalogue-rated for twice the wheel load, so they are proved by a 285 kg static proof load at TRL 4 before any person is carried, with a heavier tricycle wheel and cargo tyre if it fails. Unproven until then |
| R4 | Reduce bearer load | Average vertical load per bearer reduced by at least 60 per cent on level trail compared with carrying | Load cells in the harness cups during trail trials | Met on paper (estimate): 79 per cent (about 14 kg per bearer against 65 kg) |
| R5 | Brake holds on descents | Holds the rated load stationary on a 30 per cent grade, wet | Wet ramp test | Met with the bearer's help, not by the kit alone (decided, DLT-DDR-003): brake factor 1.23; tyre grip 1.44 on a wet ramp and 0.84 on wet clay, where the rear bearer holds about 7 kg-force on the hold-back strap; on wet clay steeper than 20 per cent (grip 1.37 at 20 per cent) the doli is lifted and carried |
| R6 | Narrow trails | Overall width with wheel at or below 700 mm (28 in) | Measure; walk a marked 0.8 m trail course | Met on the reference doli: 680 mm; any doli with poles at more than 570 mm centres is wider than 700 mm by itself |
| R7 | Portable | Kit mass at or below 10 kg (22 lb) and carried by one person | Weigh; timed carry of the bagged kit | Each load met, not one load for one person (decided, DLT-DDR-003): 15.5 kg in two bags of about 6.9 and 8.7 kg, one per bearer |
| R8 | Lift over obstacles | Two bearers lift the fitted doli over a 400 mm step without removing the wheel | Obstacle course trial | Met with four people, not two (decided, DLT-DDR-003): at steps over about 250 mm two helpers lift at the lift handles, about 36 kg each; two bearers would lift about 71 kg each to chest height |
| R9 | Low cost | Parts cost at or below $1,500 USD for the kit | Costed bill of materials | USD 482: under the value-engineering target of USD 1,500 by USD 1,018 |
| R10 | Patient release | Each patient strap frees with one pull of one hand in 3 s or less | Timed trial, gloved hand | Met by design: cam buckles with a pull tab |
| R11 | Brake within reach | The front bearer works the brake and its parking lock without letting go of the poles | Trial with bearers of 1.5 to 1.8 m | Met on paper: lever on the front right pole about 100 to 150 mm behind the pole loop |

## Assumptions

- Rated load: a 120 kg patient on a 10 kg doli; with the 12.5 kg fitted kit the rolling weight is 142.5 kg (DLT-CAL-001, A1).
- The wheel is placed under the patient's hips to within 100 mm; bearers steady the doli with about 5 per cent of the rolling weight each.
- Typical routes roll on level ground and moderate grades; bearers lift and carry at steps, rocks and water.
- Bamboo poles carry the patient through four clamps at about 600 mm spacing near mid-span.
- Ambulance services and health committees would keep and maintain kits.

> **Safety:** These requirements describe equipment that carries a person over dangerous ground. A paper result is not a test. No person is carried until the TRL 4 proof loads, including the 285 kg static proof load of the wheel and tyre, and the first checks in DLT-BLD-001 pass. R5 and R8 are met only with people doing their part: the hold-back strap on every descent, lift and carry on wet clay steeper than 20 per cent, and four bearers at steps over about 250 mm.
