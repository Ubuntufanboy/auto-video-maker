ffmpeg -loop 1 -i img.jpg -i output.mp3 -shortest -acodec copy -vcodec mjpeg video.mp4
echo 'Your video has been made sucsessfully!'
python3 upload_wizard.py
