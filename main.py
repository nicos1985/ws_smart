import pyautogui as gui
import clipboard as clip
import tkinter as tk
from tkinter import ttk, messagebox
import time
import PIL
import datetime
import os
from psutil import Process 
import psutil




def sel_click(png,x1=0,x2=0,w=gui.size()[0],h=gui.size()[1],x0=0, y0=0, grayscale=True):
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
def cli_activo(pantalla, nombre_cli,estado,sexo,fecha_nac, dni_current):
    if estado == "ACTIVO":
        print('es cliente activo')
        gui.click(pantalla[0]*0.5, pantalla[1]*0.75)
        sel_click('activo.png', int(pantalla[0]*0.12),int(pantalla[1]*0.20), int(pantalla[0]*0.50), int(pantalla[1]*0.50))
        gui.moveTo(pantalla[0]*0.4,pantalla[1]*0.5)
        time.sleep(2)
        gui.scroll(-300)
        
        time.sleep(3)
        x=1    
        punto_verde = gui.locateCenterOnScreen('punto_verde.png', grayscale=True, confidence=0.8)
        gui.click(punto_verde, button="left")
        
        print(punto_verde)

        click = gui.moveTo(int(punto_verde[0])+pantalla[0]*0.12,int(punto_verde[1])-pantalla[1]*0.10)

        gui.drag(98, 0,0.3)
        gui.hotkey('ctrl', 'c')
        monto = clip.paste()
        monto_proc = monto.replace("$", "").replace(" ", "").replace(".","")

        now = datetime.datetime.now()
        time_stamp = now.strftime("%Y-%m-%d %H:%M:%S")
        print(f'{dni_current},{nombre_cli},{estado},{sexo},{fecha_nac},{monto_proc},{time_stamp}')
        registro = (f'{dni_current},{nombre_cli},{estado},{sexo},{fecha_nac},{monto_proc},{time_stamp}')
        reg_proc = registro.splitlines()
        registro_fin = ''.join(reg_proc)
        with open(archivo_destino, 'a') as archivo:
            archivo.write(f'{registro_fin},\n')
        flujo = 'activo'
        return flujo
    else:
        print('NO ES cliente activo')
        now = datetime.datetime.now()
        time_stamp = now.strftime("%Y-%m-%d %H:%M:%S")
        print(time_stamp)
        monto_proc = 'n/c'
        print(f'{dni_current},{nombre_cli},{estado},{sexo},{fecha_nac},{monto_proc},{time_stamp}')
        
        with open(archivo_destino, 'a') as archivo:
            archivo.write(f'{dni_current},{nombre_cli},{estado},{sexo},{fecha_nac},{monto_proc},{time_stamp},\n')
        flujo = 'no activo'
        return flujo
    
def get_process(process_name):
    for process in psutil.process_iter():
        if process.name == process_name:
            return process

def abrir_explorador():
    # abre chrome
    gui.hotkey('ctrl', 'alt', 'm')
    time.sleep(8)
    # maximiza
    gui.keyDown('alt')
    gui.keyDown('space')
    gui.press('x')
    gui.keyUp('alt')
    gui.keyUp('space')
    time.sleep(4)
    print("Busca chrome")
    ruta_chrome = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
    if os.path.exists(ruta_chrome):
        print("Chrome existe")

        nombre_proceso = "chrome.exe"
        # Obtener lista de procesos en ejecución
        p = get_process('chrome.exe')
        
        for proceso in p:
            print(proceso.name)
            if proceso.name == nombre_proceso:
                print("Chrome está en ejecución.")
                return "chrome ejecutó"
            break
        else:
            print("Chrome no está en ejecución.")
            return "chrome no ejecutó"
    else:
        print("El chrome no existe.")
        return "chrome no existe"

def abre_incognito():
    #abre ventana incognito
    gui.hotkey('ctrl', 'shift', 'n')
    time.sleep(3)
    
def ingresa_smart(url):
    #ingresa a smart
    gui.hotkey('ctrl', 'l')
    smart_url = url
    clip.copy(smart_url)
    time.sleep(2)
    gui.hotkey('ctrl', 'v')
    gui.press('enter')

def log_in(mail, contrasena):
    #coloca mail y contraseña
    mail_smart = mail
    contra_smart = contrasena
    time.sleep(4)
    gui.press('home')
    gui.press('del',50)
    clip.copy(mail_smart)
    gui.hotkey('ctrl', 'v')
    gui.press('enter')
    time.sleep(4)
    clip.copy(contra_smart)
    gui.hotkey('ctrl', 'v')
    gui.press('enter')
    time.sleep(4)
    #continua la sesion abierta
    sel_click('si.png')
    time.sleep(10)
    #cambia a modo cursor para navegar
    gui.press('F7')
    time.sleep(0.5)
    gui.press('enter')
    time.sleep(0.5)
    

archivo_origen = 'origen.txt'
archivo_destino = 'destino.txt'
with open(archivo_origen, 'r') as archivo:
    contenido = archivo.read().splitlines()

lista_dni = list(contenido)
print(f'lista_dni: {lista_dni}')

ventana = tk.Tk()
ventana.geometry('100x100')



def ejecutar():
    #Abre chrome
    pantalla = gui.size()
    
    resultado_exp = abrir_explorador()
    if resultado_exp == "chrome ejecutó":
        abre_incognito()

        ingresa_smart('https://smartbg.dynamics.bancogalicia.com.ar/apps/portal')

        log_in('operador.galicia54@hotmail.com', 'Oper1234')

        #Empieza el loop de pegado de dni
        print(int(pantalla[0]*0.80),int(pantalla[1]*0.15), int(pantalla[0]*0.11), int(pantalla[1]*0.09))
        for i in range(len(lista_dni)):     
            # Buscar personas
            sel_click('busqueda_personas.png',1,int(pantalla[1]*0.2777), int(pantalla[0]*0.1010), int(pantalla[1]*0.2129),x0=50)
            time.sleep(0.5)
            gui.press('tab',2)
            
            #Traigo DNI del txt
            dni_current = lista_dni[i]
            #copio el DNI a portapapeles
            clip.copy(dni_current)
            #Pego el DNI en portapapeles
            gui.hotkey('ctrl', 'v')
            gui.press('enter')
            
            time.sleep(1)
            #Doy clic en la 1ra persona
            #gui.click(pantalla[0]*0.6,pantalla[1]*0.45,clicks=1,button='left')
            select = gui.locateCenterOnScreen('marco.png', grayscale=True, confidence=0.7)
            gui.moveTo(select)
            gui.drag(pantalla[0]*0.80,0,0.5)
            gui.hotkey('ctrl', 'c')
            cliente = clip.paste()
            print(cliente)
            nombre_cli, estado, sexo, fecha_nac  = cliente.splitlines()
            fecha_nac_corr = fecha_nac.strip()
            print(f'nombre: {nombre_cli},estado: {estado} , sexo: {sexo}, fecha nac: {fecha_nac_corr}, dni: {dni_current}')
            
            flujo = cli_activo(pantalla, nombre_cli,estado,sexo,fecha_nac_corr, dni_current)

            if flujo == 'no activo':
                continue  

    else:
        messagebox.showwarning('Error', f'{resultado_exp}')   
    

    

botton_ejecutar = ttk.Button(ventana, text='Ejecutar', command=ejecutar)
botton_ejecutar.grid(row=0, column=0)



ventana.mainloop()
