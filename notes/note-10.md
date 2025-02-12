# CS2 Spring 2025 Note 10

## Puzzle

What does the expression `[0.0] * 10` evaluate to?

## Documentation

It is a good idea to include a docstring at the beginning of each module and
each function.  It should describe what the module or function does.  By
convention this docstring appears early in the program text.

In your assignment submissions, I'd like you to include a line that identifies
who wrote the solution.  Note that this is not a standard convention in Python.

```python
"""A linear algebra module."""

__author__ = 'Jane Doe'

import math

...
```

## Functional decomposition

A long program can be greatly improved by breaking it down into multiple
functions.  This has many advantages:

* Redundant code (repeating the same statements in several places) is avoided,
  making the code shorter.
* The structure of the code is made clearer, making the code easier to read and
  write.
* Individual functions can be tested, making the code easier to debug.
* Functions can often be reused to solve other problems.

A well-designed function should do only one thing: either return a value or have
some side effect (modify a data structure in memory, draw something on the
screen, etc.).

## Module, library

A relevant [Wikipedia
article](https://en.wikipedia.org/wiki/Library_(computing)) defines a *library*
as

> a collection of read-only resources that is leveraged during software
> development to implement a computer program.

A library is also referred to as a *module*.
