# -*- coding: utf-8 -*-
import whisper
import time
import queue
import os


class Transcriber:
    """tiny
    base
    small (boa qualidade e desempenho)
    medium
    large (melhor qualidade, mais lento)
    """

    def __init__(self, model="tiny"):
        self.model = whisper.load_model(model)

    def transcribe(self, file_path):
        t = time.time()
        print("Transcrevendo arquivo: ", file_path)
        result = self.model.transcribe(file_path)
        print("Transcrição concluída em %f segundos" % (time.time() - t))
        return result["text"]
