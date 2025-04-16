# CS2 Fall 2025 Note 33

## Collection

We often have to deal with collections of data.  Examples include grades on an
exam, snow falls at the airport, visited websites, and number of seconds it
takes to sort lists varying length.

Collections usually implement at least the following operations: `add`,
`remove`, `is_empty` (the actual names of these operations may vary depending on
the type of the collection).

### Add

Adding an item to a collection does not usually require much thought.

### Remove

More considerations goes into removing an element.  Specifically, we must ask
which element should be removed?

### Last in, first out

A possible discipline consists of removing the element that was added last.  We
sometimes refer to this discipline as *last in, first out* or LIFO.  A
collection implementing such a discipline is referred to as a *stack*.

### First in, first out

Another discipline consists of removing the element that was added earliest.
We refer to this discipline as First In, First Out or FIFO for short.  A
collection implementing this discipline is referred to as a *queue*.

### Implementation with lists

Collection | `add` | `remove` | `is_empty`
-|-|-|-
Stack | `s.append(x)` | `s.pop()` | `len(s) == 0`
Queue | `q.append(x)` | `q.pop(0)` | `len(q) == 0`

### Nomenclature

Computer scientists have developed a specific vocabulary for certain collection
operations depending on the implemented discipline.

Collection | `add` | `remove`
-|-|-
Stack | push | pop
Queue | enqueue | dequeue

## Puzzle

What everyday situations remind you of a stack?  A queue?
