jinjaxelatex
============

Python script to create templated XeLaTeX documents

Usage
-----

Installation
------------

Requirements
^^^^^^^^^^^^

Goals
-------------
My goals are as follows

- Read a ``.tex.j2`` file that has Jinja2 markup in it
- Read a Yaml file with context data

  * The Yaml file should support a global context and also
    overloads for, e.g. individual recipients of a letter

- Produce one or more `.tex` files and compile those to `.pdf` format.
- Allow a custom output directory for the produced PDFs

License
-------
This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org/>

Authors
-------

`jinjaxelatex` was written by `Kyle Jensen <kljensen@gmail.com>`_.
