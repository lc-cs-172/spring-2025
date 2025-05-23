"""Unit tests for the Vector class."""

__author__ = 'Peter Drake and Alain Kägi'

from vector import Vector

import pytest

EPSILON = 0.0001

def test_getters_and_setters():
    v = Vector(8.0, 5.0)
    assert v.get_x() == 8.0
    assert v.get_y() == 5.0
    v.set_x(-2.0)
    v.set_y(10.0)
    assert v.get_x() == -2.0
    assert v.get_y() == 10.0

def test_zero_argument_initializer():
    assert Vector().__str__() == '<0.0, 0.0>'

def test_equal():
    assert Vector(1.0, 2.0) == Vector(1.0, 2.0)
    assert Vector(7.0, 7.0) != Vector(7.0, 3.0)

def test_add():
    a = Vector(1.0, 2.0)
    b = Vector(4.0, 6.0)
    assert (a + b).__str__() == '<5.0, 8.0>'

def test_add_immutability():
    a = Vector(1.0, 2.0)
    b = Vector(4.0, 6.0)
    a + b
    assert a.__str__() == '<1.0, 2.0>'
    assert b.__str__() == '<4.0, 6.0>'

def test_subtract():
    a = Vector(1.0, 2.0)
    b = Vector(4.0, 6.0)
    assert (a - b).__str__() == '<-3.0, -4.0>'

def test_sub_immutability():
    a = Vector(1.0, 2.0)
    b = Vector(4.0, 6.0)
    a - b
    assert a.__str__() == '<1.0, 2.0>'
    assert b.__str__() == '<4.0, 6.0>'

def test_scalar_product():
    a = Vector(1.0, 2.0)
    assert a.times(3.0).__str__() == '<3.0, 6.0>'

def test_scalar_product_immutability():
    a = Vector(1.0, 2.0)
    a.times(3.0)
    assert a.__str__() == '<1.0, 2.0>'

def test_distance():
    a = Vector(0.0, 3.0)
    b = Vector(4.0, 0.0)
    assert a.distance_to(b) == pytest.approx(5.0, rel = EPSILON)
