# CS2 Spring 2025 Note 28

## Composition

We have already seen *composition* at work when, for instance, we defined a
`Body` in terms of `Vector`s.

```python
class Body:
    def __init__(self, mass : float, p0 : Vector, v0 : Vector):
        self.mass = mass
        self.p = p0
        self.v = v0
```

## Inheritance

Python provides another means of defining relationships among classes called 
*inheritance*.  Let's study an example.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return 'I have spoken'

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return 'meow'
```

## Summary

Python provides support for defining relationships among classes.  One method
is *composition* where type `B` declares an attribute of type `A`.  We call
*composition* a **has a** relationship.  For instance, `Body` **has an**
attribute of type `Vector`.

Another method is *inheritance* where type `B` extends the functionality of type
`A`.  We call *inheritance* an **is a** relationship.  For instance, `Cat` **is
an** `Animal`.  We refer to `Animal` as a *base* or *superclass* class and `Cat`
as a *subclass* or *derived* class.

A derived class can *override* a method defined in the base class.

A derived class can access attributes and methods of the base class with the
built-in function `super()`.

## Fragile base class problem

Use of **is a** inheritance is controversial in some quarters.  There are two
reasons for this point of view.  First, the derived class is completely
dependent on the base class.  Any change to the base class affects the derived
class.  Second, the derived class can access any attribute of the base class
subverting its intentions.
