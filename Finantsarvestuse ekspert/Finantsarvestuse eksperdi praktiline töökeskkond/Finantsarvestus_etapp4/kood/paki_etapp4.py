"""Portatiivne allalaadimine; väldi ZIP-i rekursiivset kaasamist."""
from pathlib import Path
import zipfile,hashlib,json
ROOT=Path(__file__).resolve().parents[1]
def pack(root=ROOT):
    out=root/'dist/Finantsarvestus_etapp4.zip'
    selected=[]
    manifest={}
    with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as z:
        for p in sorted(root.rglob('*')):
            rel=p.relative_to(root)
            if not p.is_file() or p==out or any(x in {'.git','.openai','node_modules','__pycache__','.venv','.pytest_cache','test-results','playwright-report'} for x in rel.parts):continue
            if p.suffix in {'.pyc','.tar','.tgz'}:continue
            if str(rel)=='materjalid/FAILIDE_SHA256.json':continue
            z.write(p,Path('finantsarvestus_etapp4')/rel)
            manifest[str(rel)]=hashlib.sha256(p.read_bytes()).hexdigest()
        z.writestr('finantsarvestus_etapp4/materjalid/FAILIDE_SHA256.json',json.dumps(manifest,ensure_ascii=False,indent=2))
    print(out,out.stat().st_size)
    return out
if __name__=='__main__':pack()
