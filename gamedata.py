import requests
from bs4 import BeautifulSoup
import sys

sys.path.append("..")
from model.model import *

req = requests.get('https://futbolme.com/resultados-directo/torneo/preferente-grupo-2/57/1')
soup = BeautifulSoup(req.text, "lxml")

jornada = soup.title.text.split(' - ')[3]
numjornada = jornada.split(' ')[1]

matchdivs = soup.find_all("div", class_="boxpartido")
fecha = soup.find("div", class_="cajanaranja").text

lmatchs = []

for div in matchdivs:
    match = div.meta['content']
    teams = match.split(' - ')
    local = teams[0]
    visiting = teams[1]
    reslocal = div.find("p", class_="reboxL").text
    resvis = div.find("p", class_="reboxR").text
    p = Partido(local, visiting, reslocal, resvis, numjornada)
    print(p)
    lmatchs.append(p)

# jornada = Jornada(numjornada, fecha, lmatchs)
# print(jornada)
