# grove.py
========

[![Build Status](https://travis-ci.org/Seeed-Studio/grove.py.svg?branch=master)](https://travis-ci.org/Seeed-Studio/grove.py)
[![](https://img.shields.io/pypi/v/grove.py.svg)](https://pypi.python.org/pypi/grove.py)

Python library for Seeedstudio Grove Devices on embeded Linux platform, especially good on below platforms:
- [Coral Dev Board](https://www.seeedstudio.com/Coral-Dev-Board-p-2900.html) [(Wiki)](http://wiki.seeedstudio.com/Grove_Base_Hat_for_Raspberry_Pi/#software)
- [NVIDIA Jetson Nano](https://www.seeedstudio.com/NVIDIA-Jetson-Nano-Development-Kit-p-2916.html) [(Wiki)](http://wiki.seeedstudio.com/Grove_Base_Hat_for_Raspberry_Pi/#software)
- [Raspberry Pi](https://www.seeedstudio.com/category/Boards-c-17.html) [(Wiki)](http://wiki.seeedstudio.com/Grove_Base_Hat_for_Raspberry_Pi/#software)

<br><br>
## Installation on Raspberry Pi and Host
### Install pygame
```shell
python3 -m pip install -U pygame --user
```
### Install grove.py
```shell
git clone https://github.com/yruefenacht/grove.py
cd grove.py
# Python2
sudo pip install .
# Python3
sudo pip3 install .
```

<br><br>
## Usage
Run grove server on Raspberry
```shell
python grove/grove_server.py 5 6
```
Run space slide invaders on Host
```shell
python grove/space_slide_invaders.py
```

<br><br>
## API Documentation
click [here](https://seeed-studio.github.io/grove.py)

[how to update me](sphinx/README.md)

