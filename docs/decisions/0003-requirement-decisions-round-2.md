---
doc_id: DLT-DDR-003
title: DoliTrail requirement decisions on R3, R5, R7 and R8
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
  change: Amish's round-2 decisions 6A, 7A, 8A and 9A recorded and carried into the design
---

# 0003: Requirement decisions on R3, R5, R7 and R8

- **Date:** 2026-10-03
- **Status:** accepted. Decided by Amish on 2026-10-03: "i agree with all the 46 recommendations you provided. please proceed." For DoliTrail this accepts the recommendations on open decisions O1 to O4 of DLT-DEC-001 (portfolio items 6A, 7A, 8A and 9A).

## Context

The TRL 3 calculations (DLT-CAL-001 v0.1) left four requirements short or at risk: the wheel and tyre are not catalogue-rated for twice the wheel load (R3); on wet clay the tyre slides before the brake slips (R5); the kit weighed 14.8 kg in one bag (R7); and two bearers would each lift about 71 kg to chest height to clear a 400 mm step (R8). Each was posed with options in `docs/REVIEW.md` (D-A1 to D-A4).

## Options considered

The options are set out in full in `docs/REVIEW.md`, TRL 3 section, "Decisions for Amish". In short: R3 by proof load, a heavier tricycle wheel or a scooter wheel; R5 by a hold-back strap and a carry rule, a drag claw or a mud tyre; R7 by two bags, lighter parts or an aluminium frame; R8 by four lifters with handles or shoulder yokes.

## Decision

| Item | Requirement | Decision (option A in each case) |
| --- | --- | --- |
| 6A | R3 | Keep the 20 inch cargo wheel. Proof-load each bought wheel, with its tyre at full pressure, to 285 kg for 10 minutes before the kit is used; move to the heavier 20 inch tricycle wheel and 20 x 2.4 cargo tyre only if it fails. |
| 7A | R5 | Add a hold-back strap from the uphill (rear) bearer's hip belt to the rear pole ends, and the rule to lift and carry on wet clay steeper than 20 per cent. |
| 8A | R7 | Split the kit into two bags, one carried by each bearer: about 7 and 8 kg. |
| 9A | R8 | Four people lift at steps: the two bearers at the pole ends and two helpers at two lift handles added to the frame, about 36 kg each. |

## Consequences

Carried out on 2026-10-03:

- **Model** (`cad/src/model.py`): hold-back strap (BOM line 16): two closed webbing end caps 40 mm deep over the rear pole ends, so the pull bears on the end of each pole, two 25 mm legs to a 40 mm steel ring and a 600 mm tail with a cam buckle to the rear bearer's hip belt. Lift handles (line 17): a 40 mm webbing band sewn shut round each cross stub, 100 mm off centre (front stub left, rear stub right, so the helpers stand on opposite sides), with a 130 mm hand loop and a foam grip. Sixteen new constructability checks (91 of 91 pass): caps on the pole ends and 5 mm clear of the harness loops; legs, ring and tail clear of the poles, cross sticks and harness loops; handles on their stubs, clear of the arms, set screws and brake, 69 mm clear of the tyre, 162 mm of hand room under the poles and bed, 358 mm above the ground.
- **Bags:** the wheel bag (line 12) carries the fork unit with the wheel, brake, lift handles and pump kit (7.2 kg); a new parts bag (line 18) carries the arms, jaws, bolts, lever mount, straps, harnesses and hold-back strap (8.3 kg).
- **Results** (DLT-CAL-001 v0.2): R3 frame factor 2.01, wheel proof load 285 kg [S12]; R5 brake 1.23, wet ramp grip 1.44, wet clay grip 1.37 at the 20 per cent carry limit [B9], hold-back pull 65 N on 30 per cent wet clay met by surprise [B10]; R7 two bags of 7.2 and 8.3 kg [K13], [K14], 15.5 kg in all; R8 about 36 kg each with four people [H4], 350 N on each handle [H5].
- **Cost and mass:** USD 27 more (hold-back strap USD 6, two lift handles USD 6, parts bag USD 15). Value-engineering target: USD 1,500. Estimated cost of the constructable design: USD 482 (USD 1,018 under the target). Fitted kit 12.5 kg; rolling weight 142.5 kg.
- **New question:** R7 and R8 are met only in the way these decisions set out (per bag; with four people), while their wording still says one person and two bearers. Whether to restate them is posed to Amish as O5 in DLT-DEC-001.

> **Safety:** The hold-back strap helps, it does not replace the carry rule: on wet clay steeper than 20 per cent the bearers lift and carry. The wheel proof load is done with sandbags under safety stop S3 before any person is carried.
