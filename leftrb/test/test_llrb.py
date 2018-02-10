#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import pytest
import math
import random

from leftrb.test.test_bst import TestBST as Base
from leftrb.llrb import LeftRB


Tree = LeftRB


def fill_tree(items):
    tree = Tree()
    list(map(tree.insert, items))
    return tree


class TestLeftRB(Base):

    items = [5, 1, 3, 6]

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

    def test_height(self):
        for n in range(1, 16):
            items = random.sample(range(n), n)
            t = fill_tree(items)
            print("Items: {0}".format(items))
            assert t.height() <= int(2 * math.ceil(math.log(n, 2) + 1))

    def test_min(self):
        t = fill_tree(self.items)
        assert t.min() == min(self.items)

    def test_max(self):
        t = fill_tree(self.items)
        assert t.max() == max(self.items)

    def test_delete(self):
        t = fill_tree(random.sample(range(100), 90))

        key = random.randint(0, 999)
        value = str(key)
        t.insert(key, value)
        assert value == t.search(key)
        t.delete(key)
        assert None == t.search(key)
