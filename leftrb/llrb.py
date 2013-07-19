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
Leftrb/LLRB is a Left-Leaning Red-Black (LLRB) implementation
of 2–3 balanced binary search trees in Python.

This is a straightforward port of the code in the article

“Left-leaning Red-Black Trees”
http://www.cs.princeton.edu/~rs/talks/LLRB/LLRB.pdf
by Robert Sedgewick of Princeton University.
"""

import sys
from bst import BinarySearchTree


__all__ = ['LeftRB']

RED = True
BLACK = False


def is_red(h):
    """
    Is the node (h) red?
    """
    return isinstance(h, LeftRB.Node) and h.color == RED


def is_black(h):
    """
    Is the node (h) black?
    """
    return not is_red(h)


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
            self.height = 1

        def size(self):
            """
            Number of nodes in the subtree below node.
            """
            # TODO Cache into self.N
            return 1 + sum(map(lambda child: child.size(), filter(None, [self.left, self.right])))

        def __repr__(self):
            return "<{0} at {1}, key={2}, value={3}, color={4}, N={5}, height={6}>".format(
                self.__class__.__name__,
                id(self),
                self.key,
                self.val,
                'red' if is_red(self) else 'black',
                self.N,
                self.height
            )

    def is_empty(self):
        """
        Is the tree empty?
        """
        return self.root is None

    def __contains__(self, key):
        """
        Does the tree contain key?
        """
        return self.search(key) is not None

    @classmethod
    def _contains(cls, x, key):
        return cls._search(x, key) is not None

    def __len__(self):
        """
        Number of nodes in the tree.
        """
        return 0 if not self.root else self.root.size()

    def height(self):
        """
        Height of the tree.
        """
        return self._height(self.root)

    @staticmethod
    def _height(x):
        """
        The height of the tree below node (x).
        """
        return 0 if x is None else x.height

    def min(self):
        """
        Smallest node in the tree.
        """
        return None if self.root is None else self.root.min()

    def max(self):
        """
        Largest node in the tree.
        """
        return None if self.root is None else self.root.max()

    def insert(self, key, value=None):
        """
        Insert a key with optional value into the tree.
        """
        self.root = self._insert(self.root, key, value)
        self.root.color = BLACK

    @classmethod
    def _insert(cls, h, key, value=None):
        """
        Recursively insert a node with key and optional value
        into the tree below node (h).
        """
        if h is None:
            return cls.Node(key, value)

        # Move this to the end to get 2-3 trees
        if is_red(h.left) and is_red(h.right):
            cls._flip_colors(h)

        h = super(cls, cls)._insert(h, key, value)

        if is_red(h.right) and is_black(h.left):
            h = cls._rotate_left(h)
        if is_red(h.left) and h.left and is_red(h.left.left):
            h = cls._rotate_right(h)

        return cls._setHeight(h)

    def delete(self, key):
        """
        Delete a node with the given key from the tree.
        """
        if key not in self:
            sys.stderr.write("Tree does not contain key '{0}'.".format(key))
            return False

        if is_black(self.root.left) and is_black(self.root.right):
            self.root.color = RED

        self.root = self._delete(self.root, key)

        if not self.is_empty():
            self.root.color = BLACK

    def _delete(self, h, key):
        """
        Delete a node with the given key (recursively) from the tree below node (h).
        """
        assert self._contains(h, key)

        if key < h.key:
            if is_black(h.left) and h.left and is_black(h.left.left):
                h = self._move_red_left(h)
            h.left = self._delete(h.left, key)
        else:
            if is_red(h.left):
                h = self._rotate_right(h)

            if key == h.key and h.right is None:
                return None

            if is_black(h.right) and h.right and is_black(h.right.left):
                h = self._move_red_right(h)

            if key == h.key:
                h.value = self._search(h.right, self._min(h.right))
                h.key = self._min(h.right)
                h.right = self._delete_min(h.right)
            else:
                h.right = self._delete(h.right, key)

        return self._fix_up(h)

    def delete_min(self):
        """
        Delete the smallest node while maintaining balance.
        """
        self.root = self._delete_min(self.root)
        self.root.color = BLACK

    def _delete_min(cls, h):
        """
        Delete the smallest node on the (left) subtree below node(h)
        while maintaining balance.
        """
        if h.left is None:
            return None

        if is_black(h.left) and h.left and is_black(h.left.left):
            h = cls._move_red_left(h)

        h.left = cls._delete_min(h.left)

        return cls._fix_up(h)

    def delete_max(self):
        """
        Delete the largest node while maintaining balance.
        """
        self.root = self._delete_max(self.root)
        self.root.color = BLACK

    def _delete_max(cls, h):
        """
        Delete the largest node on the (right) subtree below node(h)
        while maintaining balance.
        """
        if is_red(h.left):
            h = rotateRight(h)

        if h.right is None:
            return None

        if is_black(h.right) and h.right and is_black(h.right.left):
            h = cls._move_red_right(h)

        h.right = cls._delete_max(h.right)

        return fixUp(h)

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

    @classmethod
    def _move_red_left(cls, h):
        """
        Assuming that h is red and both h.left and h.left.left
        are black, make h.left or one of its children red.
        """
        cls._flip_colors(h)
        if h.right and is_red(h.right.left):
            h.right = cls._rotate_right(h.right)
            h = cls._rotate_left(h)
            cls._flip_colors(h)
        return h

    @classmethod
    def _move_red_right(cls, h):
        """
        Assuming that h is red and both h.right and h.right.left
        are black, make h.right or one of its children red.
        """
        cls._flip_colors(h)
        if h.left and is_red(h.left.left):
            h = cls._rotate_right(h)
            cls._flip_colors(h)
        return h

    @classmethod
    def _fix_up(cls, h):
        """
        Fix the Left-leaning Red-black tree properties
        with upto two rotations and a possible color flip.
        """
        if is_red(h.right):
            h = cls._rotate_left(h)

        if is_red(h.left) and h.left and is_red(h.left.left):
            h = cls._rotate_right(h)

        if is_red(h.left) and is_red(h.right):
            cls._flip_colors(h)

        return cls._setHeight(h)

    @classmethod
    def _setHeight(cls, h):
        """
        Update size and height of node (h).
        """
        h.height = max(cls._height(h.left), cls._height(h.right)) + 1
        return h


del BinarySearchTree
