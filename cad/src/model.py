"""DoliTrail parametric model (build123d), TRL 3, constructable design (DLT-DDR-002).

Run from the repo root:  python cad/src/model.py [--check] [--export]
  --check   run the constructability checks (overlaps, contacts, clearances, widths)
  --export  write cad/step/*.step and cad/stl/*.stl

DoliTrail is a clamp-on kit for the bamboo stretcher (doli) a family already has. The doli itself
(two bamboo poles, two lashed cross sticks and a cloth bed) is CONTEXT: it is modelled as the
reference doli (poles 2,550 mm long, 60 mm diameter, 550 mm apart) so the kit can be sized and
checked against it. The kit fits poles of 40 to 80 mm diameter at 450 to 600 mm centres.

Coordinates in mm. X along the doli, +X toward the front bearer; Y across, +Y to the left of a
bearer facing +X; Z up from the ground. The wheel axle is at x = 0, y = 0, z = wheel radius. The
poles are level with their centres 720 mm above the ground (the reference doli, 60 mm poles).

Kit (BOM line numbers in brackets, see bom/bom.csv):
  [1]  fork unit: two 30 x 30 mm cross stubs, four 22 mm struts, dropout plates with the brake
       mount, welded steel (one piece)
  [2]  side arms, four: a 25 mm square spigot that slides into a stub, a post and a V saddle
  [3]  upper jaws, four: bent 3 mm steel V with two ears
  [4]  jaw liners, eight: 5 mm rubber V strips glued in the saddles and jaws
  [5]  T-handle bolts M8 (eight, close the clamps) and T-handle set screws M8 (four, hold the arms)
  [6]  wheel: 20 inch cargo wheel, 57-406 tyre, disc hub, solid 3/8 inch axle with nuts
  [7]  disc brake set: 203 mm rotor, cable caliper, lever with parking lock, cable and housing
  [8]  lever mount: a 22.2 mm bar stub on a small rubber-lined saddle, strapped to the pole
  [9]  cross strap: 50 mm webbing loop round both poles above the wheel, under the bed
  [10] patient straps, three: 50 mm webbing with quick-release cam buckles
  [11] bearer harnesses, two: shoulder yoke, hip belt and two pole loops each (pole loops shown)
  [12] wheel bag (fork unit, wheel, brake, pump), [13] fitting card, [14] hook-and-loop cable ties
  [16] hold-back strap: two webbing end caps over the rear pole ends, legs to a ring and a tail to
       the rear (uphill) bearer's hip belt (DLT-DDR-003, decision 7A)
  [17] lift handles, two: webbing loops sewn round the cross stubs for two helpers at steps
       (DLT-DDR-003, decision 9A)
  [18] parts bag (arms, jaws, bolts, lever mount, straps, harnesses, hold-back strap; decision 8A)
CONCEPT, NOT FOR FABRICATION.
"""
import math
import sys
from pathlib import Path

from build123d import (Box, Compound, Face, Pos, Rot, Solid, Torus, Vector, Wire, Plane,
                       extrude, export_step, export_stl)

ROOT = Path(__file__).resolve().parents[2]
R2 = math.sqrt(2.0)

PARAMS = {
    # reference doli (context; every doli is measured at fitting)
    "pole_d": 60.0,          # design pole diameter; the clamps take 40 to 80
    "pole_y": 275.0,         # half the pole spacing (550 mm centres)
    "pole_z": 720.0,         # pole centre above the ground with the wheel down and the doli level
    "pole_x": (-1150.0, 1400.0),
    "stick_x": (-1000.0, 1250.0),   # lashed cross sticks, on top of the poles
    "stick_d": 40.0,
    "bed_x": (-950.0, 1200.0),
    # wheel and brake (bought)
    "wheel_r": 257.0,        # 20 x 2.125 tyre, 57-406
    "tyre_w": 57.0,
    "rim_r": (182.0, 200.0),
    "rim_w": 24.0,
    "hub_old": 100.0,        # over-locknut width of the front disc hub
    "flange_y": 30.0,
    "flange_r": 29.0,
    "axle_d": 9.5,
    "rotor_r": 101.5,
    "rotor_y": -34.5,        # rotor plane, left side
    "caliper_ang": 150.0,    # rotation of the caliper about the axle from +X (puts it low at the rear)
    # fork unit (made)
    "stub_x": 300.0,         # cross stubs at x = +/-300, clear of the 514 mm wheel
    "stub_z": 505.0,         # stub centre height
    "stub_len": 320.0,
    "stub": (30.0, 2.0),     # square hollow section, side and wall
    "strut": (22.2, 1.6),    # round tube, outside diameter and wall
    "strut_y": 64.0,
    "plate_t": 5.0,          # dropout plate, inner faces at +/- hub_old / 2
    "screw_y": 135.0,        # set screw positions on the stubs
    # side arms (made)
    "arm": (25.0, 1.6),      # square hollow section that slides in the stub
    "spigot_len": 230.0,
    "saddle": (60.0, 130.0, 4.0),   # base plate: along the pole, across, thick
    "v_half": 30.0,          # half width of the saddle V (inside), 90 deg included
    "v_t": 3.0,
    "liner_t": 5.0,
    "jaw_len": 40.0,
    "bolt_dy": 52.0,         # clamp bolts either side of the pole centre
    "bolt_d": 8.0,
    "bolt_len": 130.0,
    # straps
    "web_w": 50.0,
    "web_t": 2.0,
    "patient_straps_x": [800.0, 150.0, -550.0],
    "loop_x": (1330.0, -1080.0),    # harness pole loops near the pole ends (front, rear)
    "lever_x": 1180.0,               # lever mount on the front right pole
    # decisions 7A and 9A (DLT-DDR-003)
    "cap_len": 40.0,                 # hold-back strap end caps over the rear pole ends
    "hb_ring": (-1450.0, 0.0, 860.0),  # ring where the two legs of the hold-back strap meet
    "hb_tail": 600.0,                # tail from the ring to the rear bearer's hip belt
    "handle_y": 100.0,               # lift handles: front one on the left, rear one on the right
    "handle_w": 40.0,
    "handle_drop": 130.0,            # hand loop hangs below the stub
}


