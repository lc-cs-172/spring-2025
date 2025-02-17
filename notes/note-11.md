# CS2 Spring 2025 Note 11

## Puzzle

What does the expression `[[0.0] * 4] * 3` evaluate to?  Say you assign the
result of that expression to a variable `m` (`m = [[0.0] * 4] * 3`).  Then
execute the assignment `m[0][0] = 3.1415`.  How do you expect the content of `m`
to be affected?  Can you explain the behavior?

## References

In Python *everything* is a reference.

According to
[wikipedia](https://en.wikipedia.org/wiki/Reference_(computer_science)),
*reference* is

> a value that enables a program to indirectly access a particular datum.

### Immutable types

When say that a type is *immutable* when the following condition is true when a
new value of that type is created:

> The new value is bound to a *fixed* reference for the rest of its lifetime.

### Pitfalls

The following functions do not necessarily do what you expect.

```python
def vsum(v : list[float], w : list[float]) -> list[float]:
    """Returns the sum of vectors v and w."""
    for i in range(len(v)):
        v[i] += w[i]
    return v
```

```python
def create_matrix(n : int, m : int) -> list[list[float]]:
    """Returns an n x m matrix filled with 0.0."""
    row = [0.0]*m
    mat = []
    for i in range(n):
        mat.append(row)
    return mat
```
