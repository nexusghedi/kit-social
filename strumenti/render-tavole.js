const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const [dir,blobs,outdir,pat]=process.argv.slice(2);const F=process.env.F;
const ex={};for(const f of fs.readdirSync(blobs))ex[f.split('.')[0]]=f;
const ff=`<style>@font-face{font-family:'Nunito';src:url('file://${F}Nunito[wght].ttf');font-weight:200 1000}@font-face{font-family:'Baloo 2';src:url('file://${F}Baloo2[wght].ttf');font-weight:400 800}@font-face{font-family:'Instrument Serif';src:url('file://${F}InstrumentSerif-Regular.ttf')}@font-face{font-family:'Instrument Serif';font-style:italic;src:url('file://${F}InstrumentSerif-Italic.ttf')}@font-face{font-family:'Caveat';src:url('file://${F}Caveat[wght].ttf');font-weight:400 700}</style></head>`;
const b=await chromium.launch();
for(const f of fs.readdirSync(dir).filter(x=>x.startsWith(pat))){
 let h=fs.readFileSync(dir+f,'utf8');const m=h.match(/"width":(\d+),"height":(\d+)/);
 h=h.replace(/<script[\s\S]*?<\/script>/g,'').replace(/<\/?(x-dc|helmet)>/g,'').replace(/<link[^>]*>/,'').replace('</head>',ff).replace(/\/_blob\/([0-9a-f]+)/g,(m,id)=>'file://'+blobs+'/'+ex[id]);
 const o=outdir+f.replace('.dc.html','');fs.writeFileSync(o+'.html',h);
 const p=await b.newPage({viewport:{width:+m[1],height:+m[2]}});await p.goto('file://'+o+'.html');await p.waitForTimeout(300);await p.screenshot({path:o+'.png'});await p.close();}
await b.close();})();
