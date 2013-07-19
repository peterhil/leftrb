#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import pytest
import random

from leftrb.test.test_bst import TestBST as Base
from leftrb.llrb import LeftRB


Tree = LeftRB


def fill_tree(items):
    tree = Tree()
    map(tree.insert, items)
    return tree


class TestLeftRB(Base):

    items = [5, 1, 3, 6, 2, 7]

    def test_search(self):
        t = fill_tree(self.items)
        needle = max(self.items)
        assert t.search(needle) == needle

    def test_in(self):
        t = fill_tree(self.items)
        needle = max(self.items)
        assert needle in t

    def test_len(self):
        t = fill_tree(self.items)
        assert len(t) == len(self.items)

    def test_min(self):
        t = fill_tree(self.items)
        assert t.min() == min(self.items)

    def test_max(self):
        t = fill_tree(self.items)
        assert t.max() == max(self.items)

    def test_delete(self):
        t = fill_tree(random.sample(xrange(100), 90))

        key = random.randint(0, 999)
        value = str(key)
        t.insert(key, value)
        assert value == t.search(key)
        t.delete(key)
        assert None == t.search(key)
