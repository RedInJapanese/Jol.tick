import pyautogui
import time
import pyscreeze
import cv2
import numpy as np

pyscreeze.USE_IMAGE_NOT_FOUND_EXCEPTION = False
ds_location = pyautogui.locateOnScreen('ref.png')
emulator_location = ds_location

def window_capture():
    pyautogui.keyDown('alt')
    pyautogui.press('tab')

    pyautogui.keyUp('alt')

    #opening part of the game with prof juniper
    for i in range(0,109):
        print(i)
        pyautogui.keyDown('x')
        pyautogui.keyUp('x')
        x = pyautogui.position()
        print(x)
    ds_location = pyautogui.locateOnScreen('ref.png')
    if(ds_location):
        print("got the screenshot")
        emulator_location = ds_location
    else: 
        print("retry")
        pyautogui.keyDown('x')
        pyautogui.keyUp('x')
    time.sleep(2)
    ds_location = pyautogui.locateOnScreen('ref.png')
    if(ds_location):
        print("got the screenshot")
        emulator_location = ds_location
        for i in range(0,490):
            print(i)
            pyautogui.keyDown('x')
            pyautogui.keyUp('x')
            x = pyautogui.position()
            print(x)
        return emulator_location
    return ds_location
#player gets to move


