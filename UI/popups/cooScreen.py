import dearpygui.dearpygui as dpg
import json

from scripts.screenshot import setMousePosition

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

width, height, channels, data = dpg.load_image("./ressources/images/tuto/cootuto.png")

def screen_coo_set_callback(sender):
    setMousePosition()

def screen_coo_callback(sender):
    loadData()

    if dpg.does_item_exist("modal_cooScreen"):
        dpg.delete_item("modal_cooScreen")
        dpg.delete_item("tutoCooTag")

    with dpg.texture_registry(show=False):
        dpg.add_static_texture(width=width, height=height, default_value=data, tag="tutoCooTag")

    with dpg.window(label="CooScreen", modal=True, show=True, tag="modal_cooScreen", no_title_bar=True, pos=[win_width/4, win_height/3]):
        dpg.add_text(lang["cooScreenModal"] + "x1: " + str(env["x_screen1"]) + "  y1: " + str(env["y_screen1"])  + " x2: " + str(env["x_screen1"] + env["x_screen2"]) + "  y2: " + str(env["y_screen1"] + env["y_screen2"]))
        dpg.add_separator()
        
        with dpg.group(horizontal=True):
            dpg.add_image("tutoCooTag")
            dpg.add_text(lang["cooScreenModalTuto"], wrap=125)
        dpg.add_separator()
        with dpg.group(horizontal=True):
            dpg.add_button(label="OK", width=75, callback=lambda: dpg.configure_item("modal_cooScreen", show=False))
            dpg.add_button(label="Reset", width=75, callback=screen_coo_set_callback)
    