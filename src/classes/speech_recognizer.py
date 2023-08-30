from classes.speech_recognizer_base import SpeechToTextBase


class SpeechToText(SpeechToTextBase):
    def start_listening_in_background(self, callback):
        def inner_callback(recognizer, audio):
            try:
                recording = recognizer.recognize_google(audio, language=self.language)
                callback(recording)
            except Exception as _:
                return False

            return True

        self.recognizer.listen_in_background(self.microphone, inner_callback, phrase_time_limit=2)
