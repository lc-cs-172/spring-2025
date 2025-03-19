# CS2 Spring 2025 Note 24

## Optional arguments

Python provides the means to mark a function argument as optional.  To do so you
must supply a default value.  You indicate the default value by following the
argument name with the assignment operator and an expression (see an example in
the class definition below).

## Operator overloading

An operator that behaves differently depending on the types of its operands is
said to be *overloaded*.

Python provides the programmer the means to overload most of its operators.
Here is a subset of these overloadable operators along with the corresponding
magic methods that would need to be defined.

Operator | Magic method
-|-
`==` | `__eq__(self, other)`
`!=` | `__ne__(self, other)`
`+` | `__add__(self, other)`
`-` | `__sub__(self, other)`
`*` | `__mul__(self, other)`
`/` | `__truediv__(self, other)`

Here is the latest definition of `Complex` (with a typo fixed in `__repr__` and
an optional argument for the initializer):

```python
class Complex:
    def __init__(self, real : float, imag : float = 0.0):
        self.real = real
        self.imag = imag

    def __repr__(self):
        return '({:.3f}{:+.3f}i)'.format(self.real, self.imag)

    def __str__(self):
        return self.__repr__()

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def conjugate(self):
        return Complex(self.real, -self.imag)
```
