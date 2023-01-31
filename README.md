<h1 align="center">
  VRC-ClockOSC-Py
</h1>

<h4 align="center">Very simple and highly customizable local time display for vrchat chatbox using OSC and Python.</h4>

<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#download">Download</a> •
  <a href="#spotify-dev-portal">Dev Portal Instructions</a> •
  <a href="#credits">Credits</a> •
  <a href="#license">License</a>
</p>

## Key Features
* Customizable
  - Able to change the time formatting very easy, by [following this](https://docs.python.org/2/library/time.html#time.strftime) guide on what letters do what in time.strftime, change the letters inside this string `("%I:%M:%S %p (%H:%M) in %Z"` in this line.</br> `curr_time = time.strftime("%I:%M:%S %p (%H:%M) in %Z", time.localtime())`
* Cross platform
  - Windows, macOS and Linux ready.
## How To Use

To clone and run this application, you'll need [Python](https://www.python.org/downloads/) and [git](https://gitforwindows.org/) (links for windows) From your command line:

```bash
# Clone this repository
$ git clone https://github.com/Mezque/VRC-ClockOSC-Py

# Go into the repository
$ cd VRC-ClockOSC-Py/src

# Install dependencies
$ pip install -r requirements.txt

# Run the app
$ pyhon clockOSC.py
```
> **Note**
> If you're using Windows, there is included bat files to do step 3 and 4. You just need to install first, following step 1 and 2 above or <a href="#download">download</a> section below. </br>
> (if you choose to download below you don't need to clone the repositroy or install git) </br> </br>
> If Python is failing to run properly on Windows install it from the [Microsoft Store](https://apps.microsoft.com/store/detail/python-311/9NRWMJP3717K?hl=en-us&gl=us) instead of the python website for an easy fix; this is *usally* a Windows problem to do with how python is set up under your system variables. Look into that if you wish to try and fix it otherwise.</br>

## Download

You can [download (to add)]() the latest version as well if you don't want to use git to clone the repository. It's the same thing just slower for people less experienced with usage of git through a CLI.

## Dependencies
python-osc that can be installed via pip.
```bash
pip install python-osc
```

## Credits
This software uses the following open source packages:

- [Python-Osc](https://pypi.org/project/python-osc/)
## License

MIT

---