# ---------------------------------------------------------------- helpers
def prism_x(poly_yz, x0, x1):
    """Extrude a polygon given in (y, z) from x0 to x1."""
    w = Wire.make_polygon([Vector(x0, y, z) for y, z in poly_yz], close=True)
    return extrude(Face(w), amount=x1 - x0, dir=(1, 0, 0))


def prism_y(poly_xz, y0, y1):
    """Extrude a polygon given in (x, z) from y0 to y1."""
    w = Wire.make_polygon([Vector(x, y0, z) for x, z in poly_xz], close=True)
    return extrude(Face(w), amount=y1 - y0, dir=(0, 1, 0))


def rod(a, b, r):
    a, b = Vector(*a), Vector(*b)
    v = b - a
    return Solid.make_cylinder(r, v.length, Plane(origin=a, z_dir=v))


def tube(a, b, od, t):
    return rod(a, b, od / 2) - rod(a, b, od / 2 - t)


def shs(center, size, length, wall, axis):
    """Square hollow section centred at center, along axis 'x', 'y' or 'z'."""
    dims = {"x": (length, size, size), "y": (size, length, size), "z": (size, size, length)}[axis]
    inner = {"x": (length + 2, size - 2 * wall, size - 2 * wall), "y": (size - 2 * wall, length + 2, size - 2 * wall),
             "z": (size - 2 * wall, size - 2 * wall, length + 2)}[axis]
    return Pos(*center) * (Box(*dims) - Box(*inner))


def ring_band(xc, yc, zc, r_in, t, w):
    """Webbing wrapped round a pole (axis X): an annulus r_in to r_in + t, w wide."""
    a, b = (xc - w / 2, yc, zc), (xc + w / 2, yc, zc)
    return rod(a, b, r_in + t) - rod(a, b, r_in)


# ---------------------------------------------------------------- derived sizes
def pole_center_z(d, p=PARAMS):
    """Pole centre height for a pole of diameter d sitting in the saddle (frame fixed)."""
    return v_apex(p) + (d / 2 + p["liner_t"]) * R2


def v_apex(p=PARAMS):
    """Height of the inside apex of the saddle liner's seat (the saddle steel V apex, inside)."""
    return p["pole_z"] - (p["pole_d"] / 2 + p["liner_t"]) * R2


def derived(p=PARAMS):
    za = v_apex(p)
    base_top = za - p["v_t"] * R2
    base_bot = base_top - p["saddle"][2]
    s, w = p["stub"]
    stub_top = p["stub_z"] + s / 2
    arm = p["arm"][0]
    post_bot = p["stub_z"] + arm / 2
    y_min, y_max = 225.0, 300.0                     # pole half-spacings the arms reach
    stub_end = p["stub_len"] / 2
    inner_end = lambda yp: yp + arm / 2 - p["spigot_len"]  # noqa: E731
    return {
        "v_apex": za, "base_top": base_top, "base_bot": base_bot, "post_bot": post_bot,
        "post_len": base_bot - post_bot,
        "stub_top": stub_top,
        "spacing_range": (2 * y_min, 2 * y_max),
        "insertion_min": stub_end - inner_end(y_max),          # spigot length inside the stub at the widest setting
        "spigot_gap_min": 2 * inner_end(y_min),                # gap between opposite spigot ends at the narrowest
        "pole_z_40": pole_center_z(40.0, p), "pole_z_80": pole_center_z(80.0, p),
        "width": 2 * (p["pole_y"] + p["saddle"][1] / 2),
        "strut_len": math.hypot(p["stub_x"], p["stub_z"] - s / 2 - p["wheel_r"]),
        "wheel_top": 2 * p["wheel_r"],
        "drop_below_poles": p["pole_z"],                       # tyre contact below the pole centres
    }


# ---------------------------------------------------------------- the doli (context)
def doli_context(p=PARAMS):
    x0, x1 = p["pole_x"]
    r = p["pole_d"] / 2
    poles = [rod((x0, s * p["pole_y"], p["pole_z"]), (x1, s * p["pole_y"], p["pole_z"]), r) for s in (1, -1)]
    zs = p["pole_z"] + r + p["stick_d"] / 2
    sticks = [rod((xs, -p["pole_y"] - 60, zs), (xs, p["pole_y"] + 60, zs), p["stick_d"] / 2) for xs in p["stick_x"]]
    # cloth bed: a sheet between the poles, slightly sagging, from just inside one pole to the other
    yb = p["pole_y"] - r
    zt = p["pole_z"] - 4
    sag = 40.0
    pts = [(-yb, zt), (0, zt - sag), (yb, zt), (yb, zt - 3), (0, zt - sag - 3), (-yb, zt - 3)]
    bed = prism_x(pts, *p["bed_x"])
    return {"poles": poles, "sticks": sticks, "bed": bed}


# ---------------------------------------------------------------- bought: wheel and brake
def wheel(p=PARAMS):
    r = p["wheel_r"]
    tw = p["tyre_w"]
    c = (0, 0, r)
    tyre = Pos(*c) * Rot(90, 0, 0) * Torus(r - tw / 2, tw / 2)
    ri, ro = p["rim_r"]
    rim = rod((0, -p["rim_w"] / 2, r), (0, p["rim_w"] / 2, r), ro) - rod((0, -20, r), (0, 20, r), ri)
    hw = p["hub_old"] / 2
    hub = rod((0, -hw + 6, r), (0, hw - 6, r), 17.0)
    fl = [rod((0, s * p["flange_y"] - 1.5, r), (0, s * p["flange_y"] + 1.5, r), p["flange_r"]) for s in (1, -1)]
    axle = rod((0, -hw - 8, r), (0, hw + 8, r), p["axle_d"] / 2)
    cones = [rod((0, s * hw, r), (0, s * (hw - 6), r), 9.0) for s in (1, -1)]
    nuts = [rod((0, s * (hw + p["plate_t"]), r), (0, s * (hw + p["plate_t"] + 7), r), 8.0) for s in (1, -1)]
    spokes = []
    for k in range(36):
        a = 2 * math.pi * k / 36
        s = 1 if k % 2 else -1
        f = (p["flange_r"] - 3) / ri
        a0 = (ri - 1) * math.cos(a), (ri - 1) * math.sin(a)
        spokes.append(rod((a0[0] * f, s * p["flange_y"], r + a0[1] * f), (a0[0], 0, r + a0[1]), 1.0))
    return {"tyre": tyre, "rim": rim, "hub": Compound([hub] + fl + cones), "axle": Compound([axle] + nuts),
            "spokes": Compound(spokes)}


