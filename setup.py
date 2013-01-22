#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2012, Peter Hillerström <peter.hillerstrom@gmail.com>
# All rights reserved. This software is licensed under 3-clause BSD license.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.

from __future__ import with_statement

import sys
from distutils.core import setup, Command

PACKAGE_NAME = 'leftrb'
PACKAGE_VERSION = '0.1'
PACKAGES = []

with open('README.md', 'r') as readme:
    README_TEXT = readme.read()

class PyTest(Command):
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        import sys,subprocess
        errno = subprocess.call([sys.executable, 'runtests.py'])
        raise SystemExit(errno)

setup(
    name=PACKAGE_NAME,
    version=PACKAGE_VERSION,
    packages=PACKAGES,
    requires = [],
    scripts=[],

    description="""Leftrb/LLRB is a Left-Leaning Red-Black (LLRB) implementation
of 2–3 balanced binary search trees in Python.

The LLRB method of implementing 2-3 trees is a recent improvement over the traditional
implementation — it maintains an additional invariant that all red links must lean left
except during inserts and deletes. Because of this, they can be implemented by adding
just a few lines of code to standard BST algorithms.

This is a port of the code in the article “Left-leaning Red-Black Trees”
by Robert Sedgewick of Princeton University at
http://www.cs.princeton.edu/~rs/talks/LLRB/LLRB.pdf""",
    long_description=README_TEXT,
    author='Peter Hillerström',
    author_email='peter.hillerstrom@gmail.com',
    license='MIT License',
    url='https://github.com/peterhil/leftrb',

    classifiers = [
            'Development Status :: 4 - Beta',
            'Environment :: Other Environment',
            'Intended Audience :: Developers',
            'Intended Audience :: Education',
            'Intended Audience :: Information Technology',
            'Intended Audience :: Science/Research',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 3',
            'Topic :: Other/Nonlisted Topic',
            'Topic :: Scientific/Engineering',
            'Topic :: Software Development',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Topic :: Utilities',
    ],
    cmdclass = {
        'test': PyTest
    },
)