"""
This code will play a sound according to the input char the we get from serially
"""

from pygame import mixer
import serial

i = 0.5
# Starting the mixer
mixer.init()

# Loading the song/

frmt = ".mp3"
def play_music(voice):
    # This function is to play the drum audios in the drum sound audios
    
    mixer.music.load(voice)
    print(voice)
    
    # Start playing the song
    mixer.music.play()

ser = serial.Serial('/dev/ttyACM0')  # open serial port
print(ser.name)

while 1:
    s = str(ser.readline(1))  
    frmt = ".mp3"
    direction = "/home/pi/Documents/Python-keynotes-And-projects/python-projrcts/Drum sounds/sound_track/"
    # The sounds are  included in the drum sound folder 
    snd = direction + s[2:-1] + frmt
    play_music(snd)
    print(s) # print the name of the sound that is playing
    