def brake(p=PARAMS):
    r = p["wheel_r"]
    y0 = p["rotor_y"]
    rotor = rod((0, y0 - 1, r), (0, y0 + 1, r), p["rotor_r"]) - rod((0, y0 - 2, r), (0, y0 + 2, r), 26.0)
    rotor = rotor + (rod((0, y0 - 1, r), (0, y0 + 1, r), 34.0) - rod((0, y0 - 2, r), (0, y0 + 2, r), 17.0))
    # caliper: body radially 80 to 112 mm from the axle, 60 mm along the rotor, y -26 to -50, slot for the rotor
    hw = p["hub_old"] / 2
    body = Pos(96, (-26 - hw) / 2, 0) * Box(32, hw - 26, 60)
    slot = Pos(90, y0, 0) * Box(24, 5, 70)
    cal = body - slot
    cal = Pos(0, 0, r) * Rot(0, p["caliper_ang"], 0) * cal
    return {"rotor": rotor, "caliper": cal}


def lever(p=PARAMS):
    """Brake lever with parking lock (bought) clamped on the lever mount's bar stub."""
    x, y, z = lever_bar_axis(p)
    x = x + 47.0                       # the clamp sits on the bar stub beyond the saddle
    clamp = rod((x - 7, y, z), (x + 7, y, z), 15.0) - rod((x - 8, y, z), (x + 8, y, z), 11.15)
    body = Pos(x + 25, y - 24.2, z) * Box(40, 26, 24)
    blade = Pos(x + 90, y - 30, z - 6) * Box(100, 10, 18)
    lock = Pos(x + 25, y - 22, z + 16) * Box(14, 10, 8)
    return Compound([clamp, body, blade, lock])


def cable(p=PARAMS):
    """Brake cable in its housing: caliper, up the rear left strut... modelled as straight runs."""
    r = p["wheel_r"]
    hw = p["hub_old"] / 2
    ca = math.radians(p["caliper_ang"])
    cp = (96 * math.cos(ca) * -1, -hw - 2, r + 96 * math.sin(ca))   # near the caliper's cable stop
    # rotate (96, 0) by caliper_ang about Y: x' = x cos a, z' = -x sin a
    cp = (96 * math.cos(ca), -hw - 9, r - 96 * math.sin(ca))
    sx, sz = p["stub_x"], p["stub_z"]
    s = p["stub"][0]
    run = [cp, (-sx + 30, -hw - 9, sz - s / 2 - 25), (-sx + 30, -hw - 9, sz + s / 2 + 5),
           (sx - 30, -hw - 9, sz + s / 2 + 5)]
    py = -p["pole_y"]
    pz = p["pole_z"] + p["pole_d"] / 2 + 3.5
    run += [(sx + 40, -hw - 9, sz + s / 2 + 5), (sx + 120, py + 40, pz - 30), (sx + 200, py, pz),
            (p["lever_x"] - 30, py, pz)]
    segs = [rod(run[i], run[i + 1], 2.5) for i in range(len(run) - 1)]
    return Compound(segs)


# ---------------------------------------------------------------- made: fork unit
def fork_unit(p=PARAMS):
    r = p["wheel_r"]
    sx, sz, L = p["stub_x"], p["stub_z"], p["stub_len"]
    s, w = p["stub"]
    hw = p["hub_old"] / 2
    t = p["plate_t"]
    od, wt = p["strut"]
    sy = p["strut_y"]
    parts = []
    for xs in (sx, -sx):
        st = shs((xs, 0, sz), s, L, w, "y")
        for ys in (p["screw_y"], -p["screw_y"]):
            st = st - rod((xs, ys, sz + s / 2 - w - 1), (xs, ys, sz + s / 2 + 1), 4.5)
        parts.append(st)
        for ys in (p["screw_y"], -p["screw_y"]):   # welded M8 nuts for the set screws
            nut = rod((xs, ys, sz + s / 2), (xs, ys, sz + s / 2 + 6.5), 6.5) - rod((xs, ys, sz + s / 2 - 1), (xs, ys, sz + s / 2 + 8), 4.0)
            parts.append(nut)
    # dropout plates, slot open downward; the left plate carries the caliper mount lobe
    pl = [(-50, 0), (-40, 62), (40, 62), (50, 0), (35, -30), (5, -30), (5, 5), (-5, 5), (-5, -30), (-35, -30)]
    ca = math.radians(p["caliper_ang"])
    rot = lambda x, z: (x * math.cos(ca) + z * math.sin(ca), -x * math.sin(ca) + z * math.cos(ca))  # noqa: E731
    lobe = [rot(78, -34), rot(116, -34), rot(116, 34), rot(78, 34)]
    for sgn in (1, -1):
        poly = [(x, r + z) for x, z in pl]
        plate = prism_y(poly, sgn * hw, sgn * (hw + t)) if sgn > 0 else prism_y(poly, -hw - t, -hw)
        if sgn < 0:
            lp = [(x, r + z) for x, z in [(-35, -30), (-50, 0)] + lobe[::-1]]
            lp = [(x, r + z) for x, z in [(-35, -30)] + [lobe[0], lobe[1], lobe[2], lobe[3]] + [(-50, 0)]]
            plate = plate + prism_y(lp, -hw - t, -hw)
        parts.append(plate)
    # struts: from the dropout plates (45 mm out from the axle along the strut) to the stub undersides
    for sgn in (1, -1):
        for xs in (sx, -sx):
            top = (xs, sgn * sy, sz - s / 2 + 1)
            d = Vector(xs, 0, sz - s / 2 - r)
            u = d / d.length
            bot = (u.X * 45, sgn * sy, r + u.Z * 45)
            stub_env = Pos(xs, 0, sz) * Box(s, L, s)
            parts.append(tube(bot, (top[0] + u.X * 12, top[1], top[2] + u.Z * 12), od, wt) - stub_env)
    fu = parts[0]
    for q in parts[1:]:
        fu = fu + q
    return fu


