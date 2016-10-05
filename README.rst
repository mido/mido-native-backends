Mido Native Backends
====================

These are notes and little prototypes I've made for adding native
backends for ALSA (Linux), CoreMIDI, Windows MIDI to `Mido
<https://mido.readthedocs.io/>`_.

From the research I've done it seems that it should be possible to
write pure Python code to interface with all of these APIs using
ctypes.

The default backend on each operating system could be the native API.
This would remove the external dependency (PortMidi or RtMidi). It
would also remove one layer between Mido and the operating system.


Why?
----

The current default backend (as of version 1.1.6) is PortMidi. This is
not ideal for two reasons:

    * it's hard to install, especially on Windows
    * RtMidi is better in every way

Making RtMidi the new default still has some drawbacks:

    * it's still an external dependancy
    * building python-rtmidi requires a C++ compiler. (Pre built packages
      are often available though)
    * confusion between python-rtmidi and rtmidi-python


Native Plugins
--------------

ALSA, CoreMIDI and Windows MIDI all have C APIs that can be wrapped
with pure Python code using ctypes. The idea is to default to the most
common native API on the given operating system (based on values found
in sys).

Advantages:

    * no more external dependencies
    * pure Python, no need for a compiler
    * one fewer layers between Mido and the host OS (more control)
    * more control over the things that matter to Mido

Downsides:

    * the APIs can be complex (ALSA certainly is)
    * a lot more work than wrapping one high level library
    * duplication of effort with RtMidi

(CFFI could be a lot easier to use than ctypes but would create a
dependency that also requires a C (or C++?) compiler.)


Status
------

The first step is to find out how (or if) it's possible to wrap these
libraries using only ctypes. The results so far are promising.

I've found that you can indeed:

    * link to the libraries with ctypes (macOS requires a few extra steps)
    * call a Python function from C (for callbacks)

Some challenges:

    * the APIs can be complex and require a lot of work and a lot of
      code for very little. Studying RtMidi could be a great help here.
    * setting up data structures for ALSA (which uses a lot of structs)
      looks like it could be tricky.
    * things such as thread safety and buffering must be considered

So far my conclusion is that it will be possible but a lot of
work. The question is whether it will be worth it.


Contact
-------

Ole Martin Bjørndalen - ombdalen@gmail.com
