# Stili social Nexus A–E: esempi completi (post 3, WhatsApp notizia+promemoria, storia notizia+promemoria).
# Le regole stanno nella skill nexus-nuovo-evento, §6bis.
import json
import sys
# Uso: python3 stili_gen.py <cartella project del canvas>  (genera le tavole Stile-<L>-<evento>-<formato>.dc.html e aggiorna canvas.json)
P=sys.argv[1].rstrip('/')+'/'
B=lambda i:'/_blob/'+i
INK='#1d1d1b';AR='#ef7d32';BLU='#0163a5';GIA='#f8ba32';VER='#109439';VIO='#922c7d';CREMA='#fbe7da';LAV='#c5c9ea'
LW=B('4cb9e8569df217025538ea38faac341a');LC=B('7961cecae0360e3509cd530495103ba8');PIC=B('aa926203b615fc7ed118972f794d16e1')
SERIF="'Instrument Serif', Georgia, serif";HAND="'Caveat', cursive"

def arke(mode,h):
    t1=round(h*.56);t2=round(h*.48)
    if mode=='colori':
        txt=f'<div style="font-size: {t1}px; line-height: {round(t1*.86)}px; color: #1e9a4b">ARKÈ</div><div style="font-size: {t2}px; line-height: {round(t2*.9)}px"><span style="color: #1e9a4b">i5</span><span style="color: #ef7d32">s</span><span style="color: #0a7cc1">e</span><span style="color: #f8ba32">n</span><span style="color: #e5245e">s</span><span style="color: #922c7d">i</span></div>';f=''
    else:
        c='#ffffff' if mode=='bianco' else INK;f='; filter: brightness(0) invert(1)' if mode=='bianco' else '; filter: brightness(0)'
        txt=f'<div style="font-size: {t1}px; line-height: {round(t1*.86)}px; color: {c}">ARKÈ</div><div style="font-size: {t2}px; line-height: {round(t2*.9)}px; color: {c}">i5sensi</div>'
    return f'<div style="display: flex; align-items: center; gap: {round(h*.16)}px" aria-label="Arkè i5sensi"><img src="{PIC}" alt="" aria-hidden="true" style="height: {h}px{f}"><div style="font-family: \'Baloo 2\', \'Nunito\', sans-serif; font-weight: 800; display: flex; flex-direction: column">{txt}</div></div>'
def loghi(mode,con_arke,w=170):
    h=round(w*35.42/116.4)
    src=LW if mode=='bianco' else LC;f='; filter: brightness(0)' if mode=='nero' else ''
    nx=f'<img src="{src}" alt="Nexus APS" style="width: {w}px; display: block{f}">'
    if not con_arke:return nx
    sep={'bianco':'rgba(255,255,255,0.5)','nero':'rgba(29,29,27,0.4)'}.get(mode,'#cfcfcd')
    return f'<div style="display: flex; align-items: center; gap: {round(h*.45)}px">{nx}<div style="width: 2px; height: {round(h*1.1)}px; background: {sep}"></div>{arke(mode,round(h*1.05))}</div>'
def wrap(title,body,w,h):
    return f'''<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<title>{title}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Nunito:ital,wght@0,300;0,400;0,600;0,700;0,800;0,900;1,800&amp;family=Instrument+Serif:ital@0;1&amp;family=Caveat:wght@600;700&amp;family=Baloo+2:wght@800&amp;display=swap">
<style>
body{{margin:0}}
</style>
</helmet>
{body}
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":{w},"height":{h}}}}}'>
class Component extends DCLogic {{
renderVals() {{ return {{}}; }}
}}
</script>
</body>
</html>
'''
def root(w,h,bg,col='#ffffff',extra=''):
    return f'<div style="width: {w}px; height: {h}px; position: relative; overflow: hidden; background: {bg}; font-family: \'Nunito\', system-ui, sans-serif; color: {col}{extra}">'
def nexi(e,style):
    return f'<img src="{e["nexi"]}" alt="{e["nexi_alt"]}" style="position: absolute; {style}">' if e.get('nexi') else ''
SIZES={'P1':(1080,1350),'P2':(1080,1350),'P3':(1080,1350),'WA':(1080,1080),'WA2':(1080,1080),'S':(1080,1920),'S2':(1080,1920)}
NOMI={'P1':'post 1/3','P2':'post 2/3','P3':'post 3/3','WA':'WhatsApp · notizia','WA2':'WhatsApp · promemoria','S':'storia · notizia','S2':'storia · promemoria'}

# ---------------- EVENTI ----------------
FONT=dict(id='Fontanellato',nome='Fontanellato',kicker='Arkè i5sensi · tappa 4',sub='e il re dei salumi',data='Sabato 21 novembre',d1='SAB',d2='21',d3='NOV',ora='Partenza ore 13:00',
 f1=B('a0d4df1eefef80e5ca463f3a4ea6de1d'),f1alt='La Rocca Sanvitale di Fontanellato',f2=B('e923646167c3460986860dfd3ca6f084'),f2alt='Salumi affettati',
 nexi=B('825bde7ae814c8a4cddb7d03bb8a3c75'),nexi_alt='Nexi con il basco rinascimentale che sbuca e saluta',arke=True,
 items=[('VISTA','La Rocca Sanvitale e la Camera Ottica'),('ARTE','La saletta affrescata dal Parmigianino'),('GUSTO','Il Culatello di Zibello, in cantina')],
 info=[('Partenza','ore 13:00, parcheggio di via dei Fontanili'),('Rientro','partenza verso le 19:30'),('Per gli iscritti','compresa nel corso Arkè i5sensi'),('Info','WhatsApp 331 763 4299')],
 manca='alla partenza',prom='Sabato 21 novembre · ritrovo ore 13:00 in via dei Fontanili')
LAUD=dict(id='Laudato',nome='Laudato sì',kicker='Una serata sui verbi di Francesco',sub='i verbi di Francesco',data='Sabato 28 novembre',d1='SAB',d2='28',d3='NOVEMBRE',ora='ore 20.30',
 f1=B('d4df0d1c8edf2b6d2bdbe24790647aa8'),f1alt='Giotto, la predica agli uccelli',f2=B('3e3f963fc2c7aec93c110780fc3d7ad7'),f2alt='Foglie di felce',
 nexi=None,nexi_alt='',arke=False,
 info=[('Dove','Teatro Il Gabbiano, Ghedi'),('Quando','sabato 28 novembre, ore 20.30'),('Ingresso','libero, fino a esaurimento posti'),('Con','Elisa Mastromatteo e Letizia Pari')],
 manca='alla serata',prom='Sabato 28 novembre · ore 20.30 · Teatro Il Gabbiano')
NAT=dict(id='Natale',nome="Il Natale è nell'aria",kicker='Laboratorio di decorazioni',sub='e nel tuo tocco creativo!',data='4 martedì · dal 17 novembre',d1='MAR',d2='17',d3='NOV',ora='ore 15–17',
 f1=B('5d2e6517d85a19704f321420ad5b41c8'),f1alt='Decorazioni di Natale dipinte a mano',small=[(B('7f5408ebd5676c912d79688ca38bbaa7'),'alberelli glitterati'),(B('e14b6c7fbb503d3f015fe8e640401453'),'angeli di carta'),(B('f4b76e036062c833f2e02d80a26d0f5c'),'fiocchi e ghirlande')],
 nexi=B('25d09ecb86db746cedbcc9f2726110e5'),nexi_alt='Nexi blu con il berretto di Natale che sbuca e saluta',arke=False,
 date=[('17','nov'),('24','nov'),('1','dic'),('15','dic')],
 info=[('Dove','sede Nexus, via Fabio Filzi 10'),('A cura di','Sonia Piccioni'),('Per i soci','gratis, materiali compresi'),('Iscrizioni','WhatsApp 331 763 4299')],
 manca='al primo incontro',prom='Martedì 17 novembre · ore 15–17 · in sede')
