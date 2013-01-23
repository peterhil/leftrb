#!/usr/bin/env python -u
# encoding: utf-8
#
# Copyright (c) 2013, Peter Hillerström <peter.hillerstrom@gmail.com>
# All rights reserved. This software is licensed under MIT license.

# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
"""
Leftrb/LLRB is a Left-Leaning Red-Black (LLRB) implementation
of 2–3 balanced binary search trees in Python.

This is a straightforward port of the code in the article

“Left-leaning Red-Black Trees”
http://www.cs.princeton.edu/~rs/talks/LLRB/LLRB.pdf
by Robert Sedgewick of Princeton University.
"""

from bst import BinarySearchTree


__all__ = ['LeftRB']

RED = True
BLACK = False


def is_red(h):
    """
    Is the node (h) red?
    """
    return isinstance(h, LeftRB.Node) and h.color == RED


class LeftRB(BinarySearchTree, object):
    """
    Left-Leaning Red-Black (LLRB) is an implementation of
    2–3 balanced binary search tree.

    Ported to Python from code and description on
    paper “Left-leaning Red-Black Trees” by Robert Sedgewick:
    http://www.cs.princeton.edu/~rs/talks/LLRB/LLRB.pdf
    """
    root = None

    class Node(BinarySearchTree.Node, object):
        """
        LeftRB tree node.
        """
        def __init__(self, key, val=None):
            super(self.__class__, self).__init__(key, val)
            self.color = RED  # new nodes are always red

    def insert(self, key, value=None):
        """
        Insert a key with optional value into tree.
        """
        self.root = self._insert(self.root, key, value)
        self.root.color = BLACK

    @classmethod
    def _insert(cls, h, key, value=None):
        if h is None:
            return cls.Node(key, value)

        # Move this to the end to get 2-3 trees
        if is_red(h.left) and is_red(h.right):
            cls._flip_colors(h)

        h = super(cls, cls)._insert(h, key, value)

        if is_red(h.right) and not is_red(h.left):
            h = cls._rotate_left(h)
        if is_red(h.left) and is_red(h.left.left):
            h = cls._rotate_right(h)

        return h

    @staticmethod
    def _flip_colors(h):
        """
        Flip colors to split a 4-node
        """
        h.color = not h.color
        h.left.color = not h.left.color
        h.right.color = not h.right.color

    @staticmethod
    def _rotate_left(h):
        """
        Left rotate (right link of h)

               V         |          V <--left or right, red or black
               |         |          |
        out<--(x)   <<< LEFT       (h) <--in
             // \        |         / \\  <--red  
           (h)   3       |        1   (x)
           / \           |            / \
          1   2          |           2   3
        """
        x       = h.right
        h.right = x.left
        x.left  = h
        x.color = h.color
        h.color = RED
        return x

    @staticmethod
    def _rotate_right(h):
        """
        Right rotate (left link of h)

               V         |          V <--left or right, red or black
               |         |          |
        in--> (h)     RIGHT >>>    (x)-->out
             // \        |         / \\  <--red  
           (x)   3       |        1   (h)
           / \           |            / \
          1   2          |           2   3
        """
        x       = h.left
        h.left  = x.right
        x.right = h
        x.color = h.color
        h.color = RED
        return x


del BinarySearchTree
