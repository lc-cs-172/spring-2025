# Pair Project #3: Maze Solver

This is a pair programming project.  Work with your assigned partner.  Only one
of you has to turn it in, but make sure you don't both think the other one was
doing it.

# Overview

Write a program that finds the exit of a maze described in ASCII-art form.  The
function that finds the exit must be *recursive*.

For instance, your program, given the following input of a 5x5 maze in a file
named [`maze.txt`](./maze.txt):

```
#####I#####
# #   #   #
# # # # # #
#   # # # #
# ### # # #
# #     # #
### ##### #
#   #   # #
# ### # # #
#   # #   #
#####O#####
```

should produce the following output:

```
The exit was found!  Here is one possible path to the exit:

#####I#####
# #  X#XXX#
# # #X#X#X#
#   #X#X#X#
# ###X#X#X#
# #  XXX#X#
### #####X#
#   #XXX#X#
# ###X#X#X#
#   #X#XXX#
#####O#####
```

The character `#` marks a wall, spaces for hallways, `I` marks the entrance, `O`
marks an exit.  You move through the maze only through the four cardinal
direction (north, south, east, west); no diagonal moves.

The program should work on any plain text file, with changing the filename being
the only modification needed to the code.  You can test it on these two files:

* [`maze.txt`](./maze.txt)
* [`maze10x10.txt`](./maze10x10.txt)

## Hints

* The entry is always going to be on the top row, but not at a fixed column.

* The first move is always going south by one square.

* There may be zero or more exits.

* The program must use recursion.

* If no path to an exit is found, the program should say so.

* If a path to an exit is found, the program should say so and print the maze
  with the path to the exit denoted with `X`s.

* A good signature for the recursive function is `find_exit(maze :
  list[list[str]], position : tuple[int, int]) -> bool`, where the maze is
  represented as a matrix of single-character strings (`'#'` for walls, `'I'`
  for the entry, `'O'` for an exit, `'X'` for a path, and spaces for hallways)
  and `position` is the current position considered for approaching the exit.

* There is no graphics involved in this assignment.

## What to hand in

Hand in your one file `maze_solver.py`.

Include the names of both participants in a comment at the top of your code (if
one person didn't contribute, don't include their name).
