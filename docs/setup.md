# Firmware setup

Entry point: `src/main.cpp`; framework: Arduino/PlatformIO.
Environment `esp32-s3` selects the Seeed XIAO ESP32S3 board definition with
`esp-builtin`. A successful build is still required before flashing.

Use a qualified FAT32 microSD card; microphone is the external carrier PDM
IM69D130, not a Sense expansion microphone. See [pin map](current-design.md).
Network configuration is presently unused. Never commit real credentials.
Bench-test rail droop, charge behavior, SD writes, audio and LED sequencing.