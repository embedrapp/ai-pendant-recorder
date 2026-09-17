# AI Second Brain Pendant — Updated Product Plan

This file records the current product direction. It supersedes the original
camera-based XIAO ESP32S3 Sense-stack concept. Existing PCB, firmware, and
mechanical artifacts still represent earlier revisions in places; this plan is
not evidence that the redesign has been implemented or validated.

## Product goal

Build a thin, tall, narrow wearable audio recorder centered on:

- High-quality voice capture.
- Reliable local storage.
- USB-C programming and single-cell LiPo charging through the controller board.
- Battery percentage reporting.
- Motion/context sensing.
- Optional local speaker playback and haptic feedback.

The camera is no longer a requirement. Remove the camera, camera connector,
camera apertures, privacy shutter, camera power rails, image capture firmware,
and image-upload backend requirements.

## Confirmed architecture

- Use the **base Seeed Studio XIAO ESP32S3 board**, without the Sense camera/SD
  expansion board.
- Preserve the XIAO's working ESP32-S3, flash/PSRAM, USB-C programming, onboard
  LiPo charger, boot/reset circuitry, and Wi-Fi/BLE antenna implementation.
- Create a thin custom carrier PCB that reproduces only the functions needed by
  this product: digital microphone, storage, sensors, indicators, audio, and
  haptics.
- Do not mount the XIAO on pin headers. Use low-profile direct soldering or a
  recessed/cutout arrangement after verifying accessible pads and assembly
  clearances.
- Keep the battery, XIAO, speaker, and motor in separate XY regions where
  possible. Do not stack the PCB or tall components over the LiPo pouch.
- Keep the speaker and vibration motor for the first integrated prototype;
  remove either only if measured fit, runtime, acoustic, or peak-current results
  require it.

## Controller and USB

- Confirm the exact orderable base-XIAO part identity and its current schematic,
  pad map, dimensions, and antenna requirements before changing the PCB source.
- Use the XIAO USB-C connector for both programming and charging.
- Retain access to boot/reset and provide production test points where practical.
- Do not drive USB VBUS from another 5 V source.
- Treat the onboard charger as a simple charger, not a full power-path manager.
  Measure whether the system can operate and charge acceptably at the same time.
- If authoritative charge/full/fault reporting becomes mandatory, a later
  revision may need a dedicated charger/power-path IC with status outputs.

## Audio capture

- Select an exact low-profile digital PDM MEMS microphone intended for voice:
  target at least 65 dBA SNR, preferably 68–70 dBA, high acoustic-overload
  capability, low sleep current, and 1.8–3.3 V operation.
- Do not automatically reuse the Sense-board microphone. Compare exact,
  procurable candidates using indexed manufacturer datasheets and install the
  chosen component with a verified symbol, footprint, and acoustic-port data.
- Start with one microphone. Add a second only if beamforming/noise-rejection
  requirements justify the extra spacing, power, DSP, and acoustic validation.
- Give the microphone a short dedicated sound port, perimeter gasket, and dust
  mesh. Keep it away from the speaker, motor, buttons, USB opening, switching
  currents, and enclosure leakage paths.
- Validate microphone SNR, clipping, self-noise, mechanical noise, and speech
  intelligibility on assembled hardware; schematic checks cannot validate
  acoustic performance.

## Storage

- Put a low-profile microSD socket and its required support circuitry directly
  on the custom carrier.
- Verify the exact GPIO mapping and bus sharing against the base XIAO schematic;
  do not infer mappings from Arduino aliases or the removed Sense expansion.
- Keep FAT storage, atomic file finalization, recovery scanning, and buffered
  writes.
- Prefer batched, aligned writes to reduce latency and energy use.
- Reconsider soldered flash/eMMC only if removable storage is unnecessary and
  the microSD socket becomes a thickness or reliability blocker.

## Sensors and user interfaces

- Retain the **MAX17048** for LiPo voltage and state-of-charge percentage over
  I2C. Its charge-rate estimate may indicate probable charging but is not an
  authoritative charger-status signal.
- Retain the **BMI270** for motion, wear/activity context, and wake behavior;
  use its low-power modes when possible.
- Consider a battery NTC/ADC input if the final pack exposes a documented
  thermistor.
- Retain physical record and standby controls. Do not add capacitive touch.
- Use subtle, low-current status indication. Prefer direct MCU control or a
  smaller LED solution over the PCA9685 unless the final channel count truly
  requires that device.
- Retain MAX98357A-based differential speaker drive only with a verified speaker,
  explicit gain/power limits, shutdown control, and acoustic design.
- Retain the MOSFET-driven haptic motor with gate pulldown, flyback protection,
  and a source rated for measured start/stall current. Never drive it directly
  from a GPIO.

## Battery direction

Battery selection remains open and must be based on a finished protected-pack
drawing, not the nominal pouch size code alone.

For a tall, narrow product, search for a traceable 1S LiPo pack with:

- Approximately 300–500 mAh, subject to measured runtime.
- Finished width preferably 11–18 mm.
- Finished thickness preferably no more than 4–5.5 mm.
- Length selected around the tall enclosure, approximately 45–65 mm.
- Integrated PCM or a separately designed protection circuit.
- 4.20 V charge compatibility with a documented allowed charge current.
- At least 500 mA continuous discharge and a documented higher pulse rating, or
  measured limits that support enforced load scheduling.
