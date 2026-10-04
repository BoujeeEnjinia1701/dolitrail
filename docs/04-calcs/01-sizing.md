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
  change: "Amish's round-2 decisions 6A to 9A (DLT-DDR-003): wheel proof load [S12]; hold-back strap and the 20 per cent carry rule [B9] to [B11]; two bags [K13], [K14]; lift handles and four lifters [H5] to [H7]; masses, loads and cost re-run"
---

# DoliTrail sizing calculations

On paper, the kit lets two bearers roll a 120 kg patient on the reference doli along a level trail holding about 14 kg each instead of carrying 65 kg each, clamps to poles of 40 to 80 mm without tools, and keeps the doli's own width. The steel frame and clamps carry twice the rated load with a factor of at least 2.0 on yield, and the disc brake has a factor of 1.23 on a wet 30 per cent grade. Amish decided the four results that fell short on 2026-10-03 ("i agree with all the 46 recommendations you provided. please proceed."; DLT-DDR-003): each bought wheel is proof-loaded to 285 kg before use (R3); a hold-back strap ties the uphill bearer to the rear pole ends, and the doli is lifted and carried on wet clay steeper than 20 per cent, where the tyre grip factor is 1.37 (R5); the kit travels in two bags of about 7.2 and 8.3 kg (R7); and four people lift at steps, about 36 kg each, two of them at new lift handles on the cross stubs (R8). The estimated parts cost is USD 482, under the value-engineering target of USD 1,500.

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
| A12 | Masses of bought parts | Wheel 2.60 kg, brake set 0.81 kg, harness 0.75 kg each, wheel bag 0.60 kg, parts bag 0.30 kg, pump kit 0.35 kg, hold-back strap 0.20 kg, lift handles 0.10 kg each | Catalogue values and estimates, to confirm |
| A13 | Carry limit (decision 7A) | Lift and carry on wet clay steeper than 20 per cent | Amish, 2026-10-03 |
| A14 | Webbing strength | 25 mm polyester 5 kN, 50 mm polyester 10 kN, breaking | Typical values, to confirm |

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
| [K15] | Hold-back strap; lift handles, two | 0.20; 0.20 |
| [K10] | Straps, two bags, card, ties, pump and puncture kit | 2.06 |
| [K11] | Kit, both bags | 15.53 |
| [K12] | Kit fitted to the doli, with the lift handles | 12.52 |
| [K13] | Wheel bag: fork unit with lift handles, wheel, brake, pump kit, bag | **7.21** |
| [K14] | Parts bag: arms, jaws, bolts, lever mount, straps, harnesses, hold-back strap, bag | **8.31** |

**R7 (decision 8A):** the kit travels in two bags carried by the two bearers, who walk in together: 7.2 kg and 8.3 kg, each under 10 kg. The whole kit (15.5 kg) is still more than one person's 10 kg; the requirement is restated as two bags of 10 kg or less, one per bearer (decision 1A of 2026-10-04, DLT-DDR-004), and is met.

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
| [L9], [L10] | 15 per cent side slope: roll moment; force at each hand | 170 N m; 154 N (about 16 kg) |

## 5. Brake and grip on a 30 per cent grade (R5)

*Table 5. Brake and grip.*

| Tag | Quantity | Value |
| --- | --- | --- |
| [B1], [B2] | Along-slope force; brake torque needed | 401 N; 103 N m |
| [B3], [B4] | Brake torque available, wet; factor | 127 N m; **1.23** |
| [B5] | Wheel load normal to the slope | 961 N |
| [B6] | Tyre grip factor on wet clay or mud | **0.84** |
| [B7] | Tyre grip factor on a wet test ramp | 1.44 |
| [B8] | Shortfall on wet mud | about 7 kg-force |
| [B9] | Tyre grip factor on wet clay at the 20 per cent carry limit | **1.37** |
| [B10] | Hold-back strap pull on 30 per cent wet clay, wheel at its grip limit | 65 N |
| [B11] | Hold-back strap strength against the whole along-slope force on 30 per cent | 25 (two 25 mm legs; to confirm) |

