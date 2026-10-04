---
doc_id: DLT-CAL-001
title: DoliTrail sizing calculations
project: DoliTrail
doc_type: Calculation note
version: "0.2"
status: Draft
date: '2026-10-03'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-03'
  author: Amish Chadha
  change: First issue at TRL 3, on the constructable design of DLT-DDR-002
- version: "0.2"
  date: '2026-10-03'
  author: Amish Chadha
  change: "Round 2 requirement decisions (DLT-DDR-003): wheel proof load, hold-back strap and wet clay rule, two bags, four bearers at steps with lift handles"
---

# DoliTrail sizing calculations

On paper, the kit lets two bearers roll a 120 kg patient on the reference doli along a level trail holding about 14 kg each instead of carrying 65 kg each, clamps to poles of 40 to 80 mm without tools, and keeps the doli's own width. The steel frame and clamps carry twice the rated load with a factor of at least 2.0 on yield, and the disc brake has a factor of 1.23 on a wet 30 per cent grade. Four results fell short or were at risk; Amish decided them on 2026-10-03 (DLT-DDR-003) and this issue carries the decisions. The wheel and tyre are not catalogue-rated for twice the load (R3), so they are proved by a 285 kg static proof load before any person is carried. The tyre can slide on wet clay before the brake slips (R5), so the rear bearer holds the shortfall on a hold-back strap and the doli is lifted and carried on wet clay steeper than 20 per cent. The kit, now 15.5 kg, travels in two bags of about 6.9 and 8.7 kg (R7). At steps over about 250 mm four people lift, about 36 kg each (R8). The estimated parts cost is USD 482, under the value-engineering target of USD 1,500.

Every figure comes from `docs/04-calcs/sizing.py`, which imports the parametric model (`cad/src/model.py`), so the sizes here are those of the STEP files, the drawings and the build plan. Tags in square brackets match the script output and `docs/04-calcs/results.csv`. These are screening estimates for a paper proof of concept; every one is checked by test at TRL 4.

> **Safety:** DoliTrail carries a person over steep, wet and uneven ground. These numbers are for a design review, not a release for use. No patient is carried until the frame, clamps and wheel have been proof-loaded and the brake has been tested on a wet ramp with a dummy load (DLT-BLD-001, sections 5 and 6).

## 1. Method and assumptions

The fitted doli is a rigid beam on three supports: the wheel under the patient's hips and the two bearers' pole loops at the ends. Because the bearers choose how much to lift, the wheel takes the weight and the bearers carry only what balances the doli in pitch and roll. Pitch balance comes from the error in placing the wheel under the combined centre of mass; on a slope, from the weight's component along the slope acting at the height of the centre of mass. Brake, grip, clamp friction, structural stress and lift height follow by hand methods in the script.

*Table 1. Assumptions.*

| # | Assumption | Value | Basis |
| --- | --- | --- | --- |
| A1 | Rated load | 120 kg patient on a 10 kg doli; fitted kit 12.5 kg; rolling weight 142.5 kg | R3; two 60 mm bamboo poles, sticks, cloth and rope |
| A2 | Centre of mass | 100 mm above the pole centres; wheel within 100 mm of it | Patient lying on a sagging bed; hip mark on the fitting card |
| A3 | Steadying | Each bearer holds 5 per cent of the rolling weight | Estimate |
| A4 | Tyre grip | 0.35 on wet clay or mud (knobbly tyre); 0.60 on a wet timber or concrete ramp | Estimates |
| A5 | Brake | Sintered pads 0.35 wet; 2.0 kN per pad at about 150 N hand pull, held by the parking lock; 203 mm rotor | To confirm with the bought brake |
| A6 | Clamp | Rubber on wet bamboo 0.35; 2.0 kN per clamp (two M8 bolts at 1.0 kN, hand tight) | Estimate |
| A7 | Bamboo | A 40 mm length of 60 mm culm takes 4.0 kN across its diameter in V jaws | To confirm on real poles |
| A8 | Side load | 30 per cent of the wheel load at the tyre (side slopes, roots) | Estimate |
| A9 | Steel | ERW tube, yield 210 MPa, E 205 GPa | IS 1161 YSt 210 |
| A10 | Wheel and tyre ratings | Wheel 200 kg, tyre 150 kg at maximum pressure | Seller ratings, to confirm |
| A11 | Rolling resistance | 0.08 on a dirt trail | Estimate |
| A12 | Masses of bought parts | Wheel 2.60 kg, brake set 0.81 kg, harness 0.75 kg each, two bags 0.45 kg each, pump kit 0.35 kg, lift handles 0.10 kg each, hold-back strap 0.20 kg | Catalogue values and estimates, to confirm |
| A13 | Round 2 rules (DLT-DDR-003) | Lift and carry on wet clay steeper than 20 per cent; four bearers at steps over about 250 mm | Decided by Amish |
| A14 | 25 mm polyester webbing with sewn ends | Breaking strength 5 kN | Assumed, to confirm |

