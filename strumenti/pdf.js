const {chromium}=require('playwright');const fs=require('fs');
// uso: node pdf.js src.html blobsdir out.pdf larghezza_mm altezza_mm zoom
(async()=>{const [src,blobs,out,wmm,hmm,zoom]=process.argv.slice(2);const F=process.env.F;
const ex={};for(const f of fs.readdirSync(blobs))ex[f.split('.')[0]]=f;
let h=fs.readFileSync(src,'utf8').replace(/<script[\s\S]*?<\/script>/g,'').replace(/<\/?(x-dc|helmet)>/g,'').replace(/<link[^>]*>/,'')
.replace('</head>',`<style>@font-face{font-family:'Nunito';src:url('file://${F}Nunito[wght].ttf');font-weight:200 1000}@font-face{font-family:'Montserrat';src:url('file://${F}Montserrat[wght].ttf');font-weight:100 900}@font-face{font-family:'Baloo 2';src:url('file://${F}Baloo2[wght].ttf');font-weight:400 800}
@page{size:${wmm}mm ${hmm}mm;margin:0}html,body{margin:0;padding:0;height:${hmm}mm;overflow:hidden}body>div{zoom:${zoom}}</style></head>`)
.replace(/\/_blob\/([0-9a-f]+)/g,(m,id)=>{if(!ex[id])throw new Error('blob mancante '+id);return 'file://'+blobs+'/'+ex[id]});
fs.writeFileSync(out+'.html',h);const b=await chromium.launch();const p=await b.newPage();
await p.goto('file://'+out+'.html');await p.waitForTimeout(800);
await p.pdf({path:out,preferCSSPageSize:true,printBackground:true});await b.close();})();
