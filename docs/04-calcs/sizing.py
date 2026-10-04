"""DoliTrail sizing calculations (DLT-CAL-001), on the constructable design of DLT-DDR-002 with
Amish's round-2 decisions of 2026-10-03 (6A, 7A, 8A, 9A; DLT-DDR-003).

Run from the repo root:  python docs/04-calcs/sizing.py
Prints every result with its tag and writes docs/04-calcs/results.csv. Sizes come from the
parametric model (cad/src/model.py), so the figures match the STEP files, drawings and build plan.
Screening estimates for a paper proof of concept; every figure is checked by test at TRL 4.
CONCEPT, NOT FOR FABRICATION.
"""
import csv
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "cad" / "src"))
import model as M  # noqa: E402

G = 9.81
P = M.PARAMS
D = M.derived(P)

# ---------------------------------------------------------------- assumptions (Table 1 of the note)
A = {
    "patient": 120.0,        # kg, rated patient (R3)
    "doli": 10.0,            # kg, reference doli: two 60 mm bamboo poles, two sticks, cloth and rope
    "cg_above_pole": 100.0,  # mm, patient and doli centre of mass above the pole centres
    "place_err": 100.0,      # mm, wheel placed under the patient's hips to within this
    "steady": 0.05,          # share of the rolling weight each bearer holds to steady the doli
    "grade": 0.30,           # R5 grade
    "mu_tyre_mud": 0.35,     # knobbly tyre on wet clay or mud (estimate)
    "mu_tyre_ramp": 0.60,    # tyre on a wet timber or concrete test ramp
    "mu_pad_wet": 0.35,      # sintered pads, wet
    "pad_force": 2000.0,     # N per pad at about 150 N hand pull on the locked lever (to confirm)
    "mu_rubber": 0.35,       # rubber liner on wet bamboo
    "clamp_force": 2000.0,   # N per clamp (two bolts at 1.0 kN, hand tight with the T-handles)
    "crush": 4000.0,         # N, diametral capacity of a 40 mm length of 60 mm culm in V jaws (to confirm)
    "lateral": 0.30,         # lateral force at the tyre as a share of the wheel load (side slope, roots)
    "margin": 2.0,           # R3 margin applied to the rated load
    "fy": 210.0,             # MPa, yield of ERW mild steel tube (IS 1161 YSt 210)
    "E": 205000.0,           # MPa
    "wheel_rating": 200.0,   # kg, seller's rating of a 20 inch cargo or tricycle wheel (to confirm)
    "tyre_rating": 150.0,    # kg, 20 x 2.125 cargo tyre at maximum pressure (to confirm)
    "crr": 0.08,             # rolling resistance on a dirt trail
    "cross_slope": 0.15,     # side slope for the roll check
    "step": 400.0,           # mm, R8
    "step_clear": 50.0,      # mm, wheel clear of the step edge
    "carry_limit": 0.20,     # decision 7A: lift and carry on wet clay steeper than this grade
    "web25_break": 5000.0,   # N, 25 mm polyester webbing, typical breaking strength (to confirm)
    "web50_break": 10000.0,  # N, 50 mm polyester webbing, typical breaking strength (to confirm)
}

STEEL, RUBBER = 7850.0, 1300.0
BOUGHT = {  # kg each, typical catalogue masses (to confirm when bought)
    "wheel": 2.60,           # 36 x 2.0 mm spokes, double-wall alloy rim, steel disc hub, tyre and tube
    "brake": 0.81,           # rotor 0.18, caliper 0.32, lever with lock 0.16, cable and housing 0.15
    "cross": 0.15, "patient": 0.20, "harness": 0.75, "bag": 0.60, "card": 0.02, "ties": 0.04,
    "pump": 0.35,            # mini pump, tyre levers, patches, spare tube
    "mount_straps": 0.05,
    "holdback": 0.20,        # decision 7A: caps, legs, ring, tail and buckle
    "handle": 0.10,          # decision 9A: each, webbing band, loop and foam grip
    "parts_bag": 0.30,       # decision 8A: second bag
}