# ---------------------------------------------------------------- made: side arms, jaws, liners
def saddle_v(yp, x0, x1, p=PARAMS):
    za = v_apex(p)
    h, t = p["v_half"], p["v_t"]
    o = t * R2
    poly = [(yp - h - o, za + h), (yp - h, za + h), (yp, za), (yp + h, za + h), (yp + h + o, za + h), (yp, za - o)]
    return prism_x(poly, x0, x1)


def side_arm(xs, side, p=PARAMS):
    """side = +1 (left pole) or -1 (right pole). Spigot, post, saddle base plate, V and welded nuts."""
    d = derived(p)
    yp = side * p["pole_y"]
    a, wa = p["arm"]
    sz = p["stub_z"]
    y_out = yp + side * a / 2
    y_in = y_out - side * p["spigot_len"]
    spig = shs((xs, (y_in + y_out) / 2, sz), a, p["spigot_len"], wa, "y")
    post = shs((xs, yp, (d["post_bot"] + d["base_bot"]) / 2), a, d["post_len"], wa, "z")
    bl, bw, bt = p["saddle"]
    base = Pos(xs, yp, d["base_bot"] + bt / 2) * Box(bl, bw, bt)
    for k in (1, -1):
        base = base - rod((xs, yp + k * p["bolt_dy"], d["base_bot"] - 1), (xs, yp + k * p["bolt_dy"], d["base_top"] + 1), 4.5)
    v = saddle_v(yp, xs - bl / 2, xs + bl / 2, p)
    nuts = []
    for k in (1, -1):
        yb = yp + k * p["bolt_dy"]
        nuts.append(rod((xs, yb, d["base_bot"] - 6.5), (xs, yb, d["base_bot"]), 6.5) - rod((xs, yb, d["base_bot"] - 8), (xs, yb, d["base_bot"] + 1), 4.0))
    arm = spig + post + base + v
    for n in nuts:
        arm = arm + n
    return arm


def jaw_shift(d, p=PARAMS):
    """How far the upper jaw sits above its position on the design pole, for a pole of diameter d."""
    return pole_center_z(d, p) + (d / 2) * R2 - (p["pole_z"] + (p["pole_d"] / 2) * R2)


def upper_jaw(xs, side, p=PARAMS, d=None):
    d = d or p["pole_d"]
    yp = side * p["pole_y"]
    zi = p["pole_z"] + (p["pole_d"] / 2) * R2 + p["liner_t"] * R2 + jaw_shift(d, p)   # inside apex of the steel V
    t = p["v_t"] * R2
    e = p["saddle"][1] / 2
    ze = zi - 38.8                     # underside of the ears
    poly = [(-e, ze + 3), (-40, ze + 3), (0, zi + t), (40, ze + 3), (e, ze + 3), (e, ze), (38.8, ze), (0, zi),
            (-38.8, ze), (-e, ze)]
    poly = [(yp + y, z) for y, z in poly]
    jl = p["jaw_len"]
    j = prism_x(poly, xs - jl / 2, xs + jl / 2)
    for k in (1, -1):
        j = j - rod((xs, yp + k * p["bolt_dy"], ze - 1), (xs, yp + k * p["bolt_dy"], ze + 4), 4.5)
    return j, ze + 3


def liners(xs, side, p=PARAMS, d=None):
    d = d or p["pole_d"]
    yp = side * p["pole_y"]
    za = v_apex(p)
    o = p["liner_t"] * R2
    h = p["v_half"] - 1.0
    low = [(yp - h, za + h), (yp, za), (yp + h, za + h), (yp + h, za + h + o), (yp, za + o), (yp - h, za + h + o)]
    bl = p["saddle"][0]
    lower = prism_x(low, xs - bl / 2 + 2, xs + bl / 2 - 2)
    zc = pole_center_z(d, p)
    zi = zc + (d / 2) * R2              # inside apex of the upper liner
    hu = 33.0
    up = [(yp - hu, zi - hu), (yp, zi), (yp + hu, zi - hu), (yp + hu, zi - hu + o), (yp, zi + o), (yp - hu, zi - hu + o)]
    jl = p["jaw_len"]
    upper = prism_x(up, xs - jl / 2 + 1, xs + jl / 2 - 1)
    return lower, upper


def clamp_bolts(xs, side, p=PARAMS, d=None):
    d = d or p["pole_d"]
    dd = derived(p)
    yp = side * p["pole_y"]
    _, ztop = upper_jaw(xs, side, p, d)
    out = []
    for k in (1, -1):
        yb = yp + k * p["bolt_dy"]
        washer = rod((xs, yb, ztop), (xs, yb, ztop + 1.5), 9.0) - rod((xs, yb, ztop - 1), (xs, yb, ztop + 3), 4.3)
        boss = rod((xs, yb, ztop + 1.5), (xs, yb, ztop + 13.5), 8.0)
        handle = rod((xs - 32, yb, ztop + 8), (xs + 32, yb, ztop + 8), 5.0)
        shank = rod((xs, yb, ztop + 1.5 - p["bolt_len"] + 12), (xs, yb, ztop + 1.5), p["bolt_d"] / 2)
        out.append(Compound([washer, boss, handle, shank]))
    return out


def set_screws(p=PARAMS):
    sx, sz = p["stub_x"], p["stub_z"]
    a = p["arm"][0]
    s = p["stub"][0]
    out = []
    for xs in (sx, -sx):
        for ys in (p["screw_y"], -p["screw_y"]):
            shank = rod((xs, ys, sz + a / 2), (xs, ys, sz + s / 2 + 20), 4.0)
            boss = rod((xs, ys, sz + s / 2 + 20), (xs, ys, sz + s / 2 + 30), 7.0)
            handle = rod((xs - 28, ys, sz + s / 2 + 25), (xs + 28, ys, sz + s / 2 + 25), 4.5)
            out.append(Compound([shank, boss, handle]))
    return out


