import eel
import json
from classes.translator import Translator
from classes.speech_recognizer_whisper import SpeechToWhisper


class GraphicInterface:
    def __init__(self) -> None:
        self.language = "es"
        self.whisper = SpeechToWhisper(self.language, "small")
        self.translator = Translator()

        eel.init("web")
        eel.spawn(self.whisper.start_listening_in_background(self.callback))
        eel._expose("choose_language", self.choose_language)
        eel._expose("show_mics", self.show_mics)
        eel._expose("select_mic", self.select_mic)
        eel.start(
            "index.html",
            mode="my_portable_chromium",
            host="localhost",
            port=27000,
            block=True,
        )

    def select_mic(self, mic_id):
        print(f"Selected mic {mic_id}")
        self.whisper.set_device(int(mic_id))

    def choose_language(self, language_to_set):
        self.language = language_to_set
        self.whisper.language = self.language
        print(f"Language set to {self.language}")

    def callback(self, text):
        if not text:
            return

        print(text)
        eel.show_subtitles(text)

        translation = ""
        if self.language == "en":
            translation = self.translator.english_to_spanish(text)
        elif self.language == "es":
            translation = self.translator.spanish_to_english(text)

        print(translation)
        eel.show_translation(translation)

    def show_mics(self):
        mics = SpeechToWhisper.show_microphone_list()
        mics_list = {"mics_id": [], "mics_name": []}

        for mic in mics:
            mics_list["mics_id"].append(mic[0])
            mics_list["mics_name"].append(f"{mic[0]} | {mic[1]}")

        eel.fill_select_mics(json.dumps(mics_list))

        print("Listing devices...")
        print("Value | Name")
        for mic in mics:
            print(f"{mic[0]} | {mic[1]}")


if __name__ == "__main__":
    GraphicInterface()
