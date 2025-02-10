# CS2 Spring 2025 Note 09

## Puzzle

What is the value returned by evaluating the Python expression `3 * 0.1 == 0.3'?

## Unit testing

Unit testing checks individual parts of a program (typically individual
functions or methods).  It is not meant to be exhaustive.  Instead, it is meant
to be quick (so it can be run often) and to catch obvious mistakes (e.g.,
off-by-one mistakes).  For instance, unit tests would check corner cases (e.g.,
division by zero, access the first element, access the last element, etc.).

To make it even easier to do unit testing, most languages offer multiple
frameworks.  We will be using `pytest`.
