import io
import os
import torch
import whisper
import threading
from queue import Queue
from tempfile import NamedTemporaryFile
from datetime import datetime, timedelta

from time import sleep
import speech_recognition as sr
from classes.speech_recognizer_base import SpeechToTextBase


class SpeechToWhisper(SpeechToTextBase):
    def __init__(self, device=0, language="en", whisper_model="base"):
        super().__init__(device, language)

        self.data_queue = Queue()
        self.audio_model = whisper.load_model(whisper_model)
        self.phrase_timeout = 2
        self.callback = None
        self.language = language

        self.temp_file = NamedTemporaryFile().name
        self.transcription = [""]
        self.phrase_time = datetime.utcnow()
        self.last_sample = None

        threading.Thread(
            target=self.listen_loop,
        ).start()

    def record_callback(self, _, audio: sr.AudioData) -> None:
        data = audio.get_raw_data()
        self.data_queue.put(data)

    def start_listening_in_background(self, callback):
        self.callback = callback
        self.recognizer.listen_in_background(
            self.microphone, self.record_callback, phrase_time_limit=self.phrase_timeout
        )

    def handle_audio_data(self):
        now = datetime.utcnow()
        # Pull raw recorded audio from the queue.
        if self.data_queue.empty():
            return False

        phrase_complete = False
        if self.phrase_time and now - self.phrase_time > timedelta(
            seconds=self.phrase_timeout
        ):
            self.last_sample = bytes()
            phrase_complete = True
        self.phrase_time = now

        while not self.data_queue.empty():
            data = self.data_queue.get()
            self.last_sample += data

        audio_data = sr.AudioData(
            self.last_sample,
            self.microphone.SAMPLE_RATE,
            self.microphone.SAMPLE_WIDTH,
        )
        wav_data = io.BytesIO(audio_data.get_wav_data())

        with open(self.temp_file, "w+b") as file:
            file.write(wav_data.read())

        result = self.audio_model.transcribe(
            self.temp_file,
            fp16=torch.cuda.is_available(),
        )
        language = result["language"]

        if language != self.language:
            return False

        text = result["text"].strip()

        if phrase_complete:
            self.transcription.append(text)
        else:
            self.transcription[-1] = text

        if self.callback:
            self.callback(self.transcription[-1])

        sleep(0.25)
        return True

    def listen_loop(self):
        while True:
            try:
                self.handle_audio_data()
            except Exception as exception:
                print(exception)
                # If something goes wrong, exit the program.
                exit(1)
