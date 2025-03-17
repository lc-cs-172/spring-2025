# Assignment #4: Defining Objects

This assignment is meant to give you practice defining objects.

## Three-body Problem

Associated with this assignment are three files:

* `vector_test.py`  A collection of unit tests for the class `Vector` that
                    should be defined in the file `vector.py` that you will need
                    to write
* `body.py`  The definition of a body subject to a two-dimensional gravitational
             field
* `sun_earth.py`  A example use of `body.py`
* `three_body.py`  A second example use of `body.py`

## Vectors

Currently, `body.py` uses ordered pairs to store position, velocity, and forces.
Let us refactor this code so that these items of information are stored as
instances of a class called `Vector` with two attributes: `x` and `y`.  This
class should be stored in a file called `vector.py`.

The class should be written in proper object-oriented style, including:

* Instance variables and methods
* One or more initializers
* Getters and setters
* `__str__`, `__repr__` and `__eq__` methods
* Any other methods required by the tests (see below)
* A docstring comment associated with each method

The specification for these classes is given in the form of one `pytest` test
file, `vector_test.py`.  You'll have to examine it to determine what methods you
need and what they're supposed to do.

Note that there is no main program to run here.  You're just defining a class
that will be used in other programs, such as `body.py`, `sun_earth.py` and
`three_body.py`.  Don't worry, it's just rocket science!

## Hints

First write enough of the class so that the test compiles.  Methods don't have
to do anything yet; leave them empty or with `return None` (or `return -1`) if
they are supposed to return something.  Once you can run the tests, work through
the tests in the order they appear in the test file, doing whatever is necessary
to pass each one.

There are no loops or recursion required to complete these classes; if you're
using those, you're working too hard.

## What To Hand In

Upload your version of `vector.py` (it's a text file, no need to convert it to
such).
