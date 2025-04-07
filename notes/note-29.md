# CS2 Spring 2025 Note 29

## Puzzle

Recall assignment a4.  This assignment asked you to implement a type for
two-dimensional vectors.  Consider the example use of this type below.  What do
you expect will happen if you run this code?  

```python
from vector import Vector

v1 = Vector(0+1j, 0)
v2 = Vector(1, 0)

print(v1 + v2)
print(v1.distance_to(v2))
```

## Duck typing

> When I see a bird that walks like a duck and swims like a duck and quacks like
> a duck I call that bird a duck
>                               -- J. W. Riley

A function should not care about the type of its argument, only that it can
apply the desired behavior on it.

### Advantages

* Simpler and more flexible code
* Focus on the behavior rather than the type

### Disadvantages

* Potential for runtime errors (e.g., `TypeError`, `AttributeError`)
* Code more difficult to comprehend