def masses():
    k = M.build_kit(P)
    vol = lambda key: sum(s.volume for _, s in k[key]) / 1e9  # noqa: E731
    m = {
        "fork": vol("fork") * STEEL,
        "arms": vol("arms") * STEEL,
        "jaws": vol("jaws") * STEEL,
        "liners": vol("liners") * RUBBER,
        "bolts": vol("bolts") * STEEL,
        "mount": M.lever_mount(P)["mount"].volume / 1e9 * STEEL + M.lever_mount(P)["liner"].volume / 1e9 * RUBBER
        + BOUGHT["mount_straps"],
        "wheel": BOUGHT["wheel"], "brake": BOUGHT["brake"], "cross": BOUGHT["cross"],
        "patient": 3 * BOUGHT["patient"], "harness": 2 * BOUGHT["harness"],
        "bag": BOUGHT["bag"], "card": BOUGHT["card"], "ties": BOUGHT["ties"], "pump": BOUGHT["pump"],
        "holdback": BOUGHT["holdback"], "handles": 2 * BOUGHT["handle"], "parts_bag": BOUGHT["parts_bag"],
    }
    on_doli = sum(m[x] for x in ("fork", "arms", "jaws", "liners", "bolts", "mount", "wheel", "brake", "cross", "patient",
                                 "handles"))
    m["kit"] = sum(v for x, v in m.items() if x not in ("kit",))
    m["on_doli"] = on_doli
    return m


def shs_z(b, t):
    return (b ** 4 - (b - 2 * t) ** 4) / (6 * b)


def tube_props(od, t):
    i = math.pi / 64 * (od ** 4 - (od - 2 * t) ** 4)
    a = math.pi / 4 * (od ** 2 - (od - 2 * t) ** 2)
    return a, i, i / (od / 2)


