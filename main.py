from argparse import *
from scripts.config import *
from scripts.converter import converter

from scripts.screenshot import *


def main():
    parser = ArgumentParser(prog="ArteUtil", description="A program that gets screenshot of your genshin artefacts and convert them into json")
    parser.add_argument("-s", 
                        type=int,
                        action="store",
                        metavar="Screenshot", 
                        help="Add new screenshots to the file",
                        required=False)
    parser.add_argument("-rs", 
                        type=int,
                        action="store",
                        metavar="Reset Screenshot", 
                        help="Replace all screenshot with new",
                        required=False)
    parser.add_argument("-c", 
                        help="Convert screenshots to json",
                        action="store_true",
                        required=False)
    parser.add_argument("-tesseract_path", 
                        type=str,
                        action="store",
                        metavar="PathTesseract", 
                        help="Set Tesseract path",
                        required=False)
    parser.add_argument("-lang", 
                        type=str,
                        action="store",
                        metavar="Language", 
                        help="Set Language to 'fr' or 'en'",
                        required=False)
    
    
    args = parser.parse_args()

    if args.s:
        nbArte = args.s
        addScreens(nbArte)

    elif args.rs:
        nbArte = args.rs
        addScreens(nbArte)

    elif args.c:
        converter()

    elif args.tesseract_path:
        setTesseractPath(args.tesseract_path)

    elif args.lang:
        setLang(args.lang)

    else :
        print("Use args with program")


if __name__ == '__main__':
    main()