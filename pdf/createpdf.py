from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.pdfbase.pdfmetrics import stringWidth

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
#c.setFont("Courier-BoldOblique", 12)

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
c.grid(xl2, yl2)
equipo1 = "CF SAN AGUSTÍN DEL GUADALIX 'A'"
equipo2 = "CD DOSA"
c.drawString(50, h-135, equipo1)
c.drawString(302, h-135, equipo2)

#Equipo Arbitral
arbitro = "D. Rafael Hidalgo Alejo"
aa1 = "D. Diego Retamar García"
aa2 = "D. José Adrián González Peláez"
dp = "D. nodata"
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

c.showPage()
c.save()
