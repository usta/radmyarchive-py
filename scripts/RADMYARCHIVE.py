#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os.path
import sys
import getopt
from colorama import init
from termcolor import colored
import radmyarchive



def usage(exit_status):
    """Show command line usage."""
    msg = ('Usage: RADMYARCHIVE.py [ -m ] SourceDirectory [ -o OutputDirectory ]\n'
           'RadMyArchive ( RenameAsDate My Archive ) Rearranges Image files according to their\n'
           'EXIF DateTimeOriginal information.\n\nOptions:\n'
           '-h              --help                          Display usage information and exit.\n'
           '-v              --version                       Display version information and exit.\n'
           '-m              --move                          Do not copy just Move Files.\n'
           '-o OutputFolder --output= OutputFolder          Specify output folder\n\n'
           'Ex: radmyarchive ~/photos -o ~/newArchive\n'
           '    radmyarchive -m ~/photos -o ~/newArchive\n\n'
           'Don\'t forget to wrap your path if there is space in it :\n'
           '    radmyarchive \"~/photos/old picnic\" -o \"~/new Archive\"\n')
    print(msg)
    sys.exit(exit_status)


def show_version():
    """Show the program version."""
    print('Version %s on Python%s' % (radmyarchive.__version__,
                                      sys.version_info[0]))
    sys.exit(0)


def main():
    """Parse command line options/arguments and execute."""
    args = []
    opts = []
    # TODO pattern = "*"
    source = ""
    destination = ""
    move = False
    extensions = [".JPG", ".PNG", ".GİF", ".GIF", ".JPEG", ".ARW", ".SRF", ".SR2", ".BAY", ".CRW", ".CR2",
                  ".CAP", ".TIF", ".IIQ", "İİQ", ".EIP", "EİP", ".DCS", ".DCR", ".DRF", ".K25", ".KDC", ".DNG",
                  ".ERF", ".FFF", ".MEF", ".MOS", ".MRW", ".NEF", ".NRW", ".ORF", ".PTX", ".PEF",
                  ".PXN", ".R3D", ".RAF", ".RAW", ".RW2", ".RW1", ".RWZ", ".X3F"]

    # colorama - Colorful output
    init()

    try:
        arg_names = ["help", "version", "move", "output="]
        opts, args = getopt.gnu_getopt(sys.argv[1:],
                                       "hvmo:v",
                                       arg_names)
    except getopt.GetoptError:
        usage(2)

    for option, arg in opts:
        if option in ("-h", "--help"):
            usage(0)
        if option in ("-v", "--version"):
            show_version()
        if option in ("-m", "--move"):
            move = True
        if option in ("-o", "--output"):
            destination = arg

    if not args:
        usage(2)
    else:
        source = args[0]

    for currentFile in listFiles(source):
        if os.path.splitext(currentFile)[1].upper() not in extensions:
            continue

        try:
            a = radmyarchive.RADMyArchive(os.path.join(source, currentFile),
                                          destination=destination,
                                          move=move)

            print("%s --> %s" % (colored(currentFile, "green"),
                                 colored(a.getDestinationFilePath(), "yellow")))
        except radmyarchive.radmyarchiveexceptions.Error as e:
            print("%s : %s" % (colored(e.expr, "red"),
                               e.msg))


def listFiles(path):
    """Yield file names not starting with '.' under given path."""
    if not os.path.exists(path):
        print("%s : Path couldn't be found! Make sure to wrap your path between \" and \"" % colored(path, "red"))
        usage(2)

    if sys.version_info[0] == 3 and sys.version_info[1] >= 5:
        for entry in os.scandir(path):
            if not entry.name.startswith('.') and not entry.is_dir():
                yield entry.name
    else:
        for entry in os.listdir(path):
            if not entry.startswith('.') and os.path.isfile(os.path.join(path, entry)):
                yield entry

if __name__ == '__main__':
    main()