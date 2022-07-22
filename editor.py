from pedalboard import Chorus, Distortion, Phaser, Gain, Reverb, Pedalboard
from pedalboard.io import AudioFile
from termcolor import cprint
from os import system
from silver import Silver
cprint("----- Welcome to Audio editor! -----", "green")
print("")
file = input("Editor: Enter an audio file you would like to edit! >>> ")
system(f"ffmpeg -i {file} audio.wav")

with AudioFile('audio.wav', 'r') as f:
    audio = f.read(f.frames)
    samplerate = f.samplerate

board = Pedalboard([])

print("")
print("You are going to enter edit mode. Select what effects you would like to add")

while 1:
    chorus = input("Would you like to add the Chorus effect? y/n ")
    if chorus == "y":
        c = Chorus()
        board.append(c)
        print("")
        
        print("Playing demo audio...")
        effected = board(audio, samplerate)
        with AudioFile('demo1.wav', 'w', samplerate, effected.shape[0]) as f:
            f.write(effected)
        Silver.play("demo1.wav")
        remove = input("Did you change your mind? We can remove it if you wish y/n ")
        if remove == "y":
            board.remove(c)
            effected = board(audio, samplerate)        
            with AudioFile('demo1.wav', 'w', samplerate, effected.shape[0]) as f:
                f.write(effected)
            Silver.stop()
            print("This is what it sounds like now")
            Silver.play("demo1.wav")
            input("Press enter to stop the playback")
            Silver.stop()
        else:
            Silver.stop()
            break
        break
    elif chorus == "n":
        break
    else:
        continue

while 1:
    distortion = input("Would you like to add the Distortion effect? y/n ")
    if distortion == "y":
        d = Distortion()
        board.append(d)
        print("")
        print("Playing demo audio...")
        effected = board(audio, samplerate)
        with AudioFile('demo2.wav', 'w', samplerate, effected.shape[0]) as f:
            f.write(effected)
        Silver.play("demo2.wav")
        remove = input("Did you change your mind? We can remove it if you wish y/n ")
        if remove == "y":
            board.remove(d)
            Silver.stop()
            effected = board(audio, samplerate)
            with AudioFile('demo2.wav', 'w', samplerate, effected.shape[0]) as f:
                f.write(effected)
            print("This is what it sounds like now")
            Silver.play("demo2.wav")
            input("Press enter to stop the playback")
            Silver.stop()
        else:
            Silver.stop()
            break
        break
    elif distortion == "n":
        break
    else:
        continue

while 1:
    phaser = input("Would you like to add the Phaser effect? y/n ")
    if phaser == "y":
        p = Phaser()
        board.append(p)
        print("")
        print("Playing demo audio...")
        effected = board(audio, samplerate)
        with AudioFile('demo3.wav', 'w', samplerate, effected.shape[0]) as f:
            f.write(effected)
        Silver.play("demo3.wav")
        remove = input("Did you change your mind? We can remove it if you wish y/n ")
        if remove == "y":
            board.remove(p)
            Silver.stop()
            effected = board(audio, samplerate)
            with AudioFile('demo3.wav', 'w', samplerate, effected.shape[0]) as f:
                f.write(effected)
            print("This is what it sounds like now")
            Silver.play("demo3.wav")
            input("Press enter to stop the playback")
            Silver.stop()
        else:
            Silver.stop()
            break
        break
    elif phaser == "n":
        break
    else:
        continue

while 1:
    gain = input("Would you like to add the Gain effect? y/n ")
    if gain == "y":
        amount = int(input("How much gain would you like? Less than 40 db please (Your ears will hurt)"))
        gaindb = amount
        g = Gain(gaindb)
        board.append(g)
        
        print("Playing demo audio...")
        effected = board(audio, samplerate)
        with AudioFile('demo4.wav', 'w', samplerate, effected.shape[0]) as f:
            f.write(effected)
        Silver.play("demo4.wav")
        remove = input("Did you change your mind? We can remove it if you wish y/n ")
        if remove == "y":
            board.remove(g)
            Silver.stop()
            effected = board(audio, samplerate)
            with AudioFile('demo4.wav', 'w', samplerate, effected.shape[0]) as f:
                f.write(effected)
            print("This is what it sounds like now")
            Silver.play("demo4.wav")
            input("Press enter to stop the playback")
            Silver.stop()
        else:
            Silver.stop()
            break
        break
    elif gain == "n":
        break
    else:
        continue

while 1:
    reverb = input("Would you like to add the reverb effect? y/n ")
    if reverb == "y":
        re = Reverb(room_size=0.25)
        board.append(re)
        
        print("Playing demo audio...")
        effected = board(audio, samplerate)
        with AudioFile('demo5.wav', 'w', samplerate, effected.shape[0]) as f:
            f.write(effected)
        Silver.play("demo5.wav")
        remove = input("Did you change your mind? We can remove it if you wish y/n ")
        if remove == "y":
            board.remove(re)
            Silver.stop()
            effected = board(audio, samplerate)
            with AudioFile('demo5.wav', 'w', samplerate, effected.shape[0]) as f:
                f.write(effected)
            print("This is what it sounds like now")
            Silver.play("demo5.wav")
            input("Press enter to stop the playback")
            Silver.stop()
        else:
            Silver.stop()
            break
        break
    elif reverb == "n":
        break
    else:
        continue
print("")
print("")
print("This is the end of the main effects. If you wish, you can go into the pitch shifting program")
print("The pitch shifting program is lower quality but it will still work.")
print("If you want to go into that program enter \"y\" if you don't want to enter the pitch shift program enter \"n\"")
exit_ = input(">>> ")
if exit_ == "y":
    print("Exporting audio")
    system("ffmpeg -i demo5.wav input.mp3")
    print("Removing old demo files...")
    system("rm demo1.wav")
    system("rm demo2.wav")
    system("rm demo3.wav")
    system("rm demo4.wav")
    system("rm demo5.wav")
    print("exiting...")
    system("python3 pitch.py")
elif exit_ == "n":
    print("Exporting audio...")
    system("ffmpeg -i demo5.wav output.mp3")
    print("removing old demo files...")
    system("rm demo1.wav")
    system("rm demo2.wav")
    system("rm demo3.wav")
    system("rm demo4.wav")
    system("rm demo5.wav")
    print("exiting...")
    system("./combine.sh")
