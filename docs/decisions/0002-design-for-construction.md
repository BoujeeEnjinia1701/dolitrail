---
doc_id: DLT-DDR-002
title: DoliTrail design for construction
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
  change: Design made constructable; changes C1 to C11 and assumptions A1 to A5 decided under Amish's 2026-10-03 pre-approvals
---

# 0002: Design for construction

- **Date:** 2026-10-03
- **Status:** decided. Decided by Amish under his pre-approval of 2026-10-03: "start with the first 14 repos from the list of 29 projects. I pre-approve the batch runs along with any recommendations you come up with. I also accept any cost overruns or variations from the assumed scope cost." and his instruction of the same day: "Proceed with the remaining 15 scaffolds".

## Context

STANDARDS section 18 asks that every part can be made by a stated process and fits and fastens to its neighbours. The concept named a "wheel and fork", "pole clamps", a "cross frame and strap", a "brake and lever" and "pole-end cups", but did not say how the fork reaches the poles past a sagging bed, how the clamps adjust, where the brake caliper mounts or how the lever fixes to bamboo. The constructability review of the model (`cad/src/model.py`, 75 checks: overlaps and contacts between every part, the wheel in the fork with mud clearance, the caliper on its lobe, the arms in the stubs, the liners on the pole, the clamp closing on 40 and 80 mm poles, bolts clear of the pole, strap and bed clearance over the tyre, ground clearance, width) led to the changes below. None changes what the product does or its pitch.

## Changes

*Table 1. Changes made for construction.*

| # | The concept had | The constructable design has | Why |
| --- | --- | --- | --- |
| C1 | "A single wheel in a fork under the middle" | A welded fork unit: two 30 x 30 x 2 mm square cross stubs 600 mm apart, four 22.2 x 1.6 mm struts, 5 mm dropout plates with slots open downward | The stubs sit fore and aft of the 514 mm wheel, below the bed; the struts carry the load and the braking force as a truss |
| C2 | "Pole clamps" for varied diameters | Four side arms: a 25 mm square spigot sliding in a stub, a post and a 90 deg V saddle; upper jaw of bent 3 mm strip; 5 mm rubber liners | The V centres any pole of 40 to 80 mm; the arms telescope for 450 to 600 mm pole centres |
| C3 | Clamp tightening not stated | Two M8 T-handle bolts per clamp into nuts welded under the saddle; M8 T-handle set screws lock the arms | Hand tight, no loose tools (R1, R2) |
| C4 | "Cross frame and strap" | Frame is the fork unit and arms; the strap is a 50 mm webbing loop round both poles above the wheel | Keeps the bed 174 mm above the tyre; the frame alone is rigid |
| C5 | "Cable or rod brake" | 203 mm disc rotor on the hub; cable caliper on a lobe of the left dropout plate | Mount welded into the plate; the caliper sits low at the rear, clear of struts and spokes |
| C6 | "Lever at the front bearer's hand" | Lever mount: a 22.2 mm bar stub on a rubber-lined inverted V, two cam straps round the front right pole | A bicycle lever needs a 22.2 mm bar; bamboo poles vary |
| C7 | "Pole-end cups" | Pole loops on adjustable slings (D4) | Fits every pole end |
| C8 | Wheel fixing not stated | Solid 3/8 inch axle and nuts in slots open downward | Nothing to open by mistake; the wheel stays in the fork for carrying |
| C9 | Bed and clamp clash not considered | Clamps go on bare pole: where the bed is lashed or tied, the lashing is slid aside about 70 mm at each clamp point | The inboard bolt passes beside the pole where a bed covering leaves it |
| C10 | Carry bag | Wheel bag taking the fork unit with the wheel fitted | Protects the spokes; saves fitting time |
| C11 | No maintenance items | Pump and puncture kit; hook-and-loop ties for the brake housing | A flat tyre on the trail ends the use of the kit |

## Assumptions decided with the changes

- **A1.** The doli's poles are sound bamboo of 40 to 80 mm with no splits at the clamp points; a split pole is not used. Relaxed only by crush tests on local bamboo.
- **A2.** Clamp force is set by hand on the T-handles to about 1 kN per bolt (rubber just bulging); never with a bar or spanner, so the bamboo is not crushed.
- **A3.** The bed covering can be moved aside at the clamp points. If a covering is sewn round the poles as a sleeve, the kit is not fitted to that doli until the partner trial decides how (DLT-DEC-001, item to confirm).
- **A4.** Wheel, tyre and brake ratings are confirmed when bought (DLT-DEC-001).
- **A5.** Welds by a competent welder, inspected visually; fork unit welded in a jig with a 100 mm spacer bar in the dropouts.

## Consequences

- The kit has 15 BOM lines; six are made (fork unit, side arms, jaws, liners, lever mount, harnesses), the rest bought.
- The general arrangement DLT-DWG-001 is at Rev P2; making sketches DLT-DWG-101 to 106; build plan DLT-BLD-001.
- `design_state: constructable` in `project.yaml`.

> **Safety:** The frame carries a person. Every weld is inspected, the frame and clamps are proof-loaded to twice the rated load, and the brake is tested on a wet ramp with a dummy load before any patient is carried (DLT-BLD-001, sections 5 and 6).
