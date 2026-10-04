# Review note: DoliTrail

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

## 2026-10-03: Amish's requirement decisions carried out (round 2)

Amish on 2026-10-03: "i agree with all the 46 recommendations you provided. please proceed." For DoliTrail this decides O1 to O4 of DLT-DEC-001 as recommended: 6A (R3), 7A (R5), 8A (R7) and 9A (R8). Recorded in `docs/decisions/0003-requirement-decisions-round-2.md` (DLT-DDR-003). Not committed or pushed (batch run).

### Changes

- `cad/src/model.py`: hold-back strap (BOM line 16): two closed webbing end caps 40 mm deep over the rear pole ends, two 25 mm legs to a 40 mm steel ring, a 600 mm tail with a cam buckle to the rear bearer's hip belt. Lift handles (line 17): a 40 mm webbing band sewn shut round each cross stub, 100 mm off centre (front left, rear right), with a 130 mm hand loop and foam grip. Sixteen new checks; 91 of 91 constructability checks pass. STEP and STL regenerated (the new parts are in `dolitrail-assembly.step` and `dolitrail-kit.step`).
- `bom/bom.csv`: line 12 is now the wheel bag; new lines 16 (hold-back strap, USD 6), 17 (two lift handles, USD 3 each) and 18 (parts bag, USD 15), each with its price basis.
- `docs/04-calcs/sizing.py`, `results.csv` and `01-sizing.md` v0.2: new results [K13] to [K15], [B9] to [B11], [S12], [H5] to [H7]; assumptions A13 (carry limit) and A14 (webbing strength).
- `docs/03-requirements.md` v0.3 (targets unchanged; Amish quoted; status of R3, R5, R7, R8 and R9), `docs/02-concept.md` v0.3, README cost and key components.
- `docs/05-build-plan.md` v0.2: three new rows in Table 1; section 3.11 two bags; new sections 3.12 hold-back strap and 3.13 lift handles; step 9 adds the hold-back strap; first checks for the wheel proof load before use, the hold-back strap, each bag's mass and the four-person step; safety stops S3 and S5.
- Pictures: general arrangement DLT-DWG-001 Rev P3 (lift handles shown, note line); new making sketches DLT-DWG-107 (hold-back strap) and DLT-DWG-108 (lift handle); new joints 9 (lift handle) and 10 (hold-back cap); overview and steps 1 to 9 redrawn (the fork unit now carries the handles); concept media redrawn (hero, exploded with the handles, cutaway, blueprint DLT-DWG-010 Rev P2 key figures, `model.glb`).
- Register `docs/06-design-decisions.md` v0.2: O1 to O4 moved to Decisions made; items to confirm 1, 5 and 10 updated or added; value engineering updated.
- Appearance model `cad/src/product_model.py`: hold-back strap and lift handles in the hero and exploded views; scenes re-exported to `/home/claude/renders/dolitrail`.

### New results

- R3: frame, arms and clamps factor 2.01 on yield at twice the rated load (was 2.02; 0.2 kg of handles added). Each bought wheel is proof-loaded to 285 kg (twice the 142.5 kg rolling weight) for 10 minutes before use; the heavier tricycle wheel only if it fails. Met on paper for the frame; the wheel and tyre are shown by the proof load.
- R5: brake 1.23 and wet ramp grip 1.44 (verification test met on paper). Wet clay: 0.84 at 30 per cent, so the bearers lift and carry above 20 per cent, where grip is 1.37. The hold-back strap would take the 65 N shortfall on a 30 per cent wet clay patch met by surprise; strength factor about 25 against the whole along-slope force (webbing strength to confirm).
- R7: two bags of 7.2 kg (fork unit, wheel, brake, handles, pump) and 8.3 kg (everything else), each under 10 kg; the whole kit is 15.5 kg, so it is not one load for one person.
- R8: four people at steps, about 36 kg each; 350 N on each handle (webbing factor about 29; stub bending 13 MPa). With two bearers it is still about 71 kg each, which the drill rules out.
- R2: unchanged at about 4.7 min; the handles stay on the frame and the hold-back strap goes on with the harness loops.
- R9: Value-engineering target: USD 1,500. Estimated cost of the constructable design: USD 482 (USD 1,018 under the target). `budget_usd` unchanged.
- Mass: fitted kit 12.5 kg; rolling weight 142.5 kg; level-trail bearer load about 14 kg (79 per cent less), unchanged.

### For Amish

- New open decision O5 in the register. State: R7 still reads "kit mass at or below 10 kg and carried by one person" and R8 "two bearers lift", but decisions 8A and 9A meet them with two bags and four people. Option A: restate R7 as "kit carried in two bags, each at or below 10 kg, one per bearer" and R8 as "four people (two bearers, two helpers at lift handles) lift the fitted doli over a 400 mm step without removing the wheel, about 36 kg each". Option B: keep the wording and report both as met only per bag and with four people. **Recommendation: A**, so the requirements match the design that will be tested at TRL 4. Nothing in the build changes either way.
- The photoreal renders (`media/render-*.png`), card and social preview do not show the hold-back strap or lift handles yet; re-render on the Mac from the re-exported scenes.

### Safety

- The hold-back strap helps on wet descents; it does not replace the rule to lift and carry on wet clay steeper than 20 per cent. Two bearers never lift the fitted doli over a step alone.
- Every bought wheel is proof-loaded with sandbags under safety stop S3 before any person is carried; sandbags before people is unchanged.

### Recommended next step

Amish decides O5. The design then looks ready for TRL 4 when Amish chooses to start it.

## 2026-10-04: Amish's requirement decisions carried out (round 3)

Amish on 2026-10-04: "For round 3, I agree with all your proposed recommendations". For DoliTrail this decides O5 of DLT-DEC-001 as recommended (1A). Recorded in `docs/decisions/0004-requirement-wording-round-3.md` (DLT-DDR-004). Wording and records only; no geometry. Not committed or pushed.

### Changes

- `docs/03-requirements.md` v0.4: R7 restated as "two bags of 10 kg or less, one per bearer"; R8 restated as "four people at steps, two at the lift handles"; Amish quoted.
- `docs/04-calcs/01-sizing.md`: R7 note updated to the restated wording.
- `docs/06-design-decisions.md` v0.3: O5 moved to Decisions made; Open decisions now "None."
- No model, BOM, drawing or media change was needed.

### New results

- R7: met as designed; two bags of 7.2 and 8.3 kg, one per bearer.
- R8: met as designed; four people, about 36 kg each.
- R9: Value-engineering target: USD 1,500. Estimated cost of the constructable design: USD 482 (USD 1,018 under the target). Unchanged.

### For Amish

Nothing new.

## 2026-10-04: photoreal renders redone after the round-2 and round-3 decisions

Views: hero, exploded, detail; cards regenerated; image_qc passes and `render.py --check` has no FAIL.
