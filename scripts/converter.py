from PIL import Image, ImageEnhance
from pytesseract import pytesseract
import pathlib
import json
import re
import time
from difflib import SequenceMatcher

f = open("env.json")
env = json.load(f)

path_to_tesseract = env["tesseract_path"]
pytesseract.tesseract_cmd = path_to_tesseract

f2 = open(env["lang"] + "stats.json")
lang = json.load(f2)

f3 = open(env["lang"] + "arteTypes.json")
families = json.load(f3)

data_dir = pathlib.Path("./screens")
screns = list(data_dir.glob('*.png'))
image_count = len(screns)

def arteFamilyFinder(arte):
    best_ratio = 0
    titre = arte["titre"]
    for family in families:
        if arte["type"] == lang["flowerFull"] :
            r = SequenceMatcher(None, arte["titre"], family["flower"]).ratio()
            if best_ratio < r:
                best_ratio = r
                arte["typeId"] = family["id"]
                titre = family["flower"]
        elif arte["type"] == lang["featherFull"] :
            r = SequenceMatcher(None, arte["titre"], family["feather"]).ratio()
            if best_ratio < r:
                best_ratio = r
                arte["typeId"] = family["id"]
                titre = family["feather"]
        elif arte["type"] == lang["crownFull"] :
            r = SequenceMatcher(None, arte["titre"], family["crown"]).ratio()
            if best_ratio < r:
                best_ratio = r
                arte["typeId"] = family["id"]
                titre = family["crown"]
        elif arte["type"] == lang["sandFull"] :
            r = SequenceMatcher(None, arte["titre"], family["sand"]).ratio()
            if best_ratio < r:
                best_ratio = r
                arte["typeId"] = family["id"]
                titre = family["sand"]
        elif arte["type"] == lang["cupFull"] :
            r = SequenceMatcher(None, arte["titre"], family["cup"]).ratio()
            if best_ratio < r:
                best_ratio = r
                arte["typeId"] = family["id"]
                titre = family["cup"]
        else :
            arte["typeId"] = 1
            arte["err"] = True
    arte["titre"] = titre

