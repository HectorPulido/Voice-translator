from abc import ABC, abstractmethod
import speech_recognition as sr


class SpeechToTextBase(ABC):
    def __init__(self, language):
        self.microphone = sr.Microphone()
        self.recognizer = sr.Recognizer()
        self.language = language

        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)

    def set_device(self, device):
        self.microphone = sr.Microphone(device_index=device)

    @abstractmethod
    def start_listening_in_background(self, callback):
        pass

    @staticmethod
    def show_microphone_list():
        mic_list = []

        for index, name in enumerate(sr.Microphone.list_microphone_names()):
            mic_list.append((index, name))

        return mic_list
