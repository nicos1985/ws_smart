import pyautogui as gui
import clipboard as clip
import tkinter as tk
from tkinter import ttk, messagebox
import time
import PIL
from datetime import date, datetime
import os
from psutil import Process 
import psutil 




def sel_click(png,x1=0,x2=0,w=gui.size()[0],h=gui.size()[1],x0=0, y0=0, grayscale=True):
    """Selecciona segun cordenadas de locate, mueve el mouse y hace clik en el punto indicado. Se pasan coordenadas y una png"""
    print(png)
    print(f'x1:{x1}')
    print(f'x2:{x2}')
    print(f'w:{w}')
    print(f'h:{h}')
    #gui.moveTo(x=(int(x1)), y=(int(x2)))
    #time.sleep(2)
    #gui.moveTo(x=(int(x1+w)), y=(int(x2+h)))
    #time.sleep(2)
    png_coordenadas = gui.locateCenterOnScreen(png, grayscale=grayscale, confidence=0.7, region=(x1,x2,w,h))
    print(f'png_coordenadas{png_coordenadas}')
    gui.moveTo(x=(int(png_coordenadas[0])+x0), y=(int(png_coordenadas[1])+y0))
    gui.click(x=(int(png_coordenadas[0])+x0), y=(int(png_coordenadas[1])+y0), clicks=1, button='left')

    # si esta activo el cliente entonces sigue a la proxima pantalla para poder obtener el monto
def reg_log(archivo, mensaje, *args):
    """Registra un evento en el archivo indicado, hace un time stamp y los datos que se pasen por args."""
    now = datetime.now()
    time_stamp = now.strftime("%Y-%m-%d %H:%M:%S")
    with open(archivo, 'a') as archivo:
        archivo.write(f'{mensaje},{args},{time_stamp}\n') 

def encontrar_verde(pantalla,estado):
    """ Encuentra punto verde de aprobado en pantalla de monto"""
    try:
        count_try = 0   
        punto_verde = gui.locateCenterOnScreen('punto_verde.png', grayscale=True, confidence=0.8)
        gui.click(punto_verde, button="left")
        
        print(punto_verde)

        click = gui.moveTo(int(punto_verde[0])+pantalla[0]*0.12,int(punto_verde[1])-pantalla[1]*0.10)

        gui.drag(98, 0,0.3)
        gui.hotkey('ctrl', 'c')
        monto = clip.paste()
        monto_proc = monto.replace("$", "").replace(" ", "").replace(".","")
        return monto_proc
    except:
        count_try = count_try+1
        error = f'No se encuentra el punto verde {count_try}'
        return error


def cli_activo(pantalla,estado):
    """Hace clik en el cliente activo y mueve con scroll hacia abajo."""
    if estado == "ACTIVO":
        print('es cliente activo')
        gui.click(pantalla[0]*0.5, pantalla[1]*0.75)
        sel_click('activo.png', int(pantalla[0]*0.12),int(pantalla[1]*0.20), int(pantalla[0]*0.50), int(pantalla[1]*0.50))
        gui.moveTo(pantalla[0]*0.4,pantalla[1]*0.5)
        time.sleep(2)
        gui.scroll(-300)
        
        time.sleep(3)
        x=1 
        return 'realizado'

        """
        now = datetime.now()
        time_stamp = now.strftime("%Y-%m-%d %H:%M:%S")
        print(f'{dni_current},{nombre_cli},{estado},{sexo},{fecha_nac},{monto_proc},{time_stamp}')
        registro = (f'{dni_current},{nombre_cli},{estado},{sexo},{fecha_nac},{monto_proc},{time_stamp}')
        reg_proc = registro.splitlines()
        registro_fin = ''.join(reg_proc)
        with open('destino.txt', 'a') as archivo:
            archivo.write(f'{registro_fin},\n')
        flujo = 'activo'
        return flujo
        """
    else:
        return 'no realizado'
        """
        print('NO ES cliente activo')
        now = datetime.now()
        time_stamp = now.strftime("%Y-%m-%d %H:%M:%S")
        print(time_stamp)
        monto_proc = 'n/c'
        print(f'{dni_current},{nombre_cli},{estado},{sexo},{fecha_nac},{monto_proc},{time_stamp}')
        
        with open('destino.txt', 'a') as archivo:
            archivo.write(f'{dni_current},{nombre_cli},{estado},{sexo},{fecha_nac},{monto_proc},{time_stamp},\n')
        flujo = 'no activo'
        return flujo
        """   
