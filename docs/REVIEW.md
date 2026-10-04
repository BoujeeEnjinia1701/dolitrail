# Review note: DoliTrail

## Session 2026-10-03: round 2 requirement decisions applied

Amish, 2026-10-03: "i approve all of the 47 recommendations provided by you. Execute them." For this repo that decides D-A1 to D-A4 (register O1 to O4) as recommended, recorded in `docs/decisions/0003-requirement-decisions-round2.md` (DLT-DDR-003). TRL 3 scope only: nothing built, bought, loaded or carried; the proof load and trials are TRL 4 steps in the build plan.

### What was done

- `cad/src/model.py`: two lift handles (BOM 16), 25 mm webbing loops wrapped round the cross stubs between the strut and the set screw, hanging 140 mm (front stub left of centre, rear stub right of centre); hold-back strap loops (BOM 17) on the rear pole ends, outboard of the harness loops. 83 of 83 constructability checks pass (75 before): each handle clear of the struts, set screws, arms, wheel and brake, 83 mm from the tyre and 348 mm above the ground; each hold-back loop on its pole end, 10 mm from the harness loop.
- `docs/04-calcs/sizing.py`: two bags, handle and hold-back masses, bag loads, grip at the 20 per cent rule grade, worst-case hold-back strap force, four-bearer step rule. Re-run: `results.csv` and `01-sizing.md` (DLT-CAL-001 v0.2).
- `bom/bom.csv`: line 12 two bags (USD 20 each), new line 16 lift handles (2 at USD 3), new line 17 hold-back strap (USD 6); prices estimated from the existing webbing and bag lines.
- Regenerated with the repo's scripts: STEP and STL; general arrangement DLT-DWG-001 Rev P3; making sketches DLT-DWG-101 to 106 (unchanged parts, redrawn by the same run); build plan overview, joints 1 to 8 and new joints 9 (lift handle) and 10 (hold-back loops), steps 1 to 9; concept hero, cutaway, exploded, flow and blueprint DLT-DWG-010 Rev P2; `media/model.glb` (1.7 MB, linear deflection 1.0 mm, angular deflection 0.35 rad) and `media/viewer.html`.
- Documents: DLT-REQ-001 v0.3 (status only, targets unchanged), DLT-PRC-001 v0.3, DLT-BLD-001 v0.2 (new section 3.11 lift handles and hold-back strap, two bags, wheel proof load and fallback, steps 8 and 9, first checks, safety stops S4 to S6), DLT-DEC-001 v0.2 (O1 to O4 decided, O5 added, change log), README, `cad/src/product_model.py` (handles and hold-back loops added for the next render), `project.yaml` trl_evidence.

### Requirement status

| ID | Before (DLT-CAL-001 v0.1) | After (DLT-CAL-001 v0.2) |
| --- | --- | --- |
| R3 | At risk: wheel 0.70, tyre 0.53 of twice the load on ratings | Met if the 285 kg static proof load holds; unproven until TRL 4 |
| R5 | At risk: grip 0.84 on wet clay | Met with the bearer's help: hold-back strap; lift and carry on wet clay over 20 per cent (grip 1.37 at 20 per cent) |
| R7 | Not met: 14.8 kg in one bag | Each load met, not one load for one person: 15.5 kg in bags of 6.9 and 8.7 kg |
| R8 | Not met: 71 kg each, two bearers | Met with four people at steps over about 250 mm: about 36 kg each |
| R9 | USD 455 | USD 482 |

Others unchanged (R1, R2, R4, R6, R10, R11 met on paper). Lowest structural factor 2.02 to 2.01 with the 0.2 kg of handles; rolling weight 142.3 to 142.5 kg, so twice the wheel load is still 285 kg.

### Cost

Value-engineering target: USD 1,500. Estimated cost of the constructable design: USD 482 (USD 1,018 under the target), up USD 27 from USD 455: second bag USD 15, lift handles USD 6, hold-back strap USD 6 (estimates). `budget_usd` is the target and is unchanged.

