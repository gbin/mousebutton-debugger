## Mouse Button Debugger

Have you never be in the situation where you don't trust your mouse ?

Sometimes you click something and it doesn't do anything and you start to doubt about your device or ...
Was it a bug from the application ?

This is a simple tool help you discriminating this problem by registering all your mouse clicks at the kernel device level.

Happy debugging !

It is open source under the GPL3 license.


## Installation

you need to install a dependency "evdev" with :

```
pip install evdev
```

and run mdebug.py under python 3, for example :

```
python3.2 mdebug.py
```

You will be prompt to choose between devices, choose the one you want to debug and at every click it will dump a timestamp and the event:

```
key event at 1354230638.344157, 272 (BTN_MOUSE), down
key event at 1354230638.433001, 272 (BTN_MOUSE), up
key event at 1354230638.589123, 273 (BTN_RIGHT), down
key event at 1354230638.674002, 273 (BTN_RIGHT), up
key event at 1354230639.908045, 272 (BTN_MOUSE), down
key event at 1354230639.993045, 272 (BTN_MOUSE), up
```

