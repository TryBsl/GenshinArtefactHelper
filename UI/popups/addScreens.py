import dearpygui.dearpygui as dpg
import json

from scripts.screenshot import addScreens

def loadData():
    f = open("env.json")
    global env
    env = json.load(f)

    f2 = open(env["lang"] + "interface.json")
    global lang
    lang = json.load(f2)

    f3 = open("data.json")
    global artes
    artes = json.load(f3)

    f4 = open(env["lang"] + "arteTypes.json")
    global arteTypes
    arteTypes = json.load(f4)

win_width, win_height = 1200, 800

def setamout(sender, app_data):
    global amount
    amount = app_data

def start():
    addScreens(amount)

def addScreensModal():
    loadData()
    if dpg.does_item_exist("addScreensmodal"):
        dpg.delete_item("addScreensmodal")

    with dpg.window(label="addScreens", modal=True, show=True, tag="addScreensmodal", no_title_bar=True, pos=[win_width/4, win_height/4], width=win_width/2, height=win_height/2):
        dpg.add_text(default_value="Ajout de screens")
        dpg.add_input_int(label="NombreScreen", callback=setamout, tag="nbrscreen", default_value=0)
        dpg.add_button(tag="Start", callback=start, label="Start", width=win_width/2.1, enabled=True)
        dpg.add_separator()
        dpg.add_progress_bar(label="screens", tag="progressScreens", width=win_width/2.1, default_value=0, overlay="screens 0/0")
        dpg.add_separator()
        dpg.add_progress_bar(label="Analys", tag="progressAnalys", width=win_width/2.1, default_value=0, overlay="arte 0/0")
        dpg.add_separator()
        dpg.add_button(label="Close", callback=lambda: dpg.configure_item("addScreensmodal", show=False))