#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from codecs import open
from os import path
import radmyarchive

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    readme_file = f.read()

setup(
    name="radmyarchive",
    version=radmyarchive.__version__,
    author="Ömer Fadıl Usta",
    author_email="omerusta@gmail.com",
    packages=find_packages(),
    scripts=["radmyarchive.py"],
    url="https://github.com/usta/radmyarchive-py",
    license="BSD",
    keywords="exif image photo rename metadata arrange rearrange catalogue",
    description="A simple photo rearranger with help of EXIF tags",
    long_description=readme_file,
    classifiers=(
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Topic :: Utilities",
    ),
    install_requires=['ExifRead', 'termcolor', 'colorama'],
)