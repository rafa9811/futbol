from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.platypus import Table, TableStyle

from reportlab.platypus import Flowable

def splitString(maxLenght, str):
    s = str
    if len(str) > maxLenght:
        aux = str.split(" ", 1)
        s = aux[0]
        if len(aux[1]) > maxLenght:
            aux2 = aux[1].split(" ", 1)
            s = s + " " + aux2[0]
            for c in aux2[1:]:
                s += '\n' + c
        else:
            for c in aux[1:]:
                s += '\n' + c
    return s


w, h = A4 # 595.2 puntos de ancho (width) y 841.8 puntos de alto (height).

c = canvas.Canvas("previa.pdf", pagesize=A4)
c.setFont("Helvetica", 12)

# Título de documento.
c.drawString(235, h - 50, "PREVIA DE PARTIDO")

#Grid de datos principales.
xl1 = [45, 150, 280, 350, 450, 555]
xl2 = [45, 297, 555]
yl1 = [h-65, h-100]
yl2 = [h-100, h-170]

c.grid(xl1, yl1)
c.drawString(50, h-80, "Fecha")
c.drawString(178, h-80, "CATEGORÍA")
grupo = "1"
c.drawString(155, h-93, "PREFERENTE, GR. " + grupo)
hora = "12:00"
c.drawString(300, h-87, hora)

jornada = "22"
iv = "Vuelta (Ida: 0-2)"
c.drawString(370, h-80, "Jornada " + jornada)
c.drawString(358, h-93, iv)

tipocampo = "(HA)"
campo = "Román Valero " + tipocampo
tc = c.beginText(455, h-80)
tc.textLines( splitString(15, campo) )
c.drawText(tc)

#Grid de equipos
# c.grid(xl2, yl2)
equipo1 = "CF SAN AGUSTÍN DEL GUADALIX 'A'"
equipo2 = "CD DOSA"
# c.drawString(50, h-140, equipo1)
# c.drawString(302, h-140, equipo2)

data = [[equipo1, equipo2]]
t = Table(data, colWidths=[255, 255], rowHeights=[70])
t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),colors.lavender),
('INNERGRID', (0,0), (-1,-1), 1, colors.black),
('ALIGN',(0,0),(-1,-1),'CENTER'),
('VALIGN',(0,0),(-1,-1),'MIDDLE'),
('BOX', (0,0), (-1,-1), 1, colors.black),
('FONTNAME', (0,0), (-1,-1), 'Helvetica-Bold')]))
t.wrapOn(c, w, h)
t.drawOn(c, 45, h-170)


#Equipo Arbitral
arbitro = "D. Rafael Hidalgo Alejo"
aa1 = "D. Diego Retamar García"
aa2 = "D. José Adrián González Peláez"
dp = "D. nodata, nodata"
comite = "COMITÉ MADRILEÑO"

eqa = c.beginText(45, h-195)
eqa.setFont("Helvetica-Bold", 12)
eqa.textLine("EQUIPO ARBITRAL:")
c.drawText(eqa)

c.drawString(75, h-220, "Árbitro: ")
c.drawString(75, h-240, "Asistente 1: ")
c.drawString(75, h-260, "Asistente 2: ")
c.drawString(75, h-280, "Delegado de partido: ")

eqa.setFont("Helvetica", 12)
c.drawText(eqa)

c.drawString(125, h-220, arbitro + " - " + comite)
c.drawString(149, h-240, aa1 + " - " + comite)
c.drawString(149, h-260, aa2 + " - " + comite)
c.drawString(199, h-280, dp + " - " + comite)

#Tablas de estadísitcas numéricas
data1 = [
['', 'PG', 'PE', 'PP', 'GF', 'GC'],
['Tot', '20', '21', '22', '23', '24'],
['Loc','20', '21', '22', '23', '24'],
['Últ', '31', '32', '33', '34', '34']
]
data2 = [
['PG', 'PE', 'PP', 'GF', 'GC', ''],
['20', '21', '22', '23', '24', 'Tot'],
['20', '21', '22', '23', '24', 'Vis'],
['31', '32', '33', '34', '34', 'Últ']
]
t1 = Table(data1)
t2 = Table(data2)

t1.setStyle(TableStyle([('BACKGROUND',(1,0),(1,0),colors.green),
('BACKGROUND',(2,0),(2,0),colors.orange),
('BACKGROUND',(3,0),(3,0),colors.red),
('TEXTCOLOR',(1,1),(1,2),colors.green),
('TEXTCOLOR',(2,1),(2,2),colors.orange),
('TEXTCOLOR',(3,1),(3,2),colors.red),
('FONTNAME', (1,0), (5,0), 'Helvetica-Bold'),
('INNERGRID', (1,0), (-1,-1), 0.25, colors.black),
('BOX', (1,0), (-1,-1), 0.25, colors.black)]))

t2.setStyle(TableStyle([('BACKGROUND',(0,0),(0,0),colors.green),
('BACKGROUND',(1,0),(1,0),colors.orange),
('BACKGROUND',(2,0),(2,0),colors.red),
('TEXTCOLOR',(0,1),(0,2),colors.green),
('TEXTCOLOR',(1,1),(1,2),colors.orange),
('TEXTCOLOR',(2,1),(2,2),colors.red),
('FONTNAME', (0,0), (5,0), 'Helvetica-Bold'),
('INNERGRID', (0,0), (-2,-1), 0.25, colors.black),
('BOX', (0,0), (-2,-1), 0.25, colors.black)]))

t1.wrapOn(c, w, h)
t1.drawOn(c, 40, h-390)
t2.wrapOn(c, w, h)
t2.drawOn(c, 400, h-390)

#Header de las tablas, PUNTOS.
puntos1 = '13º - 38 PUNTOS'
puntos2 = '20º - 2 PUNTOS'

data3 = [[puntos1]]
data4 = [[puntos2]]
h1 = Table(data3, colWidths=[130.02])
h2 = Table(data4, colWidths=[130.02])

h1.setStyle(TableStyle([('BACKGROUND',(0,0),(0,0),colors.lavender),
('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
('ALIGN',(0,0),(-1,-1),'CENTER'),
('BOX', (0,0), (-1,-1), 0.25, colors.black),
('FONTNAME', (0,0), (0,-1), 'Helvetica-Bold')]))

h2.setStyle(TableStyle([('BACKGROUND',(0,0),(0,0),colors.lavender),
('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
('ALIGN',(0,0),(-1,-1),'CENTER'),
('BOX', (0,0), (-1,-1), 0.25, colors.black),
('FONTNAME', (0,0), (0,-1), 'Helvetica-Bold')]))

h1.wrapOn(c, w, h)
h1.drawOn(c, 68.12, h-318)
h2.wrapOn(c, w, h)
h2.drawOn(c, 400, h-318)

c.showPage()
c.save()
