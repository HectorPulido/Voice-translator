import threading
import tkinter as tk

from classes.translator import Translator
from classes.speech_recognizer import SpeechToText
from classes.speech_recognizer_whisper import SpeechToWhisper


class TranslatorInterface(tk.Tk):
    def translate(self, *text):
        translation = ""

        if not isinstance(text, str):
            text = "".join(text)

        if "en" in self.translator.language:
            translation = self.translator.english_to_spanish(text)
        elif "es" in self.translator.language:
            translation = self.translator.spanish_to_english(text)
        else:
            translation = text

        text_to_set = f"cc: {text}\ntraduction: {translation}"
        self.caption_var.set(text_to_set)
        font_size = self.get_font_size(text_to_set)
        print("font size", font_size)
        self.caption_label.config(font=(self.font, font_size))
        return translation

    def callback(self, text):
        if not text:
            return
        threading.Thread(
            target=self.translate,
            args=(text),
        ).start()

    def get_font_size(self, text):
        buffx = max([len(line) for line in text.split("\n")])
        buffy = len(text.split("\n"))

        height_size = int(self.height / buffy)
        width_size = int(self.width / buffx)
        return min(height_size, width_size)

    def select_model(self, device, orginal_language, whisper_model):
        if whisper_model:
            return SpeechToWhisper(device, orginal_language, whisper_model)
        return SpeechToText(device, orginal_language)

    def __init__(
        self, device, theme, original_language, whisper_model, *args, **kwargs
    ):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("Real time translator")

        windows_size = theme.get("size").lower()
        self.width = int(windows_size.split("x")[0])
        self.height = int(windows_size.split("x")[1])

        self.geometry(windows_size)
        self.minsize(self.width, self.height)
        self.maxsize(self.width, self.height)

        background_color = theme.get("background_color")
        self.configure(bg=background_color)

        self.caption_var = tk.StringVar()
        self.caption_var.set("Starting...")

        text_color = theme.get("text_color")
        self.caption_label = tk.Label(
            self,
            fg=text_color,
            bg=background_color,
            textvariable=self.caption_var,
        )

        self.font = theme.get("font")
        #font_size = self.get_font_size(self.caption_var.get())
        #self.caption_label.config(font=(self.font, font_size))
        self.caption_label.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.translator = Translator(original_language)
        self.speech_to_text = self.select_model(
            device, original_language, whisper_model
        )

        self.caption_var.set("Listening...")
        self.speech_to_text.start_listening_in_background(self.callback)
