import os
import pyaudio
import numpy as np
import config


p = pyaudio.PyAudio()
frames_per_buffer = int(config.MIC_RATE / config.FPS)
stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=config.MIC_RATE,
                    input=True,
                    frames_per_buffer=frames_per_buffer)
    

while True:
    if stream.is_stopped():
        stream.start_stream() 
    buf = stream.read(1024)
    if buf:
        stream.stop_stream()