def jsonCleaner(list):
    nbFleur, nbPlume, nbDia, nbSa, nbCoupe, nbErr = 0, 0, 0, 0, 0, 0
    for arte in list:

        if re.match(lang["flower"], arte["type"], flags=re.IGNORECASE) or re.match(".*" + lang["flower"], arte["txt"], flags=re.IGNORECASE):
            arte["type"] = lang["flowerFull"]
            nbFleur += 1
            arte["mainStat"] = lang["hp"]
            arte["mainStatValue"] = "4.780"
        
        elif re.match(lang["feather"], arte["type"], flags=re.IGNORECASE) or re.match(".*" + lang["feather"], arte["txt"], flags=re.IGNORECASE):
            arte["type"] = lang["featherFull"]
            nbPlume += 1
            arte["mainStat"] = lang["dmg"]
            arte["mainStatValue"] = "311"

        elif re.match(lang["crown"], arte["type"], flags=re.IGNORECASE) or re.match(".*" + lang["crown"], arte["txt"], flags=re.IGNORECASE):
            arte["type"] = lang["crownFull"]

            if re.match(lang["hp"], arte["mainStat"], flags=re.IGNORECASE):
                arte["mainStat"] = lang["hp"]
                arte["mainStatValue"] = "46.6%"
                nbDia += 1
            elif re.match(lang["cd"], arte["mainStat"], flags=re.IGNORECASE):
                arte["mainStat"] = lang["cd"]
                arte["mainStatValue"] = "62.2%"
                nbDia += 1
            elif re.match(lang["cr"], arte["mainStat"], flags=re.IGNORECASE):
                arte["mainStat"] = lang["cr"]
                arte["mainStatValue"] = "31.1%"
                nbDia += 1
            elif re.match(lang["emShort"], arte["mainStat"], flags=re.IGNORECASE):
                arte["mainStat"] = lang["em"]
                arte["mainStatValue"] = "187"
                nbDia += 1
            elif re.match(lang["dmg"], arte["mainStat"], flags=re.IGNORECASE):
                arte["mainStat"] = lang["dmg"]
                arte["mainStatValue"] = "46.6%"
                nbDia += 1
            elif re.match(lang["def"], arte["mainStat"], flags=re.IGNORECASE):
                arte["mainStat"] = lang["def"]
                arte["mainStatValue"] = "58.3%"
                nbDia += 1
            elif re.match(lang["hbShort"], arte["mainStat"], flags=re.IGNORECASE):
                arte["mainStat"] = lang["hb"]
                arte["mainStatValue"] = "35.9%"
                nbDia += 1
            else : 
                nbErr += 1
                arte["err"] = True
                

        elif re.match(lang["sand"], arte["type"], flags=re.IGNORECASE) or re.match(".*" + lang["sand"], arte["txt"], flags=re.IGNORECASE):
            arte["type"] = lang["sandFull"]

            if re.match(lang["hp"], arte["mainStat"], flags=re.IGNORECASE):
                arte["mainStat"] = lang["hp"]
                arte["mainStatValue"] = "46.6%"
                nbSa += 1
            elif re.match(lang["dmg"], arte["mainStat"], flags=re.IGNORECASE):
                arte["mainStat"] = lang["dmg"]
                arte["mainStatValue"] = "46.6%"
                nbSa += 1
            elif re.match(lang["def"], arte["mainStat"], flags=re.IGNORECASE):
                arte["mainStat"] = lang["def"]
                arte["mainStatValue"] = "58.3%"
                nbSa += 1
            elif re.match(lang["emShort"], arte["mainStat"], flags=re.IGNORECASE):
                arte["mainStat"] = lang["em"]
                arte["mainStatValue"] = "187"
                nbSa += 1
            elif re.match(lang["erShort"], arte["mainStat"], flags=re.IGNORECASE):
                arte["mainStat"] = lang["er"]
                arte["mainStatValue"] = "51.8%"
                nbSa += 1
            else : 
                nbErr += 1
                arte["err"] = True
        
        elif re.match(lang["cup"], arte["type"], flags=re.IGNORECASE) or re.match(".*" + lang["cup"], arte["txt"], flags=re.IGNORECASE):
            arte["type"] = lang["cupFull"]

            if re.match(lang["hp"], arte["mainStat"], flags=re.IGNORECASE):
                arte["mainStat"] = lang["hp"]
                arte["mainStatValue"] = "46.6%"
                nbCoupe += 1
            elif re.match(lang["dmg"], arte["mainStat"], flags=re.IGNORECASE):
                arte["mainStat"] = lang["dmg"]
                arte["mainStatValue"] = "46.6%"
                nbCoupe += 1
            elif re.match(lang["def"], arte["mainStat"], flags=re.IGNORECASE):
                arte["mainStat"] = lang["def"]
                arte["mainStatValue"] = "58.3%"
                nbCoupe += 1
            elif re.match(lang["emShort"], arte["mainStat"], flags=re.IGNORECASE):
                arte["mainStat"] = lang["em"]
                arte["mainStatValue"] = "187"
                nbCoupe += 1
            elif re.match(lang["erShort"], arte["mainStat"], flags=re.IGNORECASE):
                arte["mainStat"] = lang["er"]
                arte["mainStatValue"] = "51.8%"
                nbCoupe += 1
            elif re.match(".*" + lang["bdPhyShort"], arte["mainStat"], flags=re.IGNORECASE) or re.match(".*" + lang["bdPhyShort"], arte["txt"], flags=re.IGNORECASE):
                arte["mainStat"] = lang["bdPhy"]
                arte["mainStatValue"] = "58.3%"
                nbCoupe += 1
            elif re.match(".*" + lang["bdHydroShort"], arte["mainStat"], flags=re.IGNORECASE) or re.match(".*" + lang["bdHydroShort"], arte["txt"], flags=re.IGNORECASE):
                arte["mainStat"] = lang["bdHydro"]
                arte["mainStatValue"] = "46.6%"
                nbCoupe += 1
            elif re.match(".*" + lang["bdElectroShort"], arte["mainStat"], flags=re.IGNORECASE) or re.match(".*" + lang["bdElectroShort"], arte["txt"], flags=re.IGNORECASE):
                arte["mainStat"] = lang["bdElectro"]
                arte["mainStatValue"] = "46.6%"
                nbCoupe += 1
            elif re.match(".*" + lang["bdDendroShort"], arte["mainStat"], flags=re.IGNORECASE) or re.match(".*" + lang["bdDendroShort"], arte["txt"], flags=re.IGNORECASE):
                arte["mainStat"] = lang["bdDendro"]
                arte["mainStatValue"] = "46.6%"
                nbCoupe += 1
            elif re.match(".*" + lang["bdAnemoShort"], arte["mainStat"], flags=re.IGNORECASE) or re.match(".*" + lang["bdAnemoShort"], arte["txt"], flags=re.IGNORECASE):
                arte["mainStat"] = lang["bdAnemo"]
                arte["mainStatValue"] = "46.6%"
                nbCoupe += 1
            elif re.match(".*" + lang["bdPyroShort"], arte["mainStat"], flags=re.IGNORECASE) or re.match(".*" + lang["bdPyroShort"], arte["txt"], flags=re.IGNORECASE):
                arte["mainStat"] = lang["bdPyro"]
                arte["mainStatValue"] = "46.6%"
                nbCoupe += 1
            elif re.match(".*" + lang["bdGeoShort"], arte["mainStat"], flags=re.IGNORECASE) or re.match(".*" + lang["bdGeoShort"], arte["txt"], flags=re.IGNORECASE):
                arte["mainStat"] = lang["bdGeo"]
                arte["mainStatValue"] = "46.6%"
                nbCoupe += 1
            elif re.match(".*" + lang["bdCryoShort"], arte["mainStat"], flags=re.IGNORECASE) or re.match(".*" + lang["bdCryoShort"], arte["txt"], flags=re.IGNORECASE):
                arte["mainStat"] = lang["bdCryo"]
                arte["mainStatValue"] = "46.6%"
                nbCoupe += 1
            else : 
                nbErr += 1
                arte["err"] = True

        else : 
            nbErr += 1
            arte["err"] = True

        i = 1
        for i in range(1, 5):
            string = arte["stat" + str(i)]
            if re.match(".*" + lang["dmg"], string, flags=re.IGNORECASE):
                arte["stat" + str(i)] = lang["dmg"]
                tab = string.split("+")
                if len(tab) < 3:
                    nbErr += 1
                    arte["err"] = True
                else :
                    arte["stat" + str(i) + "Val"] = tab[2]

            elif re.match(".*" + lang["def"], string, flags=re.IGNORECASE):
                arte["stat" + str(i)] = lang["def"]
                tab = string.split("+")
                if len(tab) < 3:
                    nbErr += 1
                    arte["err"] = True
                else :
                    arte["stat" + str(i) + "Val"] = tab[2]

            elif re.match(".*" + lang["hp"], string, flags=re.IGNORECASE):
                arte["stat" + str(i)] = lang["hp"]
                tab = string.split("+")
                if len(tab) < 3:
                    nbErr += 1
                    arte["err"] = True
                else :
                    arte["stat" + str(i) + "Val"] = tab[2]
                  
            elif re.match(".*" + lang["cr"], string, flags=re.IGNORECASE):
                arte["stat" + str(i)] = lang["cr"]
                tab = string.split("+")
                if len(tab) < 3:
                    nbErr += 1
                    arte["err"] = True
                else :
                    arte["stat" + str(i) + "Val"] = tab[2]
            
            elif re.match(".*" + lang["cd"], string, flags=re.IGNORECASE):
                arte["stat" + str(i)] = lang["cd"]
                tab = string.split("+")
                if len(tab) < 3:
                    nbErr += 1
                    arte["err"] = True
                else :
                    arte["stat" + str(i) + "Val"] = tab[2]

            elif re.match(".*" + lang["emShort"], string, flags=re.IGNORECASE):
                arte["stat" + str(i)] = lang["em"]
                tab = string.split("+")
                if len(tab) < 3:
                    nbErr += 1
                    arte["err"] = True
                else :
                    arte["stat" + str(i) + "Val"] = tab[2]
            
            elif re.match(".*" + lang["erShort"], string, flags=re.IGNORECASE):
                arte["stat" + str(i)] = lang["er"]
                tab = string.split("+")
                if len(tab) < 3:
                    nbErr += 1
                    arte["err"] = True
                else :
                    arte["stat" + str(i) + "Val"] = tab[2]
            
            else :
                nbErr += 1
                arte["err"] = True
        
        arteFamilyFinder(arte)

    print("nbErr:" + str(nbErr))

    return nbErr



