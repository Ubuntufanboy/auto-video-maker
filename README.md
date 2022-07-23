# auto-video-maker

This app takes audio from a video off of youtube and uses an image to make a video that can upload to `youtube`.

## Installation

Find a youtube link for the audio and an image that you would like to overlay that audio file.

After that, run these following commands in order:

```bash
sudo apt update && sudo apt upgrade
sudo apt install git
git clone https://github.com/Ubuntufanboy/auto-video-maker.git
cd auto-video-maker/
chmod +x main.sh combine.sh
sudo apt install ffmpeg
sudo apt install yt-dlp
```

Install `termcolor`

```python3
pip3 install termcolor
```

Install `pedalboard`

```python3
pip3 install pedalboard
```

You will also need to install Silver.
```bash
git clone https://github.com/Ubuntufanboy/Silver
```
Then move silver.py into the auto-video-maker folder


> At this stage it's recommended to set up a `venv` for python.

Install `oauth2client`.

```python3
pip3 install oauth2client
```

Congrats! You have no installed all of the tools needed to run this program!


## Setting up YouTube API

Just as a warning or disclaimer, **Youtube will LOCK all of the videos you upload via the API due to youtube not verifying the API.** But if you *MANUALY* upload the videos to Youtube it will *NOT LOCK* the video.

### Follow the below steps to setup your API

1. Navigate to [Google Cloud](https://cloud.google.com/) and make an accout if you don't already have one.

2. Click on *CONSOLE* on the top bar near your google profile image.

3. On the left side of your screen you should see a option to make a new project called *"Select a project"* click on that.

4. Click on *New Project* and name it what ever you want (But it can **NOT** be changed later).

5. Click on the bell icon and once the project is done loading click on *"Select project"*.

6. On the left side on your screen you should see some options. Scroll down until you see *"Marketplace"* (It should be the 4th option) then click on it.

7. Type into the search bar *"Youtube Data API"* then select the first option. (At the time it is called "YouTube Data API v3") then click `Enable`.

8. Once it is done downloading it should take you to a new screen that is the API menu.

9. Click Oauth consent screen on the left side of your screen.

10. Select *"External"* and click create.

11. Fill out the fields that have a red star on then. They are required. Then scroll down and click *"Save and continue"*.

12. You should now be in a menu called *Scopes*. Click `Add or Remove scopes` then in the filter bar type "Upload" then press enter and select the first option that appears.

13. Click the check mark to the left of it and click `Update`. Scroll all the way to the bottom and click *"Save an continue"*.

14. You should now be in a menu called `Test users`. Click on "*Add users*" and type in the GMail account that you would like to use the program with.

15. Click save and continue. Then scroll down and click "*Back to dashboard*".

16. Go to the left of your screen and click "Credentials" with the key icon. Then at the top click "*Create credentials*".

17. Click "API key" don't worry about it for now though. exit and click "Create credentials" again but this time click "Oauth client ID".

18. Click on the selector bar and select "Desktop app" and name it what ever you want because it doesent matter really. Then click "*Create"*.

19. Write down the client ID and cliend secret and use the for later.

20. Run the following commands:
```bash
pip3 install --upgrade google-api-python-client
pip3 install --upgrade google-auth-oauthlib google-auth-httplib2
```

21. Open/Create `client_secrets.json`.

22. Paste the following code:

```json
{
  "web": {
    "client_id": "[[ENTER CLIENT ID HERE]]",
    "client_secret": "[[ENTER CLIENT SECRET HERE]]",
    "redirect_uris": [],
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://accounts.google.com/o/oauth2/token"
  }
}
```

23. Then replace *"[[ENTER CLIENT ID HERE]]"* with your actual Client ID that you wrote down (Make sure you keep the quotes there).

24. Do the same for *"[[ENTER CLIENT SECRET HERE]]"* (Make sure you keep the quotes there).


## Usage

Make sure the image you want to use is downloaded into the auto-video-maker folder and is named ``img.jpg``.


If the file is NOT a jpg do as given below:

```bash
ffmpeg -i [[what ever the file name is with the file extention]] img.jpg
```

After that, run these commands and follow the instructions given to you.

```bash
./main.sh
```

Once, the program is finished. Check for a file with YouTube video name and extension `opus`.

```bash
ffmpeg [[what ever the file is called with the file extension]] -i input.mp3
```

```bash
python3 editor.py
```

> If you did not want to upload the video to youtube follow the next step otherwise you are finished. When the program asks for a video path press *Ctrl + C* in the terminal window and you are done.

## Support

You can support this project by starring it and following me on GitHub.
