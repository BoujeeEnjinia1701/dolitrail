"""DoliTrail concept media (TRL 3, constructable design of DLT-DDR-002), generated from the model.

Run from the repo root:  python cad/src/concept_media.py [hero|cutaway|exploded|flow|web|blueprint ...]
With no argument it draws everything; on a small machine run one picture per process. Geometry
comes from cad/src/model.py and the figures from docs/04-calcs/results.csv (DLT-CAL-001):
media/hero.png (with a 1.75 m person), media/cutaway.png (cut across the doli through the front
clamps), media/exploded.png (numbers match bom/bom.csv), media/flow.png (load path, estimates),
media/concept-blueprint.png, .pdf and .svg (DLT-DWG-010), media/model.glb and media/viewer.html.
The doli (bamboo poles, cross sticks, cloth bed) is the family's own and is drawn as context.
CONCEPT, NOT FOR FABRICATION.
"""
import csv
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / ".kit"), str(ROOT / "cad" / "src")]
import concept as K  # noqa: E402
from concept import Part  # noqa: E402
from build123d import Box, Compound, Pos  # noqa: E402
import model as M  # noqa: E402

P = M.PARAMS
PROJECT = "DoliTrail"
TITLE = "Clamp-on braked wheel and harness kit for a bamboo stretcher"
MD = ROOT / "media"
COL = {"fork": "#0F766E", "arms": "#155E75", "jaws": "#0E7490", "liners": "#1F2937", "bolts": "#9CA3AF",
       "tyre": "#27272A", "rim": "#A1A1AA", "brake": "#B91C1C", "mount": "#155E75", "cross": "#EA580C",
       "patient": "#DC2626", "harness": "#D97706", "handles": "#7C3AED", "holdback": "#1D4ED8"}
BAMBOO, CLOTH = "#C8A96A", "#E7E5E4"


def R():
    rows = {r["tag"]: r for r in csv.DictReader((ROOT / "docs" / "04-calcs" / "results.csv").open())}
    return lambda t: float(rows[t]["value"])


def doli_parts(bed=True):
    c = M.doli_context(P)
    ps = [Part("Bamboo poles and cross sticks (the family's doli)", Compound(c["poles"] + c["sticks"]), BAMBOO, None)]
    if bed:
        ps.append(Part("Cloth bed (the family's doli)", c["bed"], CLOTH, None))
    return ps


def kit_parts(k=None, explode=False):
    k = k or M.build_kit(P)
    pick = lambda key, *tok: Compound([s for n, s in k[key] if all(t in n.split() for t in tok)])  # noqa: E731
    e = (lambda v: v) if explode else (lambda v: (0, 0, 0))
    w = dict(k["wheel"])
    b = dict(k["brake"])
    return [
        Part("Fork unit", k["fork"][0][1], COL["fork"], 1, e((0, 0, -120))),
        Part("Side arms, left", pick("arms", "left"), COL["arms"], 2, e((0, 380, 0))),
        Part("Side arms, right", pick("arms", "right"), COL["arms"], 2, e((0, -380, 0))),
        Part("Upper jaws", Compound([s for _, s in k["jaws"]]), COL["jaws"], 3, e((0, 0, 260))),
        Part("Jaw liners", Compound([s for _, s in k["liners"]]), COL["liners"], 4, e((0, 0, 150))),
        Part("T-handle bolts and set screws", Compound([s for _, s in k["bolts"]]), COL["bolts"], 5, e((0, 0, 420))),
        Part("Wheel", Compound([w["tyre"], w["rim"], w["hub"], w["axle and nuts"], w["spokes"]]), COL["tyre"], 6, e((0, 0, -420))),
        Part("Disc brake set", Compound([b["rotor"], b["caliper"]]), COL["brake"], 7, e((0, -300, -300))),
        Part("Brake lever and cable", Compound([b["lever"], b["cable"]]), COL["brake"], 7, e((0, -200, 260))),
        Part("Lever mount", Compound([s for _, s in k["mount"]]), COL["mount"], 8, e((250, -200, 160))),
        Part("Cross strap", k["cross"][0][1], COL["cross"], 9, e((0, 0, 560))),
        Part("Patient straps", Compound([s for _, s in k["patient"]]), COL["patient"], 10, e((0, 0, 500))),
        Part("Bearer harness pole loops", Compound([s for _, s in k["harness"]]), COL["harness"], 11, e((0, 0, 300))),
        Part("Lift handles", Compound([s for _, s in k["handles"]]), COL["handles"], 16, e((0, 0, -250))),
        Part("Hold-back strap loops", Compound([s for _, s in k["holdback"]]), COL["holdback"], 17, e((-200, 0, 200))),
    ]


