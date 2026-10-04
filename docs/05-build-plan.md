---
doc_id: DLT-BLD-001
title: DoliTrail prototype build plan
project: DoliTrail
doc_type: Build plan
version: "0.2"
status: Draft
date: '2026-10-03'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-03'
  author: Amish Chadha
  change: First build plan; design made constructable (DLT-DDR-002)
- version: "0.2"
  date: '2026-10-03'
  author: Amish Chadha
  change: "Round 2 requirement decisions carried in (DLT-DDR-003): wheel proof load before any person is carried, hold-back strap and wet clay rule, two bags, four bearers at steps with lift handles"
---

# DoliTrail prototype build plan

**Plan, not yet built.** How to make the first DoliTrail kit and fit it to a doli, component by component. Building and testing to it is TRL 4 work. Decisions are kept in the design decisions register (`docs/06-design-decisions.md`), not here.

> **Safety:** DoliTrail will carry a person over steep, wet ground. It is an open engineering reference, not certified medical or rescue equipment. The first kit carries sandbags, never a patient, until the proof loads and the wet ramp test in sections 5 and 6 have passed. Welding, grinding and cutting need eye, hand and hearing protection and a clear, ventilated space.

## 1. What you are building

![Every component, pulled apart and numbered in build order](05-build-plan/overview.png)

*Figure 1. The kit in build order. One harness is shown laid flat.*

The kit turns a family's bamboo doli into a wheeled stretcher with a brake. A welded steel fork unit holds a 20 inch wheel; four side arms slide into its two cross stubs and end in rubber-lined V saddles that the bamboo poles sit in, each closed by an upper jaw and two T-handle bolts. A disc brake on the wheel is worked from a lever strapped to the front right pole. A cross strap keeps the bed off the tyre, three patient straps hold the patient, and two harnesses take the pole ends in slings at each bearer's knuckle height. Two webbing lift handles on the cross stubs let two helpers lift at steps, and a hold-back strap ties the rear pole ends to the rear bearer's hip belt on wet descents. Eight components are made (the fork unit, side arms, upper jaws, liners, lever mount, harnesses, lift handles and hold-back strap) by cutting, bending, drilling, welding, gluing and sewing; the rest are bought bicycle parts, fasteners and webbing. The kit travels in two bags, one per bearer. Parts cost about USD 482. The sizes are for the reference doli: two 60 mm bamboo poles at 550 mm centres; the kit adjusts to poles of 40 to 80 mm at 450 to 600 mm centres.

## 2. What changed to make it buildable

*Table 1. Changes from the concept.*

| Component | The concept had | The buildable design has | Why |
| --- | --- | --- | --- |
| Wheel and fork | "A single wheel in a fork under the middle" | A welded fork unit with two cross stubs fore and aft of the wheel, four struts and dropout plates | The stubs pass below the bed and clear of the wheel; the struts form a stiff truss |
| Pole clamps | "Adjustable clamps with rubber jaws" | Four side arms that slide in the stubs, each with a rubber-lined V saddle, an upper jaw and two T-handle bolts | Fits poles of 40 to 80 mm at 450 to 600 mm centres, by hand |
| Cross frame and strap | One frame and a strap | The fork unit and arms are the frame; the strap is a webbing loop round both poles above the wheel | Keeps the bed 174 mm above the tyre |
| Brake | "Cable or rod brake" | Disc brake with the caliper on a lobe of the left dropout plate | Works wet; the mount is part of the welded plate |
| Lever | "At the front bearer's hand" | A rubber-lined lever mount strapped on the front right pole | A bicycle lever needs a 22.2 mm bar |
| Harness | "Pole-end cups" | Pole loops on adjustable slings | Fits every pole end and bearer |
| Wheel fixing | Not stated | Solid axle and nuts in slots open downward | Nothing to open by mistake |
| Bed | Not considered | Clamps on bare pole; the bed's lashing is slid aside at the four clamp points | The inboard bolt passes beside the pole |
| Steps | Two bearers lift | Four bearers at steps over about 250 mm, the two helpers lifting at webbing handles on the cross stubs | Two bearers would each lift about 71 kg to chest height; four lift about 36 kg each (DLT-DDR-003) |
| Wet descents | Brake and tyre only | A hold-back strap from the rear bearer's hip belt to the rear pole ends; on wet clay steeper than 20 per cent the doli is lifted and carried | On wet clay the tyre grips about 7 kg-force short of holding the rated load on a 30 per cent grade (DLT-DDR-003) |
| Carrying the kit | One bag | Two bags, one per bearer, about 6.9 kg and 8.7 kg | Each load under 10 kg (DLT-DDR-003) |

