from distutils.core import setup
import py2exe

setup(
    console=['Moo.py'],
    data_files = [('',['beep.wav'])],
    options = {
        'py2exe': {
            'includes': ['docopt','pynput','playsound']
        }
    }
)
