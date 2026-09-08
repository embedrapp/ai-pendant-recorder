# AI Second Brain Pendant — Original Implementation Plan

## Current-state findings

- Start from the existing electronics-plus-firmware scaffold without replacing user files.
- Use the exact Seeed Studio XIAO ESP32S3 Sense (SKU 113991115) as the controller.
- Use the MAX98357A audio amplifier as the speaker driver; if no installable module package exists, author an exact local IC wrapper from the datasheet.
- Resolve exact battery, speaker, switch, connector, and enclosure dimensions before manufacturing claims.

## Confirmed decisions

- Firmware target: ESP32-S3 DevKitC-1-compatible PlatformIO environment, because the installed target catalog lacks an exact XIAO target.
- Audio: direct MAX98357AETE+T IC implementation.
- Initial mechanical concept: protected 3.7 V, 500 mAh LiPo envelope.

## Project configuration

- Repair `embedr.yaml` and `platformio.ini` to use the ESP32-S3-compatible environment.
- Preserve the existing project identity and scaffold.
- Add firmware configuration placeholders and documentation without committing credentials.

## PCB design

- Install the exact XIAO Sense component package.
- Create an exact local MAX98357AETE+T wrapper with verified pins, footprint, exposed pad, and datasheet provenance.
- Add the XIAO module, amplifier, bypass capacitors, I2S nets, speaker output, record button, battery input, shutdown circuitry, test points, and mechanical interfaces.
- Use two copper layers unless routing or return-path analysis proves that more are required.
- Document voltage, current, battery, GPIO, RF, microSD, camera, enclosure, and acceptance assumptions.

## Component resolution

Search and inspect exact records for:

- Wearable speaker.
- Slide switch.
- Battery connector.
- MOSFET or transistor.
- Protected LiPo battery.

Do not substitute generic headers for the named XIAO board, speaker, amplifier module, or other named assemblies. Keep unavailable or unresolved parts explicitly documented.

## Firmware

Implement maintainable ESP32-S3 firmware with:

- Separate recording and upload FreeRTOS tasks.
- Bounded queues or double buffers.
- 15-second WAV/PCM chunks stored on FAT microSD.
- Atomic file finalization and recovery scanning after power loss.
- Offline recording and bounded upload retries.
- Wi-Fi provisioning and reconnection.
- TLS API communication with credentials outside source control.
- Camera capture and image-upload support.
- Voice-question and text-to-speech response pipeline.
- Configurable assistant name, personality, language, and wake interaction.
- Optional Home Assistant REST or MQTT integration.
- Provider abstraction for ElevenLabs/OpenAI-compatible services.

## Backend and dashboard contract

Document or scaffold authenticated endpoints for:

- Live transcription.
- Recordings and chunk status.
- Topics, decisions, and action items.
- Meeting summaries.
- Meeting question answering.
- Image descriptions.
- Device state and configuration.

Prefer a persistent live-transcription transport over polling-only behavior. Keep provider credentials server-side and document authentication, retention, consent, and privacy responsibilities.

## Mechanical design

Create a parameterized enclosure with:

- Camera aperture.
- Microphone opening.
- Speaker grille.
- USB-C and microSD service access.
- Power switch and recording-button access.
- Magnetic clothing attachment.
- PCB standoffs and insertion/removal clearance.
- Battery cavity based on the 500 mAh placeholder envelope.

Mark battery, speaker, wall thickness, magnet, connector, and enclosure dimensions as assumptions until exact parts are selected.

## Validation sequence

1. Validate the project manifest and select the firmware target.
2. Synchronize PCB packages and dependencies.
3. Build the Zener source and inspect the exact netlist.
4. Generate the KiCad board.
5. Review placement visually and geometrically, including XIAO Sense stack clearance, antenna keepout, speaker/current-loop layout, battery access, and controls.
6. Route only after placement review; preserve valid copper.
7. Run ERC, DRC, and PDK-backed DFM checks.
8. Build firmware for the selected ESP32-S3-compatible environment.
9. Build and inspect the enclosure STEP revision.
10. Export and verify BOM, Gerbers, drills, and placement artifacts from one accepted board revision.

## Manufacturing-readiness limitations

Do not call the design manufacturing-ready until electrical, mechanical, firmware, placement, routing, DRC/DFM, and fabrication-export checks pass. Cloud APIs, image analysis, TTS, Home Assistant behavior, and microphone operation require configured services and physical hardware for runtime validation.