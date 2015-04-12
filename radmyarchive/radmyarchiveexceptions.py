#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Error(Exception):
    def __init__(self):
        self.expr = ""
        self.msg = ""
    pass


class FileNotFoundOrReadError(Error):
    def __init__(self, expr, msg):
        self.expr = expr
        self.msg = msg


class DateTagNotExistError(Error):
    def __init__(self, expr, msg):
        self.expr = expr
        self.msg = msg


class CreateDirError(Error):
    def __init__(self, expr, msg):
        self.expr = expr
        self.msg = msg


class SameNamedFileExistError(Error):
    def __init__(self, expr, msg):
        self.expr = expr
        self.msg = msg
