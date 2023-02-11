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
        
        self.waveform = (np.sin(2 * np.arange((self.sampleRate/2) * (self.duration/2)) * self.sineFreq / self.sampleRate)).astype(np.float32) # 1 is amplitude value

    def cleanup(self):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()

    def out(self, val):
        #amp = (val/144+0.5)
        #amp = (val/72+0.5)*np.pi
        transform = (val/144)
        
        # cut back waveform to the most recent peak - causes waves to mesh better preventing pops
        
        waveform = self.waveform.copy()
        
        n = len(waveform)-1
        if waveform[len(waveform)-1] > 0: # need to do this when positive (above line)
            while waveform[n] < waveform[n-1]:
                waveform = np.delete(waveform, n)
                n-=1
        if waveform[len(waveform)-1] < 0: # and negative (below line)
            while waveform[n] > waveform[n-1]:
                waveform = np.delete(waveform, n)
                n-=1

        
        ramp = np.arange(0,1,1/len(waveform))
        while len(waveform) < len(ramp):
            ramp = np.delete(ramp, len(ramp)-1)
        waveform *= ramp


        # need to now apply the transform to waveform:
        waveform *= transform


        waveform = np.concatenate((waveform, np.flip(waveform)), axis=None)


        output = (self.volume * waveform).tobytes()

        self.stream.write(output)

        # https://stackoverflow.com/questions/42192239/remove-control-clicking-sound-using-pyaudio-as-an-oscillator
        # doesn't work