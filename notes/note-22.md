# CS2 Spring 2025 Note 22

## Objects and classes

Every value in Python is an object.  For example, the int `5` and the string
`'hello'` objects.

Every object is an instance of some *class* (also known as a type).  Evaluating
`type(5)` and `type('hello')` will return `<class 'int'>` and `<class 'str'>`,
respectively.

Programming languages cannot foresee all the kinds of program you might wish to
write.  In particular, they cannot foresee all the types you might wish to
use in your programs.  That is why most programming language provides to extend
its functionality and in particular a means to create your own types.  Here is a
draft of a class called `Complex`:

```python
class Complex:
    pass
```

By convention, class names start with upper-case letters.  The keyword `pass`
just indicates that, for the moment, the body of the class definition is empty.

You can now create an instance of `Complex`:

```python
one = Complex()
```

### Attributes

You can add values called attributes to an object.  Continuing the previous
example:

```python
one.real = 1.0
one.imag = 0.0
```

Now you can use `one.real` or `one.imag` anywhere you want to know about these
values, but you can use `one` to refer to the entire `Complex`.  This ability to
refer to a whole collection of named values (and, for example, pass it into or
return it from a function) is a key feature of objects.

Each instance of the `Complex` class can have its own distinct values for these
attributes.  If you define:

```python
i = Complex()
i.real = 0.0
i.imag = 1.0
```
