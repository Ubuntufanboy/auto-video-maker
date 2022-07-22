import os
link = input("Enter the yt-link >>> ")
os.system(f"yt-dlp {link} -x")
