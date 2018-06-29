# Keyboard Paste as typing

This script generate keyboard events to generate a paste from clipboard like as you are writing, typing key to key.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. It's useful to use on virtual machines without shared clipboard.

### Prerequisites

This project use [Xerox](https://github.com/kennethreitz/xeroxlibrary), to install it simply:

```
$ pip install xerox
```
Note: If you are installing xerox on Windows, you will also need to install the pywin32 module.

Note: On X11 systems, Xerox requires Xclip, which can be found through your system package manager (e.g. apt-get install xclip) or at [https://github.com/astrand/xclip](https://github.com/astrand/xclip).