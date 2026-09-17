# Quiet pendant — replacement design in progress

Previous work is preserved in `archives/mechanical-before-modular.zip`; ZIP integrity was checked successfully. PCB and electrical source were not modified.

## Current status
## Current compact rear-ESP candidate (supersedes historical revisions below)
- U1 flipped to B.Cu and shifted 3 mm left, source anchor (88.083,97) mm, rotation 0. Pad-number/net mapping preserved. J1/J3 remain rear mounted; other board components unchanged.
- Battery/tray center Y=9 mm (1 mm upward); motor center (12.5,-24) mm, beside ESP. USB opening center X=-3 mm, Z=-2.58 mm is provisional. Motor cradle slightly joins the inner right wall intentionally; motor body remains clear of that wall by nominal 0.75 mm.
- Front cover lowered 4 mm; current STEP bounds 40 × 79.8 × 18.2 mm including slider. Enclosure revision `rev-5bfa146ae82b8e02a2ed9a68973a25a035a045df491911c0914c57512a0f8da1` passed 16-solid inspection. Thickness reduction is modeled, not verified hardware fit.
- Detailed PCB import refreshed: `rev-e5b4bd063105068b56bc2dc3170dd18d19d85804549e1683afb48bbd70b0b6f9`, 75 solids; four unresolved models still listed in export log. Separate from enclosure assembly.
- Rear-layer screenshot reviewed: U1 at lower end, J1/J3 at upper end, no obvious boundary overlap. Lint/evaluation pass. Fresh ERC passes with 79 advice; DRC fails with 295 errors and 107 warnings; DFM passes. Board still has no tracks and 295 airwires.
- Antenna, actual component heights, plug clearance, motor harness, swelling/thermal margins, full interference checks and exact imported model alignment remain unverified. Do not manufacture. Backups: `archives/compact-rear-esp/`.

Detailed electronics work: `mechanical/imports/populated-pcb.step` was exported from the current KiCad board at origin (100,82). Import revision `rev-8831a2c1296695153a5db99631b558a2b02e5fcd0849c88e9f24c83989725f2d` passed solid inspection (75 solids). An initial export including pads exceeded the cloud output limit; retained as `populated-pcb-with-pads.step`; the successful import omits pad detail. MK1/U5/U3/J4 models failed resolution; components without model attachments also need coverage audit. Solid count is not component count. KiCad STEP substrate reports 1.53 mm versus context general thickness 1.62 mm: resolve stackup/copper datum before combined fit claims.

Enclosure revision `rev-45f04fa9d3b8330897c55c9e502fe36548ecc7f1f51fb86039f3fc81239f8697` adds a QX1027 maximum-envelope motor (D10.1 × 2.8 mm), provisional adhesive and rear-shell cradle at (0,-23). It passes 16-solid inspection. Source: archived m1-reference manifest cites QX drawing p9; exact purchased motor identity remains unverified. Stock leads previously recorded as 27 ±2 mm cannot span directly to J3 at Y33; a longer harness/splice is required, not yet modeled.

**Not yet a complete unified assembly:** detailed PCB is a separate imported design. Current documented cloud source contract supports either a generator or standalone STEP import, but does not document project STEP asset access/composition inside generators. Do not claim these models are merged. Wiring, mating plugs, antenna, exact fasteners and missing component models remain incomplete; full visual/interference checks are not performed.

Latest rounded-edge revision: `rev-dd4c058d619f6b4cd912a214ceafe78eeedb2c6028a4c96ea232415ae9614592`, built successfully with 14 solids, 40.4 × 80.2 × 22.2 mm. Added 1 mm front/rear exterior perimeter fillets while retaining 5 mm plan-view corners. Visual and interference review remain outstanding.

Wearing orientation reviewed: lanyard at +Y (upper end), ESP/USB at -Y (lower end), LED face toward +Z (outward), battery at -Z (toward wearer). ESP remains concealed behind the opaque front cover; it shares the PCB component side with the LEDs, but is not a visible enclosure feature. No PCB positions or sides changed, including J1/J3, following the latest request to leave placement unchanged. The reference image supplies styling inspiration only, never dimensions.

Cloud generation now succeeds: revision `rev-1c98ebbe336384207eaa3cfde102f646772768f8a58efb91052e5d43dfd30b42`. STEP inspection reports 14 solids and overall bounds 40.4 × 80.2 × 22.2 mm including the slider. STEP, interactive previews and snapshot were generated. This establishes solid geometry, not interference-free fit or manufacturing readiness.

Camera hardware, camera lid and camera aperture are explicitly out of scope. The front cover is the enclosure closure with an LED diffuser and record key, not a camera lid. Historical camera-related assets remain only in the preservation archive.

## Design intent
One assembled design with separately labelled rear chassis, front cover, removable battery sled, flush optical cassette, 25-well optical baffle, record key, standby slider, acoustic gasket, and reference envelopes. Nominal source-defined exterior is 40.2 × 80.2 × 22.2 mm before small actuator protrusions; this is not a measured STEP result. PA12 is a prototype process assumption, not a production decision.

PCB frame: actual 36 × 76 × 1.62 mm board, KiCad origin (100,82), X=KiCad X, Y=-KiCad Y, Z=board front. Four 2.2 mm mounting drills are present. Board SHA256: `3e52957dc9727d29010f24683fd51a6ffb657d00eb5b7edb2c28d70e766c7b87`.

## Unfinished engineering — do not fabricate
- Inspect the generated assembly visually and complete geometric acceptance beyond solid validity.
- Verify battery identity and full cell/PCM/lead dimensions; current battery envelope is provisional, not a verified drawing extraction.
- Verify microSD insertion direction from the exact socket drawing. Current left opening and simplified socket reference are NOT validated against its overhanging courtyard.
- Verify USB mating face, plug overmold reach and height, switch actuation direction/travel, and mated JST cable routing.
- Complete separate PCB carrier, positive battery retention, optical cassette retention, captured controls, fastener selection and screw bodies, motor cradle and lead path. Current mounting pillars alone are not a modular carrier.
- BMI270 is an inertial sensor and ordinarily needs no exterior aperture. Confirm whether another externally exposed sensor was intended.
- Retain charging access in both slider positions. CAD cannot establish switched-supply or GPIO-backfeed behavior; electrical/firmware verification remains separate.
- Perform pairwise interference, tolerance, tool-access, removal-path and enclosure closure checks; inspect current-revision renders and export STEP only after success.

Proposed service sequence: remove rear screws, lift front cover and optical module, unplug battery, lift PCB/carrier, then remove battery sled without peeling adhesive from the cell. This sequence remains to be validated geometrically. No fit, sealing, strength, charging safety or manufacturing readiness is claimed.