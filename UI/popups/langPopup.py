import dearpygui.dearpygui as dpg
import json
from UI.refresh import refresh

from scripts.config import setLang

f = open("env.json")
env = json.load(f)

f2 = open(env["lang"] + "interface.json")
langu = json.load(f2)

win_width, win_height = 1200, 800

def callback():
    dpg.configure_item("modal_lang", show=False)
    refresh()

def lang_handler_callback(sender):
    if dpg.does_item_exist("modal_lang"):
        dpg.delete_item("modal_lang")

    lang = setLang(sender)

    with dpg.window(label="Lang_chg", modal=True, show=True, tag="modal_lang", no_title_bar=True, pos=[win_width/3, win_width/3] ):
        dpg.add_text(langu["lang_changed"])
        dpg.add_separator()
        with dpg.group(horizontal=True):
            dpg.add_button(label="OK", width=75, callback=callback)

