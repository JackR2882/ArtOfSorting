import time

import numpy as np
import pyaudio


class AudioOut:
    def __init__(self):
        self.sampleRate = 44000
        self.duration = 0.1
        self.sineFreq = 440.0
        self.volume = 1.0

        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=pyaudio.paFloat32,
                channels = 1,
                rate = self.sampleRate,
                output = True)

    def cleanup(self):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()

    def ordered(self):
        ordered = (np.sin(2*np.pi * np.arange(self.sampleRate * self.duration) * self.sineFreq / self.sampleRate)).astype(np.float32)
        output = (self.volume * ordered).tobytes()
        self.stream.write(output)

    def unordered(self):
        unordered = (np.sin(1*np.pi * np.arange(self.sampleRate * self.duration) * self.sineFreq / self.sampleRate)).astype(np.float32)
        output = (self.volume * unordered).tobytes()
        self.stream.write(output)


out = AudioOut()

while True:
    out.ordered()