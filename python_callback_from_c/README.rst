An example of how to call a Python function from C. This can possibly
be used for callbacks.

One issue is the Python global lock. I'm not sure how this can be
solved without calling the Python C API from C. (The API doesn't know
about the lock.)

https://docs.python.org/2/library/ctypes.html#callback-functions

https://stackoverflow.com/questions/17980167/writing-python-ctypes-for-function-pointer-callback-function-in-c
