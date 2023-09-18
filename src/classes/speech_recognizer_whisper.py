import io
import threading
from time import sleep
from queue import Queue
from datetime import datetime, timedelta

import numpy as np
import torch
import whisper
import speech_recognition as sr
import soundfile as sf

from classes.speech_recognizer_base import SpeechToTextBase


class SpeechToWhisper(SpeechToTextBase):
    def __init__(self, language="en", whisper_model="base"):
        super().__init__(language)

        self.data_queue = Queue()
        self.audio_model = whisper.load_model(whisper_model)
        self.phrase_timeout = 2
        self.callback = None
        self.language = language

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
        wav_bytes = audio_data.get_wav_data(convert_rate=16000)
        wav_stream = io.BytesIO(wav_bytes)
        audio_array, _ = sf.read(wav_stream)
        audio_array = audio_array.astype(np.float32)

        result = self.audio_model.transcribe(
            audio_array,
            fp16=torch.cuda.is_available(),
            language=self.language,
        )

        text = result["text"].strip()

        if phrase_complete:
            self.transcription.append(text)
        else:
            self.transcription[-1] = text

        if self.callback:
            self.callback(self.transcription[-1])

        sleep(0.2)
        return True

    def listen_loop(self):
        while True:
            try:
                self.handle_audio_data()
            except Exception as exception:
                print("Error: ", exception)