### Decisions for Amish

**O5. Steps below the 250 mm threshold.** **Proposed, awaiting Amish.** State: below about 250 mm two bearers still lift the whole rolling weight, about 71 kg each, by up to 300 mm (poles to about 1,020 mm), for any step the wheel cannot roll up. Cause: the wheel carries the patient, so it must be lifted with everything on it.
- A: keep the 250 mm threshold and measure the lift with sandbags at TRL 4 before any person is carried. No change now.
- B: four bearers at any step the wheel cannot roll up (about 100 mm, estimate, to find in the sandbag trials). No hardware; fitting card and safety stops.
- C: a step board carried in the kit to ramp the wheel up steps to about 250 mm. About USD 10 and 1.5 kg (estimates); worsens R7.
- **Recommendation: B**, the conservative rule: 71 kg per person is not a safe lift at any height, and four bearers are already the rule at higher steps.

### Safety notes

- **Wheel proof load first.** No person is carried until the bought wheel and tyre hold a 285 kg static proof load for 10 min (TRL 4), as well as the 260 kg frame proof load and the wet ramp test. If the wheel or tyre fails, the heavier tricycle wheel and 20 x 2.4 cargo tyre are fitted and proof-loaded before anyone is carried. A paper factor is not a test.
- **Hold-back strap and the wet clay rule.** On every descent the rear bearer's hold-back strap is clipped to the hip belt before the doli moves. On wet clay or mud steeper than 20 per cent the doli is lifted and carried, never rolled, whatever the strap. The strap works only with the braking bearer downhill and the strapped bearer uphill: if a descent would put the rear bearer downhill, the doli is turned at the top or carried. The rear bearer must be able to sit back into the strap; a tired or slipping bearer is a reason to stop and carry.
- **Four bearers at steps over about 250 mm.** Two bearers never lift the loaded doli over such a step; the two helpers lift at the handles on the cross stubs, on opposite sides, and all four lift together on a call. Below 250 mm see O5.
- **Two bags.** Two people walk to the patient with the kit, which is already how dolis travel; neither bag weighs more than 10 kg.
- Handles and hold-back strap are checked at every fitting for cuts and pulled stitches (safety stop S6) and are proof-hung on the bench before first use (75 kg per handle, 80 kg on the strap).

### Re-render

Small geometry change only: two webbing loops under the cross stubs and two short loops on the rear pole ends, both largely hidden under the doli in the hero view. A re-render is not essential for the hero; the exploded and detail views would gain the new parts at the next render on the Mac, since `product_model.py` now includes them.

### Recommended next step

- Amish decides O5. Then the design looks ready for TRL 4 once Amish chooses to start it: build one kit, proof-load the frame (260 kg) and the wheel and tyre (285 kg static) with CalRig, run the wet ramp test and a wet clay slope test with sandbags and the hold-back strap, and a four-bearer step lift with sandbags. Recommendation only, not started.

## Session 2026-09-30: scaffolded

### What was done

- Repository created from kit 1.6.0 at TRL 1, target TRL 2.
- `docs/01-problem.md` (DLT-PRB-001 v0.1): problem with cited evidence, users, environment, constraints, prior work, open questions.
- `docs/02-concept.md` (DLT-PRC-001 v0.1): how it works, components, patent design-arounds, shared blocks, safety.
- `docs/03-requirements.md` (DLT-REQ-001 v0.1): 9 proposed requirements.
- `README.md` with concept rationale, burning platform, where it could be used, and what sparked the idea.

### Next

- Run `/populate` to bring the repo to a strong TRL 2 with concept media.

## Session 2026-10-03: TRL 2 (populate)

Run as the first half of `/to-trl3` under Amish's pre-approval of 2026-10-03: "start with the first 14 repos from the list of 29 projects. I pre-approve the batch runs along with any recommendations you come up with. I also accept any cost overruns or variations from the assumed scope cost." and his instruction of the same day for batch 2: "Proceed with the remaining 15 scaffolds". Kit 1.7.0 installed.

