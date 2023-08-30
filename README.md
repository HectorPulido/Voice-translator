# Voice-translator

This is a near real time translator, recognize the speech and translate it.

## How to user
First you must to install all the dependences with the command 

if you want to use OpenAI whisper, you must install ffmpeg with the commands

~~~
# on Ubuntu or Debian
sudo apt update && sudo apt install ffmpeg

# on Arch Linux
sudo pacman -S ffmpeg

# on MacOS using Homebrew (https://brew.sh/)
brew install ffmpeg

# on Windows using Chocolatey (https://chocolatey.org/)
choco install ffmpeg

# on Windows using Scoop (https://scoop.sh/)
scoop install ffmpeg
~~~

Then install the python dependences with the command

~~~
pip install -r requirements.txt
~~~

Then you can use the software using the command from the command line, example:
~~~
python3 main.py -d 0 --t #000 --b #0f0  -s 800x50
~~~

## Optional 

usage: main.py [-h] [-d DEVICE] [-b BACKGROUND_COLOR] [-s SIZE] [-t TEXT_COLOR] [-l DEVICE_LIST] [--font FONT] [--font_size FONT_SIZE]

options:
  -h, --help                              | show this help message and exit <br>
  -d --device DEVICE                      | Device of microphone <br>
  -b --background_color BACKGROUND_COLOR  | Color of the background <br>
  -s --size SIZE                          | Size of the window <br>
  -t --text_color TEXT_COLOR              | Color of the text <br>
  -l --device_list DEVICE_LIST            | Show the device list <br>
  --font FONT                             | Font of the text <br>
  --font_size FONT_SIZE                   | Size of the font <br>


<br>

<div align="center">
<h3 align="center">Let's connect 😋</h3>
</div>
<p align="center">
<a href="https://www.linkedin.com/in/hector-pulido-17547369/" target="blank">
<img align="center" width="30px" alt="Hector's LinkedIn" src="https://www.vectorlogo.zone/logos/linkedin/linkedin-icon.svg"/></a> &nbsp; &nbsp;
<a href="https://twitter.com/Hector_Pulido_" target="blank">
<img align="center" width="30px" alt="Hector's Twitter" src="https://www.vectorlogo.zone/logos/twitter/twitter-official.svg"/></a> &nbsp; &nbsp;
<a href="https://www.twitch.tv/hector_pulido_" target="blank">
<img align="center" width="30px" alt="Hector's Twitch" src="https://www.vectorlogo.zone/logos/twitch/twitch-icon.svg"/></a> &nbsp; &nbsp;
<a href="https://www.youtube.com/channel/UCS_iMeH0P0nsIDPvBaJckOw" target="blank">
<img align="center" width="30px" alt="Hector's Youtube" src="https://www.vectorlogo.zone/logos/youtube/youtube-icon.svg"/></a> &nbsp; &nbsp;

</p>