![Cut across the doli through the front clamps](../media/cutaway.png)

*Figure 2. Cut across the doli through the front clamps: the poles sit in the saddles, the wheel runs between the stubs.*

## 3. Making the components

Make and paint the steel parts in the workshop, glue in the liners and sew the harnesses before the kit goes anywhere near a doli.

### 3.1 Fork unit

![Making sketch: fork unit](../cad/drawings/DLT-DWG-101.png)

**What it is and what it is made from.** The backbone of the kit: two cross stubs of 30 x 30 x 2 mm square steel tube, 320 mm long, joined by four struts of 22.2 x 1.6 mm round tube to two 5 mm steel dropout plates that hold the wheel axle. The left plate has a lobe that carries the brake caliper. Mild steel tube and plate, welded and painted.

**How to make it.**

1. Cut the two stubs 320 mm long, square ends. Drill a 9 mm hole in the top face of each, 135 mm either side of the centre, and weld an M8 nut over each hole.
2. Cut the two dropout plates from 5 mm plate to the outline on the sketch: a slot 10 mm wide running up from the bottom edge, with the axle centre at its top. Add the caliper lobe to the left plate and drill it for the caliper adapter.
3. Set the stubs in a jig, parallel, 600 mm apart centre to centre and level. Set the plates on a 3/8 inch spacer bar with a 100 mm spacer between them, the axle centre 233 mm below the stub undersides and midway between the stubs.
4. Cut the four struts about 380 mm long and mitre both ends so they sit flat on the stub underside and on the outer face of the plate, with their centre lines 64 mm either side of the middle.
5. Tack, check the dropouts are square to the stubs and 100 mm apart, then weld fully. Grind the slot clean, prime and paint.

**How it fits the parts next to it.**

![Close-up: side arm in the cross stub](05-build-plan/joint-02.png)

*Figure 3. A side arm's spigot in a cross stub, cut. The set screw locks it.*

The side arms' spigots slide into the stub ends with about 0.5 mm clearance each side; a T-handle set screw through each welded nut presses down on the spigot. The wheel axle drops up into the slots (Figure 5), and the caliper bolts to the inside of the lobe (Figure 6).

**Check before moving on.** A 3/8 inch rod slides through both slots square to the stubs; a stub offcut of the arm tube slides in each stub end by hand without rocking; no weld spatter in the stub bores.

### 3.2 Side arms

![Making sketch: side arm](../cad/drawings/DLT-DWG-102.png)

**What it is and what it is made from.** Four L-shaped arms of 25 x 25 x 1.6 mm square tube. Each has a 230 mm spigot that slides into a stub, a 145 mm post welded on top at its outer end, and a 60 x 130 x 4 mm saddle plate on the post carrying a 90 deg V of 3 mm plate, 60 mm wide inside. Two M8 nuts are welded under the plate ears.

**How to make it.**

1. Cut four spigots 230 mm and four posts 145 mm from the square tube.
2. Weld each post on top of its spigot, flush with the outer end, square in both directions (use the same jig for all four).
3. Cut the saddle plates 60 x 130 mm; drill two 9 mm holes 52 mm either side of the centre line; weld M8 nuts underneath.
4. Bend 3 mm plate 60 mm wide into a 90 deg V with 30 mm legs, and weld it along the plate centre line, the V running along the pole.
5. Weld the plate on top of the post, the V centred over it and running square across the spigot, so the pole lies along the doli. Grind, prime and paint.

**How it fits the parts next to it.**

