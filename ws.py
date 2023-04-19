import requests

# URL de la página protegida por contraseña
url = 'https://smartbg.dynamics.bancogalicia.com.ar/apps/portal'
# Datos del formulario de inicio de sesión
data = {
    'user': 'operador.galicia54@hotmail.com',
    'password': 'Oper1234'
}

# Envía una solicitud POST con las credenciales de inicio de sesión
response = requests.post(url, data=data)

# Verifica si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Obtén el contenido HTML de la respuesta
    html = response.text
    with open('html1.txt', 'w', encoding='utf-8') as ws:
        ws.write(html)
else:
    print('La solicitud no fue exitosa. Código de estado:', response.status_code)
