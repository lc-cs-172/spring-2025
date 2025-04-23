"""Unit tests for the ArrayList class."""

__author__ = 'Peter Drake and Alain Kägi'

from array_list import ArrayList

def test_is_initially_empty():
    list = ArrayList()
    assert str(list) == '[]'

def test_adds():
    list = ArrayList()
    list.add(5)
    list.add(2)
    list.add(8)
    assert str(list) == '[5, 2, 8]'

def test_clears():
    list = ArrayList()
    list.add(5)
    list.add(2)
    list.add(8)
    list.clear()
    assert str(list) == '[]'

def test_contains_finds_first_item():
    list = ArrayList()
    list.add(5)
    list.add(2)
    list.add(8)
    assert list.contains(5)

def test_contains_finds_last_item():
    list = ArrayList()
    list.add(5)
    list.add(2)
    list.add(8)
    assert list.contains(8)

def test_contains_finds_intermediate_item():
    list = ArrayList()
    list.add(5)
    list.add(2)
    list.add(8)
    assert list.contains(2)

def test_contains_does_not_find_absent_item():
    list = ArrayList()
    list.add(5)
    list.add(2)
    list.add(8)
    assert not list.contains(4)

def test_gets():
    list = ArrayList()
    list.add(5)
    list.add(2)
    list.add(8)
    assert list.get(2) == 8

def test_finds_index_of_first_item():
    list = ArrayList()
    list.add(5)
    list.add(2)
    list.add(8)
    assert list.index_of(5) == 0

def test_finds_index_of_last_item():
    list = ArrayList()
    list.add(5)
    list.add(2)
    list.add(8)
    assert list.index_of(8) == 2

def test_finds_index_of_intermediate_item():
    list = ArrayList()
    list.add(5)
    list.add(2)
    list.add(8)
    assert list.index_of(2) == 1

def test_does_not_find_index_of_absent_item():
    list = ArrayList()
    list.add(5)
    list.add(2)
    list.add(8)
    assert list.index_of(4) == -1

def test_finds_first_index_of_repeated_item():
    list = ArrayList()
    list.add(5)
    list.add(2)
    list.add(7)
    list.add(2)
    list.add(8)
    assert list.index_of(2) == 1

def test_removes_first_item():
    list = ArrayList()
    list.add(5)
    list.add(2)
    list.add(8)
    list.remove_at(0)
    assert str(list) == '[2, 8]'

def test_removes_last_item():
    list = ArrayList()
    list.add(5)
    list.add(2)
    list.add(8)
    list.remove_at(2)
    assert str(list) == '[5, 2]'

def test_removes_intermediate_item():
    list = ArrayList()
    list.add(5)
    list.add(2)
    list.add(8)
    list.remove_at(1)
    assert str(list) == '[5, 8]'

def test_sets():
    list = ArrayList()
    list.add(5)
    list.add(2)
    list.add(8)
    list.set(2, 7)
    assert str(list) == '[5, 2, 7]'

def test_finds_size():
    list = ArrayList()
    list.add(5)
    list.add(2)
    list.add(8)
    assert len(list) == 3

def test_equals_works():
    list = ArrayList()
    list.add(5)
    list.add(2)
    list.add(8)
    list2 = ArrayList()
    list2.add(5)
    list2.add(2)
    assert list != list2
    list2.add(8)
    assert list == list2

def test_equals_works_after_deletion():
    list = ArrayList()
    list.add(5)
    list.add(2)
    list.add(8)
    list2 = ArrayList()
    list2.add(5)
    list2.add(2)
    list2.add(8)
    list2.add(9)
    list2.remove_at(3)
    assert list == list2

def test_is_iterable():
    list = ArrayList()
    list.add(5)
    list.add(2)
    list.add(8)
    sum = 0
    for n in list:
        sum += n
    assert sum == 15 

def test_is_generic():
    list = ArrayList()
    list.add('eggs')
    list.add('bread')
    list.add('tea')
    assert str(list) == '[eggs, bread, tea]'

def test_repr():
    list = ArrayList()
    assert repr(list) == '[]'
    list.add(1)
    list.add(2)
    list.add(3)
    list.add(4)
    assert repr(list) == '[1, 2, 3, 4]'
