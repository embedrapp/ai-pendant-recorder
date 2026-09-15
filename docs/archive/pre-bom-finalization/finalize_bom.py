from pathlib import Path
import json,re,shutil,yaml
r=Path(__file__).resolve().parents[1]; a=r/'docs/archive/pre-bom-finalization'; a.mkdir(parents=True,exist_ok=True)
for f in ['embedr.yaml','pcb/ai_pendant_recorder.zen','docs/bom.md']: shutil.copy2(r/f,a/Path(f).name)
b=r/'pcb/ai_pendant_recorder.zen'; s=b.read_text(); links={}
for line in (r/'docs/bom.md').read_text().splitlines():
 c=[v.strip() for v in line.split('|')]
 if len(c)>5:
  m=re.search(r'\]\((https?://[^\s]+)\)',c[5])
  if m: links[c[3]]=m.group(1)
e='https://in.element14.com/'
links.update({'IM69D130V01XTSA1':e+'infineon/im69d130v01xtsa1/mems-microphone-3-6v-module/dp/2986420','AP2112K-3.3TRG1':e+'diodes-inc/ap2112k-3-3trg1/ldo-fixed-3-3v-0-6a-sot-25-85deg/dp/3257429','RC0603FR-0733RL':e+'yageo/rc0603fr-0733rl/res-33r-1-0-1w-0603-thick-film/dp/9238301','RC0603FR-0747KL':e+'yageo/rc0603fr-0747kl/res-47k-1-0-1w-0603-thick-film/dp/9238689','RC0603FR-07470RL':'https://www.digikey.com/en/products/detail/yageo/RC0603FR-07470RL/727256','GRM155R71C104KA88D':e+'murata/grm155r71c104ka88d/cap-mlcc-0-1uf-x7r-16v-0402/dp/4326785','PTS841GKSMTR LFS':'https://www.digikey.com/en/products/detail/c-k/PTS841GKSMTR-LFS/10445315'})
for mpn,mfr,q in [('104031-0811','Molex','udsGRKD4nA3Tvy7wqky%252BuA%3D%3D'),('TPS61023DRLR','Texas-Instruments','BJlw7L4Cy7%2FfEnwYuWeGOg%3D%3D'),('TPS22918DBVR','Texas-Instruments','f4l5qYp%2Fy%252B5F7w5ZAgmi7A%3D%3D'),('XEL4030-102MEC','Coilcraft','chTDxNqvsynxP6L4IWrGOQ%3D%3D'),('GRM21BR61A226ME44L','Murata-Electronics','eeBpzGFlv%2B8tSfxib2AMhw%3D%3D'),('GRM1555C1E102JA01D','Murata-Electronics','y02iAgv9n62vwTD5aUQSxQ%3D%3D')]: links[mpn]='https://www.mouser.in/en/ProductDetail/'+mfr+'/'+mpn+'?qs='+q
ids={'IM69D130V01XTSA1':'ds_097425d603a5861ea83c','AP2112K-3.3TRG1':'ds_943f1f6e10cbb0789dbb','GRM1555C1E102JA01D':'ds_baaefb1272b27c705358','GRM21BR61A226ME44L':'ds_9d09f353be4df0f321db','GRM155R71C104KA88D':'ds_30c2edbd41f53ac917fb','TPS61023DRLR':'ds_c3d679f9c6eab3a775cd','TPS22918DBVR':'ds_61aa790c3c3008f98c5e','104031-0811':'ds_f2a383fc62e80e613220','XEL4030-102MEC':'ds_293e09d408f8109bb968','WS2812C-2020-V1':'ds_f7eaed7171762f8cbf8e'}
for m in links:
 if m.startswith('RC0603'): ids[m]='ds_7f87b9b9c3e0a80c68cc'