def hero():
    ps = doli_parts() + kit_parts()
    return K._render(K.with_scale_figure(ps), MD / "hero.png", title=PROJECT,
                     note="Kit fitted to the reference doli; seen from the front right and above, 24 deg elevation. "
                          "Grey figure: 1.75 m person for scale")


def cutaway():
    """Cut across the doli just behind the front clamps, looking back along -X from the front."""
    xc = P["stub_x"]
    keep = Pos(xc - 3000, 0, 500) * Box(6000, 3000, 3000)
    out = []
    for q in doli_parts() + kit_parts():
        if q.name.startswith("Patient") or q.name.startswith("Bearer") or q.name.startswith("Lever") or "lever" in q.name:
            continue
        s = q.shape & keep
        if s is not None and s.volume > 1:
            out.append(Part(q.name, s, q.color, q.bom))
    return K._render(out, MD / "cutaway.png", elev=10, azim=12, size=(10, 7.5), title=f"{PROJECT}: cutaway",
                     note="Cut across the doli through the front pair of clamps; seen from the front and slightly to the "
                          "left, 10 deg elevation. Each pole sits in a rubber-lined steel V, closed by a jaw and two T-bolts; "
                          "the wheel runs between the cross stubs, below the cross strap and the bed")


def exploded():
    """The frame, wheel and brake pulled apart; left-side clamp parts move left, right-side parts right."""
    k = M.build_kit(P)
    w = dict(k["wheel"])
    b = dict(k["brake"])
    ps = []
    for side, sy in (("left", 1), ("right", -1)):
        sel = lambda key: Compound([s for n, s in k[key] if side in n.split()])  # noqa: E731
        ps += [Part("Side arms (4)", sel("arms"), COL["arms"], 2, (0, sy * 330, 120)),
               Part("Jaw liners (8)", sel("liners"), COL["liners"], 4, (0, sy * 330, 300)),
               Part("Upper jaws (4)", sel("jaws"), COL["jaws"], 3, (0, sy * 330, 470)),
               Part("T-handle bolts (8) and set screws (4)", Compound([s for n, s in k["bolts"] if side in n.split()]),
                    COL["bolts"], 5, (0, sy * 330, 640))]
    ps += [Part("T-handle bolts (8) and set screws (4)", Compound([s for n, s in k["bolts"] if n.startswith("set")]),
                COL["bolts"], 5, (0, 0, 200)),
           Part("Fork unit", k["fork"][0][1], COL["fork"], 1, (0, 0, 0)),
           Part("Wheel", Compound([w["tyre"], w["rim"], w["hub"], w["axle and nuts"], w["spokes"]]), COL["tyre"], 6, (0, 0, -380)),
           Part("Disc brake set", Compound([b["rotor"], b["caliper"]]), COL["brake"], 7, (0, -330, -380)),
           Part("Disc brake set", b["lever"], COL["brake"], 7, (-620, -650, -170)),
           Part("Lever mount", Compound([s for _, s in k["mount"]]), COL["mount"], 8, (-620, -650, -300)),
           Part("Cross strap", k["cross"][0][1], COL["cross"], 9, (0, 0, 520))]
    return K._render(ps, MD / "exploded.png", offsets=True, labels=True, elev=22, azim=-58, size=(10, 7.5),
                     title=f"{PROJECT}: exploded view",
                     note="Frame, wheel and brake seen from the front right and above, 22 deg elevation; numbers match "
                          "bom/bom.csv. Lever mount drawn near the frame (it fits on the front right pole). Not shown: "
                          "brake cable, patient straps (10), bearer harnesses (11), lift handles (16), hold-back strap (17)")


