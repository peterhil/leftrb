#!/usr/bin/env python
# encoding: utf-8
#
# Leftrb is a Left-Leaning Red-Black tree implementation in Python.
# Copyright (c) 2013, Peter Hillerström <peter.hillerstrom@gmail.com>
#
# This file is part of Leftrb.
#
# Leftrb is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as
# published by the Free Software Foundation, either version 3
# of the License, or (at your option) any later version.
#
# Leftrb is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with Leftrb.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import with_statement
from setuptools import setup, Command

PACKAGE_NAME = 'leftrb'
PACKAGE_VERSION = '0.1.2'
PACKAGES = ['leftrb']

with open('README.md', 'r') as readme:
    README_TEXT = readme.read()


class PyTest(Command):
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        import sys
        import subprocess
        errno = subprocess.call([sys.executable, 'runtests.py', '-v', 'leftrb/test'])
        raise SystemExit(errno)


setup(
    name=PACKAGE_NAME,
    version=PACKAGE_VERSION,
    packages=PACKAGES,
    requires=[],
    install_requires=['distribute'],
    tests_require=['pytest>=2.3.4'],
    scripts=[],

    description="""Leftrb is a Left-Leaning Red-Black (LLRB) implementation of 2–3 balanced binary
search trees in Python. This is a straightforward port of the `code`_ presented
by Robert Sedgewick in `his paper`_.

`README`_ at Github.

.. _code: http://www.cs.princeton.edu/~rs/talks/LLRB/Java/RedBlackBST.java
.. _`his paper`: http://www.cs.princeton.edu/~rs/talks/LLRB/LLRB.pdf
.. _README: https://github.com/peterhil/leftrb/blob/master/README.md
""",
    long_description=README_TEXT,
    author='Peter Hillerström',
    author_email='peter.hillerstrom@gmail.com',
    license='MIT License',
    url='https://github.com/peterhil/leftrb',

    classifiers = [
            'Development Status :: 4 - Beta',
            'Environment :: Other Environment',
            'Intended Audience :: Developers',
            'Intended Audience :: Information Technology',
            'Intended Audience :: Science/Research',
            'License :: OSI Approved',
            'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 3',
            'Topic :: Other/Nonlisted Topic',
            'Topic :: Scientific/Engineering',
            'Topic :: Software Development',
            'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    cmdclass = {
        'test': PyTest
    },
)
