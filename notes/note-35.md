# CS2 Spring 2025 Note 35

## Puzzle

Take the following function:

```python
def count_triples(xs : list[int]) -> int:
    """Return number of distinct triples (i, j, k) such that
    xs[i] + xs[j] + xs[k] = 0"""
    count = 0
    n = len(xs)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if xs[i] + xs[j] + xs[k] == 0:
                    count += 1
    return count
```

How would you evaluate the time it takes for `count_triples` to return a value
given an input of size *n* (i.e., the number of elements in `xs`)?
