"""DoliTrail product appearance model (build123d), TRL 3, constructable design (DLT-DDR-002).

Finished-product look for photoreal renders, built from the constructable model: every kit piece of
cad/src/model.py build_kit() is used as it is (fork unit, side arms, jaws, liners, T-bolts, wheel,
disc brake, lever mount, cross strap, patient straps, harness pole loops), fitted to the reference
doli of model.doli_context(). Only the look is added, as recorded in docs/REVIEW.md: bamboo and cloth
colours for the family's doli, and a 1.75 m mannequin standing beside the doli on its far side for
scale (never between the camera and the product). The detail view repeats the front right clamp
with a cut length of pole. APPEARANCE MODEL ONLY. CONCEPT, NOT FOR FABRICATION.

Axes as model.py: X forward along the doli, Y to the left, Z up from the ground.
Groups: "shell" (kit seen from outside), "internal" (none), "context" (doli, mannequin),
"detail" (the detail view only).
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE), str(HERE.parents[1] / ".kit")]

from build123d import Box, Compound, Pos  # noqa: E402
import model as M  # noqa: E402

TITLE = "DoliTrail: clamp-on braked wheel and harness kit for a bamboo stretcher"

RENDER_VIEWS = [
    {"name": "hero", "groups": ["shell", "internal", "context"], "explode": False, "el": 24, "az": -35,
     "note": "Product render from the front right and above (about 24 deg elevation): the kit clamped under the "
             "reference bamboo doli, 20 inch wheel under the patient's hips, brake lever on the front right pole, "
             "patient straps and harness pole loops; 1.75 m person standing beside the doli on its far side for scale"},
    {"name": "exploded", "groups": ["shell", "internal"], "explode": True, "el": 24, "az": -35,
     "note": "Exploded view from the front right and above (about 24 deg elevation): side arms, liners, jaws and "
             "T-bolts lifted off the fork unit, wheel and brake dropped below it; doli not shown"},
    {"name": "detail", "groups": ["detail"], "explode": False, "el": 18, "az": -50,
     "note": "Detail of the front right pole clamp from the front right and above (about 18 deg elevation): the "
             "bamboo pole in the rubber-lined steel V saddle, the upper jaw and two T-handle bolts, the side arm "
             "sliding into the cross stub and its set screw"},
]

C_STEEL_PAINT = "#0F5E58"
C_ARM = "#1E4E63"
C_ZINC = "#B8BEC6"
C_RUBBER = "#1F1F1F"
C_TYRE = "#232323"
C_RIM = "#B5B9BE"
C_ROTOR = "#C9CDD2"
C_CALIPER = "#2B2B2B"
C_WEB_ORANGE = "#E2621B"
C_WEB_RED = "#B91C1C"
C_HARNESS = "#C2410C"
C_BAMBOO = "#C9A465"
C_CLOTH = "#B7C4C9"
C_CLAY = "#B9B4AC"


def product_parts(p=M.PARAMS):
    k = M.build_kit(p)
    c = M.doli_context(p)
    w = dict(k["wheel"])
    b = dict(k["brake"])
    out = []

    def add(name, shape, color, material, bom, group, explode=(0, 0, 0)):
        out.append({"name": name, "shape": shape, "color": color, "material": material, "bom": bom,
                    "group": group, "explode": tuple(explode)})

    allk = lambda key: Compound([s for _, s in k[key]])  # noqa: E731
    add("Fork unit, painted steel", k["fork"][0][1].fix(), C_STEEL_PAINT, "painted", 1, "shell")
    add("Side arms, painted steel", allk("arms"), C_ARM, "painted", 2, "shell", (0, 0, 250))
    add("Upper jaws, painted steel", allk("jaws"), C_ARM, "painted", 3, "shell", (0, 0, 550))
    add("Jaw liners, rubber", allk("liners"), C_RUBBER, "rubber", 4, "shell", (0, 0, 420))
    add("T-handle bolts and set screws, zinc", allk("bolts"), C_ZINC, "metal", 5, "shell", (0, 0, 750))
    add("Tyre", w["tyre"], C_TYRE, "rubber", 6, "shell", (0, 0, -450))
    add("Rim, hub, axle and spokes", Compound([w["rim"], w["hub"], w["axle and nuts"], w["spokes"]]), C_RIM, "metal", 6,
        "shell", (0, 0, -450))
    add("Brake rotor", b["rotor"], C_ROTOR, "metal", 7, "shell", (0, -250, -450))
    add("Brake caliper", b["caliper"], C_CALIPER, "painted", 7, "shell", (0, -250, -450))
    add("Brake lever and cable", Compound([b["lever"], b["cable"]]), C_CALIPER, "painted", 7, "shell", (0, 0, 300))
    add("Lever mount", allk("mount"), C_ARM, "painted", 8, "shell", (0, 0, 200))
    add("Cross strap, webbing", allk("cross"), C_WEB_ORANGE, "fabric", 9, "shell", (0, 0, 650))
    add("Patient straps, webbing", allk("patient"), C_WEB_RED, "fabric", 10, "shell", (0, 0, 500))
    add("Bearer harness pole loops", allk("harness"), C_HARNESS, "fabric", 11, "shell", (0, 0, 400))
    add("Lift handles, webbing", allk("handles"), C_HARNESS, "fabric", 16, "shell", (0, 0, -300))
    add("Hold-back strap loops, webbing", allk("holdback"), C_WEB_ORANGE, "fabric", 17, "shell", (-250, 0, 300))
    add("Bamboo poles and cross sticks (the family's doli)", Compound(c["poles"] + c["sticks"]), C_BAMBOO, "wood", None, "context")
    add("Cloth bed (the family's doli)", c["bed"], C_CLOTH, "fabric", None, "context")
    from context_parts import mannequin
    person = Pos(700, 1050, 0) * mannequin(1750, "stand")     # far side of the doli, facing the camera
    add("Person, 1.75 m (scale), standing beside the doli", person, C_CLAY, "clay", None, "context")
    # detail: front right clamp with a cut length of pole and the stub end
    xs, yp = p["stub_x"], -p["pole_y"]
    win = Pos(xs, yp + 40, 640) * Box(260, 330, 300)
    pick = lambda key: Compound([s for n, s in k[key] if "front" in n.split() and "right" in n.split()])  # noqa: E731
    add("Detail: pole", Compound(c["poles"]) & win, C_BAMBOO, "wood", None, "detail")
    add("Detail: fork unit stub", (k["fork"][0][1] & win).fix(), C_STEEL_PAINT, "painted", 1, "detail")
    add("Detail: side arm", pick("arms"), C_ARM, "painted", 2, "detail")
    add("Detail: upper jaw", pick("jaws"), C_ARM, "painted", 3, "detail")
    add("Detail: liners", pick("liners"), C_RUBBER, "rubber", 4, "detail")
    sel_b = Compound([s for n, s in k["bolts"] if ("front" in n.split() and "right" in n.split()) or n == "set screw 2"])
    add("Detail: T-bolts and set screw", sel_b, C_ZINC, "metal", 5, "detail")
    return out


if __name__ == "__main__":
    for q in product_parts():
        s = q["shape"]
        print(f"{q['name']:55s} {q['group']:8s} {q['material']:8s} vol={s.volume / 1000:10.1f} cm3")
