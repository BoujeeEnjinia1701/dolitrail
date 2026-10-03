---
doc_id: DLT-DEC-001
title: DoliTrail design decisions register
project: DoliTrail
doc_type: Design decisions register
version: "0.1"
status: Draft
date: '2026-10-03'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-03'
  author: Amish Chadha
  change: Register opened; design decisions made under Amish's 2026-10-03 pre-approvals; four requirement decisions proposed, awaiting Amish
---

# DoliTrail design decisions register

Every design decision still to be made, and every decision made, in one place. Each decision is argued in full in its decision record under `docs/decisions/` or in `docs/REVIEW.md`; this register is the index Amish works from. The build plan (`docs/05-build-plan.md`) describes the design as it stands and does not list decisions.

> **Safety:** Several entries set safety limits (one wheel steadied with both hands, a parking lock on every kit, a solid axle, hand-tight clamps, sandbags before people, lift and carry on wet clay). Each takes the conservative option and names the evidence that would relax it. DoliTrail is not certified medical or rescue equipment.

## Open decisions

Requirements not met or at risk on paper. Each is set out in full, with the state and the estimated effect of each option, in `docs/REVIEW.md` (TRL 3 section, "Decisions for Amish"). All are **Proposed, awaiting Amish**.

*Table 1. Open decisions.*

| # | Decision needed | Options | Recommendation | Affects in the build | Source |
| --- | --- | --- | --- | --- | --- |
| O1 | R3: wheel and tyre are not catalogue-rated for twice the wheel load (wheel 0.70, tyre 0.53 of it; frame 2.02) | A: keep the 20 inch cargo wheel and prove the margin with a 285 kg static proof load of the bought wheel and tyre; B: heavier tricycle wheel and 20 x 2.4 cargo tyre; C: 10 inch scooter wheel with a drum hub | **A**, and move to B only if the proof load fails | Wheel line 6; first checks | DLT-CAL-001, section 7 |
| O2 | R5: brake factor 1.23 but tyre grip factor 0.84 on wet clay (1.44 on a wet ramp) | A: a hold-back strap from the uphill bearer's belt to the rear pole ends, and lift and carry on wet clay steeper than 20 per cent; B: a lever-dropped drag claw behind the wheel; C: a taller-knob mud tyre | **A** | Harness line 11; fitting card; safety stops | DLT-CAL-001, section 5 |
| O3 | R7: 14.8 kg in one bag | A: two bags, one per bearer (about 7 and 8 kg); B: lighter parts (about 13.6 kg); C: aluminium frame (about 11.5 kg) | **A** | Bag line 12 | DLT-CAL-001, section 3 |
| O4 | R8: two bearers would each lift about 71 kg to chest height to clear a 400 mm step | A: four bearers at steps, two lifting at handles on the cross stubs (about 36 kg each); B: padded shoulder yokes for the two bearers (71 kg each on the shoulders) | **A** | Two webbing lift handles; fitting card | DLT-CAL-001, section 8 |

## To confirm when parts are bought

These are facts that can only be settled with real parts, real dolis or the first partner. None changes a decision; each may change a size or a limit.

*Table 2. Items to confirm.*

| # | What to confirm | Why it matters | Source |
| --- | --- | --- | --- |
| 1 | Seller's ratings of the bought wheel (200 kg assumed) and tyre (150 kg) | R3 and O1 | DLT-CAL-001, A10 |
| 2 | Brake clamp force at about 150 N hand pull with the lock set (2.0 kN per pad assumed) and wet pad friction (0.35) | R5 brake factor | DLT-CAL-001, A5 |
| 3 | Diametral crushing of local bamboo poles of 40 to 80 mm in the V jaws (4.0 kN for 40 mm length assumed) | R1 crushing factor, the hand-tight rule | DLT-CAL-001, A7 |
| 4 | Rubber on wet bamboo friction (0.35 assumed) | R1 slip factor | DLT-CAL-001, A6 |
| 5 | Tyre grip on the partner's trails, wet (0.35 assumed) | R5 and O2 | DLT-CAL-001, A4 |
| 6 | How real dolis' beds are fixed to the poles; whether the lashing can be slid aside at the clamp points, and what to do with sewn sleeves | Clamp position; fitting time | DLT-DDR-002, A3 |
| 7 | Pole spacing, diameter and length of dolis in the partner's villages | Arm range and width (R6) | DLT-DDR-001, D6 |
| 8 | Masses of the bought wheel, brake, harness webbing and bag | R7 | DLT-CAL-001, A12 |
| 9 | That US7922183B2 (Hill-Rom stretcher brake) has lapsed, before any public claim about the brake | Design-around | DLT-PRC-001 |

## Value engineering

Value-engineering target: USD 1,500 (a hypothetical control target, not a limit). Estimated cost of the constructable design: USD 455 (USD 1,045 under the target). Main cost drivers and savings worth trying:

- The largest lines are the two harnesses (USD 70), the fork unit (USD 62), the four side arms (USD 60), the wheel (USD 55) and the brake set (USD 45).
- Savings worth trying: cycle-rickshaw workshops already weld similar frames and could make the fork unit and arms together in a batch (perhaps USD 30 a kit); harnesses from used truck seat-belt webbing (about USD 25); a secondhand cargo wheel inspected and proof-loaded (about USD 25).
- The target leaves room for the recommended options in O1 to O4 (each under USD 40) without passing it.

## Decisions made

*Table 3. Decisions made.*

| Date | Decision | Decided by | Record |
| --- | --- | --- | --- |
| 2026-10-03 | TRL 2 review items D1 to D9: one wheel under the hips; rubber-lined V clamps on telescoping arms with hand bolts; cable disc brake with a parking lock on every kit; pole loops on slings; 20 inch cargo wheel with a solid axle; rated patient 120 kg on a 10 kg reference doli; first-trial kits kept in the ambulance; first co-design candidates (a district 108 ambulance operator in Mayurbhanj, a maternal health NGO in the same block, a volunteer mountain rescue group; none approached yet); R10 and R11 added, R1 to R9 targets unchanged; pitch, design-arounds and budget unchanged | Amish, pre-approval of 2026-10-03: "start with the first 14 repos from the list of 29 projects. I pre-approve the batch runs along with any recommendations you come up with. I also accept any cost overruns or variations from the assumed scope cost." and "Proceed with the remaining 15 scaffolds" | DLT-DDR-001 |
| 2026-10-03 | Design for construction, changes C1 to C11: welded fork unit with cross stubs and struts; telescoping side arms with V saddles; T-handle bolts and set screws; cross strap; caliper lobe on the dropout plate; lever mount; pole loops; solid axle in open slots; clamps on bare pole; wheel bag; pump and ties | Amish, same pre-approvals | DLT-DDR-002 |
| 2026-10-03 | Assumptions A1 to A5: sound poles only; clamps hand tight, never with a bar (conservative; relaxed only by crush tests on local bamboo); sewn bed sleeves not fitted until the partner trial decides; bought ratings confirmed; jig-welded, inspected frame | Amish, same pre-approvals | DLT-DDR-002 |
| 2026-10-03 | Sandbags before people: no person on the doli before the frame and wheel proof loads and the wet ramp test pass; the first person carried is a healthy volunteer (conservative; a gate, not relaxed) | Amish, same pre-approvals | DLT-BLD-001, sections 5 and 6 |
| 2026-10-03 | Appearance model departures: bamboo and cloth colours for the family's doli, a 1.75 m mannequin standing beside the doli on its far side, and a repeated front right clamp for the detail view, drawn for the renders only | Amish, same pre-approvals | docs/REVIEW.md, TRL 3 section |
