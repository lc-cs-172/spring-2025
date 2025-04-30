"""Unit tests for linear search."""

__author__ = 'Alain Kägi'

import activities.search.binary as binary

def test_empty():
    assert binary.search([], 0) == -1

def test_singleton():
    a = [0]
    assert binary.search(a, 0) == 0
    assert binary.search(a, 1) == -1

def test_five():
    a = [0, 1, 2, 3, 4, 5]
    assert binary.search(a, 0) == 0
    assert binary.search(a, 1) == 1
    assert binary.search(a, 2) == 2
    assert binary.search(a, 3) == 3
    assert binary.search(a, 4) == 4
    assert binary.search(a, 5) == 5
    assert binary.search(a, 6) == -1

def test_strings():
    a = ['ant', 'ape', 'bee', 'cat', 'dog', 'eel', 'elkcow', 'gnu', 'owl', 'pig', 'rat', 'yak']
    assert binary.search(a, 'bee') == 2
    assert binary.search(a, 'zebra') == -1
