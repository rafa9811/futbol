import sys
import os

import itertools
from random import randint
from statistics import mean

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.platypus import Table, TableStyle, Image, Flowable

sys.path.append("..")
from forecast.forecast import *

########################### Auxiliar functions #################################

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


def drawCt(c, data, x_offset, y_offset, noficiales):
    global newh
    # Space between rows.
    padding = 17

    xheader = [0 + x_offset, 240 + x_offset]
    yheader = [h - y_offset - i*padding for i in range(2)]
    xlist = [x + x_offset for x in [0, 90, 240]]
    ylist = [h - y_offset - i*padding for i in range(1,noficiales + 2)]

    if ylist[-1] < (newh):
        newh = ylist[-1]

    c.grid(xheader, yheader)
    c.grid(xlist, ylist)

    c.drawString(xheader[0] + 75, yheader[0] - padding + 4, "CUERPO TÉCNICO")
    # j indica la licencia o el nombre y puede tomar valores 0 o 1.
    # z indica la fila
    z = -1
    for y in ylist[:-1]:
        j = 0
        z += 1
        for x in xlist[:-1]:
                c.drawString(x + 6, y - padding + 4, data[z][j])
                j+=1

def drawJs(c, data, x_offset, y_offset, njugadores):
    global newh2
    # Space between rows.
    padding = 17

    xheader = [0 + x_offset, 240 + x_offset]
    yheader = [h - y_offset - i*padding for i in range(2)]
    xlist = [x + x_offset for x in [0, 90, 240]]
    ylist = [h - y_offset - i*padding for i in range(1, njugadores + 2)]

    if ylist[-1] < (newh2):
        newh2 = ylist[-1]

    c.grid(xheader, yheader)
    c.grid(xlist, ylist)

    c.drawString(xheader[0] + 49, yheader[0] - padding + 4, "JUGADORES SANCIONADOS")
    # j indica la licencia o el nombre y puede tomar valores 0 o 1.
    # z indica la fila
    z = -1
    for y in ylist[:-1]:
        j = 0
        z += 1
        for x in xlist[:-1]:
                c.drawString(x + 6, y - padding + 4, data[z][j])
                j+=1

def pathIcon(id):
    path = 'icons/' + str(id) + '.png'
    return path

################################################################################

w, h = A4 # 595.2 puntos de ancho (width) y 841.8 puntos de alto (height).
newh = h  # Auxiliar height
newh2 = h # Auxiliar height 2

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

#El tiempo: prob_precipitacion, estado_cielo, vientodir, vientovel, tmax, tmin
tiempo = get_forecast('Barcelona', '07', '24')
print(tiempo)
path = pathIcon(tiempo['estado_cielo'])
I = Image(path)
I.drawHeight = 0.6*inch*I.drawHeight / I.drawWidth
I.drawWidth = 0.6*inch
dfor = [['Barcelona'], [I], ['Lluvia: ' + tiempo['prob_precipitacion'] + '%'],
        ['Viento: ' + tiempo['vientovel'] + ' km/h ' + tiempo['vientodir']]]
tfor = Table(dfor)
tfor.setStyle(TableStyle([('ALIGN',(0,0),(-1,-1),'CENTER')]))
tfor.wrapOn(c, w, h)
tfor.drawOn(c, 252, h-398)

#Equipamiento1
deq1 = [['', 'Camiseta'], ['Equipamiento', 'Pantalón'], ['', 'Medias']]
teq1 = Table(deq1, colWidths=[90, 150])
teq1.setStyle(TableStyle([('ALIGN',(0,0),(-1,-1),'CENTER'),
('BOX', (0,0), (-1,-1), 1, colors.black),
('INNERGRID', (1,0), (-1,-1), 1, colors.black)]))
teq1.wrapOn(c, w, h)
teq1.drawOn(c, 45, h-470)

#Equipamiento2
deq2 = [['', 'Camiseta'], ['Equipamiento', 'Pantalón'], ['', 'Medias']]
teq2 = Table(deq2, colWidths=[90, 150])
teq2.setStyle(TableStyle([('ALIGN',(0,0),(-1,-1),'CENTER'),
('BOX', (0,0), (-1,-1), 1, colors.black),
('INNERGRID', (1,0), (-1,-1), 1, colors.black)]))
teq2.wrapOn(c, w, h)
teq2.drawOn(c, 310, h-470)

