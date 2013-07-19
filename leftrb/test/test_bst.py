#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import pytest
import random

from leftrb.bst import BinarySearchTree


Tree = BinarySearchTree


class TestBST(object):

    def test_insert_and_search(self):
        t = Tree()
        r = random.sample(range(1000), 900)
        for x in r:
            t.insert(x)
        res = [t.search(x) for x in r]
        assert r == res
