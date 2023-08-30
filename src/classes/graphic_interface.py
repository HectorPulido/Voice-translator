import threading
import tkinter as tk

from classes.translator import Translator
from classes.speech_recognizer import SpeechToText
from classes.speech_recognizer_whiper import SpeechToWhisper


class TranslatorInterface(tk.Tk):
    def callback(self, text):
        if not text:
            return
        threading.Thread(
            target=self.translator.translate,
            args=(
                text,
                self.caption_var.set,
            ),
        ).start()

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
        self.geometry(windows_size)
        self.minsize(int(windows_size.split("x")[0]), int(windows_size.split("x")[1]))
        self.maxsize(int(windows_size.split("x")[0]), int(windows_size.split("x")[1]))

        background_color = theme.get("background_color")
        self.configure(bg=background_color)

        self.caption_var = tk.StringVar()
        self.caption_var.set("Starting...")

        text_color = theme.get("text_color")
        caption_label = tk.Label(
            self,
            fg=text_color,
            bg=background_color,
            textvariable=self.caption_var,
        )

        font = theme.get("font")
        font_size = theme.get("font_size")
        caption_label.config(font=(font, font_size))

        caption_label.pack(padx=10, pady=10)

        self.translator = Translator(original_language)
        self.speech_to_text = self.select_model(
            device, original_language, whisper_model
        )

        self.caption_var.set("Listening...")
        self.speech_to_text.start_listening_in_background(self.callback)
