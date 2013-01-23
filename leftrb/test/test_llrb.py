#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import pytest
import random

from leftrb.test.test_bst import TestBST as Base
from leftrb.llrb import LeftRB


Tree = LeftRB


class TestLeftRB(Base):

    def test_delete(self):
        t = Tree()
        r = random.sample(xrange(100), 90)
        for x in r:
            t.insert(x)

        key = random.randint(0, 999)
        value = str(key)
        t.insert(key, value)
        assert value == t.search(key)
        t.delete(key)
        assert None == t.search(key)
