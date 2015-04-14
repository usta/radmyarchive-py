Change Log
==========
1.1.1 2015-04-14
    * Fix setup.py import bug ( Thanks to Umut Karcı )
    
1.1.0 2015-04-14
    * a python bug fixed with changing scripts name to uppercase
    * fix for linux builds ( use os.path.join instead os string operations for path )

1.0.5 2015-04-12
    * Raw image format extensions added
    * Fix for python3 env for python2 default envs

1.0.0 2015-04-10
    * First Commit to Github

0.2.0 2015-04-09
    * colormo is used with termcolor to make Windows OSes happy about colorful output
    * missing termcolor , termcolor and exifread added as install_requare
    * add support for python < 3.5 ( os.scandir only used if python 3.5 installed )
    * add support images which don't have EXIF
    * path with spaces bug fixed
    * Checks for extension before trying to open a file


0.1.5 2015-04-08
    * Use termcolor to make Colorful output
    * -m --move argument added for just moving files instead of copying


0.1.0 2015-04-08
    * Permission checks added
    * Checks for same named file exist or not before copy/move
    * Start to use Generator instead of Lists


0.0.5 2015-04-07
    * Rewritten to obey Standart Python project template
    * Destination directory now can be changed via CLI
    * Base code rewritten more readable with separating functions
    * Some PEP8 changes
    * CLI arguments added
    * Version Information added
    * Help Information added


0.0.1 2015-04-06
    * First working draft written


2015-04-05 Project Started
    * Initial idea about project.
    * Usage of Exif-py module decided