import threading
from classes.translator import Translator
from classes.speech_recognizer import SpeechToText


import tkinter as tk

Main_window = tk.Tk()
my_string_var = tk.StringVar()
my_string_var.set("Starting...")


def callback(text):
    if not text:
        return
    threading.Thread(
        target=translator.translate,
        args=(
            text,
            lambda t: my_string_var.set(t),
        ),
    ).start()


my_label = tk.Label(Main_window, textvariable=my_string_var)
my_label.pack()


translator = Translator()
speechToText = SpeechToText(device=1)

my_string_var.set("Listening...")
speechToText.start_listening_in_background(callback)

Main_window.mainloop()
