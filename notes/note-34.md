# CS2 Fall 2025 Note 34

## Puzzle

Assume `a` is a list of integers with at least two elements and `i` is less than
`len(a) - 1`.  What does the following code do?

```python
        n = len(a)
        x = i
        j = i + 1
        while j < n:
            if a[j] < a[x]:
                x = j
            j += 1
        a[i], a[x] = a[x], a[i]
```

Try with `a = [5, 4, 3, 2, 1, 0]` and different values for `i` starting with
`0`.

What would be a better name for local variable `x` to reflect its role?
