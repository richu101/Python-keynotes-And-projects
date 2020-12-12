from pygame import mixer

i = 0.5
# Starting the mixer
mixer.init()

# Loading the song/

frmt = ".mp3"
def play_music(voice):
    """
    This function is to play the drum audios in the drum sound audios

    """
    mixer.music.load(voice)

    # Setting the volume
    mixer.music.set_volume(0.7)

    # Start playing the song
    mixer.music.play()


# infinite loop
while True:

    print("Press 'p' to pause, 'r' to resume")
    print("Press 'e' to exit the program")
    print("press 'v' to enter volume control mode")
    
    query = input(" ")
    dir = "/home/pi/Documents/Python-keynotes-And-projects/python-projrcts/Drum sounds/sound_track"
    voice = dir + query + frmt

    play_music(voice)
    if query == 'p':

        # Pausing the music
        mixer.music.pause()
    elif query == 'r':

        # Resuming the music
        mixer.music.unpause()
    elif query == 'v':
        # Volume control
        volin = input("press D to volume down & U to volume up ex to exit the volume control mode")
        c = 'n'  # to enter the volume control loop
        while c != "ex":
           # print(" Volume UP or Down")
            if volin == "u":
                if i <= 1:
                    i += .1
                    print("volume UP=")
                    print(i)
                else:
                    i = .9
                    print("You are at max volume")

                mixer.music.set_volume(i)

            if volin == "d":
                if i > 0:
                    i -= .1
                    print("volume DOWN=")
                    print(i)
                else:
                    i = 0
                    print("You are at min volume")

                mixer.music.set_volume(i)
            volin = input("")
            c = volin

    elif query == 'e':

        # Stop the mixer
        mixer.music.stop()
        break
