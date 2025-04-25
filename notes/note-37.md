# CS2 Spring 2025 Note 37

## Running time

We are given a function that solves a particular problem.  Given a particular
input, we're interested in knowing how long it will take for this function to
complete.

### Problem size

One issue to consider is related to the input.  Often we will boil down the
input characteristic to a single number, usually denoted *n*, related to the
size of said input.

In most cases it will be clear from context what *n* means: the length of the
array being sorted, the number of items stored in the collection, etc.
Helpfully, many functions take only one argument, but there are exceptions.

### Big *O* notation

Given the running time for two functions, which function is faster?  This
question appears to open a can of mathematical worms, but there is a convenient
shortcut: asymptotic notation.  We focus on what happens as *n* becomes large.

Rigorously, we say

*f(x) ∈ O(g(x))*

if there is *M* and *x0* such that

|*f(x)*| ≤ *M* |*g(x)*| for all *x ≥ x0*

Common growth functions:

Order        | Nickname
-|-
*O(2ⁿ)*      | exponential
*O(n³)*      | cubic
*O(n²)*      | quadratic
*O(n log n)* | linearithmic
*O(n)*       | linear
*O(log n)*   | logarithmic
*O(1)*       | constant

## Activities

Answer true of false:

* *2n ∈ O(n)*
* *n² ∈ O(n)*
* *n² ∈ O(n log² n)*
* *n log n ∈ O(n²)*

What is the order of growth of the following functions:

* *16n² + 3n + 16*
* *n² + 1000000n*
* *3 log n*
* *14 n log n/2*
* *14 n + log n/2*

## Fun with references

Consider the following declaration:

```python
class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next
```

and the following instantiations:

```python
n3 = Node('or', None)
n2 = Node('be', n3)
n1 = Node('to', n2)
```

Can you draw a picture of what has happened with the last three lines of code?