## 2. Geometry

*Table 2. Kit geometry.*

| Tag | Quantity | Value |
| --- | --- | --- |
| [G1] | Wheel diameter, 20 x 2.125 tyre | 514 mm |
| [G2], [G3] | Pole centres and diameters the clamps take | 450 to 600 mm; 40 to 80 mm |
| [G4] | Tyre contact below the pole centres | 720 mm |
| [G5], [G6] | Width on the reference doli; largest pole centres for 700 mm | 680 mm; 570 mm |
| [G7] | Spigot inside its stub at the widest setting | 77.5 mm |
| [Q3] | Cross strap above the tyre | 174 mm |

## 3. Mass (R7)

*Table 3. Masses.*

| Tag | Item | kg |
| --- | --- | --- |
| [K1] | Fork unit | 2.65 |
| [K2] | Side arms, four | 3.27 |
| [K3], [K4] | Upper jaws; jaw liners | 0.60; 0.21 |
| [K5] | T-handle bolts and set screws | 1.05 |
| [K6], [K7] | Wheel; disc brake set | 2.60; 0.81 |
| [K8] | Lever mount | 0.37 |
| [K9] | Bearer harnesses, two | 1.50 |
| [K10] | Straps, two bags, card, ties, pump and puncture kit, lift handles, hold-back strap | 2.46 |
| [K11] | Kit in the two bags | **15.53** |
| [K12] | Kit fitted to the doli (with the lift handles) | 12.52 |
| [K14] | Bag 1, the wheel bag: fork unit with wheel and brake, pump | 6.86 |
| [K15] | Bag 2, the parts bag: arms, jaws, bolts, lever mount, straps, harnesses, handles | 8.66 |

**R7, each load met, not one load for one person** (decided, DLT-DDR-003, option A): the kit is 15.5 kg, but it travels in two bags of 6.9 kg and 8.7 kg, one per bearer, each under 10 kg [K16]. The steel frame with its bolts (7.8 kg) and the wheel and brake (3.4 kg) alone pass 10 kg, so no single bag can hold the whole kit within R7.

## 4. Bearer loads (R4)

*Table 4. Bearer loads.*

| Tag | Case | Result |
| --- | --- | --- |
| [L1] | Rolling weight | 142.5 kg |
| [L3] | Carrying today, per bearer: two bearers (four) | 65 kg (32.5 kg) |
| [L4] | Level trail, pitch balance on the heavier end | 13.2 kg |
| [L5] | Level trail, average per bearer with steadying | 13.7 kg |
| [L6] | Reduction against two bearers carrying | **79 per cent** (R4 met, estimate) |
| [L7] | 30 per cent descent, brake on, downhill bearer | 45.6 kg (estimate) |
| [L8] | Pull to keep rolling on a level trail | 56 N each (estimate) |
| [L9], [L10] | 15 per cent side slope: roll moment; force at each hand | 170 N m; 155 N (about 16 kg) |

## 5. Brake and grip on a 30 per cent grade (R5)

*Table 5. Brake and grip.*

| Tag | Quantity | Value |
| --- | --- | --- |
| [B1], [B2] | Along-slope force; brake torque needed | 402 N; 103 N m |
| [B3], [B4] | Brake torque available, wet; factor | 127 N m; **1.23** |
| [B5] | Wheel load normal to the slope | 962 N |
| [B6] | Tyre grip factor on wet clay or mud | **0.84** |
| [B7] | Tyre grip factor on a wet test ramp | 1.44 |
| [B8] | Shortfall on wet mud, held by the rear bearer on the hold-back strap | about 7 kg-force |
| [B9] | Tyre grip factor on wet clay at 20 per cent, the lift-and-carry limit | 1.37 |
| [B10], [B11] | Hold-back strap, worst case if the wheel slides fully on 30 per cent; factor on the webbing | 402 N; 12 |

**R5 met with the bearer's help, not by the kit alone** (decided, DLT-DDR-003, option A). The brake holds, but on wet clay or mud the tyre would slide before the brake slips; the verification ramp would pass while a real trail might not. Taking part of the weight on the downhill bearer lightens the wheel and makes grip worse, so the shortfall has to be held back along the slope. The hold-back strap ties the rear pole ends to the uphill (rear) bearer's hip belt, so the bearer holds back the shortfall of about 7 kg-force with the legs; even if the wheel slid fully, the strap would see 402 N, a twelfth of its assumed strength. On wet clay steeper than 20 per cent the doli is lifted and carried; at 20 per cent the tyre's grip factor is 1.37 on its own.

## 6. Clamps (R1)

*Table 6. Clamps.*

