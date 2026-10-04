---
doc_id: DLT-DEC-001
title: DoliTrail design decisions register
project: DoliTrail
doc_type: Design decisions register
version: "0.2"
status: Draft
date: '2026-10-03'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-03'
  author: Amish Chadha
  change: Register opened; design decisions made under Amish's 2026-10-03 pre-approvals; four requirement decisions proposed, awaiting Amish
- version: "0.2"
  date: '2026-10-03'
  author: Amish Chadha
  change: O1 to O4 decided by Amish on 2026-10-03 (DLT-DDR-003) and moved to decisions made; new open decision O5; items to confirm and value engineering updated; change log added
---

# DoliTrail design decisions register

Every design decision still to be made, and every decision made, in one place. Each decision is argued in full in its decision record under `docs/decisions/` or in `docs/REVIEW.md`; this register is the index Amish works from. The build plan (`docs/05-build-plan.md`) describes the design as it stands and does not list decisions.

> **Safety:** Several entries set safety limits (one wheel steadied with both hands, a parking lock on every kit, a solid axle, hand-tight clamps, sandbags before people, the 285 kg wheel proof load before any person is carried, the hold-back strap, lift and carry on wet clay steeper than 20 per cent, four bearers at steps over about 250 mm). Each takes the conservative option and names the evidence that would relax it. DoliTrail is not certified medical or rescue equipment.

## Open decisions

O1 to O4 were decided by Amish on 2026-10-03 and are under Decisions made (DLT-DDR-003). One new decision is **Proposed, awaiting Amish**, set out in full in `docs/REVIEW.md` (session of 2026-10-03, round 2); the design and build plan stay as they are until he decides.

*Table 1. Open decisions.*

| # | Decision needed | Options | Recommendation | Affects in the build | Source |
| --- | --- | --- | --- | --- | --- |
| O5 | Steps up to the decided 250 mm threshold: two bearers still lift about 71 kg each, by up to 300 mm (poles to about 1,020 mm), because the whole rolling weight must rise for the wheel to clear any step it cannot roll up | A: keep the 250 mm threshold and measure the lift with sandbags at TRL 4 before any person is carried. B: four bearers at any step the wheel cannot roll up (about 100 mm, estimate, to find in the sandbag trials). C: a step board carried in the kit to ramp the wheel up steps to about 250 mm (about USD 10 and 1.5 kg, estimate; worsens R7) | **B**, the conservative rule: 71 kg per person is not a safe lift at any height, and four bearers are already the rule at higher steps | Fitting card and safety stops; no hardware for B | DLT-CAL-001 v0.2, H6; DLT-DDR-003 |

## To confirm when parts are bought

These are facts that can only be settled with real parts, real dolis or the first partner. None changes a decision; each may change a size or a limit.

*Table 2. Items to confirm.*

| # | What to confirm | Why it matters | Source |
| --- | --- | --- | --- |
| 1 | Seller's ratings of the bought wheel (200 kg assumed) and tyre (150 kg); the 285 kg static proof load at TRL 4 decides R3 | R3 and DLT-DDR-003, O1 | DLT-CAL-001, A10 |
| 2 | Brake clamp force at about 150 N hand pull with the lock set (2.0 kN per pad assumed) and wet pad friction (0.35) | R5 brake factor | DLT-CAL-001, A5 |
| 3 | Diametral crushing of local bamboo poles of 40 to 80 mm in the V jaws (4.0 kN for 40 mm length assumed) | R1 crushing factor, the hand-tight rule | DLT-CAL-001, A7 |
| 4 | Rubber on wet bamboo friction (0.35 assumed) | R1 slip factor | DLT-CAL-001, A6 |
| 5 | Tyre grip on the partner's trails, wet (0.35 assumed), and where wet clay steeper than 20 per cent lies on them | R5, the hold-back strap and the wet clay rule | DLT-CAL-001, A4 |
| 6 | How real dolis' beds are fixed to the poles; whether the lashing can be slid aside at the clamp points, and what to do with sewn sleeves | Clamp position; fitting time | DLT-DDR-002, A3 |
| 7 | Pole spacing, diameter and length of dolis in the partner's villages | Arm range and width (R6) | DLT-DDR-001, D6 |
| 8 | Masses of the bought wheel, brake, harness webbing, the two bags, the lift handles and the hold-back strap; each packed bag under 10 kg | R7 | DLT-CAL-001, A12 |
| 10 | Breaking strength of the 25 mm webbing with sewn ends in the lift handles and hold-back strap (5 kN assumed) | Hold-back strap factor 12; lift handles | DLT-CAL-001, A14 |
| 9 | That US7922183B2 (Hill-Rom stretcher brake) has lapsed, before any public claim about the brake | Design-around | DLT-PRC-001 |