def get_process(process_name):
    """Obtiene el proceso de google chrome de la lista de procesos de windows"""
    for process in psutil.process_iter(['pid','name']):
        print(f'process: {process.info["name"]} == {process_name}')
        if process.info['name'] == process_name:
            return process

def abrir_explorador():
    """ Abre el explorador Chrome y chequea que se haya abierto para continuar con el siguiente paso."""
    # abre chrome
    print('antes de presionar ctrl alt c')
    with gui.hold(['ctrl', 'alt']):
        gui.press('c')
    print('despues de presionar ctrl alt c')
    time.sleep(8)
    """
    # maximiza
    gui.keyDown('alt')
    gui.keyDown('space')
    gui.press('x')
    gui.keyUp('alt')
    gui.keyUp('space')
    time.sleep(4)
    """
    print("Busca chrome")
    ruta_chrome = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
    if os.path.exists(ruta_chrome):
        print("Chrome existe")

        nombre_proceso = "chrome.exe"
        # Obtener lista de procesos en ejecución
        p = get_process(nombre_proceso)
        print(f'proceso:{p}')
        if p is not None:
            print("Chrome está en ejecucion.")
            return "chrome ejecuto"
        else:
            print("Chrome no está en ejecucion.")
            return "chrome no ejecuto"
    else:
        print("El chrome no existe.")
        return "chrome no existe"

def abre_incognito():
    """ Abre la ventana de incognito de chrome"""
    #abre ventana incognito
    gui.hotkey('ctrl', 'shift', 'n')
    #gui.keyDown('ctrl')
    #gui.keyDown('shift')
    #gui.press('n')
    #gui.keyUp('ctrl')
    #gui.keyUp('shift')
    time.sleep(3)
    
def ingresa_smart(url):
    """ingresa a smart usando la url pasada."""
    #ingresa a smart
    gui.hotkey('ctrl', 'l')
    smart_url = url
    clip.copy(smart_url)
    time.sleep(2)
    gui.hotkey('ctrl', 'v')
    gui.press('enter')

def log_in(mail, contrasena):
    """Ingresa mail y contraseña para ingresar a smart"""
    #coloca mail y contraseña
    mail_smart = mail
    contra_smart = contrasena
    time.sleep(4)
    gui.press('home')
    gui.press('del',50)
    clip.copy(mail_smart)
    gui.hotkey('ctrl', 'v')
    time.sleep(0.2)
    gui.press('enter')
    time.sleep(4)
    clip.copy(contra_smart)
    gui.hotkey('ctrl', 'v')
    time.sleep(0.2)
    gui.press('enter')
    time.sleep(4)
    #continua la sesion abierta
    try:
        sel_click('si.png')
        mensaje = "Se realizó la apertura del explorador. Se logueó correctamente"
        reg_log(f'log{date.today()}.txt',mensaje)
        time.sleep(6)

        return True
    except:
        mensaje = "No se pudo abrir el explorador o no se pudo realizar el logueo. Se reintenta"
        reg_log(f'log{date.today()}.txt',mensaje)
        
        #Cerrar Chrome
        gui.keyDown('alt')
        gui.press('f4')
        gui.press('f4')
        gui.keyUp('alt')
        time.sleep(1)
        return False
        

def habilita_cursor():
    """habilita el modo de cursor para navegar y establece la pantalla al 100%"""
    #cambia a modo cursor para navegar
    gui.press('F7')
    time.sleep(0.5)
    gui.press('enter')
    time.sleep(0.5)
    #pantalla al 100%
    gui.hotkey('ctrl', '0')
    
def busca_personas(pantalla, por_x, por_y, por_w, por_h, x0):
    """Busca el boton para realizar la busqueda de personas"""
    count_try = 0
    try:
        sel_click('busqueda_personas.png',int(pantalla[0]*por_x),int(pantalla[1]*por_y), int(pantalla[0]*por_w), int(pantalla[1]*por_h),x0=x0)
        time.sleep(0.5)
        gui.press('tab',2)
        return 'buscar exitoso'
    
    except:
        count_try = count_try + 1 
        error = f'No se encuentra busqueda personas. count = {count_try}'
        return error
    
