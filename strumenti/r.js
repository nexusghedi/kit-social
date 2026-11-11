const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const [src,blobs,out]=process.argv.slice(2);const F=process.env.F;
const ex={};for(const f of fs.readdirSync(blobs))ex[f.split('.')[0]]=f;
let h=fs.readFileSync(src,'utf8').replace(/<script[\s\S]*?<\/script>/g,'').replace(/<\/?(x-dc|helmet)>/g,'').replace(/<link[^>]*>/,'')
.replace('</head>',`<style>@font-face{font-family:'Nunito';src:url('file://${F}Nunito[wght].ttf');font-weight:200 1000}@font-face{font-family:'Montserrat';src:url('file://${F}Montserrat[wght].ttf');font-weight:100 900}@font-face{font-family:'Playfair Display';font-style:italic;src:url('file://${F}PlayfairDisplay-Italic[wght].ttf');font-weight:400 900}@font-face{font-family:'Baloo 2';src:url('file://${F}Baloo2[wght].ttf');font-weight:400 800}</style></head>`)
.replace(/\/_blob\/([0-9a-f]+)/g,(m,id)=>'file://'+blobs+'/'+ex[id]);
fs.writeFileSync(out+'.html',h);const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:+(process.env.H||1080)}});
await p.goto('file://'+out+'.html');await p.waitForTimeout(500);await p.screenshot({path:out+'.png'});await b.close();})();
