"""DoliTrail general arrangement sheet DLT-DWG-001, Rev P3 (TRL 3; DLT-DDR-002 and DLT-DDR-003 applied).

Run from the repo root:  python cad/src/sheets.py
Writes cad/drawings/DLT-DWG-001.svg, .pdf and .png from cad/src/model.py with .kit/drawing.py: the
kit fitted to the reference doli (poles drawn cut short, bed and patient straps left out so the
frame shows), section A-A across the doli through the front clamps at 1:10, and the main sizes.
Spokes are left out of the views for clarity. The concept blueprint in media/ is DLT-DWG-010; the
making sketches are DLT-DWG-101 onward (cad/src/build_plan_media.py).
"""
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / ".kit"), str(ROOT / "cad" / "src")]
from build123d import Box, Compound, Pos  # noqa: E402
from drawing import Sheet, _t, project_views, INK, MUTED  # noqa: E402
import model as M  # noqa: E402

P = M.PARAMS
DATE = "2026-10-03"
SEC_K = 0.1             # 1:10


def leader(x1, y1, x2, y2, text, anchor="start"):
    return [f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="{MUTED}" stroke-width="0.15"/>',
            f'<circle cx="{x1:.2f}" cy="{y1:.2f}" r="0.5" fill="{INK}"/>',
            _t(x2 + (1 if anchor == "start" else -1), y2 + 0.8, text, 2.1, 400, INK, anchor)]


def assembly(k, x0=-700.0, x1=1400.0):
    c = M.doli_context(P)
    win = Pos((x0 + x1) / 2, 0, 600) * Box(x1 - x0, 1500, 1400)
    poles = Compound(c["poles"]) & win
    w = dict(k["wheel"])
    kit = [s for key in ("fork", "arms", "jaws", "liners", "bolts", "mount", "cross", "harness", "handles") for _, s in k[key]]
    kit = [s for s in kit if s.bounding_box().max.X > x0 and s.bounding_box().min.X < x1]
    kit += [w["tyre"], w["rim"], w["hub"], w["axle and nuts"]] + [s for _, s in k["brake"] if True]
    return Compound(kit + [poles])


def main():
    D = M.derived(P)
    k = M.build_kit(P)
    work = ROOT / "cad" / "drawings" / "_ga_views"
    asm = assembly(k)
    views = project_views(asm, work)
    xs = P["stub_x"]
    slab = Pos(xs - 40, 0, 500) * Box(120, 1500, 1200)     # front clamps, stub and struts, wheel behind
    sec = Compound([asm & slab])
    sv = project_views(sec, work / "sec")
    sb = sec.bounding_box()
    s = Sheet(project="DoliTrail", title="Clamp-on wheel kit on the reference doli: general arrangement",
              dwg_no="DLT-DWG-001", rev="P3", author="Amish Chadha", date=DATE, scale=None,
              material="Kit per bom/bom.csv; poles are the family's doli (reference shown, cut short). PRELIMINARY, NOT FOR FABRICATION",
              revisions=[("P1", "Preliminary GA for TRL 3 (from cad/src/model.py)", DATE, "AC"),
                         ("P2", "DLT-DDR-002: design for construction", DATE, "AC"),
                         ("P3", "DLT-DDR-003: lift handles on the stubs; hold-back strap noted", DATE, "AC")])
    s.add_ortho(views)
    vw = (sb.max.Y - sb.min.Y) * SEC_K
    vh = (sb.max.Z - sb.min.Z) * SEC_K
    x0, y0 = 286.0, 34.0
    s.add_svg(sv["right"], x0, y0, vw, vh, scale=SEC_K)
    L = [_t(x0 + vw / 2, y0 + vh + 6, "SECTION A-A", 2.8, 600, INK, "middle"),
         _t(x0 + vw / 2, y0 + vh + 10, "Scale 1:10; looking back along -X through the front clamps", 2.2, 400, MUTED, "middle")]
    cy, cz = (sb.min.Y + sb.max.Y) / 2, (sb.min.Z + sb.max.Z) / 2
    X = lambda y: x0 + vw / 2 + (y - cy) * SEC_K   # noqa: E731  (looking along -X, +Y is on the right)
    Z = lambda z: y0 + vh / 2 - (z - cz) * SEC_K   # noqa: E731
    tx = x0 + vw + 3
    yp = P["pole_y"]
    L += leader(X(yp), Z(P["pole_z"]), tx, 40, "POLE (FAMILY'S DOLI)")
    L += leader(X(yp - 20), Z(D["v_apex"] + 8), tx, 47, "SADDLE (2), LINER (4)")
    L += leader(X(yp + 15), Z(P["pole_z"] + 45), tx, 33, "JAW (3), T-BOLTS (5)")
    L += leader(X(120), Z(P["stub_z"]), tx, 54, "STUB (1), SPIGOT (2)")
    L += leader(X(0), Z(300), tx, 61, "WHEEL (6), CUT EDGE")
    L += leader(X(P["strut_y"]), Z(468), tx, 68, "STRUT (1)")
    s._dim(X(-yp), Z(P["pole_z"]), X(-yp), Z(0), f"{P['pole_z']:.0f}", "left", off=4)
    s._layers += L
    s.add_notes("Main sizes and figures (mm unless stated)", [
        "Poles 40 to 80 dia at 450 to 600 centres; reference 60 at 550",
        f"Pole centres {P['pole_z']:.0f} above ground, level, wheel down",
        f"Width over clamps {D['width']:.0f} on the reference doli",
        "Wheel 20 x 2.125 (57-406), 514 dia, disc hub, 3/8 axle",
        f"Cross stubs 30 x 30 x 2 SHS, {P['stub_len']:.0f} long, at +/-{P['stub_x']:.0f}",
        f"Struts 22.2 x 1.6 tube, {D['strut_len']:.0f} long; dropouts 5 plate",
        f"Arms 25 x 25 x 1.6 SHS; spigot {P['spigot_len']:.0f}, at least {D['insertion_min']:.0f} in the stub",
        "Clamps: 90 deg V, 5 rubber liner, two M8 T-bolts at 104 centres",
        "Brake: 203 rotor, cable caliper; lever with lock on front right pole",
        "Cross strap 50 webbing round both poles above the wheel",
        f"Lift handles (17) on the stubs, {P['handle_y']:.0f} off centre; hold-back strap (16) on rear pole ends, not shown",
        "Rated patient 120 kg; rolling weight about 142.5 kg",
        "Third-angle; X forward, Y to the left; (n) = BOM line",
    ], x=276, y=118, width=146)
    out = s.save(ROOT / "cad" / "drawings" / "DLT-DWG-001")
    shutil.rmtree(work, ignore_errors=True)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
