from pathlib import Path
import zipfile,hashlib,json
ROOT=Path(__file__).resolve().parents[1]
def pack(root=ROOT):
 out=root/'tarne';out.mkdir(exist_ok=True);full=out/'Finantsarvestus_loplik.zip';manifest={}
 skip={'.git','.openai','node_modules','__pycache__','.venv','tarne','.sites-checkout','test-results','playwright-report'}
 with zipfile.ZipFile(full,'w',zipfile.ZIP_DEFLATED) as z:
  for p in sorted(root.rglob('*')):
   rel=p.relative_to(root)
   if not p.is_file() or any(x in skip for x in rel.parts) or p.suffix in {'.pyc','.tgz','.tar'}:continue
   if p.suffix=='.zip' and p.name!='python_stdlib.zip':continue
   if str(rel)=='materjalid/FAILIDE_SHA256.json':continue
   z.write(p,Path('finantsarvestus')/rel);manifest[str(rel)]=hashlib.sha256(p.read_bytes()).hexdigest()
  z.writestr('finantsarvestus/materjalid/FAILIDE_SHA256.json',json.dumps(manifest,ensure_ascii=False,indent=2))
 demo=out/'Finantsvaade_avalik_demo.zip'
 with zipfile.ZipFile(demo,'w',zipfile.ZIP_DEFLATED) as z:
  for p in sorted((root/'dist').rglob('*')):
   if p.is_file():z.write(p,p.relative_to(root/'dist'))
  z.writestr('KAIVITAMINE.md','# Käivita demo\n\nPaki lahti. Käivita siin `python -m http.server 8000` ja ava http://localhost:8000. Pagesis avalda sisu koos .nojekyll failiga. Ainult sünteetilised arved; seanss pole püsiv.\n')
 sums={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [full,demo]};(out/'SHA256.json').write_text(json.dumps(sums,indent=2));print(sums)
if __name__=='__main__':pack()
