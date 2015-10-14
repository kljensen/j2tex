j2tex
============

Python script to create templated LaTeX documents using Jinja2.

Usage
-----

Installation
------------

Requirements
^^^^^^^^^^^^

Goals
-------------
My goals are as follows

- Read template files that hav Jinja2 markup in them
- Read a Yaml file with context data. The Yaml file should
  support a global context and also overloads, e.g.
  for individual recipients of a letter
- Produce one or more `.tex` files in a specified output directory.

Installation
-------------
Install via pip

.. code:: shell

  pip install -e 'git+git@github.com:kljensen/j2tex.git#egg=j2tex'

Usage
------------
There is a script called ``j2tex.py`` that you can run as follows.

.. code:: shell

  j2tex.py --context recipients.yaml --template_directory templates

Then, I use a Makefile to compile the ``.tex`` documents to PDF. Mine looks
somethign like this

.. code:: make

  #  Makefile for LaTeX documents
  #
  TARGET = *.pdf
  LATEX = xelatex
  TEMPLATE_DIRECTORY = templates
  CONTEXT_FILE = recipients.yaml
  TEMPLATES = $(TEMPLATE_DIRECTORY)/*.tex.j2
  DELETE = *.log *.pdf *.aux
  .SUFFIXES: .pdf .tex

  all: $(TARGET)
  $(MAKE) $(TARGET)

  *.tex: $(TEMPLATES) $(CONTEXT_FILE)
  j2tex.py --context $(CONTEXT_FILE) --template_directory $(TEMPLATE_DIRECTORY)

  .tex.pdf:
  $(LATEX) $<
  $(LATEX) $<

  clean:
  rm -f $(DELETE)


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

`j2tex` was written by `Kyle Jensen <kljensen@gmail.com>`_.
