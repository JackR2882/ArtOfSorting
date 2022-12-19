import time

import numpy as np
import pyaudio


class AudioOut:
    def __init__(self):
        self.sampleRate = 44000
        #self.duration = 0.00001
        self.duration = 0.05
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

    def out(self, val):
        val = val/72+0.5
        ordered = (np.sin(val*np.pi * np.arange((self.sampleRate/2) * (self.duration/2)) * self.sineFreq / self.sampleRate)).astype(np.float32)
        
        ordered = np.concatenate((ordered,np.flip(ordered)), axis=None)

        output = (self.volume * ordered).tobytes()
        
        
        #ordered = np.arange((self.sampleRate/2) * (self.duration/2)) # produces array of values in range 0 to (sampleRate*duration)-1

        # rescale these values:
        #ordered  = (ordered * self.sineFreq / self.sampleRate)*val

        #ordered = np.concatenate((ordered,np.flip(ordered)), axis=None)

        #print(ordered)
        #ordered = np.array([0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,
        #                    0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,
        #                    0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,
        #                    0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,
        #                    0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,
        #                    0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5])
        #output = (self.volume * ordered).tobytes()
        self.stream.write(output)


#out = AudioOut()

#while True:
#    out.ordered()