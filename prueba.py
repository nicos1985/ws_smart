import pyautogui as gui
import time
import datetime
"""
gui.hotkey('ctrl','alt','c')

time.sleep(4)

gui.hotkey('alt','space','n')

time.sleep(4)
gui.hotkey('alt','space','x')

gui.hotkey('ctrl','shift','n')


with gui.hold(['ctrl', 'alt']):
    gui.press('c')
gui.keyUp('alt')
gui.keyUp('ctrl')
time.sleep(2)
#with gui.hold(['alt', 'space']):
#    gui.press('x')

time.sleep(2)
with gui.hold(['ctrl', 'shift']):
    gui.press('n')

"""

with open('origen.txt', 'r') as arch_origen:
    contenido = arch_origen.read()

dni = '4436934'
contador = contenido.count(dni)
if contador <= 3:
    with open('origen.txt', 'a') as archivo:
        archivo.write(f'{dni}\n') 
    print(f'contador = {contador}')
else:
    print(f'el dni {dni} superó la cantidad de intentos. ')
