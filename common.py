#!/usr/bin/env python3

import subprocess
import sys
import json

from vosk import Model, KaldiRecognizer, SetLogLevel

SAMPLE_RATE = 16000

SetLogLevel(0)

#model = Model(lang="en-us")
model = Model(lang="ru", model_path='vosk-model-ru-0.42/')
#print(dir(Model.__init__))
rec = KaldiRecognizer(model, SAMPLE_RATE)
def recognize(audio_src):
    with subprocess.Popen(["ffmpeg", "-loglevel", "quiet", "-i",
                            audio_src,
                            "-ar", str(SAMPLE_RATE) , "-ac", "1", "-f", "s16le", "-"],
                            stdout=subprocess.PIPE) as process:

        while True:
            data = process.stdout.read(4000)
            if len(data) == 0:
                break
            if rec.AcceptWaveform(data):
                #print(rec.Result())
                pass
            else:
                pass
                #print(rec.PartialResult())

        data = rec.FinalResult()
        res = json.loads(data)
        print(res)

        return res['text']

