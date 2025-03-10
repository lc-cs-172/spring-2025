"""Write the instructions for the problem of the towers of Hanoi with n
disks.

A recursive solution."""

def move(n : int, src : str, dst : str, aux : str) -> None:
    if n == 1:
        print('move top disk from peg {} to peg {}'.format(src, dst))
        return
    move(n - 1, src, aux, dst)
    move(1, src, dst, aux)
    move(n - 1, aux, dst, src)

def hanoi(n : int) -> None:
    """Write the instructions to move n disks from a source peg, to the
    destination peg, using an auxiliary peg."""
    src = 'a'
    dst = 'c'
    aux = 'b'
    move(n, src, dst, aux)

def main():
    hanoi(4)

if __name__ == '__main__':
    main()
