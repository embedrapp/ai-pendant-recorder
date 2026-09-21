# Pendant enclosure

The maintained enclosure is generated from `pendant.py` using `pendant.cad.json`. It consumes the current board at `pcb/layout/layout.kicad_pcb`.

## Current geometry

Fresh cloud build and STEP inspection succeeded at revision `rev-db67b8b5fdb57ca66d4f7f5087f22955316bc1564d08ab42042626d73e8636f6`:

- 16 valid solids;
- overall measured bounds: 40 × 87.785 × 18.2 mm, including the lanyard loop;
- PCB frame: 36 × 76 × 1.62 mm with four 2.2 mm mounting holes;
- wearing orientation: lanyard at +Y, USB at -Y, LED face at +Z, and battery side at -Z.

The assembly includes the rear chassis, front cover, removable battery sled, optical cassette, 25-well optical baffle, record key, standby slider, acoustic gasket, and component reference envelopes. The detailed KiCad PCB STEP remains available as the separate `populated-pcb` mechanical design.

## Design assumptions

- PA12 additive manufacture is the current prototype process assumption.
- Battery envelope is 30.1 × 36 × 5.1 mm with 6.1 mm reserved thickness.
- USB and switch heights, mated connector/cable bends, antenna volume, exact motor package, and fastener selection are not yet established from complete manufacturer geometry.
- Four rear-access M2-class clearance bores and 1.6 mm blind pilot holes are modeled; screw length and pilot fit need a physical trial.

## Remaining fit validation

- Verify battery identity, swelling allowance, PCM and lead dimensions.
- Verify microSD insertion direction and the full card/finger access envelope.
- Verify USB plug overmold reach, switch travel, JST cable routing, and antenna clearance.
- Add or verify missing component 3D models and exact component heights.
- Check pairwise interference, tolerances, tool access, removal paths, enclosure closure, sealing, pull strength, and fatigue.
- Prototype the enclosure and perform an assembled hardware fit check.

A valid STEP build establishes solid geometry and measured bounds; it does not by itself establish tolerance, strength, sealing, or physical fit.