#Portero1
dp1 = [['', 'Camiseta'], ['Portero', 'Pantalón'], ['', 'Medias']]
tp1 = Table(dp1, colWidths=[90, 150])
tp1.setStyle(TableStyle([('ALIGN',(0,0),(-1,-1),'CENTER'),
('BOX', (0,0), (-1,-1), 1, colors.black),
('INNERGRID', (1,0), (-1,-1), 1, colors.black)]))
tp1.wrapOn(c, w, h)
tp1.drawOn(c, 45, h-540)

#Portero2
dp2 = [['', 'Camiseta'], ['Portero', 'Pantalón'], ['', 'Medias']]
tp2 = Table(dp2, colWidths=[90, 150])
tp2.setStyle(TableStyle([('ALIGN',(0,0),(-1,-1),'CENTER'),
('BOX', (0,0), (-1,-1), 1, colors.black),
('INNERGRID', (1,0), (-1,-1), 1, colors.black)]))
tp2.wrapOn(c, w, h)
tp2.drawOn(c, 310, h-540)

#Petos1
dpe1 = [['Petos', 'Color']]
tpe1 = Table(dpe1, colWidths=[90, 150])
tpe1.setStyle(TableStyle([('ALIGN',(0,0),(-1,-1),'CENTER'),
('BOX', (0,0), (-1,-1), 1, colors.black),
('INNERGRID', (0,0), (-1,-1), 1, colors.black)]))
tpe1.wrapOn(c, w, h)
tpe1.drawOn(c, 45, h-575)

#Petos2
dpe2 = [['Petos', 'Color']]
tpe2 = Table(dpe2, colWidths=[90, 150])
tpe2.setStyle(TableStyle([('ALIGN',(0,0),(-1,-1),'CENTER'),
('BOX', (0,0), (-1,-1), 1, colors.black),
('INNERGRID', (0,0), (-1,-1), 1, colors.black)]))
tpe2.wrapOn(c, w, h)
tpe2.drawOn(c, 310, h-575)

#Otros datos 1
dod1 = [['Suplentes: 5', 'Recogepelotas: ¿?'], ['Oficiales: 5', 'Fotógrafo: ¿?']]
tod1 = Table(dod1, colWidths=[90, 150])
tod1.setStyle(TableStyle([('BOX', (0,0), (-1,-1), 1, colors.black),
('INNERGRID', (0,0), (-1,-1), 1, colors.black)]))
tod1.wrapOn(c, w, h)
tod1.drawOn(c, 45, h-628)

#Otros datos 2
dod2 = [['Suplentes: 5', 'Recogepelotas: ¿?'], ['Oficiales: 5', 'Fotógrafo: ¿?']]
tod2 = Table(dod2, colWidths=[90, 150])
tod2.setStyle(TableStyle([('BOX', (0,0), (-1,-1), 1, colors.black),
('INNERGRID', (0,0), (-1,-1), 1, colors.black)]))
tod2.wrapOn(c, w, h)
tod2.drawOn(c, 310, h-628)

#Equipo técnico 1
eqa.setFont("Helvetica", 10)
c.drawText(eqa)
noficiales1 = 2
noficiales2 = 1
oficiales1 = [("tipo", "nombre"), ("tipo", "nombre2"), ("tipo3.", "nombre3")]
oficiales2 = [("tipo", "nombre"), ("tipo", "nombre2"), ("tipo3.", "nombre3")]
drawCt(c, oficiales1, 45, h-196.8, noficiales1)
drawCt(c, oficiales2, 310, h-196.8, noficiales2)

#A partir de aquí, la altura es variable. Usaremos newh en vez de h.
nsancionados1 = 1
nsancionados2 = 2
sancionados1 = [("tipo", "nombre"), ("tipo", "nombre2"), ("tipo3.", "nombre3")]
sancionados2 = [("tipo", "nombre"), ("tipo", "nombre2"), ("tipo3.", "nombre3")]
drawJs(c, sancionados1, 45, h-newh+17, nsancionados1)
drawJs(c, sancionados2, 310, h-newh+17, nsancionados2)

#Delegado de campo
eqa.setFont("Helvetica-Bold", 10)
c.drawText(eqa)
c.drawString(45, newh2-20, "Delegado de campo:")
eqa.setFont("Helvetica", 10)
c.drawText(eqa)
c.drawString(147, newh2-20, "Juan Hernández Maeso")


c.showPage()
c.save()
