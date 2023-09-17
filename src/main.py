import eel
from classes.translator import Translator
from classes.speech_recognizer_whisper import SpeechToWhisper


class GraphicInterface:
    def __init__(self) -> None:
        self.language = "es"
        self.whisper = SpeechToWhisper(1, self.language, "small")
        self.translator = Translator()

        eel.init("web")
        eel.spawn(self.whisper.start_listening_in_background(self.callback))
        eel._expose("choose_language", self.choose_language)
        eel.start(
            "index.html", mode="my_portable_chromium", host="localhost", port=27000, block=True
        )

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
        print("Listing devices...")
        print("Value | Name")
        for mic in mics:
            print(f"{mic[0]} | {mic[1]}")



if __name__ == "__main__":
    GraphicInterface()


# eel.init("web")

# language = "es"

# whisper = SpeechToWhisper(1, language, "small")
# translator = Translator()


# def callback(text):
#     if not text:
#         return

#     print(text)
#     eel.show_subtitles(text)

#     if language == "en":
#         translation = translator.english_to_spanish(text)
#     elif language == "es":
#         translation = translator.spanish_to_english(text)

#     print(translation)
#     eel.show_translation(translation)





# @eel.expose
# def choose_language(language_to_set):
#     global language
#     language = language_to_set
#     whisper.language = language
#     print(f"Language set to {language}")


# eel.start(
#     "index.html", mode="my_portable_chromium", host="localhost", port=27000, block=True
# )
