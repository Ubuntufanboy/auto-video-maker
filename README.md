# auto-video-maker
This app takes audio from a video off of youtube and uses an image to make a video that can upload to youtube


# HOW TO INSTALL

1. Find a youtube link that you would like to use the audio of
2. Find an image you would like to overlay that audio file
3. run ``git clone https://github.com/Ubuntufanboy/auto-video-maker``
4. run ``cd auto-video-maker``
5. run ``chmod +x main1.sh``
6. run ``chmod +x main2.sh``
7. run ``chmod +x combine.sh``
8. run ``sudo apt install ffmpeg`` if that doesent work then run ``sudo apt-get update`` then retry
9. run ``sudo apt install yt-dlp`` if that doesent work then run ``sudo apt-get update`` then retry

At this point I would suggest setting up a virtual envirment for python

10. run ``pip3 install oauth2client``

Congrats! You have no installed all of the tools needed to run this program!

## IF YOU ARE NOT GOING TO UPLOAD THE VIDEO TO YOUTUBE YOU ARE DONE HERE

: )your
: )
: )
hi
: )
: )
: )

## HOW TO SET UP YOUTUBE API

Just as a warning or disclaimer, Youtube will LOCK all of the videos you upload via the api due to youtube not verifying the api

BUT

If you MANUALY upload the videos to youtube it will NOT LOCK the video

### How to set up the youtube api (Takes a long time)

1. navigate to https://cloud.google.com/ and make an accout if you don't already have one
2. click on CONSOLE on the top bar near your google profile image
3. On the left side of your screen you should see a option to make a new project called "Select a project" click on that
4. click on New project and name it what ever you want (But it can NOT be changed later)
5. Click on the bell icon and once the project is done loading click on "Select project" 
6. On the left side on your screen you should see some options. Scroll down until you see "Marketplace" (It should be the 4th option) then click on it
7. type into the search bar "Youtube data api" then select the first option. (At the time it is called "YouTube data api v3") then click enable
8. Once it is done downloading it should take you to a new screen that is the api menu. 
9. Click Oauth consent screen on the left side of your screen.
10. select "External" and click create
11. Fill out the fields that have a red star on then. They are required. Then scroll down and click "Save and continue"
12. You should now be in a menu called Scopes. Click "Add or Remove scopes" then in the filter bar type "upload" then press enter and select the first option that appears
13. click the check mark to the left of it and click "Update". Scroll all the way to the bottom and click "Save an continue"
14. You should now be in a menu called "Test users". Click on "Add users" and type in the gmail account that you would like to use the program with
15. Click save and continue. Then scroll down and click "Back to dashboard"
16. Go to the left of your screen and click "Credentials" with the key icon. Then at the top click "Create credentials"
17. Click "Api key" don't worry about it for now though. exit and click "Create credentials" again but this time click "Oauth client ID"
18. Click on the selector bar and select "Desktop app" and name it what ever you want because it doesent matter really. Then click "Create"
19. Write down the client ID and cliend secret and use the for later. 
20. Go back to your terminal and run ``pip install --upgrade google-api-python-client`` and then run ``pip install --upgrade google-auth-oauthlib google-auth-httplib2`` 

ALMOST DONE!!!

21. run ``vim client_secrets.json``
22. press i and the paste the following code into the terminal

{
  "web": {
    "client_id": "[[ENTER CLIENT ID HERE]]",
    "client_secret": "[[ENTER CLIENT SECRET HERE]]",
    "redirect_uris": [],
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://accounts.google.com/o/oauth2/token"
  }
}

23. then replace [[ENTER CLIENT ID HERE]] with your actual cliend id that you wrote down (Make sure you keep the quotes there)
24. do the same for [[ENTER CLIENT SECRET HERE]] (Make sure you keep the quotes there)
25. press escape and type ":wq" then enter (Yes you really do need that colon)

Yay only 25 steps

## HOW TO USE THE PROGRAM
1. Make sure the image you want to use is downloaded into the auto-video-maker folder and is named ``img.jpg`` if the file is NOT a jpg follow these steps

2. (only if the image is NOT a jpg) run ``ffmpeg -i [[what ever the file name is with the file extention]] img.jpg``

3. run ``./main1.sh`` (Yes we need that dot before the slash)

4. Listen to the instructions and enter thr youtube link

5. Once the program is finished run ``ls`` and find the youtube video name that has .opus as the file extention

6. run ``ffmpeg [[what ever the file is called with the file extention]] -i input.mp3``

7. run ``./main2.sh``

8. Follow the instructions given to you

9. If you did not want to upload the video to youtube follow the next step otherwise you are finished

10. when the program asks for a video path press "ctrl + c" in the terminal window and you are done
