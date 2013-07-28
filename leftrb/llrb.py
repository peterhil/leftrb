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
from leftrb.bst import BinarySearchTree


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

        def insert(self, key, value=None):
            """
            Recursively insert a node with key and optional value into the tree below.
            """
            # Move this to the end to get 2-3 trees
            if is_red(self.left) and is_red(self.right):
                self._flip_colors()

            self = super(LeftRB.Node, self).insert(key, value)

            if is_red(self.right) and is_black(self.left):
                self = self._rotate_left()
            if is_red(self.left) and self.left and is_red(self.left.left):
                self = self._rotate_right()

            return self._setHeight()

        def size(self):
            """
            Number of nodes in the subtree below node.
            """
            # TODO Cache into self.N
            return 1 + sum(map(lambda child: child.size(), filter(None, [self.left, self.right])))

        def __repr__(self):
            return "<{0} at {1}, key={2}, value={3}, left={6}, right={7}, color={4}, height={5}>".format(
                self.__class__.__name__,
                id(self),
                self.key,
                self.val,
                'red' if is_red(self) else 'black',
                self.height,
                self.left and self.left.key or None,
                self.right and self.right.key or None,
            )

        def _fix_up(self):
            """
            Fix the Left-leaning Red-black tree properties
            with upto two rotations and a possible color flip.
            """
            if is_red(self.right):
                self = self._rotate_left()

            if is_red(self.left) and self.left and is_red(self.left.left):
                self = self._rotate_right()

            if is_red(self.left) and is_red(self.right):
                self._flip_colors()

            return self._setHeight()

        def _flip_colors(self):
            """
            Flip colors to split a 4-node
            """
            self.color = not self.color
            self.left.color = not self.left.color
            self.right.color = not self.right.color

        def _move_red_left(self):
            """
            Assuming that self is red and both self.left and self.left.left
            are black, make self.left or one of its children red.
            """
            self._flip_colors()
            if self.right and is_red(self.right.left):
                self.right = self.right._rotate_right()
                self = self._rotate_left()
                self._flip_colors()
            return self

        def _move_red_right(self):
            """
            Assuming that self is red and both self.right and self.right.left
            are black, make self.right or one of its children red.
            """
            self._flip_colors()
            if self.left and is_red(self.left.left):
                self = self._rotate_right()
                self._flip_colors()
            return self

        def _rotate_left(self):
            """
            Left rotate (right link of self)

                   V         |          V <--left or right, red or black
                   |         |          |
            out<--(x)   <<< LEFT       (s) <--in
                 // \        |         / \\  <--red
               (s)   3       |        1   (x)
               / \           |            / \
              1   2          |           2   3
            """
            x       = self.right
            self.right = x.left
            x.left  = self
            x.color = self.color
            self.color = RED
            return x

        def _rotate_right(self):
            """
            Right rotate (left link of self)

                   V         |          V <--left or right, red or black
                   |         |          |
            in--> (s)     RIGHT >>>    (x)-->out
                 // \        |         / \\  <--red
               (x)   3       |        1   (s)
               / \           |            / \
              1   2          |           2   3
            """
            x       = self.left
            self.left  = x.right
            x.right = self
            x.color = self.color
            self.color = RED
            return x

        def _setHeight(self):
            """
            Update height.
            """
            self.height = 1 + max(self.left and self.left.height or 0,
                                      self.right and self.right.height or 0)
            return self


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

    def __len__(self):
        """
        Number of nodes in the tree.
        """
        return 0 if self.root is None else self.root.size()

    def height(self):
        """
        Height of the tree.
        """
        return 0 if self.root is None else self.root.height

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
        super(LeftRB, self).insert(key, value)
        self.root.color = BLACK

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
        assert h.search(key) is not None

        if key < h.key:
            if is_black(h.left) and h.left and is_black(h.left.left):
                h = h._move_red_left()
            h.left = self._delete(h.left, key)
        else:
            if is_red(h.left):
                h = h._rotate_right()

            if key == h.key and h.right is None:
                return None

            if is_black(h.right) and h.right and is_black(h.right.left):
                h = h._move_red_right()

            if key == h.key:
                h.value = h.right.search(h.right.min())
                h.key = h.right.min()
                h.right = self._delete_min(h.right)
            else:
                h.right = self._delete(h.right, key)

        return h._fix_up()

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
            h = h._move_red_left()

        h.left = cls._delete_min(h.left)

        return h._fix_up()

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
            h = h._move_red_right()

        h.right = cls._delete_max(h.right)

        return fixUp(h)


del BinarySearchTree
