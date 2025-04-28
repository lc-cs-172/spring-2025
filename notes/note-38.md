# CS2 Spring 2025 Note 38

## Iterators

We have used loops to iterate over integers, for instance:

```python
for i in range(10):
    ...
```

But we can also use loops to iterate over members of a collection.  List is an
example of a collection.  Let us say we have a list of five strings:

```python
my_list = ['a', 'aah', 'aardvark', 'aardwolf', 'aba' ]
```

We can iterate over this list with these statements:

```python
for s in my_list:
    print(s)
```

Any collection that can be used with a `for` loop is said to be *iterable*.

The [lists](../assignments/individual/a7/README.md) assignment asks you to make 
`ArrayList` and `LinkedList` iterable.

To become iterable, a collection must implement the method `__iter__` which
should return an *iterator* object.  And the iterator object should define a
method called `__next__` which should return the next element of the collection.
When all elements of the collection have been returned, `__next__` should raise
the `StopIteration` exception (`raise StopIteration`).

For the lists assignment, it is enough to treat the collection itself as the
iterator object.  Therefore, the collection can define both `__iter__` and
`__next__`.  `__iter__` simply returns the collection (`return self`), but not
before initializing the iterator state.  The iterator state should keep track
of the last member that was supplied.  What is the simplest approach to achieve
this?

Note that some more ambitious collections may implement the iterator as a
subclass of the collection.

## Amortized performance analysis

On some occasions you will do amortized analysis, which asks, "What's the
average behavior over the worst possible sequence of operations?"  For almost
all algorithms, this is exactly the same as worst-case analysis, because the
worst possible sequence of operations is just the worst individual operation
over and over again.  For some data structures (notably resizable arrays) the
worst operation can't happen over and over again, so the amortized result may be
better.  Amortized running time is always at least as good as worst-case and at
least as bad as average.