def busco_dni(i):
    """Busca el dni siguiente en archivo de origen y lo coloca en el campo de busqueda. Da enter"""

    #Traigo DNI del txt
    dni_current = lista_dni[i]
    #copio el DNI a portapapeles
    clip.copy(dni_current)
    #Pego el DNI en portapapeles
    gui.hotkey('ctrl', 'v')
    time.sleep(0.3)
    gui.press('enter')
    time.sleep(1)
    return dni_current

def copia_datos_dni(pantalla, dni_current):
    """Copia los datos del dni encontrado y los deja en la variable cliente_proc, en caso de error, retorna el mismo."""
    try:
        select = gui.locateCenterOnScreen('marco.png', grayscale=True, confidence=0.7)
        gui.moveTo(select)
        gui.drag(pantalla[0]*0.80,0,0.5)
        gui.hotkey('ctrl', 'c')
        cliente = clip.paste()
        print(cliente)
        nombre_cli, estado, sexo, fecha_nac  = cliente.splitlines()
        fecha_nac_corr = fecha_nac.strip()
        cliente_proc = [nombre_cli, estado, sexo, fecha_nac_corr, dni_current]
        print(f'nombre: {nombre_cli},estado: {estado} , sexo: {sexo}, fecha nac: {fecha_nac_corr}, dni: {dni_current}')
        return cliente_proc
    except:
        error = 'error al copiar datos del cliente'
        return error

archivo_origen = 'origen.txt'
archivo_destino = 'destino.txt'

with open(archivo_origen, 'r') as archivo:
    contenido = archivo.read().splitlines()

lista_dni = list(contenido)
print(f'lista_dni: {lista_dni}')

ventana = tk.Tk()
ventana.geometry('100x100')



def ejecutar():
    """ejecuta el flujo del proceso. Construyendo"""
    #Abre chrome
    pantalla = gui.size()
    print('antes de ejecutar abrir chrome')
    time.sleep(2)
    resultado_exp = abrir_explorador()
    print(f'resultado_exp:{resultado_exp}')
    print('inicia proceso de abrir explorador')
    if resultado_exp == "chrome ejecuto":

        abre_incognito()
        print('inicia proceso de abrir incognito')

        ingresa_smart('https://smartbg.dynamics.bancogalicia.com.ar/apps/portal')

        res_log = log_in('operador.galicia54@hotmail.com', 'Oper1234')
        if res_log == True:
            habilita_cursor()

            #Empieza el loop de pegado de dni
            #print(int(pantalla[0]*0.80),int(pantalla[1]*0.15), int(pantalla[0]*0.11), int(pantalla[1]*0.09))
           
            for i in range(len(lista_dni)): 

                # Buscar personas
                pag_buscar = busca_personas(pantalla, 0.001, 0.2777, 0.1010, 0.2129, 50)

                if pag_buscar == 'buscar exitoso':
                    buscar_dni = busco_dni(i)
                    cliente = copia_datos_dni(pantalla, buscar_dni)

                    if cliente != 'error al copiar datos del cliente':
                        nombre_cli, estado, sexo, fecha_nac_corr, dni_current = cliente
                        flujo = cli_activo(pantalla, nombre_cli, estado, sexo, fecha_nac_corr, dni_current)
                        if flujo == 'realizado':
                            verde = encontrar_verde(pantalla, estado)
    
                    else:
                        cliente = copia_datos_dni(pantalla, buscar_dni)
                else:
                    pag_buscar = busca_personas(pantalla, 0.001, 0.2777, 0.1010, 0.2129, 50)

                if flujo == 'no activo':
                    continue  
        else:
            ejecutar()            
    else:
        ejecutar()
        reg_log(f'log{date.today()}.txt',f'{resultado_exp}')   
    

    
#Boton de ejecutar
botton_ejecutar = ttk.Button(ventana, text='Ejecutar', command=ejecutar)
botton_ejecutar.grid(row=0, column=0)



ventana.mainloop()
