from termcolor import colored

msg = colored("editor", "green")
msg = f"----- Welcome to the audio {msg}! You can change the speed of the audio here -----"
print(msg)
print("enter a value from 0.5 - 2.0 to change the speed by (1.0 will make it not change)")
print("")
value = float(input("Enter here: -> "))
from os import system
command = f"ffmpeg -i input.mp3 -af \"asetrate=44100*{value},aresample=44100\" output.mp3"
system(command)
