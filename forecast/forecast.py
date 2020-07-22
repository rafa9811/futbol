import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import xml.etree.ElementTree as et
from datetime import datetime

DRIVER_PATH = os.getcwd()[:-8] + 'chromedriver'
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")


def get_id(town):
    driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
    driver.get("http://www.aemet.es/es/portada")

    driver.find_element_by_xpath("//*[@id='buscar_municipio']").send_keys(town)
    driver.find_element_by_xpath("//*[@id='columns']/div/div[2]/div[2]/div[1]/div/form/input[5]").click()

    if not driver.current_url.startswith('http://www.aemet.es/es/eltiempo/prediccion/municipios?modo=and&orden=n&tipo=sta&str='):
        url = driver.current_url
        id = url.split("id")[-1]
        return id

    driver.find_element_by_xpath('//*[@class="resultados_busqueda"]/ul/li/a[text()="'+town+'"]').click()

    url = driver.current_url
    id = url.split("id")[-1]

    driver.quit()
    return id


def download_xml(id):
    url = "http://www.aemet.es/xml/municipios/localidad_" + id + ".xml"
    response = requests.get(url)

    with open('data.xml', 'wb') as file:
        file.write(response.content)


def parse_xml(month, day):
    tree = et.parse('data.xml')
    root = tree.getroot()
    prediction = root.find('prediccion')

    year = str(datetime.now().year)
    attr = year + '-' + str(month) + '-' + str(day)

    for child in prediction:
        if child.attrib['fecha'] == attr:
            ddate = child
            break
        else: date = False

    prob_precipitacion = ddate.find('prob_precipitacion').text
    estado_cielo = ddate.find('estado_cielo').text
    viento = ddate.find('viento')
    vientodir = viento.find('direccion').text
    vientovel = viento.find('velocidad').text
    temperatura = ddate.find('temperatura')
    tmax = temperatura.find('maxima').text
    tmin = temperatura.find('minima').text

    return prob_precipitacion, estado_cielo, vientodir, vientovel, tmax, tmin


def get_forecast(town, month, day):
    id = get_id(town)
    download_xml(id)
    return parse_xml(month, day)
