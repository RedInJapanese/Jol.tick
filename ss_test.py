import pyautogui
import pyscreeze

pyscreeze.USE_IMAGE_NOT_FOUND_EXCEPTION = False

ds_location = pyautogui.locateOnScreen('ref.png')
if(ds_location):
    print("nice.")
