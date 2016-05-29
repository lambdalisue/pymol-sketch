*******************************************************
pymol-sketch
*******************************************************

A command collection of `PyMOL`_ to draw compiled graphic objects (CGOs).

.. _PyMOL: http://www.pymol.org

Install
================================================================================
::

    $ pip install sketch-pymol

Confirm if the sketch-pymol is installed correctly by::


    import sketch_pymol

And create a ``sketch.py`` in ``~/.pymol/startup`` directory with the following
content::

    from sketch_pymol import register_commands
    register_commands()


Usage
================================================================================

The following commands will be available

======================= ========================================================
Command                 Description
======================= ========================================================
``sketch_pcoc``         Add a pseudo atom on center of coordinate
``sketch_pcom``         Add a pseudo atom on center of mass
``sketch_scoc``         Draw a sphere on center of coordinate
``sketch_scom``         Draw a sphere on center of mass
``sketch_bbox``         Draw a bounding box
======================= ========================================================


License
================================================================================
The MIT License (MIT)

Copyright (c) 2014 Alisue, hashnote.net

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
