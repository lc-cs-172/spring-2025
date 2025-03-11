def fib(n : int) -> int:
    """Return the nth element of the Fibonacci sequence."""
    if n == 0: return 0
    if n == 1: return 1
    return fib(n - 1) + fib(n - 2)

# A call to `fib(55)` would take a very long time to return.
#print(fib(55))

def fib2(n : int) -> int:
    """Return the nth element of the Fibonacci sequence.

    This implementation is much more efficient.  First, it avoids the
    exponential explosion of recursive calls to `fib`.  Second, because this
    implementation is tail recursive, a good compiler needs only allocate a
    single stack frame for the entire computation.

    To achieve this efficiency, this algorithm relies on a helper function
    named `go2`.

    There is probably a good Pythonic way to "hide" the helper function from
    users of `fib2`."""
    return go2(n, 0, 1)

def go2(n : int, a : int, b : int) -> int:
    """Helper function for an efficient computation of the nth element of the
    Fibonacci sequence.

    `a` and `b` should be initialized with the first two elements of the
    sequence."""
    if (n == 0): return a
    return go2 (n - 1, b, a + b)

print(fib2(55))
