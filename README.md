# Keyboard Paste as typing

This script generate keyboard events to generate a paste from clipboard like as you are writing, generate keystrokes events using python.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. It's useful to use on virtual machines without shared clipboard.

### Prerequisites

This project use:
* [Xerox](https://github.com/kennethreitz/xeroxlibrary)
* ~~[PyAutoGUI](https://github.com/asweigart/pyautogui)~~
* [Keyboard](https://github.com/boppreh/keyboard)

#### Xerox

To install it simply:

```
$ pip install xerox
```
Note: If you are installing xerox on Windows, you will also need to install the pywin32 module.

Note: On X11 systems, Xerox requires Xclip, which can be found through your system package manager (e.g. apt-get install xclip) or at [https://github.com/astrand/xclip](https://github.com/astrand/xclip).

#### Keyboard

* Works with Windows and Linux (requires sudo), with experimental OS X support.
* Zero dependencies.

To install it simply:

```
$ pip install keyboard
```
Note: Need more test to improve the functionality, for example, this chars have issues in some cases:

    keyboard.send("#")
    keyboard.send("=")
    keyboard.send("(")
    keyboard.send(")")

#### PyAutoGUI (optional)

This package optional considered because some [keyboard support issues exists](https://github.com/asweigart/pyautogui/issues/137). If you prefer this library over keyboard change the *usePyautogui* variable to True.

First:
* *Windows* has no dependencies.
* *OS X* needs the pyobjc-core and pyobjc module installed (in that order).
* *Linux* needs the python3-xlib (or python-xlib for Python 2) module installed (e.g. apt-get install python-xlib).

Second: Pillow needs to be installed

Finally:

```
$ pip install pyautogui
```
Note 1: To install Pillow on Linux you may need to install additional libraries to make sure Pillow's PNG/JPEG works correctly. See:

    https://stackoverflow.com/questions/7648200/pip-install-pil-e-tickets-1-no-jpeg-png-support
    http://ubuntuforums.org/showthread.php?t=1751455

Note 2: Need more test to improve the functionality, for example, this chars have issues in some cases:

    pyautogui.press("'")
    pyautogui.press("=")
    pyautogui.press(":")

## Usage

To trigger the paste script, you would start with the defined useIfStarts value, if *useIfStarts = 'keypaste'* then try to copy:
```
keypasteHello World
```

## Authors

* **Carlos Fernandez** - *Initial work* - [SnifferNandez](https://github.com/SnifferNandez)

See also the list of [contributors](https://github.com/SnifferNandez/keyboard_CopyPaste/contributors) who participated in this project.

## ToDo
[ ] Test UnicodeEncodeError