import dearpygui.dearpygui as dpg
import json
from UI.components.arteList import arteList

from UI.components.menuBar import menuBar

from UI.popups.editArte import edit_arte_callback
from UI.refresh import getShouldRefresh, setShouldRefresh


from scripts.config import *
from scripts.converter import converter
from scripts.screenshot import *

f = open("env.json")
env = json.load(f)

f2 = open(env["lang"] + "interface.json")
lang = json.load(f2)

f3 = open("data.json")
artes = json.load(f3)

f4 = open(env["lang"] + "arteTypes.json")
arteTypes = json.load(f4)

win_width, win_height = 1200, 800

def test_callback(sender):
    print(sender)

dpg.create_context()

with dpg.font_registry():
    # first argument ids the path to the .ttf or .otf file
    default_font = dpg.add_font("./ressources/font/zh-cn.ttf", 20)
    second_font = dpg.add_font("./ressources/font/zh-cn.ttf", 10)

dpg.create_viewport(title='Genshin Artefact Maximizer', width=win_width, height=win_height, resizable=False)
dpg.setup_dearpygui()

def mainWin():
    with dpg.window(tag="Main"):
        menuBar()

        dpg.add_text("Optimisateur d'artefacts")
        with dpg.group(horizontal=True):
            global arteImgList
            arteImgList = arteList()

            with dpg.group(width=win_width/2):
                dpg.add_text("Données")

        dpg.bind_font(default_font)

dpg.show_debug()
mainWin()
dpg.show_viewport()
dpg.set_primary_window("Main", True)



while dpg.is_dearpygui_running():
    if getShouldRefresh():
        mainWin()
        dpg.set_primary_window("Main", True)
        setShouldRefresh(False)
    dpg.render_dearpygui_frame()


dpg.start_dearpygui()
dpg.destroy_context()