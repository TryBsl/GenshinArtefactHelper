import pathlib
import json
import os

from UI.refresh import refresh

def deleteScreens():

    data_dir = pathlib.Path("./screens")
    screns = list(data_dir.glob('*.png'))
    image_count = len(screns)

    data_dir1 = pathlib.Path("./ressources/images/myArte")
    screns1 = list(data_dir1.glob('*.png'))

    for i in range(image_count):
        os.remove(str(screns[i]))
        os.remove(str(screns1[i]))

    json_object = json.dumps([], indent=4)

    with open("data.json", "w") as outfile:
        outfile.write(json_object)

    refresh()
