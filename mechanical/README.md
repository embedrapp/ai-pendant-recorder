# Quiet pendant — replacement design in progress

Previous work is preserved in `archives/mechanical-before-modular.zip`; ZIP integrity was checked successfully. PCB and electrical source were not modified.

## Current status
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