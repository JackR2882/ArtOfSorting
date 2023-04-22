# inspired by the following resource:
#  - https://github.com/Picovoice/porcupine/issues/255#issuecomment-876974791

import os
import pyaudio
import pvporcupine
import struct

# load enviroment variables so key can be fetched
from dotenv import load_dotenv
load_dotenv()

# fetch access_key from environment variables
access_key = os.getenv('PICOVOICE_KEY')

# init listener
listener = pyaudio.PyAudio()

# init porcupine and import hotword samples
porcupine = pvporcupine.create(access_key = access_key, keyword_paths=["/home/pi/ArtOfSorting/hotword_detection/bubble_sort/bubble-sort_en_raspberry-pi_v2_1_0.ppn",
                                                                       "/home/pi/ArtOfSorting/hotword_detection/insertion_sort/insertion-sort_en_raspberry-pi_v2_1_0.ppn",
                                                                       "/home/pi/ArtOfSorting/hotword_detection/merge_sort/merge-sort_en_raspberry-pi_v2_1_0.ppn",
                                                                       "/home/pi/ArtOfSorting/hotword_detection/selection_sort/selection-sort_en_raspberry-pi_v2_1_0.ppn",
                                                                       "/home/pi/ArtOfSorting/hotword_detection/heap_sort/heap-sort_en_raspberry-pi_v2_1_0.ppn",
                                                                       "/home/pi/ArtOfSorting/hotword_detection/quick_sort/quick-sort_en_raspberry-pi_v2_1_0.ppn",
                                                                       "/home/pi/ArtOfSorting/hotword_detection/counting_sort/counting-sort_en_raspberry-pi_v2_1_0.ppn",
                                                                       "/home/pi/ArtOfSorting/hotword_detection/bucket_sort/bucket-sort_en_raspberry-pi_v2_1_0.ppn",
                                                                       "/home/pi/ArtOfSorting/hotword_detection/radix_sort/radix-sort_en_raspberry-pi_v2_1_0.ppn",
                                                                       "/home/pi/ArtOfSorting/hotword_detection/cocktail_sort/cocktail-sort_en_raspberry-pi_v2_1_0.ppn",
                                                                       "/home/pi/ArtOfSorting/hotword_detection/tim_sort/tim-sort_en_raspberry-pi_v2_1_0.ppn",
                                                                       "/home/pi/ArtOfSorting/hotword_detection/binary_sort/binary-sort_en_raspberry-pi_v2_1_0.ppn",
                                                                       "/home/pi/ArtOfSorting/hotword_detection/shell_sort/shell-sort_en_raspberry-pi_v2_1_0.ppn",
                                                                       "/home/pi/ArtOfSorting/hotword_detection/slow_mode/slow-mode_en_raspberry-pi_v2_1_0.ppn",
                                                                       "/home/pi/ArtOfSorting/hotword_detection/fast_mode/fast-mode_en_raspberry-pi_v2_1_0.ppn"
                                                                       ])


def listen():

    # open audio stream
    stream = listener.open(
        rate=porcupine.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=porcupine.frame_length)

    while True:

        wave = stream.read(porcupine.frame_length, exception_on_overflow=False)

        # convert to more managable form (byte to decimal)
        wave = struct.unpack_from("h" * porcupine.frame_length, wave)

        # generate value corresponding to what noise is detected (hotword or not, and if hotword then which hotword)
        hotword = porcupine.process(wave)

        # if hotword is detected
        if hotword != -1:

            # if hotword detected, then which hotword is detected?
            hotwords = ["bubble", "insertion", "merge", "selection",
                        "heap", "quick", "counting", "bucket", "radix",
                        "cocktail shaker", "tim", "binary", "shell", "slow",
                        "fast"]
            
            output = hotwords[hotword]
            stream.close()
            return(output)

    
        
def clear(): # clears stream to prevent end of previous hotword from being detected

    # open audio stream
    stream = listener.open(
        rate=porcupine.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=porcupine.frame_length)
    
    for _ in range(0, 10):

        wave = stream.read(porcupine.frame_length, exception_on_overflow=False)
        #wave = stream.read(2048)

        # convert to more managable form (byte to decimal)
        wave = struct.unpack_from("h" * porcupine.frame_length, wave)
    
    stream.close()