# CS2 Spring 2025 Note 16

## Puzzle

Evaluate the following expressions (feel free to use the Python REPL).

```python
[1, 2, 3][0]
(1, 2, 3)[0]
{1, 2, 3}[0]
```

Given

```python
l = [1, 2, 3]
t = (1, 2, 3)
s = {1, 2, 3}
```

What is the result of each of the following statements?

```python
l[0] = 5
t[0] = 5
s[0] = 5
```

## Mutability, indexability

In Python, lists are mutable, while tuples and sets are not.  Likewise, lists
and tuples are indexable, while sets are not.

**Update**: I made a mistake.  Sets are mutable!

In summary:

Built-in type | Mutable | Indexable
-|-|-
`int` | no | no
`bool` | no | no
`float` | no | no
string | no | yes
list | yes | yes
tuple | no | yes
set | yes | no