**R5 (decision 7A):** the brake holds (1.23) and the tyre grips on the wet test ramp (1.44), so the verification test passes on paper. On wet clay or mud the tyre would slide before the brake slips on a 30 per cent grade, so the rule is to lift and carry on wet clay steeper than 20 per cent, where the grip factor is still 1.37. The hold-back strap gives the uphill bearer a direct hold on the rear pole ends on every wet descent; on a patch of 30 per cent wet clay met by surprise it would take the 65 N shortfall while the bearers stop and lift. Taking weight on the downhill bearer lightens the wheel and makes grip worse, which is why the help comes along the slope from the uphill bearer.

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
| [S12] | Wheel proof load before use, twice the rolling weight | **285 kg** |

**R3 (decision 6A):** the fork unit, arms and clamps meet the 2 to 1 margin (lowest factor 2.01 with the lift handles' 0.2 kg added). The wheel and tyre do not on their sellers' ratings, which are working loads with their own unstated margin. Each bought cargo wheel, with its tyre at full pressure, is therefore proof-loaded to 285 kg for 10 minutes before the kit is used; a wheel that fails is replaced by the heavier 20 inch tricycle wheel and 20 x 2.4 cargo tyre (about USD 30 more and 0.6 kg heavier), which is proof-loaded the same way.

## 8. Width, steps and fitting (R6, R8, R2)

*Table 8. Width, steps and fitting.*

| Tag | Quantity | Value |
| --- | --- | --- |
| [W1] | Width on the reference doli | 680 mm (R6 met) |
| [H1], [H2] | Rise of the poles for the wheel to clear a 400 mm step; pole height | 450 mm; 1,170 mm |
| [H3], [H4] | Lift per person: two bearers; four people | 71 kg; **36 kg** |
| [H5] | Pull on each lift handle, four lifting | 350 N |
| [H6] | Stub bending at the strut from a handle at twice its pull | 13 MPa (factor 16 on yield) |
| [H7] | Lift handle webbing strength factor | 29 (to confirm) |
| [T1] | Fitting time, two people | 4.7 min (R2 met, estimate) |

**R8 (decision 9A):** the tyre hangs 720 mm below the poles, so clearing a 400 mm step means lifting the poles from knuckle height to chest height; two bearers would lift about 71 kg each, which is not a safe lift. At steps over about 250 mm four people lift: the two bearers at the pole ends and two helpers at webbing lift handles sewn round the cross stubs (front stub left of centre, rear stub right), about 36 kg each, as on a doli carried by four today. The handles hang below the stubs with 162 mm of hand room under the poles and bed and 69 mm clear of the tyre. Fitting time (T1) assumes the wheel travels fitted in the fork unit; the handles stay on the fork unit and the hold-back strap goes on with the harness loops, so neither adds to it.

## 9. Cost (R9)

Value-engineering target: USD 1,500. Estimated cost of the constructable design: USD 482 (USD 1,018 under the target) [Q1], [Q2]. The decisions add USD 27: the hold-back strap (USD 6), two lift handles (USD 6) and the parts bag (USD 15); the wheel proof load uses the CalRig rig and sandbags. The largest lines are the two harnesses (USD 70), the fork unit (USD 62), the four side arms (USD 60) and the wheel (USD 55).

## 10. Results against the requirements

*Table 9. Results.*

| ID | Result | Status |
| --- | --- | --- |
| R1 | Clamp factor 2.6 wet; crushing factor 2.0 | Met on paper |
| R2 | About 4.7 min | Met on paper (estimate) |
| R3 | Frame 2.01; wheel 0.70 and tyre 0.53 of twice the load on ratings; every wheel proof-loaded to 285 kg before use | Met on paper for the frame; the wheel and tyre are shown by the proof load (decision 6A) |
| R4 | 79 per cent | Met on paper (estimate) |
| R5 | Brake 1.23; grip 1.44 on a wet ramp; 1.37 on wet clay at the 20 per cent carry limit; hold-back strap | Met on paper on the wet ramp; on wet clay met by the carry rule and the hold-back strap (decision 7A) |
| R6 | 680 mm | Met on the reference doli |
| R7 | Two bags, 7.2 and 8.3 kg; 15.5 kg in all | Met per bag (decision 8A); not one load for one person |
| R8 | 36 kg each, four people with two lift handles; 71 kg each with two | Met with four people (decision 9A); not with two |
| R9 | USD 482 | Under the value-engineering target |
| R10 | One pull on the tab | Met by design |
| R11 | Lever 100 to 150 mm behind the pole loop | Met on paper |
