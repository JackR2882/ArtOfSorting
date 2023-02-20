import numpy as np
import pyaudio


class AudioOut:
    def __init__(self):
        self.sampleRate = 44000
        self.duration = 0.01
        self.sineFreq = 25000.0
        self.volume = 0.5

        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=pyaudio.paFloat32,
                                  channels = 1,
                                  rate = self.sampleRate,
                                  output = True)
        
        # calculate default waveform:
        self.waveform = (np.sin(2 * np.arange((self.sampleRate/2) * (self.duration/2)) * self.sineFreq / self.sampleRate)).astype(np.float32) # 1 is amplitude value
        self.waveform =  np.concatenate((self.waveform, np.flip(self.waveform)), axis=None) # full length waveform - flip second half so that they match up

        # calculate ramp up/down to apply to waveform
        self.ramp = np.arange(0,1,1/(len(self.waveform)/2))
        self.ramp = np.concatenate((self.ramp, np.flip(self.ramp)), axis=None)

        # need to apply ramp to waveform:
        self.waveform *= self.ramp

    def cleanup(self):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()

    def out(self, val):
        
        # fetch pre-caclualted waveform:
        waveform = self.waveform.copy()

        # workout transfrom for precaclualted waveform
        transform = (val/144)

        # need to apply the transform to waveform:
        waveform *= transform

        # work out output
        output = (self.volume * waveform).tobytes()

        # write output
        self.stream.write(output)

        # https://stackoverflow.com/questions/42192239/remove-control-clicking-sound-using-pyaudio-as-an-oscillator
        # doesn't work