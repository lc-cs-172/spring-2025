# CS2 Spring 2025 Note 23

## Methods

Functions defined in a `class` are often referred to as *methods*.

### Defining methods

Methods are defined exactly like regular functions, but with two differences:

* methods are defined inside a class, and
* methods have an extra first argument `self`.

Here is an improved definition of `Complex`:

```python
class Complex:
    def __init__(self, real : float, imag : float):
        self.real = real
        self.imag = imag

    def __repr__(self):
        return '({:.0f}{:+.0f}i)'.format(self.real, self.imag)

    def __str__(self):
        return self.__repr__()

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def conjugate(self):
        return Complex(self.real, -self.imag)
```

### Activity

Define a class for circles that takes a radius as an argument and defines the
`area` and `circumference` methods with the obvious meanings.
