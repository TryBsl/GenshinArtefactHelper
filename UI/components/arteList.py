import dearpygui.dearpygui as dpg
import json
from UI.popups.addScreens import addScreensModal

from UI.popups.editArte import edit_arte_callback
from UI.refresh import *
from scripts.converter import converter
from scripts.deleteFiles import deleteScreens

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

def test_callback(sender):
    print(sender)

def arteItems():
    i = 0
    arteImgList = []
    with dpg.texture_registry(show=False):
        for arte in artes:
            width, height, channels, data = dpg.load_image(arteTypes[arte["typeId"] - 1]["path"])
            dpg.add_static_texture(width=width, height=height, default_value=data, tag="arteImg" + str(i))
            arteImgList.append("arteImg" + str(i))
            i += 1
    setArteListIMG(arteImgList)

def arteList():
     loadData()
     arteItems()

     with dpg.group(width=win_width/2):

        dpg.add_text("Mes artefactes")
        with dpg.table(header_row=False):
            dpg.add_table_column(width=win_width/4.1, width_fixed=True)
            dpg.add_table_column(width=win_width/4.1, width_fixed=True)
            with dpg.table_row():
                dpg.add_button(label="Add News", tag="AddNew", width=win_width/4.1, callback=addScreensModal)
                dpg.add_button(label="ResetArte", tag="RstArte", width=win_width/4.1, callback=deleteScreens)

        with dpg.table(header_row=False, height=win_width/2, scrollX=True, borders_innerH=True, borders_outerH=True):
            dpg.add_table_column(width=128, width_fixed=True)
            dpg.add_table_column(width=500, width_fixed=True)
            dpg.add_table_column(width=170, width_fixed=True)

            for i in range(0, len(artes)):
                with dpg.table_row():
                        dpg.add_image("arteImg" + str(i))
                        dpg.add_text(artes[i]["titre"] + "\n" 
                                     + artes[i]["mainStat"] + ": " + artes[i]["mainStatValue"] + "\n"
                                     + "-----------------------------------------\n"
                                     + artes[i]["stat1"] + ": " + artes[i]["stat1Val"] + "\n"
                                     + artes[i]["stat2"] + ": " + artes[i]["stat2Val"] + "\n"
                                     + artes[i]["stat3"] + ": " + artes[i]["stat3Val"] + "\n"
                                     + artes[i]["stat4"] + ": " + artes[i]["stat4Val"])
                        dpg.add_button(label="Edit", callback=edit_arte_callback, tag="arteEditBtn/" + str(i))