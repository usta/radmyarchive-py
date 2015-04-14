radmyarchive.py
===============

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

    $ RADMYARCHIVE.py RADMYARCHIVE.py [ -m ] SourceDirectory [ -o OutputDirectory ]

Show command line options::

    $ RADMYARCHIVE.py

