import numpy as np
import pyaudio


class AudioOut:
    def __init__(self):
        self.sampleRate = 60000
        self.duration = 0.01
        self.sineFreq = 800
        #self.volume = 200
        #self.volume = 6
        self.volume = 0

        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=pyaudio.paFloat32,
                                  channels = 1,
                                  rate = self.sampleRate,
                                  output = True)
        
        # calculate default waveform:
        #self.waveform = (np.sin(2 * np.arange((self.sampleRate/2) * (self.duration/2)) * self.sineFreq / self.sampleRate)).astype(np.float32) # 1 is amplitude value
        #self.waveform =  np.concatenate((self.waveform, np.flip(self.waveform)), axis=None) # full length waveform - flip second half so that they match up

        # calculate ramp up/down to apply to waveform
        #self.ramp = np.arange(0,1,1/(len(self.waveform)/2))
        #self.ramp = np.concatenate((self.ramp, np.flip(self.ramp)), axis=None)

        # need to apply ramp to waveform:
        #self.waveform *= self.ramp

        # var to store current output - acts as a buffer
        #self.output = self.waveform * 0

    def cleanup(self):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()


    def out(self, val):

        # calcualte freq
        freq = (2000*(val/146)) + 400

        # calculate waveform:
        waveform = (np.sin(self.volume * np.arange((self.sampleRate) * (self.duration)) * freq / self.sampleRate)).astype(np.float32) # 1 is amplitude value
        
        self.stream.write(waveform)

    #def update(self, val):

        #print(val)

        # fetch pre-caclualted waveform:
    #    waveform = self.waveform.copy()

        # workout transfrom for precaclualted waveform
        #transform = (val/146)
    #    freq = (2000*(val/146)) + 400

        # need to apply the transform to waveform:
        
        #waveform *= transform

        # work out output
        #self.output = (self.volume * waveform).tobytes()
    #    self.output = (np.sin(2 * np.arange((self.sampleRate) * (self.duration)) * freq / self.sampleRate)).astype(np.float32)
        
        #self.ramp = np.arange(0,1,1/(len(self.waveform)/2))
        #self.ramp = np.concatenate((self.ramp, np.flip(self.ramp)), axis=None)

        #self.output *= self.ramp

    #    self.out()
        

    #def out(self):

        #print("OUT, OUT, OUT, OUT, OUT, OUT")

        #while True:
            # write output until new output is given
            #out = self.output.copy()
            #self.stream.write(out)
    #    self.stream.write(self.output)


        # https://stackoverflow.com/questions/42192239/remove-control-clicking-sound-using-pyaudio-as-an-oscillator
        # doesn't work



#obj = AudioOut()

#arr = [12, 120, 30, 40, 59, 88, 11, 60]
#arr = [51, 123, 134, 52, 75, 112, 69, 110, 46, 12, 83, 22, 30, 9, 98, 72, 61, 2, 16, 39, 28, 31, 111, 11, 78, 71, 58, 131, 103, 42, 132, 76, 117, 126, 138, 90, 77, 88, 15, 38, 34, 13, 37, 27, 53, 65, 95, 62, 55, 66, 63, 125, 124, 118, 144, 3, 121, 137, 73, 84, 130, 87, 41, 93, 141, 70, 1, 8, 57, 128, 97, 56, 19, 135, 113, 105, 17, 80, 47, 104, 33, 99, 114, 79, 18, 68, 96, 107, 59, 85, 136, 109, 102, 40, 4, 89, 24, 64, 129, 43, 139, 119, 20, 108, 120, 32, 101, 23, 143, 50, 54, 26, 49, 14, 67, 25, 100, 74, 142, 122, 82, 92, 36, 127, 106, 7, 94, 35, 81, 60, 21, 6, 29, 86, 44, 10, 140, 91, 133, 116, 45, 5, 48, 115]


#for a in arr:
#    print(a)
#    obj.update(a)
#    obj.out()

#obj.update(14)
#obj.out()