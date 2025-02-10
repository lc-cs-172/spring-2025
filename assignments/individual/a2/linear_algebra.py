"""A linear algebra module.

This is a collection of functions dealing with vectors and matrices.
"""

__author__ = 'Put your name here'

import math

def vmagnitude(v : list[float]) -> float:
    """Returns the magnitude of the vector v (which may be of any
    length).

    This is found by adding up the squares of all of the elements of v
    and taking the square root of the total.
    """

    return -1.0

def vsum(v : list[float], w : list[float]) -> list[float]:
    """Returns the sum of vectors v and w.

    This is a vector of the same length, each of whose elements is the
    sum of the corresponding elements in v and w.
    """

    return None

def vdifference(v : list[float], w : list[float]) -> list[float]:
    """Returns the difference between vectors v and w.

    This is a vector of the same length, each of whose elements is the
    difference between the corresponding elements in v and w.
    """

    return None

def velementwise_product(v : list[float], w : list[float]) -> list[float]:
    """Returns the element-wise between vectors v and w.

    This is a vector of the same length, each of whose elements is the
    product of the corresponding elements in v and w.
    """

    return None

def vdot_product(v : list[float], w : list[float]) -> float:
    """Returns the dot product of vectors v and w.

    This is the sum of the products of the corresponding elements.
    """

    return -1.0

def mdimensions(m : list[list[float]]) -> list[int]:
    """Returns, as an array of two elements, the dimensions of matrix m."""

    return None

def msum(m : list[list[float]], n : list[list[float]]) -> list[list[float]]:
    """Returns the element-wise sum of matrices m and n."""

    return None

def melementwise_product(m : list[list[float]], n : list[list[float]]) -> list[list[float]]:
    """Returns the element-wise product of matrices m and n."""

    return None

def mtranspose(m : list[list[float]]) -> list[list[float]]:
    """Returns the transpose of m, that is, a matrix where element i, j
    is element j, i from m.
    """

    return None

def mproduct(m : list[list[float]], n : list[list[float]]) -> list[list[float]]:
    """Returns the matrix product of m and n.

    (Search the web for a definition.)
    """

    return None
