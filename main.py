import pyautogui as gui
import clipboard as clip
import time
import PIL
import os

gui.FAILSAFE


punto_verde = gui.locateOnScreen('punto_verde.png')
print(punto_verde)
print(gui.size())
print(gui.position())

click = gui.moveTo(int(punto_verde[0])+269,int(punto_verde[1])-84)

gui.drag(92, 0, 0.5)
gui.hotkey('ctrl', 'c')
monto = clip.paste()
monto_proc = monto.replace("$", "").replace(" ", "").replace(".","")

print(monto_proc)


