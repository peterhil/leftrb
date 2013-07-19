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
            Search the subtree for a key. Return a value or None.
            """
            if self.key == key:
                return self.val if self.val is not None else self.key
            elif key < self.key and self.left:
                return self.left.search(key)
            elif self.key < key and self.right:
                return self.right.search(key)
            return None

        def min(self):
            """
            Smallest node in the subtree.
            """
            return self.key if self.left is None else self.left.min()

        def max(self):
            """
            Largest node in the subtree.
            """
            return self.key if self.right is None else self.right.max()

    def search(self, key):
        """
        Search the tree with a key. Return a value or None.
        """
        return self.root.search(key)

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
