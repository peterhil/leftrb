#!/usr/bin/env python -u
# encoding: utf-8
#
# Copyright (c) 2013, Peter Hillerström <peter.hillerstrom@gmail.com>
# All rights reserved. This software is licensed under MIT license.

# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
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
        x = self.root
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
