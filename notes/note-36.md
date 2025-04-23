# CS2 Spring 2025 Note 36

## Puzzle

What is the order of growth of the following functions?

```python
def linear_search(key, array):
    for i in range(len(array)):
        if array[i] == key:
            return True
    return False
```

```python
def f(angle):
    return math.cos(theta)**2 - math.sin(theta)**2
```

```python
def all_pairs():
    for i in range(n):
        for j in range(n):
            print(str(i) + ', ' + str(j))
```

## Stack

### Primitive array

Primitive arrays support the following operations:

* Allocate an array
* Access a singular element
* Set a singular element to a particular value
* Get the length of an array

To use Python's convenient list syntax while limiting yourself to what a
primitive array can do, use only the following features:

Operation|Syntax
-|-
Allocate an array of length $n$|`a = [None] * n`
Access element $i$|`a[i]`
Set element $i$ to $x$|`a[i] = x`
Get the length of an array|`len(a)`

### Array-based implementation

Let's implement the stack collection using primitive arrays!