## Value engineering

Value-engineering target: USD 1,500 (a hypothetical control target, not a limit). Estimated cost of the constructable design: USD 482 (USD 1,018 under the target), including USD 27 for the round 2 decisions (second bag, lift handles, hold-back strap). Main cost drivers and savings worth trying:

- The largest lines are the two harnesses (USD 70), the fork unit (USD 62), the four side arms (USD 60), the wheel (USD 55) and the brake set (USD 45).
- Savings worth trying: cycle-rickshaw workshops already weld similar frames and could make the fork unit and arms together in a batch (perhaps USD 30 a kit); harnesses from used truck seat-belt webbing (about USD 25); a secondhand cargo wheel inspected and proof-loaded (about USD 25).
- The round 2 decisions added USD 27. If the wheel proof load fails, the heavier wheel and tyre add about USD 30.

## Decisions made

*Table 3. Decisions made.*

| Date | Decision | Decided by | Record |
| --- | --- | --- | --- |
| 2026-10-03 | TRL 2 review items D1 to D9: one wheel under the hips; rubber-lined V clamps on telescoping arms with hand bolts; cable disc brake with a parking lock on every kit; pole loops on slings; 20 inch cargo wheel with a solid axle; rated patient 120 kg on a 10 kg reference doli; first-trial kits kept in the ambulance; first co-design candidates (a district 108 ambulance operator in Mayurbhanj, a maternal health NGO in the same block, a volunteer mountain rescue group; none approached yet); R10 and R11 added, R1 to R9 targets unchanged; pitch, design-arounds and budget unchanged | Amish, pre-approval of 2026-10-03: "start with the first 14 repos from the list of 29 projects. I pre-approve the batch runs along with any recommendations you come up with. I also accept any cost overruns or variations from the assumed scope cost." and "Proceed with the remaining 15 scaffolds" | DLT-DDR-001 |
| 2026-10-03 | Design for construction, changes C1 to C11: welded fork unit with cross stubs and struts; telescoping side arms with V saddles; T-handle bolts and set screws; cross strap; caliper lobe on the dropout plate; lever mount; pole loops; solid axle in open slots; clamps on bare pole; wheel bag; pump and ties | Amish, same pre-approvals | DLT-DDR-002 |
| 2026-10-03 | Assumptions A1 to A5: sound poles only; clamps hand tight, never with a bar (conservative; relaxed only by crush tests on local bamboo); sewn bed sleeves not fitted until the partner trial decides; bought ratings confirmed; jig-welded, inspected frame | Amish, same pre-approvals | DLT-DDR-002 |
| 2026-10-03 | Sandbags before people: no person on the doli before the frame and wheel proof loads and the wet ramp test pass; the first person carried is a healthy volunteer (conservative; a gate, not relaxed) | Amish, same pre-approvals | DLT-BLD-001, sections 5 and 6 |
| 2026-10-03 | Appearance model departures: bamboo and cloth colours for the family's doli, a 1.75 m mannequin standing beside the doli on its far side, and a repeated front right clamp for the detail view, drawn for the renders only | Amish, same pre-approvals | docs/REVIEW.md, TRL 3 section |
| 2026-10-03 | Round 2 requirement decisions: O1 (R3) A, keep the 20 inch cargo wheel and prove it with a 285 kg static proof load before any person is carried, moving to B (heavier tricycle wheel and 20 x 2.4 cargo tyre) only if the proof load fails; O2 (R5) A, a hold-back strap from the rear bearer's hip belt to the rear pole ends, and lift and carry on wet clay steeper than 20 per cent; O3 (R7) A, two bags carried by the two bearers; O4 (R8) A, four bearers at steps over about 250 mm, the two helpers lifting at webbing handles on the cross stubs | Amish: "i approve all of the 47 recommendations provided by you. Execute them." | DLT-DDR-003 |

## Change log

- 2026-10-03, v0.2: O1 to O4 moved from Proposed, awaiting Amish to decided (DLT-DDR-003); O5 added as Proposed, awaiting Amish; items to confirm 1, 5 and 8 updated and 10 added; value engineering updated.
