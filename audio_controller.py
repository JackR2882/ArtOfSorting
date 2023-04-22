import numpy as np
import sounddevice as sd


class AudioOut:
    def __init__(self):
        self.sampleRate = 30000
        self.duration = 0.001 # 0.001
        self.sineFreq = 500 # controls pitch
        self.amplitude = 0 # acts as vol
        self.startI = 0

    def update(self, val):
        self.sineFreq = 500 + (2000*(val/144))

    def audio_out(self):

        def callback(outdata, frames, time, status):
            t = (self.startI + np.arange(frames)) / self.sampleRate
            t = t.reshape(-1, 1)
            outdata[:] = self.amplitude * np.sin(2 * np.pi * self.sineFreq * t)
            self.startI += frames

        # try with device 2 (speaker connected during boot)
        try:
            with sd.OutputStream(device=2, channels=1, callback=callback):
                print("running")
                input()
        except Exception as e:
            print(e)

        # otherwise try with device 3 (speaker disconected during boot)
        try:
            with sd.OutputStream(device=3, channels=1, callback=callback):
                print("running")
                input()
        except Exception as e:
            print(e)