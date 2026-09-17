# Implementation checkpoint — partial, not release-ready

Confirmed product: no camera, retain speaker/playback, microSD recording and
eventual BLE sync to Android/iPhone. No completed BLE receiver is claimed.

Implemented:
- Correct XIAO ESP32S3 target in manifest, PlatformIO and IDE selection.
- Offline recording firmware; removed Wi-Fi startup and fake uploader queue.
- Correct WAV RIFF/data sizes; sample-count-based 15-second chunks.
- Bounded acquisition queue, separate SD writer, debounced press-to-toggle control.
- NVS-reserved file IDs, checked writes, .part finalization and boot recovery;
  malformed short files retained as .bad. No automatic recording deletion.
- Full-storage/open/write/queue faults stop recording; amplifier remains disabled.
- Camera opening removed from cloud-built enclosure, speaker grille retained.

Verification: firmware compiled/linked for seeed_xiao_esp32s3 using managed
Espressif32 55.3.38 / Arduino 3.3.8. The build tool normalizes platformio.ini;
it did not use the initially requested 6.10.0 pin. Native C++ WAV/CRC tests pass
with -Wall -Wextra -Werror. No device recording test was performed.
Mechanical revision rev-85f58fc1b3e33b115722a790ac3d0f96a54bfad073769a41b468977a083f3704
uses current source/parameters/PCB context: four shapes, 32 x 76 x 24 mm assembly.
Only inspectable solids/bounds verified, not hardware fit or direct visual review.
Legacy camera parameters are inert; prior manifest geometry assumptions remain
provisional and must be reconciled before release.

Unfinished: BLE service, authenticated pairing, resumable transfer, durable
acknowledgements, Android/iPhone app, playback implementation, battery sensing,
low-battery behavior, exact component selection, PCB routing/DFM release, mic
metrology and control/connector fit. No fabrication artifacts exported.

Firmware validation still needed: SD CS=21 against exact Sense revision, microphone
sample scaling, missing card, removal mid-write, queue overflow, power cuts during
NVS update/write/header/rename, button timing around chunk rollover, full storage,
long-duration dropout detection. FAT rename/flush are NOT guaranteed power-fail
atomic; repair is best-effort and physical fault-injection is required. DMA loss
inside the driver is not yet tracked; queue fault detection alone is insufficient.
Recovered odd trailing bytes are excluded from the WAV data length, not erased.

PCB preserved unchanged this pass; earlier 33 unrouted/30-warning result remains
the baseline, not a new validation. Historical mechanical README/PCB review
revision IDs describe earlier checkpoints; this document records the current one.