DRES=dict(id='Dresda',nome='Dresda e Praga',kicker='Arkè i5sensi · viaggio',sub='e la Svizzera Sassone',data='29 marzo – 4 aprile 2027',
 f1=B('b0c295e2e0a043f18da4707ac3c8e030'),f1alt='Il Castello di Praga sulla Moldava',f2=B('329fd83f3d222be86da7af502a879c4c'),f2alt="Dresda sull'Elba",f3=B('2630d9b7c20088ebd64835d6186b4e6f'),f3alt='Il Ponte Bastei',
 nexi=B('89bcd4ed90ff6a594b07daa7dda05a80'),nexi_alt='Nexi a pallini con il cappello boemo che sbuca e saluta',arke=True,
 info=[('Quota','2.495 € con 25 partecipanti'),('Viaggio','7 giorni in aereo, tutto incluso'),('Iscrizioni','entro il 15 novembre'),('Modulo','forms.gle/r8hEiu6XuN5mHhUL8')],
 manca='alla chiusura delle iscrizioni',prom='Iscrizioni entro domenica 15 novembre')
SAL=dict(id='Salento',nome='Salento',kicker='Un risveglio per i cinque sensi',sub='5–10 dicembre 2026',data='5–10 dicembre 2026',
 f1=B('4b569995b71f523bde5d8a0112553669'),f1alt='Facciata barocca in pietra leccese',f2=B('11a1fe8fa55a6ae25c02e14400d9a849'),f2alt='Il rosone della Cattedrale di Otranto',f3=B('4c369724128bdd2e0475bccd87e2e42c'),f3alt='Spiaggia del Salento',
 nexi=B('ab9f69c6eecdfdef52ed204bce88eca2'),nexi_alt='Nexi con il tamburello che sbuca e saluta',arke=False,
 manca='alla partenza',prom='Sabato 5 dicembre · bus da Ghedi per Linate, volo alle 8:55')
MIL=dict(id='Milano',nome='Milano',kicker='Dalí, Verdi e un aperitivo in centro',data='Martedì 29 dicembre',
 f1=B('b0fab500a93569f4a7e53503a6a31eda'),f1alt="Strada della Milano dell'Ottocento",nexi=B('7a5a43da644788dea1b458387105a7ed'),nexi_alt='Nexi che sbuca e saluta',arke=False,
 manca='alla partenza',prom='Martedì 29 dicembre · partenza da Ghedi alle 7:30')

# ---------------- A · ETICHETTE ----------------
def lab(t,bg,fg,fs,rot=0,pad='6px 18px',fw=900,extra=''):
    return f'<div style="align-self: flex-start; transform: rotate({rot}deg)"><span style="background: {bg}; color: {fg}; font-size: {fs}px; line-height: {round(fs*1.32)}px; font-weight: {fw}; padding: {pad}; -webkit-box-decoration-break: clone; box-decoration-break: clone{extra}">{t}</span></div>'
def sticker(e,size,top,left,bg=AR,fg=INK,rot=-10):
    return f'<div style="position: absolute; left: {left}px; top: {top}px; width: {size}px; height: {size}px; border-radius: 50%; background: {bg}; color: {fg}; transform: rotate({rot}deg); display: flex; flex-direction: column; align-items: center; justify-content: center; line-height: 1; box-shadow: 0 10px 30px rgba(0,0,0,0.3)"><div style="font-size: {round(size*.16)}px; font-weight: 900; letter-spacing: 0.08em">{e["d1"]}</div><div style="font-size: {round(size*.42)}px; font-weight: 900">{e["d2"]}</div><div style="font-size: {round(size*.16)}px; font-weight: 900; letter-spacing: 0.08em">{e["d3"]}</div></div>'
def stileA(e):
    o={}
    hdr=lambda fs:f'{lab(e["kicker"].upper(),"#ffffff",INK,round(fs*.3),-1,"6px 14px",900,"; letter-spacing: 0.08em")}<div style="height: 10px"></div>{lab(e["nome"],INK,"#ffffff",fs,-2,"0 22px")}<div style="height: 6px"></div>{lab(e["sub"],AR,INK,round(fs*.42),1,"4px 16px",800)}'
    foot=lambda m='bianco':f'<div style="position: absolute; left: 0; right: 0; bottom: 0; height: 110px; background: {INK}; display: flex; align-items: center; justify-content: space-between; padding: 0 60px"><div style="font-size: 26px; font-weight: 800; letter-spacing: 0.12em; color: #ffffff">NEXUSGHEDI.IT</div>{loghi("bianco",e["arke"],150)}</div>'
    o['P1']=root(1080,1350,INK)+f'<img src="{e["f1"]}" alt="{e["f1alt"]}" style="position: absolute; inset: 0; width: 1080px; height: 1240px; object-fit: cover"><div style="position: absolute; left: 60px; top: 80px; display: flex; flex-direction: column; width: 900px">{hdr(150)}</div>{sticker(e,230,880,70)}{nexi(e,"right: 0; top: 640px; height: 520px")}{foot()}</div>'
    rows=''.join(f'{lab(k,"#ffffff",INK,28,0,"6px 14px",900,"; letter-spacing: 0.1em")}<div style="height: 8px"></div>{lab(v,INK,"#ffffff",52,0,"4px 18px",800)}<div style="height: 34px"></div>' for k,v in e['items'])
    o['P2']=root(1080,1350,INK)+f'<img src="{e["f2"]}" alt="{e["f2alt"]}" style="position: absolute; inset: 0; width: 1080px; height: 1240px; object-fit: cover"><div style="position: absolute; left: 60px; top: 90px">{lab("GUARDA, ASCOLTA, GUSTA",AR,INK,40,-2,"6px 20px",900,"; letter-spacing: 0.06em")}</div><div style="position: absolute; left: 60px; bottom: 170px; display: flex; flex-direction: column; width: 960px">{rows}</div>{foot()}</div>'
    inf=''.join(f'{lab(k.upper(),INK,AR,26,0,"6px 14px",900,"; letter-spacing: 0.1em")}<div style="height: 6px"></div>{lab(v,"#ffffff",INK,46,0,"4px 16px",800)}<div style="height: 30px"></div>' for k,v in e['info'])
    o['P3']=root(1080,1350,AR,INK)+f'<div style="position: absolute; left: 60px; top: 80px; display: flex; flex-direction: column; width: 960px">{lab("COME FUNZIONA",INK,"#ffffff",64,-2,"4px 22px")}<div style="height: 60px"></div>{inf}</div>{sticker(e,200,980,800,INK,"#ffffff",8)}<div style="position: absolute; left: 60px; bottom: 60px">{loghi("nero",e["arke"],170)}</div></div>'
    o['WA']=root(1080,1080,INK)+f'<img src="{e["f1"]}" alt="{e["f1alt"]}" style="position: absolute; inset: 0; width: 1080px; height: 1080px; object-fit: cover"><div style="position: absolute; left: 56px; top: 60px; display: flex; flex-direction: column; width: 760px">{hdr(130)}</div>{sticker(e,210,700,64)}{nexi(e,"right: 0; top: 330px; height: 430px")}<div style="position: absolute; right: 50px; bottom: 50px">{loghi("bianco",e["arke"],160)}</div></div>'
    o['WA2']=root(1080,1080,INK)+f'<img src="{e["f1"]}" alt="" aria-hidden="true" style="position: absolute; inset: 0; width: 1080px; height: 1080px; object-fit: cover; opacity: 0.45"><div style="position: absolute; left: 60px; top: 120px; display: flex; flex-direction: column">{lab("MANCANO",'#ffffff',INK,90,-3,"0 24px")}<div style="height: 14px"></div>{lab("3 GIORNI",AR,INK,190,-2,"0 26px")}<div style="height: 20px"></div>{lab(e["manca"],INK,"#ffffff",56,1,"4px 20px",800)}</div><div style="position: absolute; left: 60px; top: 740px; width: 760px">{lab(e["nome"]+" · "+e["prom"],"#ffffff",INK,36,0,"6px 16px",800)}</div><div style="position: absolute; right: 50px; bottom: 50px">{loghi("bianco",e["arke"],160)}</div></div>'
    o['S']=root(1080,1920,INK)+f'<img src="{e["f1"]}" alt="{e["f1alt"]}" style="position: absolute; inset: 0; width: 1080px; height: 1920px; object-fit: cover"><div style="position: absolute; left: 70px; top: 260px; display: flex; flex-direction: column; width: 940px">{hdr(150)}</div>{sticker(e,260,1060,80)}{nexi(e,"right: 0; top: 820px; height: 620px")}<div style="position: absolute; left: 0; right: 0; bottom: 300px; display: flex; justify-content: center">{lab("SCOPRI DI PIÙ · LINK QUI","#ffffff",INK,40,0,"14px 34px",900)}</div><div style="position: absolute; left: 0; right: 0; bottom: 200px; display: flex; justify-content: center">{loghi("bianco",e["arke"],170)}</div></div>'
    o['S2']=root(1080,1920,INK)+f'<img src="{e["f1"]}" alt="" aria-hidden="true" style="position: absolute; inset: 0; width: 1080px; height: 1920px; object-fit: cover; opacity: 0.4"><div style="position: absolute; left: 70px; top: 380px; display: flex; flex-direction: column">{lab("MANCANO","#ffffff",INK,110,-3,"0 26px")}<div style="height: 16px"></div>{lab("3",AR,INK,420,-2,"0 40px")}<div style="height: 16px"></div>{lab("GIORNI","#ffffff",INK,150,2,"0 26px")}<div style="height: 26px"></div>{lab(e["manca"],INK,"#ffffff",58,0,"4px 20px",800)}</div><div style="position: absolute; left: 70px; right: 70px; top: 1430px">{lab(e["prom"],"#ffffff",INK,40,0,"6px 16px",800)}</div><div style="position: absolute; left: 0; right: 0; bottom: 200px; display: flex; justify-content: center">{loghi("bianco",e["arke"],170)}</div></div>'
    return o

