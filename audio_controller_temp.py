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

    def cleanup(self):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()

    def out(self, val):
        #amp = (val/144+0.5)
        #amp = (val/72+0.5)*np.pi
        amp = (val/144)



        ordered = (np.sin(amp * np.arange((self.sampleRate/2) * (self.duration/2)) * self.sineFreq / self.sampleRate)).astype(np.float32)
        
        
        # cut back waveform to the most recent peak - causes waves to mesh better preventing pops
        n = len(ordered)-1
        if ordered[len(ordered)-1] > 0: # need to do this when positive (above line)
            while ordered[n] < ordered[n-1]:
                ordered = np.delete(ordered, n)
                n-=1
        if ordered[len(ordered)-1] < 0: # and negative (below line)
            while ordered[n] > ordered[n-1]:
                ordered = np.delete(ordered, n)
                n-=1

        
        ramp = np.arange(0,1,1/len(ordered))
        while len(ordered) < len(ramp):
            ramp = np.delete(ramp, len(ramp)-1)
        ordered *= ramp

        ordered = np.concatenate((ordered, np.flip(ordered)), axis=None)


        output = (self.volume * ordered).tobytes()

        self.stream.write(output)

        # https://stackoverflow.com/questions/42192239/remove-control-clicking-sound-using-pyaudio-as-an-oscillator
        # doesn't work