### What was done

- `docs/01-problem.md` (DLT-PRB-001 v0.2): constraints restated (value-engineering target, clamps on bare pole), open questions settled, first co-design candidates, safety section.
- `docs/02-concept.md` (DLT-PRC-001 v0.2): how it works, components with BOM numbers, key design choices, first-order numbers, design-arounds kept, safety.
- `docs/03-requirements.md` (DLT-REQ-001 v0.2): R1 to R9 with targets unchanged; R10 and R11 added; TRL 3 status.
- Concept media from `cad/src/concept_media.py`: `media/hero.png` (1.75 m person), `media/cutaway.png` (cut through the front clamps), `media/exploded.png` (BOM callouts), `media/flow.png` (where the weight goes, estimates), `media/concept-blueprint.png`, `.pdf` and `.svg` (DLT-DWG-010), `media/model.glb` (1.7 MB, coarse tessellation) and `media/viewer.html`.
- `bom/bom.csv`: 15 priced lines.

### Results

- One wheel under the patient's hips keeps the kit inside the doli's own width; the clamps reach every pole size in the problem statement.

### Requirements not met

- R3, R5, R7 and R8 (see TRL 3).

### Decisions made under the pre-approval

DLT-DDR-001, items D1 to D9: one wheel; V clamps on telescoping arms with hand bolts; cable disc brake with a parking lock; pole loops on slings; 20 inch cargo wheel with a solid axle; rated load and reference doli; first-trial kits in the ambulance; first co-design candidates (not approached); R10 and R11 added.

### Safety concerns

- The doli rolls on one wheel and can tip sideways; bearers keep both hands on the poles.

## Session 2026-10-03: TRL 3 (advance and build plan)

Run as the second half of `/to-trl3` under the same pre-approvals, which count as the TRL 2 approval. Not committed or pushed (batch run).

### What was done

- `cad/src/model.py`: parametric build123d model of the kit on the reference doli (two 60 mm bamboo poles at 550 mm centres); 75 of 75 constructability checks pass (wheel in the fork with 15 mm mud clearance, axle nuts on the plates, caliper on its lobe and clear of spokes, arms in the stubs, liners on the pole, the clamp closing on 40 and 80 mm poles, bolts clear of the pole, strap and bed 100 mm or more above the tyre, 150 mm ground clearance, width). Exports `cad/step/dolitrail-assembly.step`, `dolitrail-kit.step`, `reference-doli-context.step`, the fork unit, side arm, upper jaw and lever mount, and STL of the arm, jaw, liners and lever mount.
- `docs/04-calcs/01-sizing.md` (DLT-CAL-001 v0.1) with `docs/04-calcs/sizing.py` and `results.csv`.
- `cad/src/sheets.py`: general arrangement `cad/drawings/DLT-DWG-001` (SVG, PDF, PNG) at Rev P2, with section A-A at 1:10.
- `cad/src/build_plan_media.py`: `docs/05-build-plan/overview.png`, 6 making sketches `cad/drawings/DLT-DWG-101` to `106`, 8 joint close-ups and 9 step pictures.
- `docs/05-build-plan.md` (DLT-BLD-001 v0.1), `docs/06-design-decisions.md` (DLT-DEC-001 v0.1), `docs/decisions/0001-trl2-review-decisions.md` (DLT-DDR-001) and `docs/decisions/0002-design-for-construction.md` (DLT-DDR-002).
- `cad/src/product_model.py` (appearance model) and render scenes exported with `.kit/export_views.py` to `/home/claude/renders/dolitrail` for hero, exploded and detail views; photoreal renders and cards are made on Amish's Mac.
- `project.yaml`: trl 3, trl_target 3, `design_state: constructable`, evidence listed; `budget_usd` unchanged. README leads with `media/render-hero.png` and has a "Building the prototype" section.

### Results

