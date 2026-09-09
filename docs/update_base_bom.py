"""Render procurement draft from current compiler-generated pcb/bom.csv.
Preserve prior exact-part links, never inherit Sense/battery links for replacements.
"""
import csv
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
old = (root / 'pcb/backups/pre-base-redesign/bom.md').read_text()
rows = list(csv.DictReader((root / 'pcb/bom.csv').open()))
lines = ['# Base-XIAO audio carrier — procurement BOM (DRAFT)', '',
         '**Not released for purchase/assembly.** Supersedes the Sense/603450/RGB BOM.',
         'Generated from `pcb/bom.csv`; electrical source refs may differ from physical KiCad refs.',
         'Prior BOM and historical prices: `pcb/backups/pre-base-redesign/bom.md`.',
         'No live stock or prices checked in this revision. See [validation and GPIO map](base-redesign.md).', '',
         '## Carrier PCB components', '',
         '| Qty | Source refs | MPN | Value / function | Existing sourcing link |',
         '|---:|---|---|---|---|']
for r in rows:
    mpn = r['MPN']
    if not mpn:
        continue
    urls = []
    for line in old.splitlines():
        if mpn in line:
            urls = re.findall(r'\[[^]]+\]\((https?://[^\s]+)\)', line)
            if urls:
                break
    refs = []
    for path in r.get('Zener Paths','').split(' | '):
        if '<root>.' in path:
            refs.append(path.split('<root>.')[1].split('.')[0])
    link = f'[existing supplier]({urls[0]})' if urls else '**Link needed**'
    if mpn == '113991114':
        link = '[Seeed base board](https://www.seeedstudio.com/XIAO-ESP32S3-p-5627.html); India supplier link needed'
    lines.append(f"| {r['Quantity']} | {' / '.join(refs) or r['References']} | {mpn} | {r['Value'] or r['Package']} | {link} |")
lines += ['', '## Off-board / assembly procurement', '',
          '| Qty | Item | Requirement / source status |', '|---:|---|---|',
          '| 1 | BAT1 protected 1S LiPo, exact MPN TBD | 300–500 mAh, 11–18 mm finished width, <=4–5.5 mm thick, 45–65 mm long; >=500 mA continuous plus documented pulse, 4.20 V charge, PCM, preferred 10k NTC. **New link and manufacturer drawing required.** |',
          '| 1 | SPK1 Same Sky CMS-16093-078L100 | Retained provisionally, 8 ohm / 0.7 W; existing Mouser link in archived BOM. R24 selects 3 dB gain; output limit and cavity bench validation required. |',
          '| 1 | M1 exact vibration motor TBD | Old Robu 1027 URL served 1034. **Replacement exact link with start/stall current and dimensions required.** Must tolerate regulated 3.3 V. |',
          '| 1 | microSD card, exact MPN/capacity TBD | Prefer traceable high-endurance 16–32 GB FAT32 for prototype; **link needed**. Qualify write latency and peak/standby current. |',
          '| 1 set | Battery, speaker and motor harnesses | J1/J3 PH 2 mm, J2 SH 1 mm; confirm polarity, wire length, connector orientation. Motor PH pigtail has prior Sunrom link; **exact battery/speaker mating leads needed**. |',
          '| 1 set | Microphone acoustic gasket / dust mesh | **Supplier links needed**, thickness and acoustic impedance TBD after port design. |',
          '| 1 | XIAO-compatible 2.4 GHz antenna | Confirm supplied with base SKU; otherwise exact antenna link/drawing needed. |',
          '', '## Changes and purchasing cautions', '',
          '- Removed Sense 113991115 expansion/camera/SD/mic assembly, camera mechanics, NOVA 603450 battery, PCA9685, two RGB LEDs, C6 and R9–R14.',
          '- Added base 113991114, candidate IM69D130V01XTSA1, DM3D-SF socket, C9/C10/C11, R16–R24.',
          '- New unique resistors needing links: RC0603FR-0733RL (33 ohm, 2 pcs), RC0603FR-0747KL (47k, 5 pcs).',
          '- AP2112K-3.3TRG1 was already in the circuit but lacks a saved sourcing link.',
          '- Additional 100nF/10uF/100k parts reuse existing MPN links; no new passive selection needed for those.',
          '- H1–H4 and TP3/TP4 are PCB features, not purchased components. Mounting hardware remains mechanical-design TBD.',
          '- Flyback D1 cathode is MOTOR_3V3, NOT VBAT. Speaker terminals are differential, neither grounded.',
          '- J1/J3 through-hole PH headers and SW2 remain provisional thickness risks.',
          '- No external RGB indication. Base board GPIO21 user LED is reused.',
          '- Candidate microphone package/electrical review and socket land-pattern/no-trace regions are unresolved; do not substitute or freeze layout from this draft.', '']
(root / 'docs/bom.md').write_text('\n'.join(lines))