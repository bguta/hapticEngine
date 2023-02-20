from hapticEngine import createComplexSignal, playSignal
from pynput import keyboard



A_freq = 440 # Hz
Csh_freq = A_freq * 2 ** (4 / 12) # Hz (note ** is the exponent operator)
E_freq = A_freq * 2 ** (7 / 12) # Hz

freqs     = [A_freq, Csh_freq, E_freq] # the chosen frequencies
durations = [0.1, 0.1, 0.1] # durations for each frequency

audio = createComplexSignal(freqs, durations)

print('Press the the spacebar to play a signal or escape to exit!')
def on_press(key):

    if key == keyboard.Key.space: # listen for space bar
        print("You pressed the spacebar!")
        playSignal(audio)

exit = False
def on_release(key):
    if key == keyboard.Key.esc: # if exit key is pressed, set exit to true
        
        # Stop listener
        global exit
        exit=True
        print('You pressed the exit key. Now exiting!')
        return False

# start listening
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)

listener.start()


# go into infinite loop until exit key is pressed
while not exit:
    continue