![Close-up: the pole clamp, cut across](05-build-plan/joint-01.png)

*Figure 4. A pole clamp, cut across: the pole in the rubber-lined V, the upper jaw over it, two T-bolts into the nuts under the saddle.*

The bamboo pole lies in the V on its rubber liner; the upper jaw closes over it and the two T-handle bolts pass through the jaw's ears into the nuts under the saddle plate.

**Check before moving on.** Every arm slides into every stub end; the V is square to the spigot; a 60 mm pipe sits in the V touching both faces.

### 3.3 Upper jaws

![Making sketch: upper jaw](../cad/drawings/DLT-DWG-103.png)

**What it is and what it is made from.** Four strips of 3 x 40 mm steel, 190 mm long, bent into an inverted 90 deg V with two flat ears, 130 mm over the ears.

**How to make it.**

1. Cut the strips 190 mm long.
2. Bend at the centre to 90 deg over a former in a vice; then bend each leg flat to make the ears, so both ears lie level.
3. Drill 9 mm holes in the ears at 104 mm centres. Deburr and paint.

**How it fits the parts next to it.** The jaw sits over the pole on its own liner; its ears take the T-handle bolts (Figure 4). On a 40 mm pole the ears come down to about 28 mm above the saddle ears; on an 80 mm pole they rise about 28 mm.

**Check before moving on.** The jaw's holes line up with the saddle nuts when it sits over a 60 mm pipe in the saddle.

### 3.4 Jaw liners

![Making sketch: jaw liners](../cad/drawings/DLT-DWG-104.png)

**What it is and what it is made from.** Eight pads of 5 mm rubber sheet, or three layers of truck inner tube glued together: 56 x 84 mm for the saddles and 38 x 94 mm for the jaws.

**How to make it.**

1. Cut the pads with a sharp knife against a straightedge.
2. Fold each along its centre line.
3. Coat the pad and the inside of the V with contact adhesive, wait ten minutes, press in and roll flat.

**How it fits the parts next to it.** The liner covers both faces of the V and stops short of the bolt holes. The pole bears only on rubber.

**Check before moving on.** No loose edges; the pad cannot be peeled by hand.

### 3.5 T-handle bolts and set screws (bought)

Buy eight M8 x 130 mm T-handle bolts with 25 mm washers for the clamps, and four M8 x 40 mm T-handle set screws for the arms, zinc plated. Run each into its welded nut once to clean the thread.

### 3.6 Wheel (bought)

Buy a 20 inch (ISO 406) cargo or tricycle wheel with a double-wall rim, 36 spokes of 2.0 mm or heavier and a steel front disc hub 100 mm over the locknuts, with a solid 3/8 inch axle and nuts (not quick release). Fit a 20 x 2.125 knobbly tyre and tube. Bolt the 203 mm rotor to the hub on the left side. Check the seller's ratings against the design decisions register. No light wheel or tyre is catalogue-rated for twice the 142 kg wheel load, so this wheel and tyre are proved by a 285 kg static proof load (section 5) before any person is carried. If the proof load fails, the wheel is replaced by a heavier 20 inch tricycle wheel with 13 gauge spokes and a 20 x 2.4 cargo tyre, and the proof load is repeated on the new wheel.

![Close-up: wheel axle in the dropouts, cut](05-build-plan/joint-03.png)

*Figure 5. The axle in the dropout slots, cut: nuts outside the plates.*

### 3.7 Disc brake set (bought)

Buy a cable-operated disc caliper with sintered pads and a post-mount adapter, a 203 mm six-bolt rotor, a brake lever for a 22.2 mm bar with a parking lock, and 2.2 m of cable and housing. Fit the adapter to the caliper lobe of the left dropout plate.

![Close-up: brake caliper on the lobe](05-build-plan/joint-04.png)

*Figure 6. The caliper bolted to the lobe, the rotor running in its slot.*

### 3.8 Lever mount

![Making sketch: lever mount](../cad/drawings/DLT-DWG-105.png)

