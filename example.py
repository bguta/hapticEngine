import numpy as np # useful library that does fancy math and matrix stuff
import simpleaudio as sa # audio input/output library!!



'''
The bottom is example code taken from the simpleaudio documentation.
It creates three notes, each 0.25 seconds long. 

'''
# calculate note frequencies
A_freq = 440 # Hz
Csh_freq = A_freq * 2 ** (4 / 12) # Hz (note ** is the exponent operator)
E_freq = A_freq * 2 ** (7 / 12) # Hz

# get timesteps for each sample, T is note duration in seconds
sample_rate = 44100 # sample rate for the wave that we are going to generate for each notes
T = 0.25 # period for a single note
t = np.linspace(0, T, int(T * sample_rate), False) # time object, it slices the 0.25 seconds into the given number of samples

# generate sine wave notes
A_note = np.sin(A_freq * t * 2 * np.pi)
Csh_note = np.sin(Csh_freq * t * 2 * np.pi)
E_note = np.sin(E_freq * t * 2 * np.pi)

# concatenate notes
audio = np.hstack((A_note, Csh_note, E_note)) # combine the notes into a single object so that we can play them sequentially. 0.75s is the total length
# normalize to 16-bit range
audio *= 32767 / np.max(np.abs(audio)) 
# convert to 16-bit data
audio = audio.astype(np.int16) # necessary for audio data to be processed as audio data

# start playback
play_obj = sa.play_buffer(audio, 1, 2, sample_rate) # play audio data!

# wait for playback to finish before exiting
play_obj.wait_done()