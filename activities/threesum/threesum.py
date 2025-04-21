"""Measure the time its take to compute some function."""

import random
import time

def count_triples(xs : list[int]) -> int:
    """Return the number of distinct triples (i, j, k) such that
    xs[i] + xs[j] + xs[k] = 0"""
    count = 0
    n = len(xs)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if xs[i] + xs[j] + xs[k] == 0:
                    count += 1
    return count

def time_count_triples(n : int) -> float:
    """Run a doubling experiment."""
    xs = [ random.randint(-1000000, +1000000) for _ in range(n)]
    start = time.time()
    count_triples(xs)
    end = time.time()
    return end - start

def main():
    n = 16
    t_prev = time_count_triples(n)
    print('{:>8s} {:>8s} {:>8s}'.format('size', 'time', 'ratio'))
    while True:
        n *= 2
        t = time_count_triples(n)
        print('{:8d} {:8.1f} {:8.2f}'.format(n, t, t/t_prev))
        t_prev = t

if __name__ == '__main__':
    main()