**What it is and what it is made from.** A 110 mm stub of 22.2 x 1.6 mm tube, welded along the apex of an 80 mm long inverted V of 3 mm plate, with a 5 mm rubber liner inside the V and two 25 mm webbing cam straps.

**How to make it.**

1. Bend 3 mm plate 80 mm wide into a 90 deg V, 68 mm across the open side.
2. Weld the tube stub along the outside of the apex, centred, ends square. Paint.
3. Glue a rubber liner inside the V.
4. Sew two 25 mm webbing straps with cam buckles to pass round the pole, 28 mm either side of the centre.

**How it fits the parts next to it.**

![Close-up: lever mount on the front right pole](05-build-plan/joint-05.png)

*Figure 7. The lever mount on top of the front right pole, strapped round it; the brake lever clamps on the bar beyond the V.*

**Check before moving on.** On a 60 mm pipe, strapped tight, the mount does not turn when the lever is pulled hard.

### 3.9 Cross strap and patient straps (bought)

Buy 50 mm polyester webbing: one cross strap of 1.6 m with a cam buckle, and three patient straps of 1.8 m with cam buckles and a red pull tab. Heat-seal every cut end.

![Close-up: cross strap round both poles](05-build-plan/joint-06.png)

*Figure 8. The cross strap round both poles above the wheel, under the bed.*

![Close-up: patient strap and quick-release buckle](05-build-plan/joint-08.png)

*Figure 9. A patient strap round both poles; one pull on the tab frees it.*

### 3.10 Bearer harnesses

![Making sketch: bearer harness](../cad/drawings/DLT-DWG-106.png)

**What it is and what it is made from.** Two harnesses sewn by a tailor from 50 mm polyester webbing: a 1,000 mm hip belt with a foam pad, two padded shoulder straps joined by a chest strap, and two slings, each ending in a pole loop about 110 mm across, with cam buckles to set the length.

**How to make it.**

1. Cut and heat-seal the webbing: belt 1,000 mm, shoulder straps 600 mm, chest strap 300 mm, slings 500 mm, loops 400 mm. Sew a steel D-ring to the back of the rear bearer's hip belt for the hold-back strap.
2. Sew the shoulder straps to the belt at the back, 180 mm apart, crossing to the front; add the pads and the chest strap.
3. Sew a sling to each side of the belt, 660 mm apart; fit a cam buckle in each sling.
4. Fold each loop and box-and-cross stitch it to its sling with UV-resistant thread.

**How it fits the parts next to it.**

![Close-up: harness pole loop on a pole end](05-build-plan/joint-07.png)

*Figure 10. A harness pole loop on a pole end; the sling runs up to the bearer's yoke.*

**Check before moving on.** Hang 50 kg from each loop for one minute: no stitch pulls.

### 3.11 Lift handles and hold-back strap

**What they are and what they are made from.** Sewn by the same tailor from 25 mm polyester webbing. Two lift handles, each about 400 mm of webbing wrapped round a cross stub and bar-tacked into a loop that hangs about 140 mm below it: one on the front stub left of centre, one on the rear stub right of centre, so the two helpers stand on opposite sides. One hold-back strap: two loops that slip onto the rear pole ends, joined to a single tail about 600 mm long with a cam buckle and a steel snap hook.

**How to make them.**

1. Lift handles: wrap the webbing twice round a 30 mm square bar, then bar-tack the loop closed below it with UV-resistant thread; heat-seal the ends.
2. Hold-back strap: sew two pole loops about 200 mm round, join their tails in a Y, and sew the cam buckle and snap hook to the single tail.

**How they fit the parts next to them.** Each handle wraps the stub between the strut and the set screw, clear of the wheel by about 80 mm (Figure 11). The hold-back loops ride on the rear pole ends, outboard of the harness pole loops (Figure 12); the snap hook clips to the D-ring on the rear bearer's hip belt and the cam buckle sets the length so the strap is taut with the bearer standing upright.

![Close-up: lift handle on the front cross stub](05-build-plan/joint-09.png)

*Figure 11. A lift handle wrapped round the front cross stub.*

![Close-up: hold-back strap loops on the rear pole ends](05-build-plan/joint-10.png)

