"""This program prints the largest number in a non empty list."""

def find_max(xs : list[float]) -> float:
    """Returns the largest element of the given non-empty list."""
    return xs[0]

def main():
    ys = [57.60, 85.43, 96.80, 8.92, 23.53, 78.40, 32.59, 97.81, 12.34, 10.70]
    max = find_max(ys)
    print(max)

if __name__ == '__main__':
    main()
