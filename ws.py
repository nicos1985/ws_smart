"""import requests

# URL de la página protegida por contraseña
url = 'https://previ.com.ar'
# Datos del formulario de inicio de sesión


# Envía una solicitud POST con las credenciales de inicio de sesión
response = requests.post(url)
# Verifica si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Obtén el contenido HTML de la respuesta
    html = response.text
    with open('html.txt', 'w', encoding='utf-8') as ws:
        ws.write(html)
else:
    print('La solicitud no fue exitosa. Código de estado:', response.status_code)
"""
from selenium import webdriver
import time

browser = webdriver.Chrome()
print(type(browser))

browser.get('https://smartbg.dynamics.bancogalicia.com.ar/main.aspx?appid=b81740e9-28ee-ea11-b827-005056001541&pagetype=webresource&webresourceName=mcs_%2Fcomponents%2Fbusquedapersona%2Findex.html')
time.sleep(10)
login = browser.find_element('class','form-control')
print(login.tag_name)
login.send_keys('31363667')
time.sleep(2)
#password = browser.find_element('id', 'password')
#password.send_keys('antares313')
#time.sleep(1)
login.submit()