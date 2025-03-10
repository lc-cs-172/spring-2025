"""Write the instructions for the problem of the towers of Hanoi with n
disks.

Inspired by an iterative solution that appears in Wikipedia
(https://en.wikipedia.org/wiki/Tower_of_Hanoi#Iterative_solution)."""

stacks = {'a': [], 'b': [], 'c': []}

def move(x : str, y : str) -> None:
    """Move a disk from x to y, or vice versa, whichever is legal."""
    if (len(stacks[y]) == 0 or
        (len(stacks[x]) > 0 and stacks[x][-1] < stacks[y][-1])):
        print('move disk {} from peg {} to peg {}'.format(stacks[x][-1], x, y))
        stacks[y].append(stacks[x].pop())
    else:
        move(y, x)

def hanoi(n : int) -> None:
    """Write the instructions to move n disks from a source peg, to the
    destination peg, using an auxiliary peg."""
    src = 'a'
    dst = 'c'
    aux = 'b'
    for d in range(n, 0, -1):
        stacks[src].append(d)
    all_moves = 2**n - 1
    if n%2 == 0:
        dst, aux = aux, dst
    for i in range(1, all_moves + 1):
        if i%3 == 1:
            move(src, dst)
        if i%3 == 2:
            move(src, aux)
        if i%3 == 0:
            move(aux, dst)

def main():
    hanoi(4)

if __name__ == '__main__':
    main()
