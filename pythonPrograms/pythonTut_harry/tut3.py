from playsound import playsound

playsound("play.mp3")


# Download and Play wav and mp3 Files from URL

#!/usr/bin/env python3
# Import necessary modules
from pydub import AudioSegment
from pydub.playback import play
import urllib

# Set the wav filename
filename = "service-bell.wav"
# Download the wav file from url
print("downloading wav file....")
urllib.request.urlretrieve("http://soundbible.com/grab.php?id=2218&type=wav", filename)
# load the file into pydub
sound = AudioSegment.from_file(filename)
print("Playing wav file...")
# play the file
play(sound)

# Set the mp3 filename
filename = "birds.mp3"
# Download an mp3 file
print("downloading mp3 file....")
urllib.request.urlretrieve("http://soundbible.com/grab.php?id=2207&type=mp3", filename)
# load the file into pydub
birdsound = AudioSegment.from_mp3(filename)
print("Playing mp3 file...")
# Play the result
play(birdsound)
print("Finished.")