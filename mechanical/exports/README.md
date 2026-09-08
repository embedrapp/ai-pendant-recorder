# Fit-prototype STEP — NOT a print/manufacturing release

`pendant-fit-prototype.step` is the verified download of cloud revision
`rev-2bb8bd148f702798fa68bb3c0a29be70159b11d2553938bf927ad826dfe70c13`.
SHA256: `15ae5e8e897ff6b4f2ecbe6e9c12221407b1db2ff2e491846c019204b7b17a1d`.
Units: mm. Four shapes; body 32 x 76 x 22 mm, 26.5 mm overall including backer.
Import STEP into a STEP-capable slicer and separate bodies; do not print the
closed assembled arrangement. No STL/3MF or slicer verification was performed.

Changes: PCB R2 tangent corners preserving 28 x 70 bounds; enclosure bosses
read the four actual carrier mounting-hole centers; expanded 26 x 42 battery
tray cavity with end locators; rectangular 16.6 x 9.6 speaker seat and matching
dot field; record-switch opening follows its current board Y coordinate.

Validation: cloud solid inspection/build and verified STEP hash download;
PCB screenshot reviewed; fresh ERC passes, DFM reports pass, DRC retains
33 unrouted connections and 30 warnings. No routing was performed.

Release blockers: exact camera-free Sense stack/microphone inlet and antenna
envelope, battery maximum protected-pack dimensions/current limits, battery
protection from J1/SW2 tails, captive record plunger and travel stop, screw
selection/torque, speaker retention/gasket, assembly interference tests and
process-specific minimum-feature/mesh/slicer checks. PCB outline clearance
must be tested against the curved inner shell, not only rectangular bounds.
Mounting-center agreement alone does not prove the assembled PCB fits.

The earlier claim in docs/new-bom-routing-status.md that placement was ready
for final routing is superseded: mechanical/antenna constraints remain open.
Do not release or route as a production design until those constraints are
resolved. Firmware is unchanged.