# ---------------- B · EDITORIALE ----------------
PIN='<svg width="34" height="34" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 21s-7-6.2-7-11.5A7 7 0 0 1 19 9.5C19 14.8 12 21 12 21z"></path><circle cx="12" cy="9.5" r="2.5"></circle></svg>'
CLK='<svg width="34" height="34" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="9"></circle><path d="M12 7v5l3 2"></path></svg>'
def stileB(e):
    o={};acc=GIA
    def info_row(fs=30):
        return f'<div style="display: flex; gap: 40px; align-items: center; border-top: 1.5px solid rgba(255,255,255,0.4); padding-top: 26px"><div style="display: flex; gap: 14px; align-items: center; font-size: {fs}px; line-height: {round(fs*1.3)}px; font-weight: 600">{PIN}<span>Teatro Il Gabbiano<br>Ghedi</span></div><div style="width: 1.5px; align-self: stretch; background: rgba(255,255,255,0.4)"></div><div style="display: flex; gap: 14px; align-items: center; font-size: {fs}px; line-height: {round(fs*1.3)}px; font-weight: 600">{CLK}<span>Ore 20.30<br>Ingresso libero</span></div></div>'
    o['P1']=root(1080,1350,INK)+f'''<div style="position: absolute; left: 0; top: 0; width: 1080px; height: 640px; overflow: hidden"><img src="{e["f1"]}" alt="{e["f1alt"]}" style="width: 1080px; height: 720px; object-fit: cover; object-position: top"></div>
<div style="position: absolute; left: 70px; top: 600px; right: 70px; display: flex; gap: 40px; align-items: flex-end"><div style="font-family: {SERIF}; font-size: 330px; line-height: 250px; color: {acc}">28</div><div style="padding-bottom: 14px"><div style="font-size: 36px; font-weight: 900; letter-spacing: 0.12em; color: {acc}">NOVEMBRE</div><div style="font-size: 30px; font-weight: 600">sabato · ore 20.30</div></div></div>
<div style="position: absolute; left: 70px; top: 900px; right: 70px"><div style="font-family: {SERIF}; font-style: italic; font-size: 130px; line-height: 120px">Laudato sì</div><div style="font-size: 40px; line-height: 50px; font-weight: 300; margin-top: 10px">una serata sui verbi di Francesco</div></div>
<div style="position: absolute; left: 70px; right: 70px; bottom: 60px; display: flex; justify-content: space-between; align-items: flex-end">{info_row(28)}{loghi("bianco",False,150)}</div></div>'''
    o['P2']=root(1080,1350,INK)+f'''<div style="position: absolute; left: 70px; top: 80px; font-size: 28px; font-weight: 900; letter-spacing: 0.14em; color: {acc}">UN VERBO DELLA SERATA</div>
<div style="position: absolute; left: 70px; top: 150px; font-family: {SERIF}; font-style: italic; font-size: 230px; line-height: 210px">Osservare</div>
<img src="{e["f2"]}" alt="{e["f2alt"]}" style="position: absolute; right: 70px; top: 470px; width: 520px; height: 700px; object-fit: cover; border-radius: 260px 260px 0 0">
<div style="position: absolute; left: 70px; top: 520px; width: 380px; font-size: 40px; line-height: 54px; font-weight: 300">Uno dei momenti della serata è dedicato all'<span style="font-family: {SERIF}; font-style: italic; font-size: 50px">osservare</span>.<br><br><b style="font-weight: 800">Lo cura Nexus.</b></div>
<div style="position: absolute; left: 70px; bottom: 70px">{loghi("bianco",False,150)}</div></div>'''
    rows=''.join(f'<div style="display: grid; grid-template-columns: 260px 1fr; gap: 30px; border-top: 1.5px solid rgba(255,255,255,0.35); padding: 26px 0"><div style="font-size: 26px; font-weight: 900; letter-spacing: 0.12em; color: {acc}">{k.upper()}</div><div style="font-size: 40px; line-height: 50px; font-weight: 400">{v}</div></div>' for k,v in e['info'])
    o['P3']=root(1080,1350,INK)+f'''<div style="position: absolute; left: 70px; top: 80px; font-family: {SERIF}; font-size: 120px; line-height: 110px">Ci vediamo<br><i>a teatro</i></div>
<div style="position: absolute; left: 70px; right: 70px; top: 420px; display: flex; flex-direction: column">{rows}</div>
<div style="position: absolute; left: 70px; right: 70px; bottom: 70px; display: flex; justify-content: space-between; align-items: center"><div style="font-size: 28px; font-weight: 700">nexusghedi.it</div>{loghi("bianco",False,150)}</div></div>'''
    o['WA']=root(1080,1080,INK)+f'''<div style="position: absolute; left: 0; top: 0; width: 470px; height: 1080px; overflow: hidden"><img src="{e["f1"]}" alt="{e["f1alt"]}" style="width: 470px; height: 1260px; object-fit: cover; object-position: top"></div>
<div style="position: absolute; left: 520px; top: 60px; right: 50px; display: flex; flex-direction: column; gap: 6px"><div style="display: flex; align-items: flex-end; gap: 18px"><div style="font-family: {SERIF}; font-size: 220px; line-height: 170px; color: {acc}">28</div><div style="font-size: 30px; font-weight: 900; letter-spacing: 0.1em; color: {acc}; padding-bottom: 10px">NOV</div></div>
<div style="font-family: {SERIF}; font-style: italic; font-size: 96px; line-height: 92px; margin-top: 30px">Laudato sì</div><div style="font-size: 34px; line-height: 44px; font-weight: 300">i verbi di Francesco</div></div>
<div style="position: absolute; left: 520px; right: 50px; top: 640px; display: flex; flex-direction: column; gap: 22px; font-size: 32px; line-height: 40px; font-weight: 600"><div style="display: flex; gap: 14px; align-items: center">{PIN}Teatro Il Gabbiano, Ghedi</div><div style="display: flex; gap: 14px; align-items: center">{CLK}Ore 20.30 · ingresso libero</div></div>
<div style="position: absolute; left: 520px; bottom: 50px">{loghi("bianco",False,150)}</div></div>'''
    o['WA2']=root(1080,1080,INK)+f'''<div style="position: absolute; left: 70px; top: 70px; font-size: 30px; font-weight: 900; letter-spacing: 0.14em; color: {acc}">LAUDATO SÌ · I VERBI DI FRANCESCO</div>
<div style="position: absolute; left: 60px; top: 130px; font-family: {SERIF}; font-size: 560px; line-height: 480px; color: {acc}">3</div>
<div style="position: absolute; left: 430px; top: 230px; font-family: {SERIF}; font-style: italic; font-size: 140px; line-height: 130px">giorni<br>{e["manca"].split()[-1] if False else "alla serata"}</div>
<div style="position: absolute; left: 70px; right: 70px; top: 700px">{info_row(32)}</div>
<div style="position: absolute; left: 70px; bottom: 60px">{loghi("bianco",False,150)}</div></div>'''
    o['S']=root(1080,1920,INK)+f'''<div style="position: absolute; left: 0; top: 0; width: 1080px; height: 880px; overflow: hidden"><img src="{e["f1"]}" alt="{e["f1alt"]}" style="width: 1080px; height: 980px; object-fit: cover; object-position: top"></div>
<div style="position: absolute; left: 80px; top: 840px; display: flex; gap: 40px; align-items: flex-end"><div style="font-family: {SERIF}; font-size: 360px; line-height: 270px; color: {acc}">28</div><div style="padding-bottom: 16px"><div style="font-size: 40px; font-weight: 900; letter-spacing: 0.12em; color: {acc}">NOVEMBRE</div><div style="font-size: 34px; font-weight: 600">sabato · ore 20.30</div></div></div>
<div style="position: absolute; left: 80px; right: 80px; top: 1170px"><div style="font-family: {SERIF}; font-style: italic; font-size: 150px; line-height: 140px">Laudato sì</div><div style="font-size: 44px; line-height: 56px; font-weight: 300; margin-top: 10px">una serata sui verbi di Francesco</div></div>
<div style="position: absolute; left: 80px; right: 80px; top: 1500px">{info_row(32)}</div>
<div style="position: absolute; left: 80px; bottom: 220px">{loghi("bianco",False,170)}</div></div>'''
    o['S2']=root(1080,1920,INK)+f'''<div style="position: absolute; left: 80px; top: 280px; font-size: 34px; font-weight: 900; letter-spacing: 0.14em; color: {acc}">LAUDATO SÌ · I VERBI DI FRANCESCO</div>
<div style="position: absolute; left: 50px; top: 360px; font-family: {SERIF}; font-size: 820px; line-height: 700px; color: {acc}">3</div>
<div style="position: absolute; left: 80px; top: 1080px; font-family: {SERIF}; font-style: italic; font-size: 170px; line-height: 150px">giorni<br>alla serata</div>
<div style="position: absolute; left: 80px; right: 80px; top: 1440px">{info_row(34)}</div>
<div style="position: absolute; left: 80px; bottom: 220px">{loghi("bianco",False,170)}</div></div>'''
    return o