def flow():
    r = R()
    W = r("L1")
    bearers = 2 * r("L5")
    return K.flow_diagram(
        [("Patient and doli, rated", round(r("L1") - r("K12"), 1)), ("Rolling weight with the kit", round(W, 1)),
         ("Four clamps to the fork unit", round(W - r("K12") + r("K1"), 1)), ("Wheel to the ground", round(W - bearers, 1))],
        MD / "flow.png", f"{PROJECT}: where the weight goes on a level trail (all values are estimates)", "kg",
        [(1, "Front and rear bearers together (est.)", round(bearers, 1))])


def web():
    """Coarse glTF tessellation (1 mm chord, 0.35 rad) keeps media/model.glb a few MB."""
    import functools
    import build123d as bd
    orig = bd.export_gltf
    bd.export_gltf = functools.partial(orig, linear_deflection=1.0, angular_deflection=0.35)
    try:
        return K.export_web_model(doli_parts() + kit_parts(), "media", title=f"{PROJECT}: {TITLE}")
    finally:
        bd.export_gltf = orig


def blueprint():
    from drawing import Sheet, project_views
    r = R()
    ps = doli_parts(bed=False) + kit_parts()
    shown = K.with_scale_figure(ps)
    views = project_views(Compound([p.shape for p in ps]), MD / "_views")
    views["iso"] = project_views(Compound([p.shape for p in shown]), MD / "_views_fig")["iso"]
    s = Sheet(project=PROJECT, title=f"{TITLE} concept", dwg_no="DLT-DWG-010", rev="P2", author="Amish Chadha",
              date="2026-10-03", theme="blueprint", material="Massing model for concept communication",
              revisions=[("P1", "Concept sheet from the constructable model (DLT-DDR-002)", "2026-10-03", "AC"),
                         ("P2", "DLT-DDR-003: lift handles, hold-back strap, two bags", "2026-10-03", "AC")])
    s.add_ortho(views)
    s.add_svg(views["iso"], 276, 32, 140, 118, label="Isometric view", sublabel="Not to scale; figure is a 1.75 m person")
    s.add_notes("Key figures", [
        "Clamps on to the family's bamboo doli: poles 40 to 80 mm, 450 to 600 mm apart",
        "20 inch wheel under the patient's hips; disc brake, lever on the front right pole",
        f"Rated patient 120 kg; rolling weight {r('L1'):.0f} kg with doli and kit",
        f"Level trail: about {r('L5'):.0f} kg per bearer against {r('L3') if False else 65:.0f} kg carried (est.)",
        f"Brake holds a 30 % grade, factor {r('B4'):.2f}; wet mud grip {r('B6'):.2f}: hold-back strap",
        "Wet clay over 20 %: lift and carry; steps over 250 mm: four bearers",
        f"Width {r('W1'):.0f} mm on 550 mm poles; kit {r('K11'):.1f} kg in two bags; about USD {r('Q1'):.0f}",
        "Not certified rescue or medical equipment",
    ], x=276, y=168, width=140)
    s.save(MD / "concept-blueprint")
    shutil.rmtree(MD / "_views", ignore_errors=True)
    shutil.rmtree(MD / "_views_fig", ignore_errors=True)
    return MD / "concept-blueprint.png"


if __name__ == "__main__":
    fns = {"hero": hero, "cutaway": cutaway, "exploded": exploded, "flow": flow, "web": web, "blueprint": blueprint}
    for w in sys.argv[1:] or list(fns):
        print(w, "->", fns[w]())
