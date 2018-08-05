# MooScript

Roleplay in games with MooScript.

MooScript replaces the words you write with the sounds of the animal or thing you want, so if you want to become a cow, and you type `How are you guys doing?` it would become `Mooo mooo mooo mooo mooooo? (How are you guys doing?)`, it puts the text you write in a bracket so that people could understand what you write xD

### Technology Stack
MooScript is made using,

- Python
- (Docopt)[http://docopt.org/], Command-line interface description language.
- (pynput)[https://pypi.org/project/pynput/], Monitor and control user input devices.
- (playsound)[https://pypi.org/project/playsound/], Pure Python, cross platform, single function module with no dependencies for playing sounds.

### How does it work?
- MooScript keylogs what you type (don't worry it doesn't send anything to any server, you can check the scripts yourself)
- Then when f11 is pressed, it transforms the text you typed by replacing letters by sound you defined in CLI and concats the text in the end inside the brackets
- It doesn't replace the punctuations as it adds a bit detail in roleplay
- Then it types the transformed text with a small delay between keystroke (as games usually run on low then MooScript), and then presses enter

### How to use?
- Download a release from [here](https://github.com/adsau59/MooScript/releases)
- then run Moo.exe with options
	- `--start=STARTSEQ` (optional) string to put in start of sound, For Moooo, it'll be 'M'
	- `--mid=MIDDLESEQ` string to replace the letters, For Mooo, it'll be 'o'
	- `--end=ENDSEQ` (optional) string to put in end of sound, For Woof, it'll be 'f'
	- `--timeDelay=TIME_DELAY` (optional) delay between keystrokes to type in letters, must be lower than game's fps.

### Feeling generous?
You can donate me on [PayPal](https://www.paypal.me/AdamSaudagar).

### Licencse
This project is licence to the MIT License, check out the full licence over [here](https://github.com/adsau59/MooScript/blob/master/LICENSE).