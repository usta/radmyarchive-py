#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from codecs import open
from os import path
import re
import ast
here = path.abspath(path.dirname(__file__))

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('radmyarchive/__init__.py', 'rb') as vf:
    version = str(ast.literal_eval(_version_re.search(
        vf.read().decode('utf-8')).group(1)))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    readme_file = f.read()

setup(
    name="radmyarchive",
    version=version,
    author="Ömer Fadıl Usta",
    author_email="omerusta@gmail.com",
    packages=find_packages(),
    scripts=["scripts/RADMYARCHIVE.py"],
    url="https://github.com/usta/radmyarchive-py",
    license="BSD",
    keywords="exif image photo rename metadata arrange rearrange catalogue",
    description="A simple photo rearranger with help of EXIF tags",
    install_requires=['exifread', 'termcolor', 'colorama'],
    long_description=readme_file,
    classifiers=(
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.4",
        "Topic :: Utilities",
    ),
)