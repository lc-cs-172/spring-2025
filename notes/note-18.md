# CS2 Spring 2025 Note 18

## Puzzle

Compare the execution of

```python
def fac(n):
    if n == 1: return 1
    return n*fac(n - 1)

fac(3)
```

and

```python
def fac2(n):
    return itfac2(n, 1)

def itfac2(n, a):
    if n == 1: return a
    return itfac2(n - 1, n*a)

fac2(3)
```
