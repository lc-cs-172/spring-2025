# CS2 Spring 2025 Note 04

## Puzzle

What is the result of the `round(1.5)`?  What is the result of `round(2.5)`?
Can you explain the result?

## For each loop

Assuming we define the following array:

```python
xs = [34, 48, 19, 38]
```

and we would like to sum its elements.  Coming from C, you might be tempted to
write the following Python code to achieve this goal:

```python
sum = 0
i = 0
while i < len(xs):
    sum += xs[i]
    i += 1
```

But Python provides the following alternative:

```python
sum = 0
for x in xs:
    sum += x
```

With this form, we no longer need to manage the access to each of the distinct
elements of the array with a separate variable (usually referred to as an index,
here `i`).  The `for` loop takes care of that task for us behind the scenes.

The `for` loop syntax is as follows:

<pre>
for <em>variable</em> in <em>array (or array-like)</em>:
    <em>statement</em>
    ...
</pre>

Its flow is:

1. If there are no values in the array that haven't been accessed yet, stop.
2. Assign the variable to the next value in the array.
3. Execute the statements in the body of the loop.
4. Go back to step 1.

We call this type of iterative construct a "for each" loop.  Its genesis comes
from the realization that more often than not, when we have an array we are
likely to want to iterate over every element of its content (whether it is to
sum the elements, print them, find the minimum, etc).  The motto is "let's make
the common case convenient to express."
