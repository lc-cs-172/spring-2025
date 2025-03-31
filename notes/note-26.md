# CS2 Spring 2025 Note 26

## Puzzle

Do the following two code sequences produce the same output?

```python
odd_numbers_doubled = []
for item in range(10):
    if item % 2 == 1:
        odd_numbers_doubled.append(2*item)
```

```python
odd_numbers_doubled = [2*item for item in range(10) if item % 2 == 1]
```

## List comprehensions

List comprehensions let you build lists concisely.  The syntax is as follows

<pre>
[ <em>f(x)</em> for <em>x</em> in <em>sequence</em> if <em>condition(x)</em> ]
</pre>

where the *if* component is optional.  Its flow is:

1. Iterate over the elements of the *sequence*
2. For each such element, check the *condition*
3. If the *condition* is true, then apply the function *f* to the element and
   add the result to the list comprehension 

## Refactoring

Martin Fowler defines *refactoring* as a disciplined technique for restructuring
an existing body of code, altering its internal structure without changing its
external behavior.
