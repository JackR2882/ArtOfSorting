import numpy as np
import sounddevice as sd


class AudioOut:
    def __init__(self):
        self.sampleRate = 60000
        self.duration = 0.01
        self.sineFreq = 440
        self.amplitude = 1
        self.start_idx = 0

    def update(self, val):
        self.sineFreq = 440 + (2000*(val/144))

    def audio_out(self):

        def callback(outdata, frames, time, status):
            #global start_idx
            t = (self.start_idx + np.arange(frames)) / self.sampleRate
            t = t.reshape(-1, 1)
            outdata[:] = self.amplitude * np.sin(2 * np.pi * self.sineFreq * t)
            self.start_idx += frames

        try:
            with sd.OutputStream(device=1, channels=1, callback=callback):
                print("running")
                input()
        except Exception as e:
            print(e)