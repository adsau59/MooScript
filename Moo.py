"""
Moo.py

Usage:  
  Moo.py -h | --help
  Moo.py [--start=STARTSEQ] --mid=MIDDLESEQ [--end=ENDSEQ] [--timeDelay=TIME_DELAY]

Options:
  -h, --help       Show this screen.
  STARTSEQ         Start Sequence (eg m).
  MIDDLESEQ        Middle Sequence (eg e).
  ENDSEQ           End Sequence (eg w).
  TIME_DELAY       Delay to send messages.

"""

from docopt import docopt

arg = docopt(__doc__)
from pynput import keyboard as kb
from playsound import playsound
import time

print("""Controls
f10: reset text
f11: enter text
f12: exit

Go to the chat box,
press f10 then type,
then press f11""")

recordText = True

pause = False

text = ""

keyboard = kb.Controller()

start = arg["--start"] if arg["--start"] is not None else ""
middle = arg["--mid"]
end = arg["--end"] if arg["--end"] is not None else ""
TIME_DELAY = int(arg["--timeDelay"]) if arg["--timeDelay"] is not None else 0.01

"""
records the text typed
"""


def pressButton(key):
    global keyboard
    keyboard.press(key)
    time.sleep(TIME_DELAY)
    keyboard.release(key)


"""
Processes text
Erases the text then re types it
"""


def eraseAndType():
    global keyboard, text, recordText, arg, start, middle, end, n, smWord

    mooWordsLen = []

    toType = ""

    c = list(text)

    i = 0
    while i < len(c):
        if c[i] == "!":
            toType += "!"
        elif c[i] == "?":
            toType += "?"
        elif c[i] == ".":
            toType += "."
        elif c[i] == "?":
            toType += "?"
        elif c[i] == " ":
            toType += " "
        elif c[i].isdigit():
            toType += c[i]
        elif c[i] == ",":
            toType += ","

        elif i <= 0 or c[i - 1] == " ":

            toType += start + middle
        else:
            toType += middle
            if i + 1 >= len(c) or not c[i + 1].isalpha():
                toType += end

        i += 1

    toType += " (" + text + ")"

    for i in range(0, len(text)):
        pressButton(kb.Key.backspace)

    print(toType)
    for i in list(toType):
        pressButton(i)

    pressButton(kb.Key.enter)


"""
Key press callback
"""


def on_press(key):
    global text, recordText, pause
    try:
        if key == kb.Key.f10:
            playsound("beep.wav")
            recordText = True
            text = ""

        if key == kb.Key.f12:
            return False

        if not pause:
            if key == kb.Key.f11:
                if recordText:
                    eraseAndType()
                    text = ""
                    recordText = False

            if recordText:
                text += key.char
                if len(text) > 160:
                    text = ""

        if key == kb.Key.enter:
            recordText = True

    except AttributeError:

        if not pause:
            if recordText:
                if key == kb.Key.space:
                    text += " "
                if key == kb.Key.backspace:
                    text = text[:-1]

# Collect events until released
with kb.Listener(
        on_press=on_press) as listener:
    listener.join()
