#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from jazzyml.skeleton import fib

__author__ = "Vassilis S. Moustakas"
__copyright__ = "Vassilis S. Moustakas"
__license__ = "apache"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
