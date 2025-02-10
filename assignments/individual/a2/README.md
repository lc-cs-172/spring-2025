# Assignment #2: Linear Algebra Functions

This assignment is meant to give you some practice writing methods that deal
with arrays/lists.

In this assignment you will be working with two files:

* [`linear_algebra.py`](./linear_algebra.py), and
* [`linear_algebra_test.py`](./linear_algebra_test.py),

Copy these two files in the same directory.  Better yet, clone this repository
(or update your existing clone).  Start Visual Studio Code at that directory (or
`spring-2025`, if you are using your clone).  When you open either of the above
files in the editor, a beaker icon should appear on the left.  Click on that
icon, click on `Configure Python Test`, select the `pytest framework`, select
the `Root directory`, wait a few seconds, then your directory name (or
`spring-2025`, if you are using a clone) should appear on the `TESTING` pane
towards the left.  When you hover over `linear_algebra_test.py`, various icons
will appear to its right.  One of these icons is the play button.  If you click
on it, all tests defined in `linear_algebra_test.py` will run.

You should now be able to run the tests.  12 should fail and 9 should pass
(because those 9 are just verifying that your functions don't do certain
things).

Work your way through `linear_algebra.py`, completing each function so that it
passes the associated tests.

## Hints

Don't modify `linear_algebra_test.py`.

Each function has a `return` statement put there just so that the code compiles.
Replace that statement with your own code (which will include some kind of
`return` statement).

Looking at the tests might give you a hint as to what the code is supposed to
do.

You can assume that input parameters are "properly" shaped.  For instance, you
do not have to check that the two vectors being added have the same length,
assume that they do.

## What To Hand In

Upload your version of `linear_algebra.py`.
