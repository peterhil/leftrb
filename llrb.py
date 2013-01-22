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

__all__ = ['LeftRB']

RED = True
BLACK = False


def rotate_left(h):
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


def rotate_right(h):
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


def flip_colors(h):
    """
    Flip colors to split a 4-node
    """
    h.color = not h.color
    h.left.color = not h.left.color
    h.right.color = not h.right.color


def is_red(h):
    """
    Is the node (h) red?
    """
    return h is not None and h.color == RED


class LeftRB(object):
    """
    Left-Leaning Red-Black (LLRB) is an implementation of
    2–3 balanced binary search tree.

    Ported to Python from code and description on
    paper “Left-leaning Red-Black Trees” by Robert Sedgewick:
    http://www.cs.princeton.edu/~rs/talks/LLRB/LLRB.pdf
    """
    root = None

    class Node(object):
        """
        LLRB tree node.
        """
        left = right = None

        def __init__(self, key, val=None):
            self.key = key
            self.val = val
            self.color = RED  # new nodes are always red

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
        self.root.color = BLACK

    @staticmethod
    def _insert(h, key, value=None):
        """
        Private insert function for recursion.
        """
        if h is None:
            return LeftRB.Node(key, value)

        # Move this to the end to get 2-3 trees
        if is_red(h.left) and is_red(h.right):
            flip_colors(h)

        if h.key == key:
            h.val = value
        elif key < h.key:
            h.left = LeftRB._insert(h.left, key, value);
        else:
            h.right = LeftRB._insert(h.right, key, value);

        if is_red(h.right) and not is_red(h.left):
            h = rotate_left(h)
        if is_red(h.left) and is_red(h.left.left):
            h = rotate_right(h)

        return h
