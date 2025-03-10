def harmonic(n : int) -> float:
    """Return the sum of the first n term of the harmonic series."""
    if n == 1: return 1.0
    return harmonic(n - 1) + 1.0/n

print(harmonic(2))
