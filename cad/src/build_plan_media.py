"""DoliTrail prototype build plan pictures (DLT-BLD-001, STANDARDS section 18).

Run from the repo root:  python cad/src/build_plan_media.py [overview|sheets|joints|steps ...]
With no argument it draws everything. Every picture is drawn from cad/src/model.py, so the
pictures and the model never disagree:
    docs/05-build-plan/overview.png    every component pulled apart, numbered in build order
    cad/drawings/DLT-DWG-101 to 108    making sketches for the made components
    docs/05-build-plan/joint-NN.png    close-ups of the joints that need explaining
    docs/05-build-plan/step-NN.png     one picture per assembly step
The clamp pictures show the front right clamp; the other three are the same.
Uses .kit/build_views.py. BUILD PLAN ILLUSTRATION, PLAN NOT YET BUILT.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / ".kit"), str(ROOT / "cad" / "src")]
import build_views as bv  # noqa: E402
from build_views import Part  # noqa: E402
from build123d import Box, Compound, Pos, Rot  # noqa: E402
import model as M  # noqa: E402

P = M.PARAMS
D = M.derived(P)
OUT = ROOT / "docs" / "05-build-plan"
DATE = "2026-10-03"
K = M.build_kit(P)
C = M.doli_context(P)
W = dict(K["wheel"])
B = dict(K["brake"])
MT = dict(K["mount"])
COL = {"fork": "#0F766E", "arm": "#155E75", "jaw": "#0E7490", "liner": "#1F2937", "bolt": "#6B7280",
       "tyre": "#27272A", "brake": "#B91C1C", "mount": "#155E75", "cross": "#EA580C", "patient": "#DC2626",
       "harness": "#D97706", "pole": "#C8A96A", "bag": "#78716C", "holdback": "#7C3AED", "handle": "#CA8A04"}
XS, YP = P["stub_x"], -P["pole_y"]


def pick(key, *tok):
    return Compound([s for n, s in K[key] if all(t in n.split() for t in tok)])


def allk(key):
    return Compound([s for _, s in K[key]])


def box(x0, x1, y0, y1, z0, z1):
    return Pos((x0 + x1) / 2, (y0 + y1) / 2, (z0 + z1) / 2) * Box(x1 - x0, y1 - y0, z1 - z0)


def poles(x0=-650.0, x1=650.0):
    return Compound(C["poles"]) & box(x0, x1, -500, 500, 0, 1000)


WHEEL = Compound([W["tyre"], W["rim"], W["hub"], W["axle and nuts"], W["spokes"]])
FORK = K["fork"][0][1]
HANDLES = allk("handles")
FORKH = Compound([FORK, HANDLES])          # the lift handles stay sewn on the fork unit
HB = dict(K["holdback"])
HOLDBACK = allk("holdback")


def parts_bag(origin=(0, 0, 0)):
    """Second carry bag (decision 8A): a canvas backpack, drawn as an open box."""
    ox, oy, oz = origin
    return Pos(ox, oy, oz + 225) * Box(330, 220, 450) - Pos(ox, oy, oz + 235) * Box(310, 200, 450)


def components():
    harness = M.harness_flat(P)
    return [
        Part("Fork unit, welded", FORK, COL["fork"], 1, (0, 0, -150)),
        Part("Side arms (4)", allk("arms"), COL["arm"], 2, (0, 0, 300)),
        Part("Upper jaws (4)", allk("jaws"), COL["jaw"], 3, (0, 0, 800)),
        Part("Jaw liners (8), rubber", allk("liners"), COL["liner"], 4, (0, 0, 550)),
        Part("T-handle bolts (8) and set screws (4)", Compound([s for n, s in K["bolts"] if n.startswith("bolt")]
                                                               + [s for n, s in K["bolts"] if n.startswith("set")]),
             COL["bolt"], 5, (0, 0, 1050)),
        Part("Wheel (bought)", WHEEL, COL["tyre"], 6, (0, 0, -600)),
        Part("Disc brake set (bought)", Compound([B["rotor"], B["caliper"], B["lever"]]), COL["brake"], 7, (0, -500, -500)),
        Part("Lever mount", allk("mount"), COL["mount"], 8, (-200, -900, 400)),
        Part("Cross strap", allk("cross"), COL["cross"], 9, (0, 0, 1350)),
        Part("Patient straps (3)", allk("patient"), COL["patient"], 10, (0, 0, 1750)),
        Part("Bearer harnesses (2), one shown flat", Pos(1500, -1900, 0) * harness, COL["harness"], 11, (0, 0, 0)),
        Part("Hold-back strap", HOLDBACK, COL["holdback"], 12, (-250, 0, 0)),
        Part("Lift handles (2), sewn on the stubs", HANDLES, COL["handle"], 13, (0, 0, -380)),
        Part("Wheel bag, parts bag, card, ties, pump (bought)",
             Compound([Pos(2300, 1600, 0) * M.bag(P), parts_bag((2300, 2150, 0))]), COL["bag"], 14, (0, 0, 0)),
    ]


def overview():
    bv.overview(components(), OUT / "overview.png", "DoliTrail: the kit, in build order",
                subtitle="Every component pulled apart and numbered in build order; harness shown laid flat. Plan, not yet built",
                elev=26, azim=-50, size=(11, 7.5), key=True)


def sheets():
    nb_frame = [Part("Frame", Compound([FORK, allk("arms"), allk("jaws")]), "#D1D5DB"),
                Part("Poles", poles(), "#D1D5DB"), Part("Wheel", Compound([W["tyre"], W["rim"]]), "#D1D5DB")]
    bv.component_sheet(Part("Fork unit", FORK, COL["fork"]), nb_frame[1:], "DoliTrail", "DLT-DWG-101",
                       "Fork unit (welded)", "Steel tube 30 x 30 x 2 SHS, 22.2 x 1.6 round, 5 mm plate",
                       [f"Two cross stubs, 30 x 30 x 2 square tube, {P['stub_len']:.0f} long,",
                        f"  {2 * XS:.0f} apart centre to centre, tops level.",
                        "Four struts 22.2 x 1.6 tube, about 380 long, ends mitred",
                        "  to sit on the stub undersides 64 either side of centre.",
                        "Dropout plates 5 mm, inner faces 100 apart; 10 slot",
                        "  open downward, axle centre 233 below the stub undersides.",
                        "Left plate carries the caliper lobe (post-mount holes).",
                        "Drill 9 in each stub top 135 from centre; weld M8 nuts over.",
                        "Weld in a jig with a 100 mm spacer bar in the dropouts."],
                       DATE, inset_view=(24, -58))
    arm = pick("arms", "front", "right")
    bv.component_sheet(Part("Side arm", arm, COL["arm"]), nb_frame[:2], "DoliTrail", "DLT-DWG-102",
                       "Side arm (4)", "25 x 25 x 1.6 SHS, 4 mm plate, 3 mm plate V",
                       [f"Spigot 25 x 25 x 1.6 square tube, {P['spigot_len']:.0f} long.",
                        f"Post of the same tube, {D['post_len']:.0f} long, welded on top",
                        "  of the spigot, flush with its outer end.",
                        "Saddle plate 60 x 130 x 4 on the post top, centred.",
                        "V of 3 mm plate bent to 90 deg, 60 wide inside at the top,",
                        "  welded along the plate centre line.",
                        "Drill 9 at 52 either side of the V; weld M8 nuts underneath.",
                        "Check: spigot slides into a stub offcut by hand, no rock."],
                       DATE, inset_view=(24, -58))
    jaw = pick("jaws", "front", "right")
    bv.component_sheet(Part("Upper jaw", jaw, COL["jaw"]), [Part("Pole", poles(), "#D1D5DB"), Part("Arm", arm, "#D1D5DB")],
                       "DoliTrail", "DLT-DWG-103", "Upper jaw (4)", "3 x 40 mm steel strip",
                       ["Cut 3 x 40 strip 190 long.",
                        "Bend to an inverted 90 deg V at the centre,",
                        "  then bend both ears flat, 130 over the ears.",
                        "Drill 9 holes at 104 centres in the ears.",
                        "Deburr; paint; glue a liner inside the V.",
                        "Fits over the pole; the T-bolts pass the ears",
                        "  into the nuts under the saddle."],
                       DATE, inset_view=(24, -58))
    lin = Compound([s for n, s in K["liners"] if "front" in n.split() and "right" in n.split()])
    bv.component_sheet(Part("Jaw liners", lin, COL["liner"]), [Part("Arm", arm, "#D1D5DB"), Part("Jaw", jaw, "#D1D5DB")],
                       "DoliTrail", "DLT-DWG-104", "Jaw liners (8)", "5 mm rubber sheet or truck inner tube",
                       ["Saddle liner: 56 x 84 rubber, 5 thick; jaw liner 38 x 94.",
                        "Inner tube: three layers glued into one 5 mm pad.",
                        "Fold along the centre line into the V.",
                        "Glue in with contact adhesive, both faces, 10 min.",
                        "Liners must not reach the bolt holes.",
                        "Replace when worn through or loose."],
                       DATE, inset_view=(30, -58))
    mount = MT["lever mount"]
    bv.component_sheet(Part("Lever mount", Compound([mount, MT["mount liner"]]), COL["mount"]),
                       [Part("Pole", Compound(C["poles"]) & box(1000, 1400, -500, 0, 600, 900), "#D1D5DB")],
                       "DoliTrail", "DLT-DWG-105", "Lever mount", "22.2 x 1.6 tube, 3 mm plate, 5 mm rubber",
                       ["Inverted V of 3 mm plate, 80 long, 90 deg, 68 across.",
                        "Bar stub 22.2 x 1.6 tube, 110 long, welded along",
                        "  the apex of the V, ends square.",
                        "Glue a 5 mm rubber liner inside the V.",
                        "Two 25 webbing straps with cam buckles,",
                        "  sewn loops 28 either side of centre.",
                        "Sits on top of the front right pole; the brake",
                        "  lever clamps on the bar beyond the V."],
                       DATE, inset_view=(24, -58))
    h = M.harness_flat(P)
    bv.component_sheet(Part("Bearer harness", h, COL["harness"]), [], "DoliTrail", "DLT-DWG-106",
                       "Bearer harness (2), laid flat", "50 mm polyester webbing, 25 mm foam, cam buckles",
                       ["Hip belt 1,000 long, 25 foam pad 320 x 90 at the back.",
                        "Two shoulder straps 600 long with 80 x 200 pads,",
                        "  crossed by a 300 chest strap.",
                        "Two slings, 500 long, from the belt sides at 660",
                        "  apart, each with a cam buckle to set the length.",
                        "Each sling ends in a pole loop 110 across,",
                        "  box-and-cross stitched, sewn with UV thread.",
                        "Set: pole loops at the bearer's knuckle height."],
                       DATE, inset_view=(60, -90))
    pe = Part("Rear pole ends", Compound(C["poles"]) & box(-1200, -900, -500, 500, 600, 900), "#D1D5DB")
    bv.component_sheet(Part("Hold-back strap", HOLDBACK, COL["holdback"]), [pe], "DoliTrail", "DLT-DWG-107",
                       "Hold-back strap", "50 and 25 mm polyester webbing, 40 mm steel ring, cam buckle",
                       ["Two end caps: 50 webbing sewn into closed sleeves",
                        f"  {P['cap_len']:.0f} deep, a 25 cam strap round each mouth",
                        "  to cinch it on poles of 40 to 80.",
                        "Two legs of 25 webbing, about 420 long, from the",
                        "  cap ends to one 40 steel ring.",
                        f"Tail of 25 webbing, {P['hb_tail']:.0f} long, ring to a cam buckle",
                        "  that clips to the rear bearer's hip belt.",
                        "Box-and-cross stitch every joint, UV thread.",
                        "Check: hang 100 kg from the ring for 1 min."],
                       DATE, inset_view=(24, -58))
    h1 = pick("handles", "front")
    bv.component_sheet(Part("Lift handle", h1, COL["handle"]), [Part("Fork unit", FORK, "#D1D5DB")], "DoliTrail", "DLT-DWG-108",
                       "Lift handle (2)", "50 mm polyester webbing, 25 mm foam tube",
                       [f"Band of 50 webbing round a cross stub, {P['handle_w']:.0f} wide,",
                        "  sewn shut by hand round the painted stub.",
                        f"Hand loop hangs {P['handle_drop']:.0f} below the stub, 70 across.",
                        "Foam grip sleeve 60 long on the bottom of the loop.",
                        f"Front stub: {P['handle_y']:.0f} left of centre; rear stub:",
                        f"  {P['handle_y']:.0f} right of centre (helpers on opposite sides).",
                        "Sits between the strut and the set screw nut.",
                        "Check: hang 70 kg from the loop for 1 min."],
                       DATE, inset_view=(24, -58))


def joints():
    win = box(XS - 60, XS + 60, YP - 100, YP + 100, 600, 800)
    # 1 the pole clamp, cut across through the clamp
    pole = Compound(C["poles"]) & box(XS - 120, XS + 120, YP - 60, YP + 60, 600, 800)
    bv.joint([Part("Pole", pole, COL["pole"]), Part("Saddle (side arm)", pick("arms", "front", "right") & box(XS - 60, XS + 60, YP - 80, YP + 80, 630, 720), COL["arm"]),
              Part("Liners", Compound([s for n, s in K["liners"] if "front" in n.split() and "right" in n.split()]), COL["liner"]),
              Part("Upper jaw", pick("jaws", "front", "right"), COL["jaw"]),
              Part("T-handle bolts", Compound([s for n, s in K["bolts"] if n.startswith("bolt front right")]), COL["bolt"])],
             OUT / "joint-01.png", "Joint 1: the pole clamp, cut across",
             "Pole in the rubber-lined V; jaw over the top; two T-bolts into the nuts under the saddle", cut="+X", elev=12, azim=-165)
    del win
    # 2 spigot in the stub with the set screw, cut along the stub
    w2 = box(XS - 40, XS + 40, -300, 0, 470, 560)
    bv.joint([Part("Cross stub (fork unit)", FORK & w2, COL["fork"]),
              Part("Side arm spigot", pick("arms", "front", "right") & box(XS - 40, XS + 40, -300, 0, 470, 560), COL["arm"]),
              Part("Set screw", pick("bolts", "set", "screw", "2"), COL["bolt"])],
             OUT / "joint-02.png", "Joint 2: side arm in the cross stub, cut",
             "The spigot slides in with 0.5 mm clearance; the set screw locks it at the pole spacing", cut="+X", elev=14, azim=-160)
    # 3 wheel axle in the dropouts, cut
    w3 = box(-80, 80, -90, 90, 180, 340)
    bv.joint([Part("Dropout plates (fork unit)", FORK & w3, COL["fork"]), Part("Hub and axle with nuts", Compound([W["hub"], W["axle and nuts"]]), COL["bolt"]),
              Part("Rotor", B["rotor"] & w3, COL["brake"])],
             OUT / "joint-03.png", "Joint 3: wheel axle in the dropouts, cut",
             "Solid 3/8 inch axle in slots open downward; nuts outside the plates, tightened by hand spanner", cut="+X", elev=14, azim=-160)
    # 4 caliper on the lobe
    w4 = box(-150, 40, -90, 0, 120, 340)
    bv.joint([Part("Left dropout plate and lobe", FORK & w4, COL["fork"]), Part("Rotor", B["rotor"] & w4, "#9CA3AF"),
              Part("Caliper", B["caliper"], COL["brake"])],
             OUT / "joint-04.png", "Joint 4: brake caliper on the dropout lobe",
             "Caliper bolted to the inside of the lobe with its adapter; rotor runs centred in the slot", elev=10, azim=-120)
    # 5 lever mount on the pole
    lx = P["lever_x"]
    bv.joint([Part("Pole", Compound(C["poles"]) & box(lx - 150, lx + 250, YP - 60, YP + 60, 600, 850), COL["pole"]),
              Part("Lever mount", MT["lever mount"], COL["mount"]), Part("Liner", MT["mount liner"], COL["liner"]),
              Part("Mount straps", MT["mount straps"], COL["cross"]), Part("Brake lever with lock", B["lever"], COL["brake"])],
             OUT / "joint-05.png", "Joint 5: lever mount on the front right pole",
             "Rubber-lined V on top of the pole, two cam straps; the lever clamps on the bar stub", elev=22, azim=-55)
    # 6 cross strap above the wheel
    bv.joint([Part("Poles", Compound(C["poles"]) & box(-150, 150, -400, 400, 600, 800), COL["pole"]),
              Part("Cross strap", allk("cross"), COL["cross"]), Part("Tyre", W["tyre"] & box(-200, 200, -50, 50, 350, 600), COL["tyre"])],
             OUT / "joint-06.png", "Joint 6: cross strap round both poles",
             "Under the bed, 174 mm above the tyre; it keeps the bed from sagging onto the wheel", elev=12, azim=-80)
    # 7 harness pole loop on a pole end
    lf = P["loop_x"][0]
    bv.joint([Part("Pole end", Compound(C["poles"]) & box(lf - 120, lf + 120, YP - 60, YP + 60, 600, 900), COL["pole"]),
              Part("Harness pole loop and sling", pick("harness", "loop", "2"), COL["harness"])],
             OUT / "joint-07.png", "Joint 7: harness pole loop on a pole end",
             "The loop rides on the pole 70 mm from its end; the sling runs up to the bearer's shoulder yoke", elev=18, azim=-55)
    # 8 patient strap buckle
    x2 = P["patient_straps_x"][1]
    bv.joint([Part("Poles", Compound(C["poles"]) & box(x2 - 120, x2 + 120, -400, 400, 600, 850), COL["pole"]),
              Part("Patient strap with cam buckle and pull tab", pick("patient", "strap", "2"), COL["patient"])],
             OUT / "joint-08.png", "Joint 8: patient strap and quick-release buckle",
             "Round both poles; one pull on the red tab frees it", elev=30, azim=-60)
    # 9 lift handle on the front cross stub
    hy = P["handle_y"]
    w9 = box(XS - 90, XS + 90, hy - 110, hy + 110, 330, 560)
    bv.joint([Part("Cross stub and strut (fork unit)", FORK & w9, COL["fork"]),
              Part("Lift handle", pick("handles", "front"), COL["handle"]),
              Part("Set screw", Compound([s for n, s in K["bolts"] if n.startswith("set")]) & w9, COL["bolt"])],
             OUT / "joint-09.png", "Joint 9: lift handle on the front cross stub",
             "Webbing sewn shut round the stub between the strut and the set screw; hand loop below", elev=16, azim=-60)
    # 10 hold-back strap cap on a rear pole end
    x0 = P["pole_x"][0]
    bv.joint([Part("Pole end", Compound(C["poles"]) & box(x0, x0 + 200, -P["pole_y"] - 60, -P["pole_y"] + 60, 600, 900), COL["pole"]),
              Part("Harness pole loop", pick("harness", "loop", "4"), COL["harness"]),
              Part("Hold-back end cap", HB["hold-back cap right"], COL["holdback"]),
              Part("Hold-back leg", HB["hold-back legs ring and tail"] & box(x0 - 200, x0, -400, 0, 600, 900), COL["holdback"])],
             OUT / "joint-10.png", "Joint 10: hold-back strap cap on a rear pole end",
             "The cap bears on the end of the pole; the leg runs back to the ring and the rear bearer's belt",
             elev=20, azim=-130)


def steps():
    pl = Part("Doli poles", poles(-700, 1450), COL["pole"])
    fork = Part("Fork unit with lift handles", FORKH, COL["fork"], None, (0, 0, 0))
    wheel = Part("Wheel with rotor", Compound([WHEEL, B["rotor"]]), COL["tyre"], None, (0, 0, -350))
    cal = Part("Caliper", B["caliper"], COL["brake"], None, (0, -200, 0))
    arms = Part("Side arms", allk("arms"), COL["arm"], None, (0, 0, 0))
    arms_l = Part("Side arms, left", pick("arms", "left"), COL["arm"], None, (0, 250, 0))
    arms_r = Part("Side arms, right", pick("arms", "right"), COL["arm"], None, (0, -250, 0))
    sets = Part("Set screws", Compound([s for n, s in K["bolts"] if n.startswith("set")]), COL["bolt"], None, (0, 0, 150))
    lin = Part("Liners", allk("liners"), COL["liner"], None, (0, 0, 0))
    jaws = Part("Upper jaws and T-bolts", Compound([allk("jaws")] + [s for n, s in K["bolts"] if n.startswith("bolt")]),
                COL["jaw"], None, (0, 0, 250))
    frame_up = Part("Frame and wheel", Compound([FORKH, allk("arms"), allk("liners"), WHEEL, B["rotor"], B["caliper"],
                                                 Compound([s for n, s in K["bolts"] if n.startswith("set")])]), COL["fork"], None, (0, 0, -300))
    cross = Part("Cross strap", allk("cross"), COL["cross"], None, (0, 0, 250))
    mnt = Part("Lever mount, lever and cable", Compound([allk("mount"), B["lever"], B["cable"]]), COL["mount"], None, (0, 0, 200))
    pat = Part("Patient straps", allk("patient"), COL["patient"], None, (0, 0, 250))
    har = Part("Harness pole loops", allk("harness"), COL["harness"], None, (0, 0, 250))
    hbk = Part("Hold-back strap", HOLDBACK, COL["holdback"], None, (-250, 0, 150))
    seq = [
        ([fork], [wheel], "Step 1: fit the rotor and the wheel", "Rotor on the hub, left side; axle up into the slots, nuts outside", [], -58),
        ([fork, wheel], [cal], "Step 2: bolt the caliper to the lobe", "Centre it on the rotor; set the pads 0.5 mm off", [], -58),
        ([fork, wheel, cal], [arms_l, arms_r], "Step 3: slide the side arms into the stubs", "Set the saddles to the doli's pole spacing", [], -58),
        ([fork, wheel, cal, arms], [sets], "Step 4: lock the set screws", "Hand tight with the T-handles", [], -58),
        ([], [frame_up], "Step 5: frame under the poles, wheel under the hips", "Doli raised on knees or blocks; saddles under both poles", [pl], -50),
        ([frame_up], [jaws], "Step 6: close the four clamps", "Jaws over the poles; T-bolts into the nuts, even turns, hand tight", [pl], -50),
        ([frame_up, jaws], [cross], "Step 7: fit the cross strap", "Round both poles above the wheel, under the bed; pull tight", [pl], -50),
        ([frame_up, jaws, cross], [mnt], "Step 8: lever mount on the front right pole", "Two cam straps; housing tied along the arm and pole", [pl], -50),
        ([frame_up, jaws, cross, mnt], [pat, har, hbk], "Step 9: patient straps, harness loops, hold-back strap",
         "Straps round both poles; pole loops on the pole ends; caps over the rear pole ends", [Part("Doli poles", poles(-1150, 1400), COL["pole"])], -50),
    ]
    for i, (done, new, title, sub, ctx, az) in enumerate(seq, 1):
        bv.step([Part(q.name, q.shape, q.color) for q in done], new, OUT / f"step-{i:02d}.png", title, sub, context=ctx,
                elev=24, azim=az, size=(8, 6), label_done=(i <= 4))


if __name__ == "__main__":
    what = sys.argv[1:] or ["overview", "sheets", "joints", "steps"]
    for w in what:
        globals()[w]()
        print("done", w)
