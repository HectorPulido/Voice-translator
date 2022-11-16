import argparse

from utils_func import str2bool, get_or
from classes.speech_recognizer import SpeechToText
from classes.graphic_interface import TranslatorInterface

parser = argparse.ArgumentParser(
    description="This software allows the near real time translation."
)
parser.add_argument("-d", "--device", type=int, help="Device of microphone")
parser.add_argument(
    "-b", "--background_color", type=str, help="Color of the background"
)
parser.add_argument("-s", "--size", type=str, help="Size of the window")
parser.add_argument("-t", "--text_color", type=str, help="Color of the text")
parser.add_argument("-l", "--device_list", type=str2bool, help="Show the device list")
parser.add_argument("--font", type=str, help="Font of the text")
parser.add_argument("--font_size", type=int, help="Size of the font")

args = parser.parse_args()
variables = vars(args)

if __name__ == "__main__":

    device = get_or(variables, "device", 0)
    background_color = get_or(variables, "background_color", "#000")
    text_color = get_or(variables, "text_color", "#fff")
    size = get_or(variables, "size", "800x90")

    font = get_or(variables, "font", "Helvatical bold")
    font_size = get_or(variables, "font_size", 20)

    if variables.get("device_list", False):
        mics = SpeechToText.show_microphone_list()

        print("Listing devices...")
        print("Value | Name")
        for mic in mics:
            print(f"{mic[0]} | {mic[1]}")

    theme = {
        "text_color": text_color,
        "background_color": background_color,
        "size": size,
        "font_size": font_size,
        "font": font,
    }

    translator_interface = TranslatorInterface(device, theme)
    translator_interface.mainloop()
