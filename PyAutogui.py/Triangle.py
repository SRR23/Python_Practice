

import pyautogui
from time import sleep
sleep(6)

for i in range(5):
    for j in range(i+1):
        pyautogui.write('#',interval=0.20)
    pyautogui.press('enter')

