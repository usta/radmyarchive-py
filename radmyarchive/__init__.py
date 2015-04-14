#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__version__ = "1.1.1"


from fileinput import close
import exifread
import os
import shutil
import time
from .radmyarchiveexceptions import *


class RADMyArchive:
    def __init__(self, filepath, destination=".//NewImageArchive", move=False):

        self._filePath = filepath
        self._fileExt = os.path.splitext(self._filePath)[1]
        self._file = None
        self._destinationBasePath = destination
        self._destinationFilePath = ""
        self._imgFullDate = ""
        self._imgYear = ""
        self._imgMonth = ""
        self._imgDay = ""
        self._imgTime = ""
        self._move = move

        self._parseDate()
        self._createDestinationDirs()

        self._destinationFilePath = os.path.join(self._destinationBasePath,
                                                 self._imgYear,
                                                 self._imgMonth,
                                                 self._imgDay, "") + self._imgFullDate + self._fileExt

        self._fileOperation()

    def _fileOperation(self):
        if os.path.exists(self._destinationFilePath):
            raise SameNamedFileExistError(self._destinationFilePath,
                                          "There is already a file exist with Same name")

        if self._move:
            shutil.move(self._filePath,
                        self._destinationFilePath)
        else:
            shutil.copyfile(self._filePath,
                            self._destinationFilePath)

    def _createDestinationDirs(self):
        path = os.path.join(self._destinationBasePath,
                            self.getYear(),
                            self.getMonth(),
                            self.getDay())
        try:
            os.makedirs(path,
                        exist_ok=True)
        except:
            raise CreateDirError(self._destinationBasePath,
                                 "Destination Directories couldn't created")

    def _openImageFile(self):
        try:
            self._file = open(self._filePath, 'rb')
        except:
            raise FileNotFoundOrReadError(self._filePath,
                                          "Couldn't Found or couldn't Open")

    def _closeImageFile(self):
        close()
        del self._file  # We need to delete and free file variable otherwise windows couldn't move current file
        self._file = None

    def _parseDate(self):
        self._openImageFile()
        tags = exifread.process_file(self._file,
                                     stop_tag='DateTimeOriginal',
                                     details=False)
        self._closeImageFile()

        if not tags:
            self._parseDateWOExif()
        else:
            self._parseDateExif(tags)

        self._imgFullDate = ("%s-%s-%s %s" % (self._imgYear,
                                              self._imgMonth,
                                              self._imgDay,
                                              self._imgTime))

    def _parseDateExif(self, tags):
        if 'EXIF DateTimeOriginal' not in tags.keys():
            if 'Image DateTime' in tags.keys():
                date_information = tags['Image DateTime'].printable
            elif 'DateTime' in tags.keys():
                date_information = tags['DateTime'].printable
            else:
                raise DateTagNotExistError(self._filePath + " DateTimeOriginal TAG :",
                                           "Tag Not Found")
        else:
            date_information = tags['EXIF DateTimeOriginal'].printable

        self._imgYear = date_information[:4]
        self._imgMonth = date_information[5:7]
        self._imgDay = date_information[8:10]
        self._imgTime = ("%s.%s.%s" % (date_information[11:13],
                                       date_information[14:16],
                                       date_information[17:19]))


    def _parseDateWOExif(self):
        mdate = os.path.getmtime(self._filePath)
        cdate = os.path.getctime(self._filePath)
        if mdate < cdate:
            date = mdate
        else:
            date = cdate

        self._imgYear = ("%s" % ("%02d" % time.gmtime(date)[0]))
        self._imgMonth = ("%s" % ("%02d" % time.gmtime(date)[1]))
        self._imgDay = ("%s" % ("%02d" % time.gmtime(date)[2]))
        self._imgTime = ("%s.%s.%s" % (("%02d" % time.gmtime(date)[3]),
                                       ("%02d" % time.gmtime(date)[4]),
                                       ("%02d" % time.gmtime(date)[5])))

    def getFullDate(self):
        return self._imgFullDate

    def getYear(self):
        return self._imgYear

    def getMonth(self):
        return self._imgMonth

    def getDay(self):
        return self._imgDay

    def getTime(self):
        return self._imgTime

    def getFileExt(self):
        return self._fileExt

    def getDestinationFilePath(self):
        return self._destinationFilePath