def converter():

    list = []

    for i in range(10):

        img = Image.open(str(screns[i]))

        cpimg = img.copy()
        cpimg.thumbnail((200, 200))
        cpimg.save("./ressources/images/myArte/arte" + str(i) + ".png")

        img = img.convert(mode="L")

        filter = ImageEnhance.Brightness(img)
        br_img = filter.enhance(0.8)

        filter = ImageEnhance.Contrast(br_img)
        con_img = filter.enhance(1.99)

        filter = ImageEnhance.Sharpness(con_img)
        sha_img = filter.enhance(1.3)

        txt = pytesseract.image_to_string(sha_img)

        txt_array = txt.split("\n")

        titre = txt_array[0]
        typeA = txt_array[2]
        mainStat = txt_array[4]
        mainStatValue = txt_array[6]
        j = len(txt_array)-2

        if txt_array[j] == "":
            while txt_array[j] == "":
                j = j-1
                stat4 = txt_array[j]
        else :
            stat4 = txt_array[j]
        j = j-1

        if txt_array[j] == "":
            while txt_array[j] == "":
                j = j-1
                stat3 = txt_array[j]
        else :
            stat3 = txt_array[j]
        j = j-1

        if txt_array[j] == "":
            while txt_array[j] == "":
                j = j-1
                stat2 = txt_array[j]
        else :
            stat2 = txt_array[j]
        j = j-1

        if txt_array[j] == "":
            while txt_array[j] == "":
                j = j-1
                stat1 = txt_array[j]
        else :
            stat1 = txt_array[j]
        j = j-1
            
        

        list.append({"path": "./ressources/images/myArte/arte" + str(i) + ".png", 
                    "titre": titre, 
                    "type": typeA, 
                    "mainStat": mainStat,
                    "mainStatValue": mainStatValue,
                    "stat1": stat1,
                    "stat1Val": "",
                    "stat2": stat2,
                    "stat2Val": "",
                    "stat3": stat3,
                    "stat3Val": "",
                    "stat4": stat4,
                    "stat4Val": "",
                    "err": False,
                    "typeId": "",
                    "txt": txt.replace("\n", " ")})

        print(str(i) + "/" + str(image_count))

    jsonCleaner(list)
    json_object = json.dumps(list, indent=4)

    with open("data.json", "w") as outfile:
        outfile.write(json_object)