def run():
    R = []

    def out(tag, what, value, unit="", note=""):
        R.append({"tag": tag, "quantity": what, "value": value, "unit": unit, "note": note})
        v = f"{value:,.2f}" if isinstance(value, float) else str(value)
        print(f"[{tag}] {what}: {v} {unit} {note}".rstrip())

    m = masses()
    # ---------------------------------------------------------------- geometry
    out("G1", "Wheel diameter (20 x 2.125 tyre)", 2 * P["wheel_r"], "mm")
    out("G2", "Pole centres the clamps reach", f"{D['spacing_range'][0]:.0f} to {D['spacing_range'][1]:.0f}", "mm")
    out("G3", "Pole diameters the clamps close on", "40 to 80", "mm")
    out("G4", "Tyre contact below the pole centres (60 mm pole)", D["drop_below_poles"], "mm")
    out("G5", "Width over clamps, reference doli (550 mm centres)", D["width"], "mm")
    max_c = 2 * (350.0 - P["saddle"][1] / 2)
    out("G6", "Largest pole centres for a width of 700 mm", max_c, "mm")
    out("G7", "Spigot inside its stub at 600 mm centres", D["insertion_min"], "mm")
    # ---------------------------------------------------------------- masses (R7)
    for key, tag in (("fork", "K1"), ("arms", "K2"), ("jaws", "K3"), ("liners", "K4"), ("bolts", "K5"),
                     ("wheel", "K6"), ("brake", "K7"), ("mount", "K8"), ("harness", "K9")):
        out(tag, f"Mass, {M.BOM[key][1].lower()}", m[key], "kg")
    soft = m["cross"] + m["patient"] + m["bag"] + m["card"] + m["ties"] + m["pump"] + m["parts_bag"]
    out("K10", "Mass, straps, two bags, card, ties, pump and puncture kit", soft, "kg")
    out("K11", "Kit mass, everything in the two bags", m["kit"], "kg")
    out("K12", "Kit mass fitted to the doli (frame, wheel, brake, straps, lift handles)", m["on_doli"], "kg")
    bag_a = m["fork"] + m["handles"] + m["wheel"] + m["brake"] + m["pump"] + m["bag"]
    bag_b = m["kit"] - bag_a
    out("K13", "Wheel bag: fork unit with lift handles, wheel, brake, pump kit and bag (decision 8A)", bag_a, "kg")
    out("K14", "Parts bag: arms, jaws, bolts, lever mount, straps, harnesses, hold-back strap and bag", bag_b, "kg")
    out("K15", "Mass, hold-back strap; lift handles (two)", f"{m['holdback']:.2f}; {m['handles']:.2f}", "kg")
    # ---------------------------------------------------------------- loads (R3, R4)
    W = A["patient"] + A["doli"] + m["on_doli"]
    out("L1", "Rolling weight: rated patient, doli and fitted kit", W, "kg")
    af, ar = P["loop_x"][0], -P["loop_x"][1]
    out("L2", "Bearer loops ahead of and behind the wheel", f"{af:.0f} and {ar:.0f}", "mm")
    carry2 = (A["patient"] + A["doli"]) / 2
    carry4 = (A["patient"] + A["doli"]) / 4
    out("L3", "Carrying today: load per bearer, two bearers (four bearers)", f"{carry2:.1f} ({carry4:.1f})", "kg")
    pitch = W * A["place_err"] / min(af, ar)
    avg = (pitch + 2 * A["steady"] * W) / 2
    out("L4", "Level trail: pitch balance on the heavier end (100 mm placement error)", pitch, "kg")
    out("L5", "Level trail: average load per bearer with steadying allowance", avg, "kg")
    out("L6", "Reduction against carrying with two bearers (R4)", 100 * (1 - avg / carry2), "%")
    th = math.atan(A["grade"])
    H = P["pole_z"] + A["cg_above_pole"]
    down = W * math.sin(th) * H / af + pitch + A["steady"] * W
    out("L7", "30 % descent, brake on: downhill (front) bearer load", down, "kg", "estimate")
    crr = A["crr"] * W * G
    out("L8", "Level trail: pull to keep rolling, shared by two bearers", crr / 2, "N each", "estimate")
    roll_m = W * G * (H / 1000) * math.sin(math.atan(A["cross_slope"]))
    hand = roll_m / 2 / (2 * P["pole_y"] / 1000)
    out("L9", "15 % side slope: roll moment held by the bearers", roll_m, "N m")
    out("L10", "15 % side slope: up and down force at each bearer's hands", hand, "N", f"about {hand / G:.0f} kg")
    # ---------------------------------------------------------------- brake and grip (R5)
    F_slope = W * G * math.sin(th)
    T_need = F_slope * P["wheel_r"] / 1000
    r_eff = (P["rotor_r"] - 11.0) / 1000
    T_brake = 2 * A["mu_pad_wet"] * A["pad_force"] * r_eff
    out("B1", "Along-slope force on a 30 % grade, rated load", F_slope, "N")
    out("B2", "Brake torque needed at the wheel", T_need, "N m")
    out("B3", "Brake torque available, wet sintered pads, 203 mm rotor, lever locked", T_brake, "N m")
    out("B4", "Brake factor (available / needed)", T_brake / T_need)
    N_w = W * G * math.cos(th) - (W * math.sin(th) * H / af + pitch) * G
    grip_mud = A["mu_tyre_mud"] * N_w / F_slope
    grip_ramp = A["mu_tyre_ramp"] * N_w / F_slope
    out("B5", "Wheel load normal to the slope (bearer share taken off)", N_w, "N")
    out("B6", "Tyre grip factor on wet clay or mud (mu 0.35)", grip_mud)
    out("B7", "Tyre grip factor on a wet test ramp (mu 0.60)", grip_ramp)
    hold_back = max(0.0, F_slope - A["mu_tyre_mud"] * N_w) / G
    out("B8", "Shortfall on wet mud, to be held back by the uphill bearer", hold_back, "kg-force")
    # decision 7A: hold-back strap and the lift-and-carry rule on wet clay steeper than 20 per cent
    th2 = math.atan(A["carry_limit"])
    F2 = W * G * math.sin(th2)
    N2 = W * G * math.cos(th2) - (W * math.sin(th2) * H / af + pitch) * G
    out("B9", "Tyre grip factor on wet clay at the 20 % carry limit (rolling allowed up to here)", A["mu_tyre_mud"] * N2 / F2)
    out("B10", "Hold-back strap pull, 30 % wet clay, wheel at the grip limit", hold_back * G, "N",
        "the rule says carry here; shown for a patch met by surprise")
    out("B11", "Hold-back strap strength factor against the whole along-slope force on 30 %",
        2 * A["web25_break"] / F_slope, "", "two 25 mm legs; webbing strength to confirm")
    # ---------------------------------------------------------------- clamps (R1)
    f_clamp = A["mu_rubber"] * A["clamp_force"] * math.sqrt(2) * 2
    out("C1", "Slip resistance of one clamp along the pole (wet)", f_clamp, "N")
    out("C2", "Slip resistance of the two clamps on one pole", 2 * f_clamp, "N")
    out("C3", "Clamp factor against the 1.5 kN pull of R1, one pole", 2 * f_clamp / 1500.0)
    out("C4", "Bamboo crush factor at the clamp force", A["crush"] / A["clamp_force"], "", "to confirm on real poles")
    v_clamp = (A["patient"] + A["doli"]) * G / 4
    out("C5", "Vertical load on each saddle, rated load", v_clamp, "N")
    out("C6", "Braking pull per clamp on a 30 % grade", F_slope / 4, "N")
    # ---------------------------------------------------------------- structure at twice the rated load (R3)
    k2 = A["margin"]
    a_s, i_s, z_s = tube_props(*P["strut"])
    L_s = D["strut_len"]
    sin_a = (P["stub_z"] - P["stub"][0] / 2 - P["wheel_r"]) / L_s
    Wd = k2 * W * G
    ax = Wd / (4 * sin_a)
    lat = k2 * A["lateral"] * W * G
    m_bend = lat / 4 * (L_s / 1000) / 2
    push = lat * P["wheel_r"] / 1000 / (2 * P["strut_y"] / 1000) / 2 / sin_a
    s_strut = (ax + push) / a_s + m_bend * 1000 / z_s
    p_euler = math.pi ** 2 * A["E"] * i_s / L_s ** 2
    out("S1", "Strut axial load, twice the rated load", ax + push, "N")
    out("S2", "Strut stress, twice the rated load with the side load", s_strut, "MPa")
    out("S3", "Strut factor on yield at twice the rated load", A["fy"] / s_strut)
    out("S4", "Strut buckling factor at twice the rated load", p_euler / (ax + push))
    v2 = k2 * v_clamp
    m_stub = 2 * v2 * (P["pole_y"] - P["strut_y"]) / 1000      # two clamps per stub, one each side: per side
    m_stub = v2 * (P["pole_y"] - P["strut_y"]) / 1000
    s_stub = m_stub * 1000 / shs_z(*P["stub"])
    out("S5", "Stub bending stress at the strut, twice the rated load", s_stub, "MPa")
    m_sp = v2 * (P["pole_y"] - P["stub_len"] / 2) / 1000
    s_sp = m_sp * 1000 / shs_z(*P["arm"])
    out("S6", "Spigot bending stress at the stub end, twice the rated load", s_sp, "MPa")
    out("S7", "Lowest structural factor on yield at twice the rated load", A["fy"] / max(s_strut, s_stub, s_sp))
    out("S8", "Clamp bolt tension, each (two per clamp)", A["clamp_force"] / 2, "N", "M8 class 4.6 proof load about 8.4 kN")
    out("S9", "Wheel: seller's rating / twice the wheel load", A["wheel_rating"] / (k2 * W))
    out("S10", "Tyre: rating / twice the wheel load", A["tyre_rating"] / (k2 * W))
    out("S11", "Tyre: rating / the rated wheel load", A["tyre_rating"] / W)
    out("S12", "Wheel proof load before use, twice the rolling weight (decision 6A)", k2 * W, "kg")
    # ---------------------------------------------------------------- width, steps, fitting (R6, R8, R2)
    out("W1", "Overall width with wheel, reference doli (R6)", D["width"], "mm")
    rise = A["step"] + A["step_clear"]
    out("H1", "Rise of the poles at the wheel to clear a 400 mm step", rise, "mm")
    out("H2", "Pole height while the wheel clears the step", P["pole_z"] + rise, "mm")
    out("H3", "Lift per bearer, two bearers", W / 2, "kg")
    out("H4", "Lift per bearer, four bearers", W / 4, "kg")
    # decision 9A: two helpers lift at webbing handles on the cross stubs
    h_pull = W / 4 * G
    arm_h = (P["handle_y"] - P["strut_y"]) / 1000
    s_h = k2 * h_pull * arm_h * 1000 / shs_z(*P["stub"])
    out("H5", "Pull on each lift handle, four lifting", h_pull, "N")
    out("H6", "Stub bending at the strut from a handle, twice the handle pull", s_h, "MPa")
    out("H7", "Lift handle webbing strength factor (50 mm)", A["web50_break"] / h_pull)
    fit = [("Set the arms to the pole spacing and lock the set screws (wheel travels fitted in the fork unit)", 45),
           ("Raise the doli on two bearers' knees or blocks", 20), ("Slide the frame under, wheel under the hip mark", 30),
           ("Close four clamps (eight T-bolts, two people in parallel)", 80), ("Cross strap", 25),
           ("Lever mount and cable ties on the front pole", 50), ("Check: shake test and brake test", 30)]
    t = sum(s for _, s in fit)
    out("T1", "Fitting time, two people (estimate)", t / 60, "min")
    # ---------------------------------------------------------------- cost (R9)
    rows = list(csv.DictReader((ROOT / "bom" / "bom.csv").open()))
    cost = sum(float(r["qty"]) * float(r["unit_cost_usd"]) for r in rows)
    out("Q1", "Estimated cost of the constructable design", cost, "USD")
    out("Q2", "Against the value-engineering target of USD 1,500", cost - 1500.0, "USD", "negative = under")
    out("Q3", "Cross strap above the tyre", (P["pole_z"] - P["pole_d"] / 2 - P["web_t"]) - 2 * P["wheel_r"], "mm")
    return R, fit


if __name__ == "__main__":
    R, fit = run()
    with (ROOT / "docs" / "04-calcs" / "results.csv").open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["tag", "quantity", "value", "unit", "note"])
        w.writeheader()
        for r in R:
            r = dict(r)
            if isinstance(r["value"], float):
                r["value"] = f"{r['value']:.3f}"
            w.writerow(r)
    print("wrote docs/04-calcs/results.csv")