# ---------------- C · QUADERNO ----------------
CARTA="background-color: #fdfcf7; background-image: linear-gradient(90deg, transparent 118px, rgba(229,36,94,0.35) 118px, rgba(229,36,94,0.35) 121px, transparent 121px), repeating-linear-gradient(180deg, transparent 0, transparent 57px, rgba(1,99,165,0.18) 57px, rgba(1,99,165,0.18) 59px)"
def tape(x,y,rot,w=150):
    return f'<div style="position: absolute; left: {x}px; top: {y}px; width: {w}px; height: 46px; background: rgba(248,186,50,0.55); transform: rotate({rot}deg); z-index: 3"></div>'
def foto_t(src,alt,x,y,w,h,rot,cap=None,capfs=44):
    c=f'<div style="font-family: {HAND}; font-size: {capfs}px; line-height: 1; color: {INK}; text-align: center; padding-top: 10px">{cap}</div>' if cap else ''
    return f'<div style="position: absolute; left: {x}px; top: {y}px; width: {w}px; background: #ffffff; padding: 16px 16px {20 if cap else 16}px; box-sizing: border-box; transform: rotate({rot}deg); box-shadow: 0 12px 26px rgba(0,0,0,0.18); z-index: 2"><img src="{src}" alt="{alt}" style="width: 100%; height: {h}px; object-fit: cover; display: block">{c}</div>'+tape(x+w/2-75,y-20,rot*-2)
def evid(t,col=GIA):
    return f'<span style="background: linear-gradient(transparent 52%, {col} 52%, {col} 92%, transparent 92%); padding: 0 6px">{t}</span>'
