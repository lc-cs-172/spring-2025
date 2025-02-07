# CS2 Spring 2025 Note 08

## Puzzle

A for each loop can always be transformed into a while loop.  For example,
consider the following for each loop:

```python
for i in range(10):
    statement1
    statement2
    ...
```

It can be rewritten as a while loop as follows:

```python
i = 0
while i < 10:
    statement1
    statement2
    ...
    i += 1
```

It appears we can simply copy, as is, the body of the for each loop into the
while loop and add the update to the index variable to complete the
transformation.  Can you think of any cases where this simple transformation
will *not* work?

## Lists

Lists are a fundamental collection supported in Python.  Python lists combine
some characteristics of arrays (e.g, indexing with square brackets) with
characteristics of lists found in other languages (e.g., the append operation).

### Examples

```python
v1 = []                  # initialization: an empty list
v2 = [1, 2, 3]           # initialization: a list of whole numbers
v3 = [1., 2., 3.]        # initialization: a list of floats
v4 = ['a', 'ab', 'abc']  # initialization: a list of strings
v4[2]                    # indexing: access the third element (zero-based index)
v4[-2]                   # indexing: access the second element from the end
v4[2] = 'xyz'            # indexing: replace the content of the third element
len(v4)                  # length: number of elements in the list
v4.append('abcd')        # method: add an element at the end
v4.pop()                 # method: remove the last element

# list of lists
m1 = [ ['a', 'b', 'c'], ['x', 'y', 'z'] ]

# can be used to hold matrices
m2 = [
        [ 1.0,  2.0,  3.0],
        [ 4.0,  5.0,  6.0],
        [ 7.0,  8.0,  9.0],
        [10.0, 11.0, 12.0]
    ]

# indexing
m2[1][0]                 # similar to C, second row, first column (i.e., 4.0)
```

## Slices

A slice is a copy of a contiguous sequence of elements from a source list.  The
syntax is `a[i:j]` where `a` is the source list.  This expression returns a new
list with elements `a[i]`, `a[i + 1]`, ..., `a[j - 1]`.  If you do not specify
`i`, it defaults to `0`; if you do not specify `j`, it defaults to `len(a)`.

### Examples

```python
v5 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
v5[2:6]                   # [2, 3, 4, 5]
v5[7:]                    # [7, 8, 9]
v5[:3]                    # [0, 1, 2]
v5[2:-2]                  # [2, 3, 4, 5, 6, 7]
v5[:]                     # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```
