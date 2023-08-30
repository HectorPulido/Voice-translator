from abc import ABC, abstractmethod
import speech_recognition as sr


class SpeechToTextBase(ABC):
    def __init__(self, device, language):
        self.microphone = sr.Microphone(device_index=device)
        self.recognizer = sr.Recognizer()
        self.language = language

        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)

    @abstractmethod
    def start_listening_in_background(self, callback):
        pass

    @staticmethod
    def show_microphone_list():
        mic_list = []

        for index, name in enumerate(sr.Microphone.list_microphone_names()):
            mic_list.append((index, name))

        return mic_list
