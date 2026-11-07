let py, sessionReady=false;
const BASE=new URL('runtime/',self.location.href).href;
async function init(){
 if(py)return;
 const {loadPyodide}=await import('./runtime/pyodide.mjs');
 py=await loadPyodide({indexURL:BASE});
 await py.loadPackage(['pydantic','micropip']);
 await py.runPythonAsync("import micropip");
 for(const f of ['et_xmlfile-2.0.0-py3-none-any.whl','openpyxl-3.1.5-py2.py3-none-any.whl']){
  py.globals.set('wheel_url',new URL('vendor/'+f,self.location.href).href);
  await py.runPythonAsync('await micropip.install(wheel_url, deps=False)');
 }
 for(const name of ['kood/menetlus.py','kood/andmeleping.py','kood/veeb_adapter.py','sql/001_skeem.sql','sql/002_menetlus.sql']){
  const response=await fetch('python/'+name);if(!response.ok)throw Error('Pythoni moodul puudub: '+name);
  const path='/projekt/'+name;py.FS.mkdirTree(path.slice(0,path.lastIndexOf('/')));py.FS.writeFile(path,await response.text());
 }
 await py.runPythonAsync(`import sys, json, base64, pydantic, sqlite3
sys.path.insert(0,'/projekt/kood')
from veeb_adapter import WebSession, export_table`);
}
self.onmessage=async ({data:{id,action,payload}})=>{
 try{
  await init();py.globals.set('payload_json',JSON.stringify(payload));
  let code='p=json.loads(payload_json)\n';
  if(action==='start')code+="session=WebSession(p['rows'],p['as_of'])\nresult=session.snapshot()\nresult['runtime']={'python':sys.version.split()[0],'pydantic':pydantic.__version__}";
  else if(action==='import')code+="result=session.import_file(base64.b64decode(p['content']),p['kind'])";
  else if(action==='check')code+="from datetime import date\nsession.as_of=date.fromisoformat(p['as_of']).isoformat()\nresult=session.snapshot()";
  else if(action==='invoice_export')code+="result={'content':base64.b64encode(session.export(p['ids'],p['fmt'])).decode()}";
  else if(action==='table_export')code+="result={'content':base64.b64encode(export_table(p['rows'],p['fmt'],p['title'])).decode()}";
  else throw Error('Tundmatu toiming');
  const result=await py.runPythonAsync(code+`
json.dumps(result,ensure_ascii=False)`);
  self.postMessage({id,result:JSON.parse(result)});
 }catch(e){self.postMessage({id,error:String(e.message||e)});}
};
