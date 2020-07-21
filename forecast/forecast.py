from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import xml.etree.ElementTree as et
from datetime import datetime

DRIVER_PATH = '/Users/rafahidalgo/Desktop/entornov/futbol/forecast/chromedriver'
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")


def get_id(municipio):
    driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
    driver.get("http://www.aemet.es/es/portada")

    driver.find_element_by_xpath("//*[@id='buscar_municipio']").send_keys(municipio)
    driver.find_element_by_xpath("//*[@id='columns']/div/div[2]/div[2]/div[1]/div/form/input[5]").click()
    driver.find_element_by_xpath('//*[@class="resultados_busqueda"]/ul/li/a[text()="'+municipio+'"]').click()

    url = driver.current_url
    id = url.split("id")[-1]

    driver.quit()
    return id


def download_xml(municipio):
    url = "http://www.aemet.es/xml/municipios/localidad_" + get_id(municipio) + ".xml"
    response = requests.get(url)

    with open('data.xml', 'wb') as file:
        file.write(response.content)


def parse_xml(path):
    tree = et.parse(path)
    root = tree.getroot()
    prediction = root.find('prediccion')

    year = str(datetime.now().year)
    mes = '07'
    day = '27'
    attr = year + '-' + mes + '-' + day

    for child in prediction:
        if child.attrib['fecha'] == attr:
            date = child
            break
        else: date = False

    print(date.find('estado_cielo').text)


parse_xml('data.xml')
