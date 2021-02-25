#import simple
from simple import add, is_leap
import pytest

def test_add_one():
    assert 30 == add(10,20)
    assert 40 == add(12,18)

def test_leap():
    assert is_leap(2012)


