from reportlab.lib import colors
from bs4 import BeautifulSoup
import requests
import sys
import os

sys.path.append("..")
from model.model import *


def get_path():
    path_list = os.getcwd().split('/')
    generic_path = ""

    for elem in path_list[1:]:
        if not elem == 'futbol':
            generic_path += '/'
            generic_path += elem
        else:
            generic_path += '/'
            generic_path += elem
            break
    path = generic_path + '/gamedata/gamedata.txt'
    return path


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
                local = teams[0].strip()
                visiting = teams[1].strip()
                reslocal = div.find("p", class_="reboxL").text.strip()
                resvis = div.find("p", class_="reboxR").text.strip()
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
    file = open(get_path(), 'w')
    file.write(get_game_data(grupo).toString())
    file.close()


def fileToModel():
    with open(get_path(), 'r') as file:
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


def process_goals(temporada, team):
    against_goals = 0
    favor_goals = 0
    local_against_goals = 0
    local_favor_goals = 0
    vis_against_goals = 0
    vis_favor_goals = 0
    flag = 0

    for j in temporada.get_jornadas():
        for p in j.get_partidos():
            if p.get_local() == team or p.get_visiting() == team:
                flag = 1
                if p.get_local() == team:
                    local_favor_goals += int(p.get_reslocal())
                    local_against_goals += int(p.get_resvisiting())
                if p.get_visiting() == team:
                    vis_favor_goals += int(p.get_resvisiting())
                    vis_against_goals += int(p.get_reslocal())

    if flag == 0:
        print('El equipo introducido no se encuentra. Error')
        return -1

    against_goals = local_against_goals + vis_against_goals
    favor_goals = local_favor_goals + vis_favor_goals
    return str(against_goals), str(favor_goals), str(local_against_goals), str(local_favor_goals), str(vis_against_goals), str(vis_favor_goals)


def process_matchs(temporada, team):
    lmatchs = []
    ind = 5
    jornadas = temporada.get_jornadas()
    if len(jornadas) < 5:
        ind = len(jornadas)

    for j in jornadas[-5:]:
        for p in j.get_partidos():

            if p.get_local() == team:
                if int(p.get_reslocal()) > int(p.get_resvisiting()):
                    lmatchs.append(['G', colors.green])
                elif int(p.get_reslocal()) < int(p.get_resvisiting()):
                    lmatchs.append(['P', colors.red])
                else:
                    lmatchs.append(['E', colors.orange])

            if p.get_visiting() == team:
                if int(p.get_reslocal()) < int(p.get_resvisiting()):
                    lmatchs.append(['G', colors.green])
                elif int(p.get_reslocal()) > int(p.get_resvisiting()):
                    lmatchs.append(['P', colors.red])
                else:
                    lmatchs.append(['E', colors.orange])

    return lmatchs
