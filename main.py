import pyautogui as gui
import clipboard as clip
import tkinter as tk
from tkinter import ttk, messagebox
import time
import PIL


gui.FAILSAFE


def sel_click(png,x1,x2,w,h,x0=0, y0=0):
    print(png)
    png_coordenadas = gui.locateCenterOnScreen(png, grayscale=True, confidence=0.7, region=(x1,x2,w,h))
    print(f'png_coordenadas{png_coordenadas}')
    gui.click(x=(int(png_coordenadas[0])+x0), y=(int(png_coordenadas[1])+y0), clicks=1, button='left')

archivo_origen = 'origen.txt'
archivo_destino = 'destino.txt'
with open(archivo_origen, 'r') as archivo:
    contenido = archivo.read().splitlines()

lista_dni = list(contenido)
print(f'lista_dni: {lista_dni}')

ventana = tk.Tk()
ventana.geometry('100x100')



def ejecutar():
    for i in range(len(lista_dni)):
        print(gui.position())
        sel_click('busqueda_personas.png',0,300, 200, 230,x0=50)
        #sel_click('buscar_registro.png', 1600,170, 250, 100, x0=-30)
        time.sleep(1)
        gui.click(1800,210,clicks=1,button='left')


        dni_current = lista_dni[i]
        clip.copy(dni_current)

        gui.hotkey('ctrl', 'v')
        gui.press('enter') 

        time.sleep(1)
        gui.click(1680,354,clicks=1,button='left')
        
        #gui.moveTo(1680, 700)
        #time.sleep(1)
        #gui.scroll(-1000)

        time.sleep(5)
        
        punto_verde = gui.locateOnScreen('punto_verde.png')
        
        print(punto_verde)


        click = gui.moveTo(int(punto_verde[0])+269,int(punto_verde[1])-84)

        gui.drag(92, 0,0.3)
        gui.hotkey('ctrl', 'c')
        monto = clip.paste()
        monto_proc = monto.replace("$", "").replace(" ", "").replace(".","")

        print(f'{dni_current},{monto_proc}')

        with open(archivo_destino, 'a') as archivo:
            archivo.write(f'{dni_current},{monto_proc}\n')

botton_ejecutar = ttk.Button(ventana, text='Ejecutar', command=ejecutar)
botton_ejecutar.grid(row=0, column=0)



ventana.mainloop()
