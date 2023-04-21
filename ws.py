import requests

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
