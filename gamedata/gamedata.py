import requests
from bs4 import BeautifulSoup
import sys

sys.path.append("..")
from model.model import *

def grupo_request(grupo, jornada):
    if grupo == '1':
        url = 'https://futbolme.com/resultados-directo/torneo/preferente-grupo-1/56/'
        req = requests.get(url + jornada)
        soup = BeautifulSoup(req.text, "lxml")
    else:
        url = 'https://futbolme.com/resultados-directo/torneo/preferente-grupo-2/57/'
        req = requests.get(url + jornada)
        soup = BeautifulSoup(req.text, "lxml")
    return soup

def get_game_data(grupo):
    if grupo == '1' or grupo == '2':
        ljornadas = []

        for i in range(1, 50):
            soup = grupo_request(grupo, str(i))

            jornada = soup.title.text.split(' - ')[3]
            numjornada = jornada.split(' ')[1]

            #Comprobar si la jornada se ha jugado:
            comp = soup.find("span", class_="text-center marco")
            if comp != None:
                print('La jornada ' + str(i) + ' no se ha jugado en su totalidad.')
                break

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
                lmatchs.append(p)

            jornada = Jornada(numjornada, fecha, lmatchs)
            ljornadas.append(jornada)

        numt = soup.title.text.split(' - ')[2]
        temporada = Temporada(numt, ljornadas)
        return temporada

    else:
        print('El número de grupo no es el correcto')
        return

def gd_toFile(grupo):
    file = open('gamedata.txt', 'w')
    file.write(get_game_data(grupo).toString())
    file.close()

def fileToModel():
    with open('gamedata.txt', 'r') as file:
        lineas = file.readlines()

    numt = lineas[0]
    ljornadas = []
    for l in lineas[1:]:
        jp = l.split('*')
        lmatre = jp[2]
        lmat = lmatre.split('|')
        lmatchs = []

        for m in lmat[:-1]:
            data = m.split('#')
            p = Partido(data[0], data[3], data[1], data[2], jp[0])
            lmatchs.append(p)

        jornada = Jornada(jp[0], jp[1], lmatchs)
        ljornadas.append(jornada)

    temporada = Temporada(numt, ljornadas)

    return temporada


gd_toFile('1')
fileToModel()
