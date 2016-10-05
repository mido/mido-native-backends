import ctypes

lib = ctypes.CDLL('./test.so')

def callback(i):
    print(i)

# WINFUNCTYPE in Windows
# https://stackoverflow.com/questions/17980167/writing-python-ctypes-for-function-pointer-callback-function-in-c
FUNC = ctypes.CFUNCTYPE(None, ctypes.c_int)

lib.call_callback(FUNC(callback))