# ---------------------------------------------------------------- made: lever mount
def lever_bar_axis(p=PARAMS):
    """Centre of the lever mount's 22.2 mm bar stub (it runs along X above the front right pole)."""
    r = p["pole_d"] / 2
    zt = p["pole_z"] + (r + p["liner_t"]) * R2 + p["v_t"] * R2
    return p["lever_x"], -p["pole_y"], zt + 11.1


def lever_mount(p=PARAMS):
    x = p["lever_x"]
    yp = -p["pole_y"]
    r = p["pole_d"] / 2
    zi = p["pole_z"] + (r + p["liner_t"]) * R2       # inside apex of the inverted steel V
    t = p["v_t"] * R2
    h = 34.0
    poly = [(yp - h, zi - h), (yp, zi), (yp + h, zi - h), (yp + h, zi - h + t), (yp, zi + t), (yp - h, zi - h + t)]
    sad = prism_x(poly, x - 40, x + 40)
    bx, by, bz = lever_bar_axis(p)
    bar = tube((x - 55, by, bz), (x + 55, by, bz), 22.2, 1.6)
    lin_poly = [(yp - h + 1, zi - h + 1 - p["liner_t"] * R2), (yp, zi - p["liner_t"] * R2), (yp + h - 1, zi - h + 1 - p["liner_t"] * R2),
                (yp + h - 1, zi - h + 1), (yp, zi), (yp - h + 1, zi - h + 1)]
    liner = prism_x(lin_poly, x - 38, x + 38)
    straps = [ring_band(x + k * 28, yp, p["pole_z"], r, 1.5, 20.0) for k in (1, -1)]
    return {"mount": sad + bar, "liner": liner, "straps": Compound(straps)}


# ---------------------------------------------------------------- soft goods
def cross_strap(p=PARAMS):
    r = p["pole_d"] / 2
    zb = p["pole_z"] - r - p["web_t"]
    band = Pos(0, 0, zb + p["web_t"] / 2) * Box(p["web_w"], 2 * p["pole_y"], p["web_t"])
    loops = [ring_band(0, s * p["pole_y"], p["pole_z"], r, p["web_t"], p["web_w"]) for s in (1, -1)]
    buckle = Pos(0, 90, zb - 6) * Box(56, 40, 12)
    s = band + loops[0] + loops[1]
    return Compound([s, buckle])


def patient_straps(p=PARAMS):
    r = p["pole_d"] / 2
    zt = p["pole_z"] + r
    out = []
    for xs in p["patient_straps_x"]:
        band = Pos(xs, 0, zt + p["web_t"] / 2) * Box(p["web_w"], 2 * p["pole_y"], p["web_t"])
        loops = [ring_band(xs, s * p["pole_y"], p["pole_z"], r, p["web_t"], p["web_w"]) for s in (1, -1)]
        buckle = Pos(xs, 110, zt + p["web_t"] + 7) * Box(56, 45, 14)
        tab = Pos(xs, 150, zt + p["web_t"] + 3) * Box(30, 50, 3)
        out.append(Compound([band + loops[0] + loops[1], buckle, tab]))
    return out


def harness_loops(p=PARAMS):
    r = p["pole_d"] / 2
    out = []
    for xl in p["loop_x"]:
        for s in (1, -1):
            loop = ring_band(xl, s * p["pole_y"], p["pole_z"], r, 2.5, p["web_w"])
            sling = Pos(xl, s * p["pole_y"], p["pole_z"] + r + 2.5 + 60) * Box(p["web_w"], 3, 120)
            out.append(loop + sling)
    return out


def hold_back_strap(p=PARAMS):
    """Hold-back strap (decision 7A): two closed webbing end caps over the rear pole ends, so the pull
    bears on the end of each pole, two 25 mm legs to a steel ring, and a tail with a cam buckle to the
    rear (uphill) bearer's hip belt (tail drawn up to the bearer's side, belt not drawn)."""
    r = p["pole_d"] / 2
    x0 = p["pole_x"][0]
    t = 2.5
    caps, legs = [], []
    rx, ry, rz = p["hb_ring"]
    for s in (1, -1):
        y = s * p["pole_y"]
        sleeve = rod((x0, y, p["pole_z"]), (x0 + p["cap_len"], y, p["pole_z"]), r + t) - rod(
            (x0 - 1, y, p["pole_z"]), (x0 + p["cap_len"] + 1, y, p["pole_z"]), r)
        end = rod((x0 - t, y, p["pole_z"]), (x0, y, p["pole_z"]), r + t)
        caps.append(sleeve + end)
        legs.append(rod((x0 - t, y, p["pole_z"]), (rx + 14, ry + s * 8, rz), 3.0))
    ring = Pos(rx, ry, rz) * Rot(90, 0, 0) * Torus(14.0, 3.0)
    tail = rod((rx - 14, ry, rz), (rx - 14 - p["hb_tail"], ry, rz + 60), 3.0)
    buckle = Pos(rx - 14 - p["hb_tail"], ry, rz + 60) * Box(40, 30, 12)
    return {"caps": caps, "legs": Compound(legs + [ring, tail, buckle])}


def lift_handles(p=PARAMS):
    """Lift handles (decision 9A): a 40 mm webbing band sewn shut round each cross stub, with a hand
    loop hanging below. Front stub: left of centre; rear stub: right of centre (helpers on opposite
    sides of the doli)."""
    s = p["stub"][0]
    sz = p["stub_z"]
    w = p["handle_w"]
    t = 2.0
    out = []
    for xs, side in ((p["stub_x"], 1), (-p["stub_x"], -1)):
        y = side * p["handle_y"]
        band = Pos(xs, y, sz) * (Box(s + 2 * t, w, s + 2 * t) - Box(s, w + 2, s))
        zb = sz - s / 2 - t
        lw, lh = 70.0, p["handle_drop"]
        loop = Pos(xs, y, zb - lh / 2) * (Box(lw, w, lh) - Box(lw - 2 * t, w + 2, lh - 2 * t))
        # foam grip sleeve on the bottom of the loop (25 mm foam tube, drawn as a solid round)
        zg = zb - lh + 12.0
        grip = rod((xs - lw / 2 + t, y, zg), (xs + lw / 2 - t, y, zg), 12.0)
        out.append(band + loop + grip)
    return out