*Figure 12. The hold-back strap loops on the rear pole ends, outboard of the harness pole loops.*

**Check before moving on.** Hang 75 kg from each lift handle and 80 kg from the hold-back strap's snap hook for one minute each: no stitch pulls.

### 3.12 Carry bags, fitting card, ties and pump (bought)

Two canvas bags with shoulder straps, one per bearer: the wheel bag, about 700 x 340 x 560 mm, takes the fork unit with the wheel and brake fitted and the pump (about 6.9 kg packed), and the parts bag, about 500 x 300 x 250 mm, takes the arms, jaws, bolts, lever mount, straps, harnesses, lift handles and hold-back strap (about 8.7 kg packed); an A4 laminated fitting card with the pictures of section 4 and the safety stops; eight hook-and-loop ties; a mini pump, tyre levers, patches and a spare tube.

## 4. Putting it together

Steps 1 to 4 are done once in the workshop; the wheel then stays in the fork unit. Steps 5 to 9 are the fitting to a doli, about five minutes for two people.

### Step 1: fit the rotor and the wheel

![Step 1](05-build-plan/step-01.png)

Bolt the rotor to the hub (left side) to the torque on its packet. Lift the axle up into both slots and tighten the nuts outside the plates with a spanner. Spin the wheel: it runs true and clear of the struts.

### Step 2: bolt the caliper to the lobe

![Step 2](05-build-plan/step-02.png)

Bolt the caliper and adapter to the lobe, centre it on the rotor, set the pads about 0.5 mm off, and run the cable through the housing to the lever (the lever stays loose for now).

### Step 3: slide the side arms into the stubs

![Step 3](05-build-plan/step-03.png)

Slide each arm into its stub end, posts upward and outward. Set the saddles to the doli's pole spacing (measure centre to centre).

### Step 4: lock the set screws

![Step 4](05-build-plan/step-04.png)

Tighten the four set screws by hand. Each spigot must be at least 75 mm inside its stub.

### Step 5: set the frame under the poles, wheel under the hips

![Step 5](05-build-plan/step-05.png)

Two people raise the doli on their knees or on two blocks. Slide the frame under it so the wheel sits under the patient's hips (the belt line), and the saddles sit under both poles at bare pole, sliding any bed lashing about 70 mm aside.

### Step 6: close the four clamps

![Step 6](05-build-plan/step-06.png)

Lay each upper jaw over its pole; run both T-bolts into the nuts in even turns until the rubber just bulges. Hand tight only, never with a bar.

### Step 7: fit the cross strap

![Step 7](05-build-plan/step-07.png)

Pass the strap round both poles just ahead of the wheel's top, under the bed, and pull it tight.

### Step 8: fit the lever mount and the lift handles

![Step 8](05-build-plan/step-08.png)

Wrap a lift handle round each cross stub between the strut and the set screw (front stub left of centre, rear stub right of centre) if they are not left on the frame. Strap the lever mount on top of the front right pole about 150 mm behind where the front bearer's pole loop will sit. Clamp the lever on its bar, blade toward the bearer's hand. Tie the housing along the arm and the pole with the hook-and-loop ties, with no tight bends. Pull the lever: the wheel locks; set the parking lock: it stays locked.

### Step 9: patient straps, harness loops and hold-back strap

![Step 9](05-build-plan/step-09.png)

Pass the three patient straps round both poles at the chest, hips and legs. The bearers put on their harnesses, set the slings to knuckle height and slip the pole loops over the pole ends. Slip the hold-back loops over the rear pole ends, outboard of the harness loops, and clip the snap hook to the rear bearer's hip belt before any descent.

## 5. First checks

These are listed here and recorded in a TRL 4 test report. Sandbags stand in for a patient.

*Table 2. First checks.*

