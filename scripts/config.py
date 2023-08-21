import json

f = open("env.json")
env = json.load(f)

def setLang(lang):
    if lang == "fr":
        lp = "./ressources/lang/fr/"
        
    elif lang == "en":
        lp = "./ressources/lang/en/"
        
    env["lang"] = lp        
    
    json_object = json.dumps(env, indent=4)
    with open("env.json", "w") as outfile:
        outfile.write(json_object)

    return lp

def setTesseractPath(tpath):
    env["tesseract_path"] = tpath
    
    json_object = json.dumps(env, indent=4)
    with open("env.json", "w") as outfile:
        outfile.write(json_object)