def harness_flat(p=PARAMS, origin=(0, 0, 0)):
    """One bearer harness laid flat (for the making sketch and the overview): hip belt, shoulder
    yoke, two slings with pole loops and cam buckles. X along the belt, Y up the back."""
    ox, oy, oz = origin
    t = 4.0
    belt = Pos(ox, oy, oz + t / 2) * Box(1000, 60, t)
    pad = Pos(ox, oy, oz + t + 5) * Box(320, 90, 10)
    straps = []
    for k in (1, -1):
        a = (ox + k * 90, oy + 30, oz + t / 2)
        b = (ox + k * 140, oy + 620, oz + t / 2)
        straps.append(Pos((a[0] + b[0]) / 2, (a[1] + b[1]) / 2, oz + t / 2) * Rot(0, 0, -k * math.degrees(math.atan2(50, 590))) * Box(55, 595, t))
        straps.append(Pos(ox + k * 140, oy + 560, oz + t + 6) * Box(80, 200, 12))   # shoulder pad
        straps.append(Pos(ox + k * 330, oy - 250, oz + t / 2) * Box(50, 500, t))     # sling
        straps.append(Pos(ox + k * 330, oy - 540, oz + t / 2) * Box(110, 80, t))     # pole loop, flat
        straps.append(Pos(ox + k * 330, oy - 40, oz + t + 5) * Box(56, 40, 10))      # cam buckle
    chest = Pos(ox, oy + 470, oz + t / 2) * Box(300, 40, t)
    return Compound([belt, pad, chest] + straps)


def bag(p=PARAMS, origin=(0, 0, 0)):
    ox, oy, oz = origin
    return Pos(ox, oy, oz + 140) * Box(620, 280, 280) - Pos(ox, oy, oz + 140) * Box(600, 260, 260)


def card(origin=(0, 0, 0)):
    ox, oy, oz = origin
    return Pos(ox, oy, oz + 1) * Box(297, 210, 2)


# ---------------------------------------------------------------- assembly
BOM = {  # key: (BOM line, name)
    "fork": (1, "Fork unit"),
    "arms": (2, "Side arms"),
    "jaws": (3, "Upper jaws"),
    "liners": (4, "Jaw liners"),
    "bolts": (5, "T-handle bolts and set screws"),
    "wheel": (6, "Wheel"),
    "brake": (7, "Disc brake set"),
    "mount": (8, "Lever mount"),
    "cross": (9, "Cross strap"),
    "patient": (10, "Patient straps"),
    "harness": (11, "Bearer harnesses"),
    "holdback": (16, "Hold-back strap"),
    "handles": (17, "Lift handles"),
}


def build_kit(p=PARAMS, d=None):
    """Every kit piece as lists of (label, shape). d: pole diameter the clamps are closed on."""
    d = d or p["pole_d"]
    out = {k: [] for k in BOM}
    out["fork"].append(("fork unit", fork_unit(p)))
    for xs, tag in ((p["stub_x"], "front"), (-p["stub_x"], "rear")):
        for side, st in ((1, "left"), (-1, "right")):
            out["arms"].append((f"arm {tag} {st}", side_arm(xs, side, p)))
            j, _ = upper_jaw(xs, side, p, d)
            out["jaws"].append((f"jaw {tag} {st}", j))
            lo, up = liners(xs, side, p, d)
            out["liners"].append((f"liner {tag} {st} lower", lo))
            out["liners"].append((f"liner {tag} {st} upper", up))
            for k, b in enumerate(clamp_bolts(xs, side, p, d)):
                out["bolts"].append((f"bolt {tag} {st} {'outer' if k == 0 else 'inner'}", b))
    for k, s in enumerate(set_screws(p)):
        out["bolts"].append((f"set screw {k + 1}", s))
    w = wheel(p)
    out["wheel"] = [("tyre", w["tyre"]), ("rim", w["rim"]), ("hub", w["hub"]), ("axle and nuts", w["axle"]),
                    ("spokes", w["spokes"])]
    b = brake(p)
    out["brake"] = [("rotor", b["rotor"]), ("caliper", b["caliper"]), ("lever", lever(p)), ("cable", cable(p))]
    m = lever_mount(p)
    out["mount"] = [("lever mount", m["mount"]), ("mount liner", m["liner"]), ("mount straps", m["straps"])]
    out["cross"] = [("cross strap", cross_strap(p))]
    out["patient"] = [(f"patient strap {k + 1}", s) for k, s in enumerate(patient_straps(p))]
    out["harness"] = [(f"harness pole loop {k + 1}", s) for k, s in enumerate(harness_loops(p))]
    hb = hold_back_strap(p)
    out["holdback"] = [("hold-back cap left", hb["caps"][0]), ("hold-back cap right", hb["caps"][1]),
                       ("hold-back legs ring and tail", hb["legs"])]
    out["handles"] = [(f"lift handle {tag}", s) for tag, s in zip(("front", "rear"), lift_handles(p))]
    return out


def build_components(p=PARAMS):
    k = build_kit(p)
    return {key: Compound([s for _, s in k[key]]) for key in k}


def context_compound(p=PARAMS):
    c = doli_context(p)
    return Compound(c["poles"] + c["sticks"] + [c["bed"]])


def frame_only(p=PARAMS, kit=None):
    """The steel and rubber that bolt together: fork unit, arms, jaws, liners, bolts."""
    k = kit or build_kit(p)
    return Compound([s for key in ("fork", "arms", "jaws", "liners", "bolts") for _, s in k[key]])


# ---------------------------------------------------------------- constructability checks
def _vol(a, b):
    try:
        r = a & b
        return r.volume if r is not None else 0.0
    except Exception:
        return float("nan")


