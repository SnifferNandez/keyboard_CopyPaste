# Keyboard Paste as typing

This script generate keyboard events to generate a paste from clipboard like as you are writing, generate keystrokes events using python.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. It's useful to use on virtual machines without shared clipboard.

### Prerequisites

This project use [Xerox](https://github.com/kennethreitz/xeroxlibrary), to install it simply:

```
$ pip install xerox
```
Note: If you are installing xerox on Windows, you will also need to install the pywin32 module.

Note: On X11 systems, Xerox requires Xclip, which can be found through your system package manager (e.g. apt-get install xclip) or at [https://github.com/astrand/xclip](https://github.com/astrand/xclip).

## Usage

To trigger the paste script, you would start with the defined useIfStarts value, if *useIfStarts = 'keypaste'* then try to copy:
```
keypasteHello World
```

## Authors

* **Carlos Fernandez** - *Initial work* - [SnifferNandez](https://github.com/SnifferNandez)

See also the list of [contributors](https://github.com/csieteco/mvp_vocational_test/contributors) who participated in this project.

## ToDo
[ ] Test UnicodeEncodeError