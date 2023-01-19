from keyboard import mouse, write
from time import sleep
import pyautogui
import os
from random import randint
import threading

SOURCE = 'exitImg'
templates = next(os.walk(SOURCE, topdown=False))[2]
mine = (0,0)

def locate(templates):
    global mine
    result = []
    for img in templates:
        res = pyautogui.locateAllOnScreen(SOURCE + '/' + img)
        result += res
    result = [(box.left, box.top) for box in result]
    forbidden = pyautogui.locateOnScreen('forbidden.PNG')
    try:
        for i in result:
            if i[0]>forbidden.left and i[0]<forbidden.left + forbidden.width:
                if i[1]>forbidden.top and i[1]<forbidden.top + forbidden.height:
                    result.remove(i)
                    mine = i
                    break
    except:
        pass
    return result


def focus(dest):
    for i in range(50,0,-1):
        cur = mouse.get_position()
        x = dest[0] - cur[0]
        y = dest[1] - cur[1]
        mouse.move(cur[0]+x/i, cur[1]+y/i)
        sleep(0.015)

os.system('cls')

while locate(templates):
    for i in locate(templates):
        focus(i)
        sleep(0.2)
        mouse.click()
        sleep(0.2)
        print(locate(templates))


t = threading.Thread(target=input)
t.start()
write('Good Bye', delay=0.1)
focus(mine)
sleep(1)
mouse.click()