def _dist(a, b):
    return a.distance_to(b)


def checks(p=PARAMS):
    """Return a list of (name, passed, detail). Overlap tolerance 1 mm3, contact tolerance 0.5 mm."""
    dd = derived(p)
    res = []

    def add(name, ok, detail=""):
        res.append((name, bool(ok), detail))

    doli = doli_context(p)
    poles = Compound(doli["poles"])
    k = build_kit(p)
    fork = k["fork"][0][1]
    w = dict(k["wheel"])
    wheel_all = Compound(list(w.values()))
    br = dict(k["brake"])
    # wheel in the fork
    for name, s in (("tyre", w["tyre"]), ("rim", w["rim"]), ("spokes", w["spokes"]), ("hub", w["hub"])):
        v = _vol(s, fork)
        add(f"wheel {name}: no overlap with the fork unit", v < 1.0, f"{v:.1f} mm3")
    gap = _dist(w["tyre"], fork)
    add("tyre clear of the fork unit by at least 15 mm (mud)", gap >= 15.0, f"{gap:.1f} mm")
    add("axle nuts bear on the dropout plates", _dist(w["axle and nuts"], fork) < 0.5 and _vol(w["axle and nuts"], fork) < 1.0,
        f"gap {_dist(w['axle and nuts'], fork):.2f} mm")
    add("tyre touches the ground and nothing else does", abs(wheel_all.bounding_box().min.Z) < 0.5,
        f"lowest point {wheel_all.bounding_box().min.Z:.1f} mm")
    # brake
    v = max(_vol(br["caliper"], br["rotor"]), _vol(br["caliper"], w["spokes"]), _vol(br["caliper"], w["rim"]))
    add("caliper straddles the rotor, clear of the spokes and rim", v < 1.0, f"{v:.1f} mm3")
    add("caliper sits on the left dropout plate's mount lobe", _dist(br["caliper"], fork) < 0.5 and _vol(br["caliper"], fork) < 1.0,
        f"gap {_dist(br['caliper'], fork):.2f} mm")
    v = max(_vol(br["rotor"], fork), _vol(br["rotor"], w["spokes"]))
    add("rotor clear of the fork unit and spokes", v < 1.0, f"{v:.1f} mm3")
    add("rotor on the hub", _dist(br["rotor"], w["hub"]) < 0.5, f"gap {_dist(br['rotor'], w['hub']):.2f} mm")
    low = min(fork.bounding_box().min.Z, br["caliper"].bounding_box().min.Z)
    add("ground clearance under the fork unit and caliper at least 150 mm", low >= 150.0, f"{low:.0f} mm")
    # arms in the stubs, saddles under the poles
    for name, arm in k["arms"]:
        v = _vol(arm, fork)
        add(f"{name}: slides in its stub without overlap", v < 1.0, f"{v:.1f} mm3")
        add(f"{name}: spigot bears in its stub (0.5 mm clearance)", _dist(arm, fork) < 0.6, f"gap {_dist(arm, fork):.2f} mm")
        v = _vol(arm, poles)
        add(f"{name}: no overlap with the pole", v < 1.0, f"{v:.1f} mm3")
        v = max(_vol(arm, w["tyre"]), _vol(arm, br["caliper"]))
        add(f"{name}: clear of the wheel and brake", v < 1.0, f"{v:.1f} mm3")
    add("spigot length inside the stub at 600 mm pole centres at least 60 mm", dd["insertion_min"] >= 60,
        f"{dd['insertion_min']:.1f} mm")
    add("gap between opposite spigots at 450 mm pole centres at least 10 mm", dd["spigot_gap_min"] >= 10,
        f"{dd['spigot_gap_min']:.1f} mm")
    for name, s in k["liners"]:
        add(f"{name}: touches the pole, no overlap", _dist(s, poles) < 0.5 and _vol(s, poles) < 1.0,
            f"gap {_dist(s, poles):.2f} mm")
    arms = Compound([s for _, s in k["arms"]])
    jaws = Compound([s for _, s in k["jaws"]])
    for name, s in k["liners"]:
        host = arms if "lower" in name else jaws
        add(f"{name}: seated in its V", _dist(s, host) < 0.5 and _vol(s, host) < 1.0, f"gap {_dist(s, host):.2f} mm")
    for name, s in k["bolts"]:
        if name.startswith("bolt"):
            v = max(_vol(s, poles), _vol(s, jaws), _vol(s, arms))
            add(f"{name}: passes the ears clear of the pole", v < 1.0 and _dist(s, poles) >= 2.0,
                f"{v:.1f} mm3, {_dist(s, poles):.1f} mm from the pole")
        else:
            v = max(_vol(s, fork), _vol(s, arms))
            add(f"{name}: through its welded nut onto the spigot", v < 1.0 and _dist(s, arms) < 0.6,
                f"{v:.1f} mm3, gap {_dist(s, arms):.2f} mm")
    # the clamp range: 40 and 80 mm poles
    for dp in (40.0, 80.0):
        q = dict(p, pole_d=dp, pole_z=p["pole_z"])
        za = v_apex(p)
        zc = za + (dp / 2 + p["liner_t"]) * R2
        pole = rod((p["stub_x"] - 100, p["pole_y"], zc), (p["stub_x"] + 100, p["pole_y"], zc), dp / 2)
        lo, up = liners(p["stub_x"], 1, p, dp)
        j, _ = upper_jaw(p["stub_x"], 1, p, dp)
        arm = side_arm(p["stub_x"], 1, p)
        bolts = Compound(clamp_bolts(p["stub_x"], 1, p, dp))
        ok = _dist(lo, pole) < 0.5 and _dist(up, pole) < 0.5 and max(_vol(lo, pole), _vol(up, pole), _vol(j, arm)) < 1.0
        ok = ok and _dist(bolts, pole) >= 2.0 and _dist(j, arm) >= 2.0
        add(f"clamp closes on a {dp:.0f} mm pole: liners touch, jaw clear of the saddle, bolts clear",
            ok, f"jaw to saddle {_dist(j, arm):.1f} mm, bolts to pole {_dist(bolts, pole):.1f} mm")
        del q
    # lever mount
    m = dict(k["mount"])
    add("lever mount liner sits on the pole", _dist(m["mount liner"], poles) < 0.5 and _vol(m["mount liner"], poles) < 1.0,
        f"gap {_dist(m['mount liner'], poles):.2f} mm")
    add("lever mount sits on its liner", _dist(m["lever mount"], m["mount liner"]) < 0.5, "")
    add("lever clamped on the bar stub", _dist(br["lever"], m["lever mount"]) < 0.6 and _vol(br["lever"], m["lever mount"]) < 1.0, "")
    add("mount straps round the pole", _dist(m["mount straps"], poles) < 0.5 and _vol(m["mount straps"], poles) < 1.0, "")
    # straps
    cs = k["cross"][0][1]
    gap = _dist(cs, w["tyre"])
    add("cross strap round both poles", _dist(cs, poles) < 0.5 and _vol(cs, poles) < 1.0, "")
    add("cross strap at least 100 mm above the tyre", gap >= 100.0, f"{gap:.0f} mm")
    gap = _dist(doli["bed"], w["tyre"])
    add("bed clear of the tyre by at least 100 mm", gap >= 100.0, f"{gap:.0f} mm")
    frame = Compound([fork, arms, jaws])
    for name, s in k["patient"]:
        v = max(_vol(s, frame), _vol(s, Compound(doli["sticks"])))
        add(f"{name}: round both poles, clear of the clamps and cross sticks", v < 1.0 and _dist(s, poles) < 0.5, f"{v:.1f} mm3")
    for name, s in k["harness"]:
        add(f"{name}: on the pole end", _dist(s, poles) < 0.5 and _vol(s, poles) < 1.0, "")
    # hold-back strap (decision 7A)
    hb = dict(k["holdback"])
    sticks = Compound(doli["sticks"])
    harn = Compound([s for _, s in k["harness"]])
    for side in ("left", "right"):
        cap = hb[f"hold-back cap {side}"]
        add(f"hold-back cap {side}: over the pole end, bearing on the end face, no overlap",
            _dist(cap, poles) < 0.5 and _vol(cap, poles) < 1.0, f"gap {_dist(cap, poles):.2f} mm")
        g = _dist(cap, harn)
        add(f"hold-back cap {side}: clear of the harness pole loop by at least 3 mm", g >= 3.0, f"{g:.1f} mm")
    legs = hb["hold-back legs ring and tail"]
    v = max(_vol(legs, poles), _vol(legs, sticks), _vol(legs, harn))
    add("hold-back legs, ring and tail clear of the poles, cross sticks and harness loops", v < 1.0, f"{v:.1f} mm3")
    add("hold-back legs joined to the caps", _dist(legs, Compound([hb["hold-back cap left"], hb["hold-back cap right"]])) < 0.5, "")
    # lift handles (decision 9A)
    sets = Compound([s for n, s in k["bolts"] if n.startswith("set")])
    for name, h in k["handles"]:
        add(f"{name}: sewn round its cross stub, no overlap with the fork unit",
            _dist(h, fork) < 0.5 and _vol(h, fork) < 1.0, f"gap {_dist(h, fork):.2f} mm")
        v = max(_vol(h, arms), _vol(h, sets), _vol(h, br["caliper"]), _vol(h, br["cable"]))
        add(f"{name}: clear of the arms, set screws and brake", v < 1.0, f"{v:.1f} mm3")
        g = _dist(h, w["tyre"])
        add(f"{name}: hand loop clear of the tyre by at least 15 mm", g >= 15.0, f"{g:.1f} mm")
        g = min(_dist(h, poles), _dist(h, doli["bed"]))
        add(f"{name}: room for a hand between the loop and the poles and bed (at least 100 mm)", g >= 100.0, f"{g:.0f} mm")
        low = h.bounding_box().min.Z
        add(f"{name}: at least 150 mm above the ground", low >= 150.0, f"{low:.0f} mm")
    # width over the clamps (R6)
    bb = Compound([frame_only(p, k), poles]).bounding_box()
    add("width over the clamps and poles at most 700 mm on the reference doli", bb.size.Y <= 700.0, f"{bb.size.Y:.0f} mm")
    return res


