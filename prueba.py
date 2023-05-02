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

"""
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