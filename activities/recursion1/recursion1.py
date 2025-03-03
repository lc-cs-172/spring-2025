"""Recursion exercises adapted from the CodingBat code practice web
pages https://codingbat.com/java/Recursion-1 developed by Nick
Parlante.
"""

def factorial(n : int) -> int:

    """Given `n` of 1 or more, return the factorial of `n`, which is "n *
    (n-1) * (n-2) ... 1".  Compute the result recursively (without
    loops).

    factorial(1) → 1
    factorial(2) → 2
    factorial(3) → 6
    """

    return 1

def bunny_ears(bunnies : int) -> int:

    """We have a number of bunnies and each bunny has two big floppy
    ears.  We want to compute the total number of ears across all the
    bunnies recursively (without loops or multiplication).

    bunny_ears(0) → 0
    bunny_ears(1) → 2
    bunny_ears(2) → 4
    """

    return 1

def fibonacci(n : int) -> int:

    """The fibonacci sequence is a famous bit of mathematics, and it
    happens to have a recursive definition.  The first two values in
    the sequence are 0 and 1 (essentially 2 base cases).  Each
    subsequent value is the sum of the previous two values, so the
    whole sequence is: 0, 1, 1, 2, 3, 5, 8, 13, 21 and so on.  Define a
    recursive `fibonacci(n)` method that returns the `n`th fibonacci
    number, with `n` = 0 representing the start of the sequence.

    fibonacci(0) → 0
    fibonacci(1) → 1
    fibonacci(2) → 1
    """

    return 1

def bunny_ears2(bunnies : int) -> int:

    """We have bunnies standing in a line, numbered 1, 2, ...  The odd
    bunnies (1, 3, ...) have the normal 2 ears.  The even bunnies (2,
    4, ...) we'll say have 3 ears, because they each have a raised
    foot.  Recursively return the number of "ears" in the bunny line 1,
    2, ... n (without loops or multiplication).

    bunny_ears2(0) → 0
    bunny_ears2(1) → 2
    bunny_ears2(2) → 5
    """

    return 1

def triangle(rows : int) -> int:

    """We have triangle made of blocks.  The topmost row has 1 block, the
    next row down has 2 blocks, the next row has 3 blocks, and so
    on.  Compute recursively (no loops or multiplication) the total
    number of blocks in such a triangle with the given number of rows.

    triangle(0) → 0
    triangle(1) → 1
    triangle(2) → 3
    """

    return 1

def sum_digits(n : int) -> int:

    """Given a non-negative int `n`, return the sum of its digits
    recursively (no loops).  Note that mod (`%`) by 10 yields the
    rightmost digit (`126 % 10` is `6`), while floor division (`//`) by 10
    removes the rightmost digit (`126 // 10` is `12`).

    sum_digits(126) → 9
    sum_digits(49) → 13
    sum_digits(12) → 3
    """

    return 1

def count_7(n : int) -> int:

    """Given a non-negative int `n`, return the count of the occurrences of
    `7` as a digit, so for example `717` yields `2`.  (no loops).  Note that
    mod (`%`) by 10 yields the rightmost digit (`126 % 10` is `6`), while
    floor division (`//`) by 10 removes the rightmost digit (`126 // 10`
    is `12`).

    count_7(717) → 2
    count_7(7) → 1
    count_7(123) → 0
    """

    return 1

def power_n(base : int, n : int) -> int:

    """Given `base` and `n` that are both `1` or more, compute recursively (no
    loops) the value of base to the `n` power, so `power_n(3, 2)` is `9` (3
    squared).  Do not use the power operator (`**`), only multiplications.

    power_n(3, 1) → 3
    power_n(3, 2) → 9
    power_n(3, 3) → 27
    """

    return 1

def change_xy(s : str) -> str:

    """Given a string, compute recursively (no loops) a new string where
    all the lowercase 'x' chars have been changed to 'y' chars.

    change_xy('codex') → 'codey'
    change_xy('xxhixx') → 'yyhiyy'
    change_xy('xhixhix') → 'yhiyhiy'
    """

    return ''

def no_x(s : str) -> str:

    """Given a string, compute recursively a new string where all the 'x'
    chars have been removed.

    no_x('xaxb') → 'ab'
    no_x('abc') → 'abc'
    no_x('xx') → ''
    """

    return ''

def array_6(nums : int) -> bool:

    """Given an array of `int`s, compute recursively if the array contains a
    `6`.

    array_6([1, 6, 4]) → True
    array_6([1, 4]) → False
    array_6([6]) → True
    """

    return False

def array_220(nums : int) -> bool:

    """Given an array of `int`s, compute recursively if the array contains
    somewhere a value followed in the array by that value times `10`.

    array_220([1, 2, 20]) → True
    array_220([3, 30]) → True
    array_220([3]) → False
    """

    return False

def all_star(s : str) -> str:

    """Given a string, compute recursively a new string where all the
    adjacent chars are now separated by a '*'.

    allStar('hello') → 'h*e*l*l*o'
    allStar('abc') → 'a*b*c'
    allStar('ab') → 'a*b'
    """

    return ''

def pair_star(s : str) -> str:

    """Given a string, compute recursively a new string where identical
    chars that are adjacent in the original string are separated from
    each other by a '*'.

    pair_star('hello') → 'hel*lo'
    pair_star('xxyy') → 'x*xy*y'
    pair_star('aaaa') → 'a*a*a*a'
    """

    return ''
