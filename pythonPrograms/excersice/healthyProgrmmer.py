from pygame import mixer
mixer.init()
mixer.music.load('play.mp3')
mixer.music.play()

def drink_water(str):
    print("drink water is running")
    if str == "phydone":
        mixer.music.rewind()
    else:
        mixer.music.load('play.mp3')


def excer_eyes():
    print("Excerise for eyes is running")
    mixer.music.rewind()

def physical_excer():
    print("Physical exsercise is running")
    mixer.music.rewind()


while True:
    s = input(' ')
    if s == "drank":
        excer_eyes()
    elif s == "eyesdone":
        physical_excer()
    elif s=="phydone":
        drink_water("phydone")
    elif s == "stop":
        print("Done for now")
        break