FRECCIA='<svg width="150" height="110" viewBox="0 0 150 110" fill="none" stroke="#1d1d1b" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M8 20 C 50 0, 110 20, 128 80"></path><path d="M106 70 L 129 84 L 138 58"></path></svg>'
def stileC(e):
    o={}
    titolo=lambda fs:f'<div style="font-size: {round(fs*.3)}px; line-height: 1.2; font-weight: 900; letter-spacing: 0.12em; color: {BLU}">{e["kicker"].upper()}</div><div style="font-size: {fs}px; line-height: {round(fs*1.02)}px; font-weight: 900; color: {INK}">{evid("Il Natale")}<br>è nell\'aria</div><div style="font-family: {HAND}; font-size: {round(fs*.5)}px; line-height: 1; color: {BLU}; margin-top: 8px">{e["sub"]}</div>'
    o['P1']=root(1080,1350,'#fdfcf7',INK,'; '+CARTA)+f'<div style="position: absolute; left: 150px; top: 90px; width: 860px">{titolo(120)}</div>'+foto_t(e['f1'],e['f1alt'],170,560,560,520,-3)+f'<div style="position: absolute; left: 740px; top: 640px; font-family: {HAND}; font-size: 56px; line-height: 56px; color: {INK}; transform: rotate(4deg)">4 martedì,<br>ore 15–17!</div><div style="position: absolute; left: 700px; top: 780px; transform: scaleX(-1) rotate(10deg)">{FRECCIA}</div>{nexi(e,"right: 0; top: 880px; height: 380px")}<div style="position: absolute; left: 150px; bottom: 60px">{loghi("colori",False,170)}</div></div>'
    sm=e['small']
    o['P2']=root(1080,1350,'#fdfcf7',INK,'; '+CARTA)+f'<div style="position: absolute; left: 150px; top: 90px; font-size: 84px; line-height: 90px; font-weight: 900">Cosa {evid("creeremo")}</div>'+foto_t(sm[0][0],sm[0][1],170,300,400,330,-4,sm[0][1])+foto_t(sm[1][0],sm[1][1],600,380,400,330,3,sm[1][1])+foto_t(sm[2][0],sm[2][1],320,790,440,360,-1,sm[2][1])+f'<div style="position: absolute; left: 780px; top: 900px; font-family: {HAND}; font-size: 52px; line-height: 56px; transform: rotate(-4deg); color: {BLU}">i materiali<br>li mettiamo noi</div><div style="position: absolute; left: 150px; bottom: 60px">{loghi("colori",False,150)}</div></div>'
    dd=''.join(f'<div style="width: 170px; height: 170px; border: 5px solid {BLU}; border-radius: 50% 46% 52% 44%; display: flex; flex-direction: column; align-items: center; justify-content: center; transform: rotate({r}deg)"><div style="font-size: 76px; line-height: 70px; font-weight: 900">{a}</div><div style="font-family: {HAND}; font-size: 44px; line-height: 40px; color: {BLU}">{b}</div></div>' for (a,b),r in zip(e['date'],[-4,3,-2,5]))
    rows=''.join(f'<div style="font-size: 38px; line-height: 58px"><b style="font-weight: 900">{k}:</b> {v}</div>' for k,v in e['info'])
    o['P3']=root(1080,1350,'#fdfcf7',INK,'; '+CARTA)+f'<div style="position: absolute; left: 150px; top: 90px; font-size: 84px; line-height: 90px; font-weight: 900">{evid("Segna le date")}</div><div style="position: absolute; left: 150px; top: 260px; display: flex; gap: 26px">{dd}</div><div style="position: absolute; left: 150px; top: 520px; font-family: {HAND}; font-size: 54px; color: {BLU}">sempre di martedì, dalle 15 alle 17</div><div style="position: absolute; left: 150px; top: 640px; width: 860px">{rows}</div>{nexi(e,"right: 0; top: 980px; height: 300px")}<div style="position: absolute; left: 150px; bottom: 60px">{loghi("colori",False,150)}</div></div>'
    o['WA']=root(1080,1080,'#fdfcf7',INK,'; '+CARTA)+f'<div style="position: absolute; left: 150px; top: 60px; width: 860px">{titolo(104)}</div>'+foto_t(e['f1'],e['f1alt'],160,470,440,400,-3)+f'<div style="position: absolute; left: 640px; top: 520px; font-family: {HAND}; font-size: 52px; line-height: 54px; transform: rotate(4deg)">dal 17 novembre<br>4 martedì<br>ore 15–17</div><div style="position: absolute; left: 640px; top: 720px; font-size: 32px; font-weight: 900; color: {BLU}">GRATIS PER I SOCI</div>{nexi(e,"right: 0; top: 760px; height: 300px")}<div style="position: absolute; left: 640px; bottom: 50px">{loghi("colori",False,150)}</div></div>'
    o['WA2']=root(1080,1080,'#fdfcf7',INK,'; '+CARTA)+f'<div style="position: absolute; left: 150px; top: 80px; font-family: {HAND}; font-size: 80px; color: {BLU}; transform: rotate(-3deg)">ci siamo quasi!</div><div style="position: absolute; left: 150px; top: 190px; font-size: 120px; line-height: 120px; font-weight: 900">mancano<br>{evid("3 giorni",GIA)}</div><div style="position: absolute; left: 150px; top: 470px; font-size: 52px; line-height: 64px; font-weight: 300">{e["manca"]} di<br><b style="font-weight: 900">Il Natale è nell\'aria</b></div><div style="position: absolute; left: 150px; top: 700px; width: 600px; font-family: {HAND}; font-size: 48px; line-height: 52px; color: {BLU}">{e["prom"]}</div>{nexi(e,"right: 0; top: 520px; height: 420px")}<div style="position: absolute; left: 150px; bottom: 50px">{loghi("colori",False,150)}</div></div>'
    o['S']=root(1080,1920,'#fdfcf7',INK,'; '+CARTA)+f'<div style="position: absolute; left: 150px; top: 260px; width: 860px">{titolo(130)}</div>'+foto_t(e['f1'],e['f1alt'],170,780,620,560,-3)+f'<div style="position: absolute; left: 180px; top: 1420px; font-family: {HAND}; font-size: 64px; line-height: 64px; transform: rotate(-2deg)">4 martedì, ore 15–17 · in sede</div>{nexi(e,"right: 0; top: 1050px; height: 440px")}<div style="position: absolute; left: 150px; bottom: 300px; background: {BLU}; color: #ffffff; padding: 16px 34px; font-size: 38px; font-weight: 900; transform: rotate(-2deg)">SCRIVICI SU WHATSAPP</div><div style="position: absolute; left: 150px; bottom: 200px">{loghi("colori",False,170)}</div></div>'
    o['S2']=root(1080,1920,'#fdfcf7',INK,'; '+CARTA)+f'<div style="position: absolute; left: 150px; top: 300px; font-family: {HAND}; font-size: 96px; color: {BLU}; transform: rotate(-3deg)">ci siamo quasi!</div><div style="position: absolute; left: 150px; top: 440px; font-size: 150px; line-height: 150px; font-weight: 900">mancano</div><div style="position: absolute; left: 130px; top: 590px; font-size: 520px; line-height: 460px; font-weight: 900">{evid("3",GIA)}</div><div style="position: absolute; left: 150px; top: 1060px; font-size: 150px; line-height: 150px; font-weight: 900">giorni</div><div style="position: absolute; left: 150px; top: 1250px; width: 820px; font-size: 52px; line-height: 64px; font-weight: 300">{e["manca"]} di <b style="font-weight: 900">Il Natale è nell\'aria</b></div><div style="position: absolute; left: 150px; top: 1420px; width: 640px; font-family: {HAND}; font-size: 56px; line-height: 60px; color: {BLU}">{e["prom"]}</div>{nexi(e,"right: 0; top: 1240px; height: 420px")}<div style="position: absolute; left: 150px; bottom: 200px">{loghi("colori",False,170)}</div></div>'
    return o

# ---------------- D · SFUMATO ----------------
def sfondo(src,w,h,grad):
    return f'<img src="{src}" alt="" aria-hidden="true" style="position: absolute; left: -80px; top: -80px; width: {w+160}px; height: {h+160}px; object-fit: cover; filter: blur(34px) saturate(1.3)"><div style="position: absolute; inset: 0; background: {grad}"></div>'
GRAD_D='linear-gradient(160deg, rgba(239,125,50,0.55) 0%, rgba(146,44,125,0.35) 55%, rgba(1,99,165,0.45) 100%)'
def cap(t,b=50):
    return f'<div style="position: absolute; left: 0; right: 0; bottom: {b}px; text-align: center; font-size: 26px; font-weight: 300; color: rgba(255,255,255,0.8); letter-spacing: 0.04em">{t}</div>'
