import sys,io
from pypdf import PdfReader,PdfWriter,Transformation,PageObject
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
W,H=297*mm,210*mm
def taglio():
    b=io.BytesIO();c=canvas.Canvas(b,pagesize=(W,H));c.setStrokeColorRGB(.78,.78,.78);c.setDash(3,3);c.setLineWidth(.5)
    c.line(W/2,0,W/2,H);c.setFillColorRGB(.6,.6,.6);c.setFont('Helvetica',8);c.drawCentredString(W/2,H-9,'✂ taglia qui'.replace('✂','')) ;c.save();return PdfReader(b).pages[0]
def due(sx,dx,linea=True):
    p=PageObject.create_blank_page(width=W,height=H)
    for i,src in enumerate((sx,dx)):
        a=PdfReader(src).pages[0];w=float(a.mediabox.width);h=float(a.mediabox.height)
        x=i*W/2+(W/2-w)/2;y=(H-h)/2
        p.merge_transformed_page(a,Transformation().translate(x,y))
    if linea: p.merge_page(taglio())
    return p
def scrivi(out,pagine):
    w=PdfWriter()
    for p in pagine: w.add_page(p)
    w.add_metadata({'/Title':out.split('/')[-1],'/Author':'Nexus APS'})
    w.write(out)
S='stampa/'
scrivi(S+'dresda-volantini-A5-2perfoglio-fronte-retro.pdf',[due(S+'Dresda-Volantino-A5.pdf',S+'Dresda-Volantino-A5.pdf'),due(S+'Dresda-Volantino2-A5.pdf',S+'Dresda-Volantino2-A5.pdf')])
scrivi(S+'tunisia-pieghevole-A4-fronte-retro.pdf',[due(S+'Tunisia-Pieghevole4-A5.pdf',S+'Tunisia-Pieghevole1-A5.pdf',False),due(S+'Tunisia-Pieghevole2-A5.pdf',S+'Tunisia-Pieghevole3-A5.pdf',False)])
import shutil
shutil.copy(S+'Dresda-A4.pdf',S+'dresda-locandina-A4-bacheca.pdf');shutil.copy(S+'Dresda-A3.pdf',S+'dresda-locandina-A3.pdf')
