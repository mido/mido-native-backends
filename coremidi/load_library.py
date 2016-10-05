"""Load CoreMIDI library on macOS.

Some rough code I threw togther. I was able to load the library and
call functions in it.

Loading a library is different from loading a .dynlib
file. Fortunately ctypes has support for this.
"""
import ctypes
import ctypes.util
from ctypes import CFUNCTYPE

def load_library(name):
    """Load a library (not a .dynlib file)"""
    path = ctypes.util.find_library(name)
    print(path)
    return ctypes.cdll.LoadLibrary(path)

# + Foundation?

core_midi = load_library('CoreMIDI')
foundation = load_library('Foundation')

num_devs = core_midi.MIDIGetNumberOfDevices()

dev = core_midi.MIDIGetDevice(0)
print(dev)

# print(num_devs)

# client_name = core_foundation()