def tondo(n,size=70,top=70):
    return f'<div style="position: absolute; left: 50%; top: {top}px; transform: translateX(-50%); width: {size}px; height: {size}px; border-radius: 50%; border: 3px solid #ffffff; display: flex; align-items: center; justify-content: center; font-size: {round(size*(.55 if len(str(n))<3 else .32))}px; font-weight: 800">{n}</div>'
def stileD(e):
    o={}
    mix=lambda fs:f'<div style="font-size: {fs}px; line-height: {round(fs*1.08)}px; font-weight: 800; text-align: center">Sette giorni<br><span style="font-family: {SERIF}; font-style: italic; font-weight: 400; font-size: {round(fs*1.25)}px">per sentire</span><br>Dresda e Praga</div>'
    o['P1']=root(1080,1350,INK)+sfondo(e['f1'],1080,1350,GRAD_D)+tondo('1')+f'<div style="position: absolute; left: 80px; right: 80px; top: 360px">{mix(110)}</div><div style="position: absolute; left: 0; right: 0; top: 860px; text-align: center; font-size: 38px; font-weight: 600">29 marzo – 4 aprile 2027</div>{nexi(e,"right: 0; top: 920px; height: 360px")}<div style="position: absolute; left: 0; right: 0; bottom: 110px; display: flex; justify-content: center">{loghi("bianco",True,150)}</div>'+cap('Arkè i5sensi · viaggio',50)+'</div>'
    o['P2']=root(1080,1350,INK)+sfondo(e['f2'],1080,1350,GRAD_D)+tondo('2')+f'<img src="{e["f2"]}" alt="{e["f2alt"]}" style="position: absolute; left: 190px; top: 200px; width: 700px; height: 760px; object-fit: cover; border-radius: 350px 350px 40px 40px; box-shadow: 0 30px 60px rgba(0,0,0,0.3)"><div style="position: absolute; left: 80px; right: 80px; top: 1010px; text-align: center; font-size: 48px; line-height: 60px; font-weight: 800">Dresda, Praga<br>e la <span style="font-family: {SERIF}; font-style: italic; font-weight: 400; font-size: 62px">Svizzera Sassone</span></div>'+cap('Dresda',50)+'</div>'
    rows=''.join(f'<div style="display: flex; flex-direction: column; align-items: center; gap: 4px"><div style="font-size: 26px; font-weight: 300; letter-spacing: 0.1em">{k.upper()}</div><div style="font-size: 50px; line-height: 58px; font-weight: 800">{v}</div></div>' for k,v in e['info'])
    o['P3']=root(1080,1350,INK)+sfondo(e['f3'],1080,1350,GRAD_D)+tondo('3')+f'<div style="position: absolute; left: 80px; right: 80px; top: 220px; display: flex; flex-direction: column; gap: 46px; text-align: center">{rows}</div><div style="position: absolute; left: 0; right: 0; bottom: 110px; display: flex; justify-content: center">{loghi("bianco",True,150)}</div>'+cap('nexusghedi.it',50)+'</div>'
    o['WA']=root(1080,1080,INK)+sfondo(e['f1'],1080,1080,GRAD_D)+f'<img src="{e["f1"]}" alt="{e["f1alt"]}" style="position: absolute; left: 90px; top: 420px; width: 420px; height: 540px; object-fit: cover; border-radius: 210px 210px 30px 30px; box-shadow: 0 30px 60px rgba(0,0,0,0.3)"><div style="position: absolute; left: 80px; right: 80px; top: 70px">{mix(84)}</div><div style="position: absolute; left: 560px; top: 520px; right: 60px; font-size: 40px; line-height: 52px; font-weight: 700">29 marzo –<br>4 aprile 2027<br><span style="font-weight: 300">7 giorni in aereo<br>2.495 € tutto incluso</span></div>{nexi(e,"right: 0; top: 760px; height: 300px")}<div style="position: absolute; left: 560px; bottom: 60px">{loghi("bianco",True,140)}</div></div>'
    o['WA2']=root(1080,1080,INK)+sfondo(e['f2'],1080,1080,'linear-gradient(200deg, rgba(239,125,50,0.6), rgba(197,201,234,0.55))')+f'<div style="position: absolute; left: 50%; top: 130px; transform: translateX(-50%); width: 400px; height: 400px; border-radius: 50%; background: rgba(255,255,255,0.18); border: 4px solid #ffffff; display: flex; align-items: center; justify-content: center; font-size: 300px; line-height: 1; font-weight: 800">3</div><div style="position: absolute; left: 80px; right: 80px; top: 580px; text-align: center; font-size: 76px; line-height: 84px; font-weight: 800">giorni <span style="font-family: {SERIF}; font-style: italic; font-weight: 400; font-size: 92px">{e["manca"]}</span></div><div style="position: absolute; left: 80px; right: 80px; top: 790px; text-align: center; font-size: 36px; line-height: 46px; font-weight: 600">Dresda e Praga · {e["prom"]}</div><div style="position: absolute; left: 0; right: 0; bottom: 50px; display: flex; justify-content: center">{loghi("bianco",True,140)}</div></div>'
    o['S']=root(1080,1920,INK)+sfondo(e['f1'],1080,1920,GRAD_D)+f'<img src="{e["f1"]}" alt="{e["f1alt"]}" style="position: absolute; left: 190px; top: 240px; width: 700px; height: 820px; object-fit: cover; border-radius: 350px 350px 40px 40px; box-shadow: 0 30px 60px rgba(0,0,0,0.3)"><div style="position: absolute; left: 80px; right: 80px; top: 1110px">{mix(96)}</div><div style="position: absolute; left: 0; right: 0; top: 1500px; text-align: center; font-size: 40px; font-weight: 600">29 marzo – 4 aprile 2027</div>{nexi(e,"right: 0; top: 760px; height: 420px")}<div style="position: absolute; left: 0; right: 0; bottom: 200px; display: flex; justify-content: center">{loghi("bianco",True,170)}</div></div>'
    o['S2']=root(1080,1920,INK)+sfondo(e['f2'],1080,1920,'linear-gradient(200deg, rgba(239,125,50,0.6), rgba(197,201,234,0.55))')+f'<div style="position: absolute; left: 50%; top: 360px; transform: translateX(-50%); width: 560px; height: 560px; border-radius: 50%; background: rgba(255,255,255,0.18); border: 5px solid #ffffff; display: flex; align-items: center; justify-content: center; font-size: 420px; line-height: 1; font-weight: 800">3</div><div style="position: absolute; left: 80px; right: 80px; top: 1000px; text-align: center; font-size: 96px; line-height: 104px; font-weight: 800">giorni<br><span style="font-family: {SERIF}; font-style: italic; font-weight: 400; font-size: 110px">{e["manca"]}</span></div><div style="position: absolute; left: 100px; right: 100px; top: 1360px; text-align: center; font-size: 42px; line-height: 54px; font-weight: 600">Dresda e Praga<br>{e["prom"]}</div><div style="position: absolute; left: 0; right: 0; bottom: 300px; display: flex; justify-content: center"><div style="background: #ffffff; color: {INK}; border-radius: 999px; padding: 22px 46px; font-size: 38px; font-weight: 800">ISCRIVITI · LINK QUI</div></div><div style="position: absolute; left: 0; right: 0; bottom: 190px; display: flex; justify-content: center">{loghi("bianco",True,170)}</div></div>'
    return o

