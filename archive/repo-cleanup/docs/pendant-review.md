# Pendant revision: edge controls and restrained shell

Preserve 43-part electrical design, 1-cell battery, existing 3.3 V interfaces and two copper layers. No new parts or copper removal. Existing board is unrouted. All components are on FRONT (the module is at the bottom edge, not on bottom copper).

44 x 60 mm closed R3 board; target shell 49 x 65 mm. Four M2 mounts constrain corner radii. Retain PETG prototype process and 0.3 mm mating clearance. Existing 34 x 50 x 6 mm provisional cell and 15 mm Sense stack prevent an honestly ultra-thin case without changing hardware.

SW1 local +Y actuator rotated 90 degrees faces board +X; actuator tip at X122.0, exactly the right board edge. SW2 shifted to X117.4: outward actuator overhang intentional, outer pad center X120.7 retained inside X122 edge. D2/D3 unchanged at X79.2, Y90/94; top-emitting LEDs need front-directed light guides.

Acceptance: source build; explicit schematic positions and visual review; current-board screenshot; closed outline and pad clearances; fresh checks; cloud STEP solid and interference checks; assembled and cutaway images. Unknown heights, USB plug/port datums, button stroke/force, battery PCM/lead exit and motor identity remain measurement gates. Renderer collisions must not be described as a clean schematic.