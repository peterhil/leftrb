#!/usr/bin/env python -u
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
"""
Binary search tree.
"""

class BinarySearchTree(object):
    """
    Basic unbalanced (inefficient) binary search tree.
    For extending into different balanced binary trees.
    """
    root = None

    class Node(object):
        """
        BST tree node.
        """
        left = right = None

        def __init__(self, key, val=None):
            self.key = key
            self.val = val

    def search(self, key):
        """
        Search the tree with a key. Return a value or None.
        """
        return self._search(self.root, key)

    @staticmethod
    def _search(x, key):
        """
        Search the subtree below node (x) with a key. Return a value or None.
        """
        while x is not None:
            if x.key == key:
                return x.val if x.val is not None else x.key
            elif key < x.key:
                x = x.left
            elif x.key < key:
                x = x.right
        return None

    def insert(self, key, value=None):
        """
        Insert a key with optional value into tree.
        """
        self.root = self._insert(self.root, key, value)

    @classmethod
    def _insert(cls, h, key, value=None):
        """
        Insert a node (h) node recursively.
        """
        if h is None:
            return cls.Node(key, value)

        if h.key == key:
            h.val = value
        elif key < h.key:
            h.left = cls._insert(h.left, key, value)
        else:
            h.right = cls._insert(h.right, key, value)

        return h