# ---------------- E · TIPO GRANDE E FINESTRE ----------------
def angoli(t1,t2,t3,t4,col):
    s=f'font-size: 20px; font-weight: 800; letter-spacing: 0.12em; color: {col}'
    return f'<div style="position: absolute; left: 50px; top: 40px; {s}">{t1}</div><div style="position: absolute; right: 50px; top: 40px; {s}">{t2}</div><div style="position: absolute; left: 50px; bottom: 40px; {s}">{t3}</div><div style="position: absolute; right: 50px; bottom: 40px; {s}">{t4}</div>'
def petali(cx,cy,r,col):
    out=''
    for i in range(8):
        import math
        a=i*math.pi/4;x=cx+math.cos(a)*r-90;y=cy+math.sin(a)*r-90
        out+=f'<div style="position: absolute; left: {x:.0f}px; top: {y:.0f}px; width: 180px; height: 180px; background: {col}; border-radius: 0 100% 0 100%; transform: rotate({i*45+45}deg)"></div>'
    return out
def stileE(e):
    o={};A='NEXUS APS';Bt='NEXUSGHEDI.IT';C='5–10 DIC 2026';D='VIAGGI'
    o['P1']=root(1080,1350,CREMA,AR)+angoli(A,Bt,C,D,AR)+f'<img src="{e["f1"]}" alt="{e["f1alt"]}" style="position: absolute; left: 290px; top: 360px; width: 500px; height: 640px; object-fit: cover; border-radius: 250px 250px 30px 30px"><div style="position: absolute; left: 0; right: 0; top: 150px; text-align: center; font-size: 300px; line-height: 300px; font-weight: 900; letter-spacing: -0.05em; mix-blend-mode: multiply">salento</div><div style="position: absolute; left: 0; right: 0; top: 1040px; text-align: center; font-size: 40px; line-height: 50px; font-weight: 800; color: {INK}">un risveglio per i cinque sensi</div><div style="position: absolute; left: 0; right: 0; top: 1110px; display: flex; justify-content: center"><div style="background: {AR}; color: {INK}; border-radius: 999px; padding: 10px 30px; font-size: 30px; font-weight: 800">5–10 dicembre · aereo e bus GT</div></div>{nexi(e,"right: 0; top: 560px; height: 380px")}</div>'
    o['P2']=root(1080,1350,AR,INK)+angoli(A,Bt,C,D,INK)+petali(540,560,250,CREMA)+f'<img src="{e["f2"]}" alt="{e["f2alt"]}" style="position: absolute; left: 340px; top: 360px; width: 400px; height: 400px; object-fit: cover; border-radius: 30px"><div style="position: absolute; left: 0; right: 0; top: 500px; text-align: center; font-family: {SERIF}; font-style: italic; font-size: 130px; color: #ffffff; text-shadow: 0 4px 24px rgba(0,0,0,0.35)">cinque sensi</div><div style="position: absolute; left: 140px; right: 140px; top: 960px; text-align: center; font-size: 32px; line-height: 44px; font-weight: 800; letter-spacing: 0.04em; text-transform: uppercase">la pietra leccese, il mare, il pasticciotto, una serata di pizzica</div></div>'
    o['P3']=root(1080,1350,CREMA,AR)+angoli(A,Bt,C,D,AR)+f'<img src="{e["f3"]}" alt="{e["f3alt"]}" style="position: absolute; left: 340px; top: 120px; width: 400px; height: 400px; object-fit: cover; border-radius: 50%"><div style="position: absolute; left: 110px; right: 110px; top: 590px; font-size: 100px; line-height: 96px; font-weight: 900; letter-spacing: -0.03em">Otranto, Leuca,<br>Gallipoli, Lecce.</div><div style="position: absolute; left: 110px; right: 110px; top: 820px; font-size: 32px; line-height: 44px; font-weight: 700; text-transform: uppercase; color: {AR}">E poi Ostuni, Nardò, Galatina, Martina Franca: sei giorni con volo da Linate e pullman GT, guida e pasti compresi.</div><div style="position: absolute; left: 110px; bottom: 110px">{loghi("colori",False,150)}</div></div>'
    o['WA']=root(1080,1080,AR,CREMA)+angoli(A,Bt,C,D,CREMA)+f'<img src="{e["f1"]}" alt="{e["f1alt"]}" style="position: absolute; left: 330px; top: 300px; width: 420px; height: 520px; object-fit: cover; border-radius: 210px 210px 30px 30px"><div style="position: absolute; left: 0; right: 0; top: 120px; text-align: center; font-size: 250px; line-height: 250px; font-weight: 900; letter-spacing: -0.05em">salento</div><div style="position: absolute; left: 0; right: 0; top: 860px; text-align: center; font-size: 40px; font-weight: 800; color: {INK}">5–10 dicembre · un risveglio per i cinque sensi</div>{nexi(e,"right: 0; top: 520px; height: 320px")}<div style="position: absolute; left: 0; right: 0; bottom: 90px; display: flex; justify-content: center">{loghi("nero",False,150)}</div></div>'
    o['WA2']=root(1080,1080,CREMA,AR)+petali(540,470,230,AR)+f'<img src="{e["f2"]}" alt="{e["f2alt"]}" style="position: absolute; left: 365px; top: 295px; width: 350px; height: 350px; object-fit: cover; border-radius: 30px; filter: grayscale(0.2)"><div style="position: absolute; left: 0; right: 0; top: 400px; text-align: center; font-family: {SERIF}; font-style: italic; font-size: 120px; color: #ffffff; text-shadow: 0 4px 24px rgba(0,0,0,0.4)">mancano 3</div><div style="position: absolute; left: 0; right: 0; top: 800px; text-align: center; font-size: 46px; font-weight: 900; text-transform: uppercase">giorni {e["manca"]}</div><div style="position: absolute; left: 120px; right: 120px; top: 880px; text-align: center; font-size: 30px; line-height: 40px; font-weight: 700; color: {INK}">{e["prom"]}</div>'+angoli(A,Bt,'SALENTO','VIAGGI',AR)+'</div>'
    o['S']=root(1080,1920,CREMA,AR)+angoli(A,Bt,C,D,AR)+f'<img src="{e["f1"]}" alt="{e["f1alt"]}" style="position: absolute; left: 240px; top: 560px; width: 600px; height: 800px; object-fit: cover; border-radius: 300px 300px 40px 40px"><div style="position: absolute; left: 0; right: 0; top: 320px; text-align: center; font-size: 300px; line-height: 300px; font-weight: 900; letter-spacing: -0.05em; mix-blend-mode: multiply">salento</div><div style="position: absolute; left: 0; right: 0; top: 1400px; text-align: center; font-size: 46px; line-height: 56px; font-weight: 800; color: {INK}">un risveglio per i cinque sensi<br><span style="color: {AR}">5–10 dicembre 2026</span></div>{nexi(e,"right: 0; top: 900px; height: 460px")}<div style="position: absolute; left: 0; right: 0; bottom: 230px; display: flex; justify-content: center">{loghi("colori",False,170)}</div></div>'
    o['S2']=root(1080,1920,AR,INK)+petali(540,820,270,CREMA)+f'<img src="{e["f2"]}" alt="{e["f2alt"]}" style="position: absolute; left: 330px; top: 610px; width: 420px; height: 420px; object-fit: cover; border-radius: 30px"><div style="position: absolute; left: 0; right: 0; top: 740px; text-align: center; font-family: {SERIF}; font-style: italic; font-size: 150px; color: #ffffff; text-shadow: 0 4px 24px rgba(0,0,0,0.4)">mancano 3</div><div style="position: absolute; left: 0; right: 0; top: 1240px; text-align: center; font-size: 64px; font-weight: 900; text-transform: uppercase">giorni {e["manca"]}</div><div style="position: absolute; left: 120px; right: 120px; top: 1340px; text-align: center; font-size: 40px; line-height: 52px; font-weight: 700; color: {CREMA}">{e["prom"]}</div>'+angoli(A,Bt,'SALENTO','VIAGGI',INK)+f'<div style="position: absolute; left: 0; right: 0; bottom: 230px; display: flex; justify-content: center">{loghi("nero",False,170)}</div></div>'
    return o

