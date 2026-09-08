# Quiet pendant — DEVELOPMENT, not manufacturing release

**Exact-part selection:** See `../docs/pendant-parts-selection.md` for the proposed
500 mAh protected pack, wired speaker, side record switch, keyed connector split
and magnets. These require tray/seat/control changes; they are NOT incorporated
in CAD yet. Current `pendant.py` is camera-free; older camera-bore notes below
describe historical geometry.

**PCB update notice:** The carrier now has 15 footprints, a 28 x 70 mm chamfered
outline and four aligned mounting holes. This enclosure revision has NOT been
rebuilt against that board. Read `../docs/pcb-release-review.md` for current
conflicts: front-versus-side record actuation, connector tails over the cell,
module stack height and missing exact acoustic/antenna geometry. Historical
no-outline/no-hole statements below describe the enclosure's original build input.

Source: `pendant.py`; parameters and uncertainty register: `pendant.cad.json`.
Current successful revision: `rev-ec844702af50c0b20748c6d12a1ec81089e2805f71f6472f5c0b91bda5bc5e73`.
Source, parameters and PCB context were current at this build. Earlier box/single-shell
revisions were diagnostic builds, NOT finished designs.

## Form and modeled features

32 x 76 x 19.5 mm main body; 24 mm total including 3 mm clothing backer and
1.5 mm garment gap. Rounded 5 mm plan corners, intended matte charcoal PA12.
This is elongated, but NOT yet an aggressively thin wearable; exact stack metrology
and side-by-side rather than stacked battery placement are the next miniaturization gate.

Four separate solids: rear shell, front cover, removable battery tray, clothing backer.
The STEP preserves separate solids; named assembly hierarchy is not retained by the
current flattened-compound export workaround.

- Front camera bore: 6.6 mm with 8.2 mm shallow bezel.
- Microphone: 1.2 mm dedicated bore and underside gasket land; its X/Y are explicit
  provisional parameters, NOT aligned to a measured microphone location.
- Speaker: 0.9 mm dot grid at 1.6 mm pitch, over a 16 mm nominal speaker seat;
  underside locating ring includes a wire escape.
- Top USB opening, recessed right-side switch/button openings.
- microSD: lid-off service, deliberately no exposed dust-catching external slot.
- Four PCB standoffs and front screw channels, slip-fit cover skirt.
- Open-top LiPo tray, lead notch and strap slots. Nominal cell 20 x 34 x 4 mm;
  21 x 35 mm tray cavity, 0.6 mm tray floor. The battery is not modeled or selected.
- Four blind magnet pockets in each shell/backer; hidden backer lanyard tunnel.

## Proposed assembly, requiring prototype confirmation

1. Install magnet pairs with correct polarity and qualified retention/encapsulation.
2. Fit insulated cell in tray; use a non-compressive strap and route leads out the notch.
3. Lower tray into locators, then install carrier PCB onto standoffs. Keep underside
   components, solder points and battery wires outside the cell envelope.
4. Fit speaker rim gasket/adhesive retention and acoustically resistive grille mesh;
   connect speaker with enough service slack to lift the cover without tearing leads.
5. Fit a closed-cell mic gasket from the REAL microphone sound inlet to its dedicated
   cover land. Do not couple the mic to the common speaker cavity.
6. Verify camera lens depth/FOV, cable clearance and control travel before closing.
7. Fit cover and qualified small plastic-thread screws. Pilot bores are provisional;
   screw MPN, length, torque and cycle life are not released.

## Evidence and release blockers

Cloud build and STEP inspection succeeded: four shapes, inspectable solid geometry,
32 x 76 x 24 mm assembly bounds. A snapshot was generated, but no image pixels were
available to the agent for direct visual inspection. No whole-assembly interference,
minimum-wall analysis, acoustic validation, hardware fit or physical prototype tests
have passed. A successful solid check is NOT a manufacturing/fit check.

Canonical PCB context reports NO Edge.Cuts, NO mounting holes and unknown component
heights. Its fallback 100 x 80 bounds are NOT PCB intent. Existing components are not
inside this proposed mechanical coordinate system. No PCB source or placement was
changed in this mechanical pass. Proposed 27 x 67 carrier and mounting centers must
be reconciled with real footprints, hole-edge clearances, USB mating plane and RF layout.

Before release:

- Select exact protected cell, speaker, controls, magnets, fasteners and mating leads.
  Validate LiPo charging/power isolation and cell expansion per supplier; do not clamp
  a pouch cell or allow fastener tips to reach it.
- Fix exact XIAO Sense camera revision (OV2640 versus OV3660), installed orientation,
  mic inlet center and stack heights. Verify lens clearance and FOV at worst tolerance.
- Revise mic port to actual coordinates; select gasket height/compression and test
  speech response, grille attenuation, speaker leakage/feedback and clothing rub noise.
- Reserve the external antenna and coax bend envelope, away from magnets, cell,
  speaker metal and body; test worn RF performance. No RF pocket is verified yet.
- Validate screw/boss strength, lid skirt overlap, tray retention, insertion paths,
  USB plug overmold clearance, microSD extraction, button travel and strain relief.
- Soften exposed front/back perimeter edges with process-qualified edge radii; the
  present rounded outline alone does not remove every sharp perimeter edge.
- Confirm MJF/SLS service minimum features: 0.6 mm tray floor and fine grille may need
  thickening or secondary drilling. Injection molding needs a separate draft/tooling review.
- Verify magnet retention/holding force through representative clothing. Add implant
  warnings; use a breakaway neck cord, not an untested non-breakaway tether.
- Test skin temperature during recording, Wi-Fi upload, charging and playback; sweat,
  drop, snag, abrasion, chemical resistance and skin-contact finish. No IP rating claimed.
- Complete PCB components, placement, routing, ERC/DRC/DFM and same-revision exports.

No fabrication files should be ordered from this development concept.