| Check | Requirement | How | Pass when |
| --- | --- | --- | --- |
| Clamp range | R1 | Close a clamp on 40, 60 and 80 mm bamboo | Both liners touch; jaw clear of the saddle |
| Clamp slip | R1 | Pull the fitted frame along the poles with CalRig | No slip at 1.5 kN on wet poles |
| Proof load | R3 | 260 kg of sandbags on the fitted doli, wheel on a block, 10 min | No permanent set in the frame, no weld cracks, no clamp movement |
| Wheel proof load | R3 | 285 kg static load on the bought wheel and tyre alone, 10 min, before any person is carried | No spoke, rim or tyre damage; if it fails, fit the heavier tricycle wheel and cargo tyre and repeat |
| Fitting time | R2 | Two people with only the fitting card | Under 5 min |
| Bearer load | R4 | Load cells in the slings, level trail | Average load per bearer down by 60 per cent or more |
| Brake hold | R5 | Rated sandbag load on a wet 30 per cent ramp, lever locked | Stays put for 5 min |
| Hold-back on wet clay | R5 | Rated sandbag load on a wet clay slope, lever locked, the rear bearer on the hold-back strap | The bearer holds the doli still; force on the strap recorded |
| Width | R6 | Measure over the clamps | 700 mm or less on the reference doli |
| Mass | R7 | Weigh each of the two packed bags | Each 10 kg or less |
| Step | R8 | 400 mm step with sandbags, four bearers: two at the pole ends, two helpers at the lift handles | Wheel clears the step; the lift per person recorded |
| Release | R10 | Pull each tab, gloved hand | Free in 3 s |
| Brake reach | R11 | Bearers of 1.5 to 1.8 m | Lever and lock worked without letting go |

## 6. Safety stops

Work stops at each point until what is listed is true.

- **S1, before welding:** jig checked square; fire extinguisher and screens in place.
- **S2, before any load:** every weld inspected by eye for cracks and full fusion; every set screw and T-bolt tight; wheel nuts tight.
- **S3, before the proof load:** sandbags only; people stand clear of the doli's sides; the wheel rests on a block.
- **S4, before the wet ramp test:** the proof loads (section 5), including the 285 kg static proof load of the wheel and tyre, have passed; a person holds a safety rope to the rear poles; the ramp has a run-out clear of people.
- **S5, before any trail trial with a person:** the 285 kg static proof load of the wheel and tyre and the ramp test have passed, the bearers have practised with sandbags, including the hold-back strap and a four-bearer lift at a step, and the partner's crew agree. No person is carried on a wheel or tyre that has not passed its proof load. The first person carried is a healthy volunteer, not a patient. Bearers keep both hands on the poles and never roll through moving water. On every descent the rear bearer's hold-back strap is clipped to the hip belt; on wet clay or mud steeper than 20 per cent the doli is lifted and carried, not rolled. At any step over about 250 mm four bearers lift, two at the pole ends and two helpers at the lift handles; two bearers never lift the doli over such a step.
- **S6, every fitting:** lift handles and hold-back strap checked for cuts and pulled stitches; clamps checked by shaking the doli; poles checked for splits at the clamp points; brake pulled and the lock tried before anyone is strapped on.

## 7. Tools, skills and workspace

- Workshop: a welder (stick or MIG) and a competent welder; angle grinder with cutting and grinding discs; drill press or hand drill with 9 mm bit; bench vice and a 90 deg bending former; files; a flat bench for the jig.
- Tailor: a heavy sewing machine for webbing and bar-tacks, UV-resistant thread, a hot knife for sealing.
- Bicycle mechanic: spoke key, 15 mm spanner, Torx or hex keys for the rotor and caliper, cable cutters.
- Fitting: no tools beyond the kit; the T-handles are turned by hand.
- Space: a covered workshop for the steel; a level yard and a test ramp for the checks.

## 8. Where the numbers come from

- Model: `cad/src/model.py` (sizes, constructability checks), `cad/step/` and `cad/stl/`.
- Drawings: `cad/drawings/DLT-DWG-001` (general arrangement) and `DLT-DWG-101` to `106` (making sketches).
- Calculations: `docs/04-calcs/01-sizing.md` (DLT-CAL-001), `docs/04-calcs/sizing.py`, `docs/04-calcs/results.csv`.
- Bill of materials: `bom/bom.csv`.
- Pictures: `cad/src/build_plan_media.py`.