# ---------------- F · GRADIENTE ----------------
def mesh(w,h,seed=0):
    sets=[('#ef7d32',20,20),('#f6a7b8',75,25),('#f8ba32',30,75),(LAV,85,80),('#e74035',60,55)]
    if seed:sets=[('#ef7d32',70,30),(LAV,20,25),('#f6a7b8',40,80),('#f8ba32',85,75),('#922c7d',15,60)]
    bg=', '.join(f'radial-gradient(circle at {x}% {y}%, {c} 0%, transparent 55%)' for c,x,y in sets)
    return f'<div style="position: absolute; inset: -60px; background: {bg}, {LAV}; filter: blur(40px)"></div>'
def stileF(e):
    o={}
    txt=lambda t,fs,top:f'<div style="position: absolute; left: 140px; right: 140px; top: {top}px; text-align: center; font-size: {fs}px; line-height: {round(fs*1.18)}px; font-weight: 800">{t}</div>'
    o['P1']=root(1080,1350,LAV)+mesh(1080,1350)+tondo('29',110,110)+txt('Dalí, Verdi<br>e un aperitivo<br>in centro.',96,430)+f'<div style="position: absolute; left: 0; right: 0; top: 900px; text-align: center; font-size: 40px; font-weight: 800">Milano · martedì 29 dicembre</div>{nexi(e,"right: 0; top: 960px; height: 300px")}'+cap('una giornata con Nexus APS',60)+'</div>'
    o['P2']=root(1080,1350,'#f4f3f1',LAV)+f'<div style="position: absolute; left: 110px; top: 120px; right: 110px; font-size: 96px; line-height: 104px; font-weight: 900; color: {VIO}">Cosa faremo<br>a Milano?</div><div style="position: absolute; left: 110px; right: 110px; top: 440px; display: flex; flex-direction: column; gap: 30px; font-size: 48px; line-height: 58px; font-weight: 800; color: {INK}"><div>Dalí a Palazzo Reale</div><div>La Milano di Verdi<br><span style="font-weight: 300">con i visori VR</span></div><div>Un aperitivo in centro</div></div><div style="position: absolute; left: 0; right: 0; bottom: 0; height: 200px; overflow: hidden">{mesh(1080,200,1)}</div></div>'
    o['P3']=root(1080,1350,LAV)+mesh(1080,1350,1)+tondo('85 €',150,110)+txt('Partenza da Ghedi<br>alle 7:30,<br>rientro in serata.',84,430)+f'<div style="position: absolute; left: 0; right: 0; bottom: 130px; display: flex; justify-content: center">{loghi("bianco",False,160)}</div>'+cap('programma completo su nexusghedi.it',60)+'</div>'
    o['WA']=root(1080,1080,LAV)+mesh(1080,1080)+tondo('29',100,80)+txt('Dalí, Verdi<br>e un aperitivo<br>in centro.',86,290)+f'<div style="position: absolute; left: 0; right: 0; top: 720px; text-align: center; font-size: 38px; font-weight: 800">Milano · martedì 29 dicembre · 85 €</div>{nexi(e,"right: 0; top: 700px; height: 300px")}<div style="position: absolute; left: 0; right: 0; bottom: 60px; display: flex; justify-content: center">{loghi("bianco",False,150)}</div></div>'
    o['WA2']=root(1080,1080,LAV)+mesh(1080,1080,1)+tondo('3',300,90)+txt(f'giorni<br>{e["manca"]}.',100,450)+f'<div style="position: absolute; left: 140px; right: 140px; top: 740px; text-align: center; font-size: 38px; line-height: 50px; font-weight: 600">{e["prom"]}</div>'+cap('Milano · Dalí, Verdi e un aperitivo',60)+'</div>'
    o['S']=root(1080,1920,LAV)+mesh(1080,1920)+tondo('29',130,280)+txt('Dalí, Verdi<br>e un aperitivo<br>in centro.',110,620)+f'<div style="position: absolute; left: 0; right: 0; top: 1150px; text-align: center; font-size: 44px; font-weight: 800">Milano · martedì 29 dicembre</div>{nexi(e,"right: 0; top: 1230px; height: 380px")}<div style="position: absolute; left: 0; right: 0; bottom: 230px; display: flex; justify-content: center">{loghi("bianco",False,170)}</div></div>'
    o['S2']=root(1080,1920,LAV)+mesh(1080,1920,1)+tondo('3',440,300)+txt(f'giorni<br>{e["manca"]}.',112,820)+f'<div style="position: absolute; left: 140px; right: 140px; top: 1150px; text-align: center; font-size: 44px; line-height: 56px; font-weight: 600">{e["prom"]}</div>'+cap('Milano · Dalí, Verdi e un aperitivo',230)+'</div>'
    return o

STILI=[('A','Etichette',FONT,stileA,'come nastri di carta: testo in strisce piene sopra la foto'),('B','Editoriale',LAUD,stileB,'serif grande, numero della data gigante, righe con icone'),('C','Quaderno',NAT,stileC,'carta a righe, foto con lo scotch, scritte a mano, evidenziatore'),('D','Sfumato',DRES,stileD,'foto sfocata e colorata, testo bianco con una parola in corsivo'),('E','Parola grande',SAL,stileE,'una parola enorme, foto in una finestra ad arco, petali')]  # F Gradiente: scartato dall'utente (12/11/2026)
c=json.load(open(P+'canvas.json'))
if not any(p['id']=='stili' for p in c['pages']):c['pages'].append({'id':'stili','name':'Stili nuovi · 6 stili declinati (post 3 immagini, WhatsApp e storie: notizia e promemoria)'})
c['notes']=c.get('notes',{})
ordine=['P1','P2','P3','WA','WA2','S','S2'];y=300
for L,nome,ev,fn,desc in STILI:
    out=fn(ev);x=0
    for k in ordine:
        w,h=SIZES[k];f=f'Stile-{L}-{ev["id"]}-{k}.dc.html'
        open(P+f,'w').write(wrap(f'Stile {L} {nome} · {ev["nome"]} · {NOMI[k]}',out[k],w,h))
        c['boards'][f]={'x':x,'y':y,'w':w,'h':h,'page':'stili','title':f'{L} · {nome} · {NOMI[k]}'}
        if f not in c['order']:c['order'].append(f)
        x+=w+80
    c['notes'][f'stile{L}']={'x':0,'y':y-260,'text':f'{L} · {nome} — {desc} (esempio: {ev["nome"]})','kind':'title1','maxW':x-80,'page':'stili'}
    y+=1920+400
json.dump(c,open(P+'canvas.json','w'),ensure_ascii=False,indent=1)
print('ok')
