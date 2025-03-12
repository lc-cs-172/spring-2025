# CS2 Spring 2025 Note 21

## Puzzle

What does `func` do?

def func(s):
    if s == "":
        return [""]
    else:
        ans = []
        for x in func(s[1:]):
            for y in range(len(x) + 1):
                ans.append(x[:y] + s[0] + x[y:])
        return ans

## Factorial

```python
def fac_iter(n : int) -> int:
    ans = 1
    for i in range(1, n + 1):
        ans *= i
    return ans
```

```python
def fac_rec(n : int) -> int:
    if n == 1: return 1
    return n*fac_rec(n - 1)
```

### Iteration vs. recursion

* Recursion may be more intuitive

* Iteration may be more efficient

### Reasoning about correctness

Goal: Prove that an algorithm will always produce the correct result (i.e.,
functional correctness).
