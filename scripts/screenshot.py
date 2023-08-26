import pyautogui
import dearpygui.dearpygui as dpg
import time
import json
from playsound import playsound
import pathlib

from scripts.converter import converter

def setMousePosition():
    f = open("env.json")
    env = json.load(f)
    time.sleep(3)
    playsound('./ressources/beep.wav')
    p1 = pyautogui.position()
    x1 = p1.x
    y1 = p1.y
    playsound('./ressources/beep.wav')
    time.sleep(3)
    p2 = pyautogui.position()
    x2 = p2.x - x1
    y2 = p2.y - y1
    playsound('./ressources/beep.wav')
    env["x_screen1"] = x1
    env["y_screen1"] = y1
    env["x_screen2"] = x2
    env["y_screen2"] = y2

    json_object = json.dumps(env, indent=4)
    with open("env.json", "w") as outfile:
        outfile.write(json_object)

def addScreens(nbArte):
    f = open("env.json")
    env = json.load(f)
    data_dir = pathlib.Path("./screens")
    screns = list(data_dir.glob('*.png'))
    image_count = len(screns)
    time.sleep(3)
    playsound('./ressources/beep.wav')
    for i in range(image_count, image_count + nbArte):

        time.sleep(1)

        im = pyautogui.screenshot("./screens/screen" + str(i) +".png", region=(env["x_screen1"], env["y_screen1"], env["x_screen2"], env["y_screen2"]))

        playsound('./ressources/beep.wav')
        dpg.configure_item("progressScreens", default_value=(i-image_count+1)/(nbArte), overlay="Arte " + str(i-image_count+1) + "/" + str(nbArte))
    converter(image_count)
