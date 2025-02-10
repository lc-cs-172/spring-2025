"""Unit tests for the Linear Algebra Functions assignment."""

__author__ = 'Peter Drake and Alain Kägi'

import linear_algebra

import pytest

EPSILON = 0.0001

def create_matrix(num_row : int, num_col : int) -> list[list[float]]:
    """Create a matrix of the given shape."""
    m = []
    for i in range(0, num_row):
        r = []
        for j in range(0, num_col):
            r += [None]
        m += [r]
    return m

def test_vector_magnitude():
    v = [1.0, 2.0, 3.0]
    assert linear_algebra.vmagnitude(v) == pytest.approx(3.7416, rel = EPSILON)

def test_vector_magnitude_does_not_modify_input():
    v = [1.0, 2.0, 3.0, 4.0]
    w = [1.0, 2.0, 3.0, 4.0]  # Second copy so that we can verify that v doesn't change
    linear_algebra.vmagnitude(v)
    assert v == w

def test_vector_sum():
    v = [1.0, 2.0, 3.0]
    w = [4.0, 5.0, 6.0]
    expected = [5.0, 7.0, 9.0]
    assert linear_algebra.vsum(v, w) == pytest.approx(expected, rel = EPSILON)

def test_vector_sum_does_not_modify_inputs():
    v = [1.0, 2.0, 3.0, 4.0]
    w = [1.0, 2.0, 3.0, 4.0]
    linear_algebra.vsum(v, v)
    assert v == w

def test_vector_difference_returns_correct_answer():
    v = [1.0, 2.0, 3.0]
    w = [4.0, 1.0, 0.0]
    expected = [-3.0, 1.0, 3.0]
    assert linear_algebra.vdifference(v, w) == pytest.approx(expected, rel = EPSILON)

def test_vector_difference_does_not_modify_inputs():
    v = [1.0, 2.0, 3.0, 4.0]
    w = [1.0, 2.0, 3.0, 4.0]
    linear_algebra.vdifference(v, v)
    assert v == w

def test_vector_elementwise_product_returns_correct_answer():
    v = [1.0, 2.0, 3.0]
    w = [4.0, 1.0, 0.0]
    expected = [4.0, 2.0, 0.0]
    assert linear_algebra.velementwise_product(v, w) == pytest.approx(expected, rel = EPSILON)

def test_vector_elementwise_product_does_not_modify_inputs():
    v = [1.0, 2.0, 3.0, 4.0]
    w = [1.0, 2.0, 3.0, 4.0]
    linear_algebra.velementwise_product(v, w)
    assert v == w

def test_dot_product_returns_correct_answer():
    v = [1.0, 2.0, 3.0]
    w = [4.0, 1.0, 0.0]
    assert linear_algebra.vdot_product(v, w) == pytest.approx(6.0 , rel = EPSILON)

def test_dot_product_does_not_modify_inputs():
    v = [1.0, 2.0, 3.0, 4.0]
    w = [1.0, 2.0, 3.0, 4.0]
    p = [1.0, 2.0, 3.0, 4.0]
    q = [5.0, 5.0, 5.0, 5.0]
    linear_algebra.vdot_product(v, v)
    assert v == w

def test_dimensions_works_for_small_square_matrix():
    m = create_matrix(3, 3)
    expected = [3, 3]
    assert linear_algebra.mdimensions(m) == expected

def test_dimensions_works_for_large_rectangular_matrix():
    m = create_matrix(20, 100)
    expected = [20, 100]
    assert linear_algebra.mdimensions(m) == expected

def test_matrix_sum_returns_correct_answer():
    m = [[1.0, 2.0],
         [3.0, 4.0]]
    n = [[5.0, 6.0],
         [7.0, 8.0]]
    expected = [[ 6.0,  8.0],
                [10.0, 12.0]]
    result = linear_algebra.msum(m, n)
    assert len(result) == len(expected)
    for row in range (len(expected)):
        assert result[row] == pytest.approx(expected[row], rel = EPSILON)

def test_matrix_sum_does_not_modify_inputs():
    m = [[1.0, 2.0],
         [3.0, 4.0]]
    n = [[1.0, 2.0],
         [3.0, 4.0]]
    linear_algebra.msum(m, m)
    assert m == n

def test_matrix_elementwise_product_returns_correct_answer():
    m = [[1.0, 2.0],
         [3.0, 4.0]]
    n = [[5.0, 6.0],
         [7.0, 8.0]]
    expected = [[ 5.0, 12.0],
                [21.0, 32.0]]
    result = linear_algebra.melementwise_product(m, n)
    assert len(result) == len(expected)
    for row in range (len(expected)):
        assert result[row] == pytest.approx(expected[row], rel = EPSILON)

def test_matrix_elementwise_product_does_not_modify_inputs():
    m = [[1.0, 2.0],
         [3.0, 4.0]]
    n = [[1.0, 2.0],
         [3.0, 4.0]]
    linear_algebra.melementwise_product(m, m)
    assert m == n

def test_transpose_returns_correct_answer():
    m = [[1.0, 2.0, 3.0],
         [4.0, 5.0, 6.0]]
    expected = [[1.0, 4.0],
                [2.0, 5.0],
                [3.0, 6.0]]
    result = linear_algebra.mtranspose(m)
    assert len(result) == len(expected)
    for row in range(len(expected)):
        assert result[row] == expected[row]

def test_transpose_does_not_modify_inputs():
    m = [[1.0, 2.0, 3.0],
         [4.0, 5.0, 6.0]]
    n = [[1.0, 2.0, 3.0],
         [4.0, 5.0, 6.0]]
    linear_algebra.mtranspose(m)
    assert m == n

def test_matrix_product_works_for_square_matrices():
    m = [[1.0, 2.0],
         [3.0, 4.0]]
    n = [[5.0, 6.0],
         [7.0, 8.0]]
    expected = [[19.0, 22.0],
                [43.0, 50.0]]
    result = linear_algebra.mproduct(m, n)
    assert len(result) == len(expected)
    for row in range(len(expected)):
        assert result[row] == pytest.approx(expected[row], rel = EPSILON)

def test_matrix_product_works_for_rectangular_matrices():
    m = [[1.0, 2.0, 3.0],
         [4.0, 5.0, 6.0]]
    n = [[1.0,  2.0,  3.0,  4.0],
         [5.0,  6.0,  7.0,  8.0],
         [9.0, 10.0, 11.0, 12.0]]
    expected = [[38.0, 44.0,  50.0,  56.0],
                [83.0, 98.0, 113.0, 128.0]]
    result = linear_algebra.mproduct(m, n)
    assert len(result) == len(expected)
    for row in range(len(expected)):
        assert result[row] == pytest.approx(expected[row], rel = EPSILON)

def test_matrix_product_does_not_modify_inputs():
    m = [[1.0, 2.0],
         [3.0, 4.0]]
    n = [[1.0, 2.0],
         [3.0, 4.0]]
    linear_algebra.mproduct(m, m)
    assert m == n