- Rolling weight 142 kg (120 kg patient, 10 kg doli, 12.3 kg fitted kit).
- Level trail: about 14 kg per bearer against 65 kg carried by two bearers, 79 per cent less (estimate). On a 30 per cent descent with the brake on, the front bearer holds about 46 kg (estimate).
- Brake factor 1.23 on a wet 30 per cent grade; tyre grip factor 1.44 on a wet ramp and 0.84 on wet clay.
- Clamps: 3.96 kN slip resistance per pole, wet (factor 2.6); bamboo crushing factor 2.0 to confirm.
- Lowest structural factor on yield at twice the rated load: 2.02 (struts).
- Width 680 mm on the reference doli; fitting about 4.7 min (estimate); kit 14.8 kg in the bag.
- Value-engineering target: USD 1,500. Estimated cost of the constructable design: USD 455 (USD 1,045 under the target).

### Requirements not met or at risk

R3 and R5 are at risk; R7 and R8 are not met. Each is posed below for Amish to decide. R9 is under the value-engineering target. R2 and R4 rest on estimates.

### Decisions for Amish

All four are recorded in DLT-DEC-001 as **Proposed, awaiting Amish**.

**D-A1. R3, wheel and tyre margin.**
- State: the fork unit, arms and clamps carry twice the rated load with a factor of 2.02 on yield, but the wheel's catalogue rating (200 kg assumed) is 0.70 of twice the wheel load and the tyre's (150 kg) is 0.53 of it. Cause: no light bicycle-type wheel or tyre is catalogue-rated for twice a 142 kg load.
- Option A: keep the 20 inch cargo wheel and show the margin by a 285 kg static proof load of the bought wheel and tyre before any person is carried. Effect: R3 met if the proof load holds; cost and mass unchanged.
- Option B: a heavier 20 inch tricycle wheel (13 gauge spokes, about 300 kg rating) and a 20 x 2.4 cargo tyre (about 200 kg). Effect: wheel about 1.05 and tyre about 0.70 of twice the load on ratings, still needing the proof load for the tyre; about USD 30 more and 0.6 kg heavier (worsens R7).
- Option C: a 10 inch scooter wheel with a drum hub (3.00-10 tyre, about 190 kg). Effect: about 0.67 on rating; about USD 20 more, 2.4 kg heavier, a new brake and 54 mm less ground clearance.
- **Recommendation: A**, moving to B only if the proof load fails. Ratings are working loads with their own unstated margin, so only a proof load shows the real one.

**D-A2. R5, grip on a wet descent.**
- State: the brake holds (factor 1.23), and the tyre holds on a wet test ramp (1.44), but on wet clay or mud the tyre grip factor is 0.84: the wheel would slide with about 7 kg-force unheld. Cause: tyre friction on mud is about equal to the slope.
- Option A: a hold-back strap from the uphill (rear) bearer's hip belt to the rear pole ends, plus the rule to lift and carry on wet clay steeper than 20 per cent. Effect: the bearer holds the shortfall; R5 met with the bearer's help, not by the kit alone; about USD 6 and 0.2 kg.
- Option B: a lever-dropped steel drag claw behind the wheel, hinged on the rear stub. Effect: grip factor about 1.5 on mud (estimate); about USD 35 and 1.1 kg (worsens R7); can catch on roots.
- Option C: a mud tyre with taller knobs (friction about 0.45). Effect: grip factor about 1.08, a thin margin; about USD 10 and 0.1 kg.
- **Recommendation: A.** It keeps a person in control of the load on the worst ground and costs almost nothing; C can be added later if trail tests show the margin is needed.