pos=s.index('def sourced_passives(c):'); s=s[:pos]+'PURCHASE_LINKS = '+json.dumps(links,indent=4)+'\nDATASHEET_INDEX = '+json.dumps(ids,indent=4)+'\n\n'+s[pos:]
s=s.replace('    sources = {','    if c.mpn in PURCHASE_LINKS:\n        c.properties["source_url"] = PURCHASE_LINKS[c.mpn]\n        c.properties["note"] = "User-confirmed purchase link and in-stock status; no numeric stock or price provided."\n    if c.mpn in DATASHEET_INDEX:\n        c.properties["datasheet"] = "https://www.embedr.app/api/datasheets/" + DATASHEET_INDEX[c.mpn] + "/pdf"\n    sources = {',1)
s=s.replace('        "RC0603FR-072KL": ("YAGEO", "DigiKey", "311-2.00KHRCT-ND"),\n','').replace('        "BM02B-SRSS-TB(LF)(SN)": ("JST", "DigiKey", "455-1788-1-ND"),\n','')
b.write_text(s)
p=r/'embedr.yaml'; d=yaml.safe_load(p.read_text()); bad=['JST SH','7Semi','generic-lp603450','MAX98357','Same Sky','Kingbright','QX Flat','Sense documentation','Sense expansion','Hirose','WLY 104050','601145','LP 451860','503562','SK6805','TPS22950','TPS2552','PKCELL LP-523334','Infineon IM69D130 Datasheet v1.0','Diodes AP2112 datasheet','Yageo RC series']
removed=[v for v in d['datasheets'] if any(x.lower() in v.get('name','').lower() for x in bad)]; d['datasheets']=[v for v in d['datasheets'] if v not in removed]; p.write_text(yaml.safe_dump(d,sort_keys=False)); (a/'removed-datasheet-entries.json').write_text(json.dumps(removed,indent=2))
for name in ['base-redesign.md','schematic-plan-review.md','schematic-datasheet-review.md','bom-source-review.md']:
 p=r/'docs'/name; shutil.copy2(p,a/name); p.write_text('# Superseded reference\n\nHistorical content: [archive](archive/pre-bom-finalization/'+name+'). Use [current BOM](bom.md), [LED contract](rgb-matrix.md), and the current Zen source. Historical checks do not release this revision.\n')
for name in ['seeed-xiao-esp32s3-sense-113991115.pdf','qx-flat-1027.pdf','7semi-max17048-breakout.pdf','jst-sh-series.pdf','jst-sh.pdf','max98357a-max98357b.pdf','kingbright-apgf0607g32b33r23-05.pdf','generic-lp603450-1100mah.pdf','same-sky-cms-16093-078x.pdf','JST_SH_BM02B-SRSS-TB_1x02-1MP_P1.00mm_Vertical.kicad_mod']:
 p=r/'docs/datasheets'/name
 if p.exists():
  dest=a/'datasheets'/name; dest.parent.mkdir(exist_ok=True); shutil.move(p,dest)
for name in ['DM3.pdf','DM3D-SF.kicad_mod','IM69D128S.pdf']:
 p=r/'docs/redesign-evidence'/name
 if p.exists():
  dest=a/'redesign-evidence'/name; dest.parent.mkdir(exist_ok=True); shutil.move(p,dest)
p=r/'docs/bom.md'; lines=[]
for line in p.read_text().replace('| 4 | C2 / C7 / C8 / C11 |','| 5 | C2 / C7 / C8 / C11 / C12 |').splitlines():
 c=[v.strip() for v in line.split('|')]
 if len(c)>5 and c[3] in links: c[5]='[Purchase]('+links[c[3]]+')'; line='| '+' | '.join(c[1:-1])+' |'
 lines.append(line)
p.write_text('\n'.join(lines)+'\n\n## Finalized carrier sourcing\nLinks confirmed in stock by user; no numeric inventory or prices provided. Exact components unchanged. Motor/card/acoustic procurement and manufacturing release remain open. C40 manufacturer search flags NRND: retain approved part, review lifecycle before production.\n')
print('links',len(links),'indexes',len(ids),'archived entries',len(removed))
