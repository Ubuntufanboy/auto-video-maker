print("Welcome to the editing app!")
print("enter a value 0.5 - 2.0 to change the speed by")
print("")
value = float(input("Enter here: -> "))
from os import system
command = f"ffmpeg -i input.mp3 -af \"asetrate=44100*{value},aresample=44100\" output.mp3"
system(command)