- Preferably a 10 kΩ NTC, plus IEC 62133/IS 16046 and UN38.3 evidence for the
  exact pack.

The WLY601145 300 mAh pack may be used for an early narrow prototype, but its
finished maximum envelope is approximately 6.5 × 11.5 × 47.5 mm. It therefore
implies a thicker enclosure and is not the preferred final thin-pack choice.
Do not accept unverified high-capacity marketplace claims without a manufacturer
datasheet, finished dimensions, protection details, and discharge test results.

Before schematic freeze, calculate and then measure simultaneous peak demand
from ESP32 radio activity, SD writes, speaker output, and motor startup. If the
pack cannot support overlapping peaks, enforce load scheduling in firmware and
document those prohibited combinations.

## Power and runtime strategy

Removing an inactive camera mainly improves thickness and removes unused rails;
the largest runtime gains must come from power management:

1. Keep Wi-Fi off during ordinary recording and batch uploads later.
2. Shut down the speaker amplifier except during playback.
3. Enable the motor rail only for short haptic events.
4. Run the BMI270 and microphone in the lowest modes compatible with behavior.
5. Turn indicators off quickly and use low PWM current.
6. Buffer microSD writes rather than issuing frequent small transactions.
7. Reduce ESP32 clock/peripheral activity when workload permits.
8. Use deep sleep when the product is neither recording nor synchronizing.

Create an operating-state current budget for off, standby, recording, playback,
haptic, upload, and USB-connected operation. Capacity and runtime claims require
bench measurements on the assembled prototype.

## Firmware plan

- Use the managed `seeed_xiao_esp32s3` target and preserve credentials outside
  source control.
- Separate recording and upload work with bounded buffers/queues.
- Store recoverable WAV/PCM chunks and finalize files atomically.
- Support offline recording, bounded upload retries, provisioning, TLS, and
  reconnection.
- Read MAX17048 voltage/SOC and expose a clearly qualified probable-charging
  state only when supported by USB presence and charge-rate evidence.
- Use BMI270 interrupts/low-power modes for context and wake behavior.
- Add explicit power-state control for microphone, SD, amplifier, motor, LEDs,
  and radio where hardware permits.
- Remove camera initialization, capture, image upload, image-description, and
  camera privacy-control code and configuration.
- Retain voice-question/TTS and optional Home Assistant integration only as
  secondary features behind stable recording and storage.

## Mechanical direction

- Target a smooth, tall, narrow pendant rather than widening around a large
  battery.
- Begin with a 0.8 mm carrier PCB and a recessed/direct-mounted base XIAO.
- Align the XIAO USB-C connector with an enclosure opening.
- Reserve the full antenna body and feed geometry against a plastic wall, away
  from battery, copper, speaker magnet, motor, and metal attachment hardware.
- Provide microphone port/gasket/mesh, speaker grille, microSD service access,
  physical controls, and a reinforced external attachment loop.
- Keep the battery in its own supported cavity with swelling allowance, wire
  strain relief, insulation, and no sharp or compressive features.
- Use exact maximum component and pack envelopes before accepting enclosure
  width, length, or thickness. An 8 mm finished thickness is not assumed.

## PCB redesign sequence

1. Preserve the existing board and source as the prior prototype revision.
2. Confirm the exact base XIAO schematic, dimensions, pads, USB, charging, and
   antenna constraints.
3. Select and datasheet-verify the microphone, microSD socket, battery, speaker,
   motor, controls, and all exact footprints.
4. Revise the Zener source to remove the Sense/camera expansion and camera-only
   circuitry, then add the custom microphone/storage interfaces.
5. Reassess GPIO allocation, boot straps, shared buses, startup states, I2C
   pull-ups, decoupling, shutdowns, and test points.
6. Build and inspect the exact netlist; perform a fresh datasheet pin/strap and
   electrical-limit review.
7. Create a new board revision rather than destroying the existing routed
   artifact. Review mechanical anchors, antenna keepout, acoustic zones, battery
   cavity, connector access, and current loops before routing.
8. Route and review return paths, power integrity, SD and PDM signals, audio
   current loops, motor noise, and RF clearances.

## Acceptance and validation

The revised product is not ready until all applicable evidence is complete:

1. Manifest and firmware-target validation.
2. Zener build, exact netlist inspection, and independent ERC.
3. Datasheet-grounded review of every IC and selected pack.
4. Verified symbols, pad numbering, footprints, and package dimensions.
5. Whole-board placement review, routing review, DRC, and DFM.
6. Firmware build plus hardware tests for recording, file recovery, upload,
   battery reporting, controls, sensor behavior, speaker, and haptics.
7. Current and runtime measurements in every operating state, including USB
   charging while operating.
8. Microphone acoustic testing in the final enclosure.
9. Enclosure STEP inspection with battery swelling, antenna, USB, microSD,
   acoustic, control, and assembly clearances.
10. Fabrication and assembly exports generated from one accepted revision.

Cloud services, RF range, acoustic quality, battery safety, charging behavior,
and real runtime require physical hardware validation; successful source builds
or schematic checks alone do not establish them.