| Tag | Quantity | Value |
| --- | --- | --- |
| [C1], [C2] | Slip resistance, one clamp; two clamps on one pole | 1.98 kN; 3.96 kN |
| [C3] | Factor on the 1.5 kN pull of R1 | **2.6** |
| [C4] | Bamboo crushing factor at the clamp force | 2.0 (to confirm) |
| [C5], [C6] | Vertical load per saddle; braking pull per clamp | 319 N; 100 N |

The V jaws wedge the pole, so the friction force is 2.83 times the bolt force times the friction coefficient. The vertical load is carried in bearing by the saddles, not by friction. **R1 met on paper**, with the crushing capacity of real bamboo to confirm.

## 7. Structure at twice the rated load (R3)

*Table 7. Structure.*

| Tag | Quantity | Value |
| --- | --- | --- |
| [S1], [S2] | Strut axial load; stress with side load | 2.51 kN; 104 MPa |
| [S3], [S4] | Strut factor on yield; buckling factor | 2.01; 31 |
| [S5], [S6] | Stub; spigot bending stress | 69 MPa; 67 MPa |
| [S7] | Lowest structural factor on yield | **2.01** |
| [S8] | Clamp bolt tension | 1.0 kN each (proof load about 8.4 kN) |
| [S9] | Wheel rating against twice the wheel load | **0.70** |
| [S10], [S11] | Tyre rating against twice the wheel load; against the wheel load | **0.53**; 1.05 |

**R3 met if the proof load holds** (decided, DLT-DDR-003, option A, moving to B only if the proof load fails): the fork unit, arms and clamps meet the 2 to 1 margin; the wheel and tyre do not on their sellers' ratings. Sellers' ratings are working loads with their own unstated margin, so the margin can only be shown by proof-loading the bought wheel: a 285 kg static load (twice the 142.5 kg wheel load) on the wheel and tyre, at TRL 4, before any person is carried. If it fails, a heavier 20 inch tricycle wheel (about 1.05 of twice the load on rating) and a 20 x 2.4 cargo tyre (about 0.70) are fitted, about USD 30 and 0.6 kg more, and the proof load is repeated. Until it passes, R3 is unproven.

## 8. Width, steps and fitting (R6, R8, R2)

*Table 8. Width, steps and fitting.*

| Tag | Quantity | Value |
| --- | --- | --- |
| [W1] | Width on the reference doli | 680 mm (R6 met) |
| [H1], [H2] | Rise of the poles for the wheel to clear a 400 mm step; pole height | 450 mm; 1,170 mm |
| [H3], [H4] | Lift per bearer: two bearers; four bearers | **71 kg**; 36 kg |
| [H5] | Steps lifted by four bearers: above | 250 mm |
| [H6] | Lift per bearer, two bearers, at a 250 mm step (poles rise 300 mm to about 1,020 mm) | 71 kg |
| [T1] | Fitting time, two people | 4.7 min (R2 met, estimate) |

**R8 met with four people, not two** (decided, DLT-DDR-003, option A): the tyre hangs 720 mm below the poles, so clearing a 400 mm step means lifting the poles from knuckle height to chest height; two bearers would lift about 71 kg each. At steps over about 250 mm two helpers lift at webbing handles on the cross stubs with the two bearers, about 36 kg each, as on a doli carried by four today. Below 250 mm two bearers still lift 71 kg each, by up to 300 mm [H6]; that is a new question for Amish. Fitting time (T1) assumes the wheel travels fitted in the fork unit; the steps are listed in `sizing.py`.

## 9. Cost (R9)

Value-engineering target: USD 1,500. Estimated cost of the constructable design: USD 482 (USD 1,018 under the target) [Q1], [Q2], up USD 27 with the second bag (USD 15), the lift handles (USD 6) and the hold-back strap (USD 6), all estimates. The largest lines are the two harnesses (USD 70), the fork unit (USD 62), the four side arms (USD 60) and the wheel (USD 55).

## 10. Results against the requirements

*Table 9. Results.*

| ID | Result | Status |
| --- | --- | --- |
| R1 | Clamp factor 2.6 wet; crushing factor 2.0 | Met on paper |
| R2 | About 4.7 min | Met on paper (estimate) |
| R3 | Frame 2.01; wheel 0.70 and tyre 0.53 of twice the load; 285 kg static proof load at TRL 4 | Met if the proof load holds (unproven until TRL 4) |
| R4 | 79 per cent | Met on paper (estimate) |
| R5 | Brake 1.23; grip 1.44 on a ramp, 0.84 on wet mud with the hold-back strap; carried above 20 per cent on wet clay | Met with the bearer's help |
| R6 | 680 mm | Met on the reference doli |
| R7 | 15.5 kg in two bags of 6.9 and 8.7 kg | Each load met; not one load for one person |
| R8 | 36 kg each with four people at steps over about 250 mm | Met with four people, not two |
| R9 | USD 482 | Under the value-engineering target |
| R10 | One pull on the tab | Met by design |
| R11 | Lever 100 to 150 mm behind the pole loop | Met on paper |
