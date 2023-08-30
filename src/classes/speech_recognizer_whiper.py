
# import io
# import torch
# import whisper
# from tempfile import NamedTemporaryFile
# from classes.speech_recognizer_base import SpeechToTextBase


# class SpeechToWhisper(SpeechToTextBase):
#     def __init__(self, device=0, language="en-US"):
#         super().__init__(device, language)

#         self.data_queue = Queue()
#         self.audio_model = self.load_model("base", "en" in language)

#         self.temp_file = NamedTemporaryFile().name

#     def load_model(self, model, english=False):
#         if model != "large" and english:
#             model = model + ".en"
#         audio_model = whisper.load_model(model)
#         return audio_model

#     def start_listening_in_background(self, callback):
#         def inner_callback(recognizer, audio):
#             try:
#                 audio_data = self.recognizer.AudioData(audio.get_raw_data(), self.microphone.SAMPLE_RATE, self.microphone.SAMPLE_WIDTH)
#                 wav_data = io.BytesIO(audio_data.get_wav_data())

#                 with open(self.temp_file, 'w+b') as file:
#                     file.write(wav_data.read())

#                 result = self.audio_model.transcribe(self.temp_file, fp16=torch.cuda.is_available())
#                 text = result['text'].strip()
#                 print(text)


#                 #recording = recognizer.recognize_google(audio, language=self.language)
#                 callback(recording)
#             except Exception as exception:
#                 print(exception)
#                 return False

#             return True

#         self.recognizer.listen_in_background(self.microphone, inner_callback)
