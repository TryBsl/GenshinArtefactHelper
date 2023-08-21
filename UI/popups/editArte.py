import dearpygui.dearpygui as dpg
import json

f = open("env.json")
env = json.load(f)

f2 = open(env["lang"] + "interface.json")
lang = json.load(f2)

f3 = open("data.json")
artes = json.load(f3)

f4 = open(env["lang"] + "arteTypes.json")
arteTypes = json.load(f4)

win_width, win_height = 1200, 800

def edit_arte_callback(sender):
    if dpg.does_item_exist("modal_edit_arte"):
        dpg.delete_item("modal_edit_arte")
        dpg.delete_item("imgCompare")

        
    idCurrArte = int(sender.split('/')[1])
    currArte = artes[idCurrArte]

    def edit_arte_value_callback(sender, app_data):
        currArte[sender] = app_data

    with dpg.window(label="Edit_Arte", modal=True, show=True, tag="modal_edit_arte", no_title_bar=True, pos=[win_width/4, win_height/4], width=win_width/2, height=win_height/2):
        dpg.add_text("Edit artefact")
        dpg.add_separator()
        dpg.add_text("Titre :")
        dpg.add_input_text(tag="titre", default_value=currArte["titre"], callback=edit_arte_value_callback, on_enter=True)
        dpg.add_separator()
        with dpg.table(header_row=False):
                dpg.add_table_column(width=win_width/16, width_fixed=True)
                dpg.add_table_column(width=win_width/16, width_fixed=True)
                dpg.add_table_column(width=win_width/16, width_fixed=True)
                dpg.add_table_column(width=win_width/16, width_fixed=True)
                with dpg.table_row():
                    dpg.add_text("MainStat :")
                    dpg.add_combo(tag="mainStat", items=["ATQ", "DEF", "PV", "Taux CRIT"], default_value=currArte["mainStat"], callback=edit_arte_value_callback, width=win_width/8)
                    dpg.add_text("MainStatValue :")
                    dpg.add_input_text(tag="mainStatValue", default_value=currArte["mainStatValue"], callback=edit_arte_value_callback, on_enter=True, width=win_width/8)
                with dpg.table_row():
                    dpg.add_separator()
                    dpg.add_separator()
                    dpg.add_separator()
                    dpg.add_separator()
                with dpg.table_row():
                    dpg.add_text("stat1 :")
                    dpg.add_combo(tag="stat1", items=["ATQ", "DEF", "PV"], default_value=currArte["stat1"], callback=edit_arte_value_callback, width=win_width/8)
                    dpg.add_text("stat1Val :")
                    dpg.add_input_text(tag="stat1Val", default_value=currArte["stat1Val"], callback=edit_arte_value_callback, on_enter=True, width=win_width/8)
                with dpg.table_row():
                    dpg.add_text("stat2 :")
                    dpg.add_combo(tag="stat2", items=["ATQ", "DEF", "PV"], default_value=currArte["stat2"], callback=edit_arte_value_callback, width=win_width/8)
                    dpg.add_text("stat2Val :")
                    dpg.add_input_text(tag="stat2Val", default_value=currArte["stat2Val"], callback=edit_arte_value_callback, on_enter=True, width=win_width/8)
                with dpg.table_row(): 
                    dpg.add_text("stat3 :")
                    dpg.add_combo(tag="stat3", items=["ATQ", "DEF", "PV"], default_value=currArte["stat3"], callback=edit_arte_value_callback, width=win_width/8)
                    dpg.add_text("stat3Val :")
                    dpg.add_input_text(tag="stat3Val", default_value=currArte["stat3Val"], callback=edit_arte_value_callback, on_enter=True, width=win_width/8)
                with dpg.table_row():
                    dpg.add_text("stat4 :")
                    dpg.add_combo(tag="stat4", items=["ATQ", "DEF", "PV"], default_value=currArte["stat4"], callback=edit_arte_value_callback, width=win_width/8)
                    dpg.add_text("stat4Val :")
                    dpg.add_input_text(tag="stat4Val", default_value=currArte["stat4Val"], callback=edit_arte_value_callback, on_enter=True, width=win_width/8)
        dpg.add_separator()
        width, height, channels, data = dpg.load_image(currArte["path"])
        with dpg.texture_registry(show=False):
            dpg.add_static_texture(width=width, height=height, default_value=data, tag="imgCompare")
        dpg.add_image("imgCompare")
        dpg.add_separator()
        with dpg.group(horizontal=True):

            dpg.add_button(label="Close", callback=lambda: dpg.configure_item("modal_edit_arte", show=False))
