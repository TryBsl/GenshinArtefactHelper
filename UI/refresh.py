import dearpygui.dearpygui as dpg

arteImgList = []
shouldRefresh =False

def setArteListIMG(list):
    global arteImgList
    arteImgList = list

def getShouldRefresh():
    return shouldRefresh

def setShouldRefresh(bool):
    global shouldRefresh
    shouldRefresh = bool

def refresh():
    dpg.delete_item("Main")
    dpg.delete_item("file_dialog")
    for tag in arteImgList:
        dpg.delete_item(tag)
    global shouldRefresh
    shouldRefresh = True