**D-A3. R7, kit mass.**
- State: 14.8 kg in one bag (12.3 kg fitted). Cause: the steel frame with its bolts (7.8 kg) and the wheel and brake (3.4 kg) alone pass the R7 figure.
- Option A: two bags carried by the two bearers, who walk in together: the fork unit with the wheel, brake and pump (about 6.9 kg with its bag), and the arms, jaws, bolts, lever mount, straps and harnesses (about 8.3 kg). Effect: each load within R7, but not one load for one person; about USD 15 and 0.3 kg.
- Option B: lighter parts: aluminium-handled T-bolts, 1.2 mm wall arms, an alloy hub. Effect: about 13.6 kg, still not met; structural factors stay above 2 on paper; about USD 25.
- Option C: an aluminium frame, TIG welded. Effect: about 11.5 kg, still not met; about USD 120; cannot be repaired by a village welder.
- **Recommendation: A.** Two bearers always walk to the patient, and the steel frame stays repairable.

**D-A4. R8, lifting over a 400 mm step.**
- State: two bearers would each lift about 71 kg from knuckle height to about 1,170 mm (chest height). Cause: the tyre hangs 720 mm below the poles, so the poles must rise 450 mm for the wheel to clear the step.
- Option A: four bearers at steps over about 250 mm: the two extra helpers lift at two webbing handles on the cross stubs. Effect: about 36 kg each, as on a doli today; R8 met with four people, not two; about USD 6 and 0.2 kg.
- Option B: padded shoulder yokes so the two bearers lift the pole ends onto their shoulders (about 1,350 mm). Effect: the wheel clears, but each bearer takes about 71 kg on the shoulders; about USD 20 and 1.2 kg (worsens R7).
- **Recommendation: A.** Villages already carry in relays, and 71 kg per person to chest height is not a safe lift.

### Decisions made under the pre-approval

- DLT-DDR-002: design for construction, changes C1 to C11 and assumptions A1 to A5.
- Sandbags before people: no person carried until the proof loads and the wet ramp test pass; the first person is a healthy volunteer.
- Appearance model departures (renders only): bamboo and cloth colours for the family's doli, a 1.75 m mannequin standing beside the doli on its far side (never between the camera and the product), and a repeated front right clamp for the detail view.

### Build plan findings

- Design changes for construction (2026-10-03), all in DLT-DDR-002: a welded fork unit with cross stubs fore and aft of the wheel and four struts; telescoping side arms with rubber-lined V saddles; upper jaws with two T-handle bolts; T-handle set screws; a webbing cross strap above the wheel; the caliper on a lobe of the left dropout plate; a strapped lever mount; pole loops on slings; a solid axle in open slots; clamps on bare pole with the bed lashing slid aside; a wheel bag; a pump and ties.
- A clamp that closes round a pole cannot pass a bed covering sewn round the pole as a sleeve; such dolis are not fitted until the partner trial decides how (item to confirm 6 in DLT-DEC-001).
- Items to confirm with real parts (wheel, tyre and brake ratings, bamboo crushing, friction, bed fixing, local doli sizes, masses, the brake patent's lapse) are in DLT-DEC-001.

### Safety concerns

- Patient transport over steep wet ground: not certified medical or rescue equipment. Safety stops S1 to S6 in DLT-BLD-001 gate welding, loading, the wet ramp test, any trail trial with a person and every fitting.
- One wheel: the doli can tip sideways; on a 15 per cent side slope each bearer's hands hold about 16 kg up or down.
- Wet clay descents: grip, not the brake, is the limit (D-A2).
- Steps: lifting by two bearers is unsafe (D-A4).
- Bamboo can split under a clamp; clamps are hand tight only and poles are checked at every fitting.

### Recommended next step

Amish decides D-A1 to D-A4. Then the design looks ready for TRL 4 once Amish chooses to start it: build one kit, proof-load the frame and the wheel with CalRig, run the wet ramp test with sandbags, and take the first checks in DLT-BLD-001 section 5 to the first co-design candidate.

## 2026-10-03: photoreal renders

Rendered with Blender Cycles on Amish's Mac from `cad/src/product_model.py`; captioned with `.kit/photo_caption.py`; `media/card.png` and `media/social-preview.png` made with `.kit/cards.py`. Views: hero, exploded, detail. image_qc passes and `render.py --check` has no FAIL.
