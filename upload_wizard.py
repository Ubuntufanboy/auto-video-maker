print("Welcome to the YT uploader! We can upload videos to yt for u!!!")
print("")
path = input("What is the video path? ")
print("")
title = input("What do you want the title to be? ")
print("")
des = input("What do you want the description to be? ")
print("")
tags = input("What should the tags be? ")
print("")

while 1:
    sec = input("Do you want the video to be public? (Recomended) y/n ")
    if sec == "y" or sec == "n":
        break
    else:
        print("That isnt valid")

if sec == "y":
    stats = "public"
else:
    stats = "private"
# python3 upload_video.py --file="/home/apollo/没有人能救我.mp4" --title="e" --description="e" --keywords="" --category="22" --privacyStatus="private"

command = f"python3 upload_video.py --file=\"{path}\" --title=\"{title}\" --description=\"{des}\" --keywords=\"{tags}\" --category \"22\" --privacyStatus=\"{stats}\""
print(command)
import os
os.system(command)