def export(p=PARAMS):
    step = ROOT / "cad" / "step"
    stl = ROOT / "cad" / "stl"
    step.mkdir(parents=True, exist_ok=True)
    stl.mkdir(parents=True, exist_ok=True)
    k = build_kit(p)
    kit = Compound([s for key in BOM for _, s in k[key]])
    export_step(Compound([kit, context_compound(p)]), str(step / "dolitrail-assembly.step"))
    export_step(kit, str(step / "dolitrail-kit.step"))
    export_step(context_compound(p), str(step / "reference-doli-context.step"))
    export_step(k["fork"][0][1], str(step / "fork-unit.step"))
    export_step(k["arms"][0][1], str(step / "side-arm.step"))
    export_step(k["jaws"][0][1], str(step / "upper-jaw.step"))
    export_step(lever_mount(p)["mount"], str(step / "lever-mount.step"))
    kw = dict(tolerance=0.2, angular_tolerance=0.3)
    export_stl(k["arms"][0][1], str(stl / "side-arm.stl"), **kw)
    export_stl(k["jaws"][0][1], str(stl / "upper-jaw.stl"), **kw)
    export_stl(k["liners"][0][1], str(stl / "jaw-liner-lower.stl"), **kw)
    export_stl(k["liners"][1][1], str(stl / "jaw-liner-upper.stl"), **kw)
    export_stl(lever_mount(p)["mount"], str(stl / "lever-mount.stl"), **kw)


if __name__ == "__main__":
    d = derived()
    print({k: (round(v, 2) if isinstance(v, float) else v) for k, v in d.items()})
    if "--check" in sys.argv:
        r = checks()
        for name, ok, det in r:
            if not ok:
                print("FAIL", name, det)
        print(f"{sum(ok for _, ok, _ in r)} of {len(r)} constructability checks pass")
    if "--export" in sys.argv:
        export()
        print("exported STEP and STL")
