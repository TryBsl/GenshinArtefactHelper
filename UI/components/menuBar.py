import dearpygui.dearpygui as dpg
import json

from UI.popups.cooScreen import screen_coo_callback
from UI.popups.langPopup import lang_handler_callback

from scripts.config import setTesseractPath

f = open("env.json")
env = json.load(f)

f2 = open(env["lang"] + "interface.json")
lang = json.load(f2)

win_width, win_height = 1200, 800

def file_callback(sender, app_data):
    setTesseractPath(app_data["file_path_name"])


def menuBar():

    with dpg.file_dialog(directory_selector=False, show=False, callback=file_callback, cancel_callback=lambda: print("Return"), tag="file_dialog", width=700, height=400, default_path=env["tesseract_path"].rstrip("\\abcdefghijklmnopqrstuvwxyz.exe")):
        dpg.add_file_extension("", color=(150, 255, 150, 255))
        dpg.add_file_extension(".exe", color=(0, 255, 255, 255))

    with dpg.menu_bar():
        with dpg.menu(label=lang["options"]) as menu:
            with dpg.menu(label=lang["lang"], tag="lang"):
                dpg.add_menu_item(label="FR", tag="fr", callback=lang_handler_callback)
                dpg.add_menu_item(label="EN", tag="en", callback=lang_handler_callback)
            
            with dpg.tooltip("lang"):
                dpg.add_text(lang["lang_tooltip"])

            dpg.add_menu_item(label=lang["tesseract"], tag="tesseract", callback=lambda: dpg.show_item("file_dialog"))
            
            with dpg.tooltip("tesseract"):
                dpg.add_text(lang["tesseract_tooltip"])

            dpg.add_menu_item(label=lang["cooScreen"], tag="setScreenCoo", callback=screen_coo_callback)
    
    return menu
