import os
from dotenv import load_dotenv
from classes.speech_recognizer import SpeechToText
from classes.graphic_interface import TranslatorInterface

load_dotenv()

if __name__ == "__main__":
    language = os.getenv("LANGUAGE")
    device = int(os.getenv("DEVICE"))
    background_color = os.getenv("BACKGROUND_COLOR")
    text_color = os.getenv("TEXT_COLOR")
    size = os.getenv("SIZE")
    font = os.getenv("FONT")
    whisper_model = os.getenv("WHISPER_MODEL")
    device_list = bool(os.getenv("DEVICE_LIST") == "True")

    if device_list:
        mics = SpeechToText.show_microphone_list()

        print("Listing devices...")
        print("Value | Name")
        for mic in mics:
            print(f"{mic[0]} | {mic[1]}")

    theme = {
        "text_color": text_color,
        "background_color": background_color,
        "size": size,
        "font": font,
    }

    translator_interface = TranslatorInterface(
        device, theme, language, whisper_model=whisper_model
    )
    translator_interface.mainloop()
