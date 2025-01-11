radmyarchive.py
===============

************
Upcoming Rewrite
************

I will soon begin a complete rewrite of the RADMyArchive project. This decision is driven by several factors:

1. **Modernization:** The original code was written over 10 years ago, and it is essential to update it to be compatible with Python 3.10 and take advantage of modern programming practices and libraries.
2. **Enhanced Functionality:** The rewrite will allow for improved handling of EXIF data and better overall performance.
3. **User Experience:** I aim to implement better error handling and user feedback mechanisms to enhance the usability of the tool.
4. **Maintainability:** A fresh codebase will make it easier to maintain and extend the project in the future.

************
RADMyArchive
************

RADMyArchive is a simple photo rearranger with help of EXIF tags

RadMyArchive ( RenameAsDate My Archive ) Rearranges Image files according to their
EXIF DateTimeOriginal information ( If exiftags are missing it uses mdate/cdate of image files ).

Written by Ömer Fadıl Usta

************
Installation
************

PyPI
****
The recommended process is to install the PyPI package, as it allows easily staying up to date::

    $ pip install radmyarchive

See the `pip documentation <http://www.pip-installer.org/en/latest/>`_ for more info.


*****
Usage
*****

Command line
************
::

    $ RADMYARCHIVE.py [ -m ] SourceDirectory [ -o OutputDirectory ]

Show command line options::

    $ RADMYARCHIVE.py

