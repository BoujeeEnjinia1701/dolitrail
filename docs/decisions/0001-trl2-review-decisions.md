---
doc_id: DLT-DDR-001
title: DoliTrail TRL 2 review decisions
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
  change: TRL 2 review items decided under Amish's 2026-10-03 pre-approvals
---

# 0001: TRL 2 review decisions

- **Date:** 2026-10-03
- **Status:** decided. Decided by Amish under his pre-approval of 2026-10-03: "start with the first 14 repos from the list of 29 projects. I pre-approve the batch runs along with any recommendations you come up with. I also accept any cost overruns or variations from the assumed scope cost." and his instruction of the same day for this batch: "Proceed with the remaining 15 scaffolds".

## Context

The scaffold (DLT-PRB-001, DLT-PRC-001 and DLT-REQ-001, all v0.1) described a single wheel in a fork under the doli, clamps on the poles, a cable or rod brake, padded harnesses with pole-end cups and quick-release patient straps. It left five open questions: one wheel or two, how much of a route rolls, where kits are kept, what commercial kits exist, and whether a harness shifts load safely. Populating the concept to TRL 2 meant settling these and choosing the main parts. Items that touch safety take the conservative option and say what evidence would relax it. Partners are the first candidates to approach, not agreements. Requirements that the design does not meet are not decided here; they are posed to Amish (DLT-DEC-001).

## Options considered

*Table 1. Options.*

| # | Item | Options |
| --- | --- | --- |
| D1 | Wheels | (a) one wheel under the patient's hips; (b) two wheels side by side; (c) two wheels in line |
| D2 | Pole fixing | (a) rubber-lined V clamps on telescoping arms, hand bolts; (b) ratchet straps only; (c) U-bolts and nuts |
| D3 | Brake | (a) cable disc brake, 203 mm rotor, lever with parking lock; (b) rim brake; (c) hub drum brake |
| D4 | Harness to pole | (a) pole-end cups; (b) webbing pole loops on adjustable slings |
| D5 | Wheel | (a) 20 inch cargo or tricycle wheel, knobbly 2.125 tyre; (b) 16 inch; (c) wheelbarrow wheel |
| D6 | Rated load and reference doli | 120 kg patient (R3), 10 kg doli of two 60 mm poles at 550 mm centres |
| D7 | Kit storage for the first trial | (a) in the ambulance; (b) at the road end; (c) in the village |
| D8 | Co-design partner | 108 ambulance operators, maternal health NGOs, village health committees, rescue groups |
| D9 | Requirements | Keep R1 to R9 and their targets; add patient release and brake reach |

## Decision

- **D1 (a).** One wheel under the patient's hips. The wheel stays inside the doli's own width (R6); the bearers steady it in roll. Conservative consequence: the tipping hazard is named in every document and bearers keep both hands on the poles.
- **D2 (a).** Rubber-lined 90 deg V saddles on four square-tube arms that telescope into the fork unit's stubs, closed by upper jaws and two T-handle bolts each. Straps alone could creep on wet bamboo; U-bolts need spanners and crush thin poles.
- **D3 (a).** Cable disc brake with sintered pads and a lever with a parking lock, on the front right pole. A rim brake fails in mud; a drum hub of the needed torque is heavy and harder to find. The parking lock is required on every kit (conservative), so the doli never relies on a hand to stay put on a slope.
- **D4 (b).** Pole loops on slings fit any pole end and any bearer height; cups would need sizes.
- **D5 (a).** 20 inch cargo or tricycle wheel with a knobbly 57-406 tyre and a solid axle (no quick release, conservative). A 16 inch wheel rolls worse over roots; a wheelbarrow wheel takes no disc brake.
- **D6.** Rated patient 120 kg; reference doli two 60 mm bamboo poles 2.55 m long at 550 mm centres, 10 kg with sticks, cloth and rope.
- **D7 (a).** First trial kits travel in the ambulance and are carried in by the crew, so a service maintains them.
- **D8.** First candidates to approach, in order (none approached yet): a district 108 ambulance operator in Mayurbhanj, Odisha; a maternal health NGO working with village health committees in the same block; a volunteer mountain rescue group for trail technique.
- **D9.** R1 to R9 kept with their targets unchanged. R10 (each patient strap frees with one pull in 3 s or less) and R11 (the front bearer works the brake and lock without letting go) added.
- **Unchanged:** the pitch, the problem, the design-arounds (own clamp geometry and colours; lapse of US7922183B2 to be confirmed) and `budget_usd` (USD 1,500), read as a value-engineering target.

## Consequences

- The kit is a welded steel frame, a bought wheel and brake and sewn webbing; a village workshop and a tailor can make and repair it.
- R3, R5, R7 and R8 fall short or are at risk on paper (DLT-CAL-001); each is posed to Amish in DLT-DEC-001 with options and a recommendation.
- The design is made constructable in DLT-DDR-002.

> **Safety:** D1, D3 and D5 carry the conservative choices: both hands on the poles, a parking lock on every kit and a solid axle. The single-wheel tipping hazard would be relaxed only by trail trials with a dummy load showing that bearers hold it on side slopes.
