import speech_recognition as sr


class SpeechToText:
    def __init__(self, device=0, language="es"):
        self.m = sr.Microphone(device_index=device)
        self.r = sr.Recognizer()
        self.language = language

        with self.m as source:
            self.r.adjust_for_ambient_noise(source)

    def recognize(self):
        with self.m as source:
            audio = self.r.listen(source)
        try:
            text = self.r.recognize_google(audio, language=self.language)
        except Exception as exception:
            text = ""

        return text

    def start_listening_in_background(self, callback):
        def inner_callback(recognizer, audio):
            try:
                recording = recognizer.recognize_google(audio, language=self.language)
                callback(recording)
            except Exception as exception:
                return

        self.r.listen_in_background(self.m, inner_callback)

    def show_microphone_list(self):
        mic_list = []

        for index, name in enumerate(sr.Microphone.list_microphone_names()):
            mic_list.append((index, name))

        return mic_list
