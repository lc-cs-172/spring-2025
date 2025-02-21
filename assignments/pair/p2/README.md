# Pair Project #2: Segregation Simulation

This is a pair programming project.  Work with your assigned partner.  Only one
of you has to turn it in, but make sure you don't both think the other one was
doing it.

## Overview

Implement Schelling's model of segregation, as described in [Frank McCown's
assignment](http://nifty.stanford.edu/2014/mccown-schelling-model-segregation/).

Your program should behave like the example embedded in the web page above.  Use
a smaller grid size (e.g., 20×20) but otherwise use the same default parameters
(similarity at 30%, red/blue ratio at 50%, and empty/total ratio at 10%).  At
the end of the simulation, please print the number of rounds it took to get to
100% satisfaction to the terminal.

At each step, you should find all of the unsatisfied agents and then move each
unsatisfied agent to a random unoccupied cell.  Agents are allowed to move to
cells that became vacant in the same round.

Clarification: an agent with no neighbors is satisfied.

You don't have to provide buttons or sliders, and you don't need to implement
the ability to stop or start; it should just start when the window opens.  I
should be able to change each parameter by changing it in one place in your
program.

You don't have to implement any variants, just the basic version.

This is your first assignment where you have the opportunity to break your logic
up into functions.  You should not have one large main function.  Try to make
your code readable, using appropriate variable and function names to communicate
their purpose.  Use test-driven development to create each function.

## What To Hand In

Hand in your main program `segregation.py` and your test class
`segregation_test.py`.

Include the names of both participants in a comment at the top of your code (if
one person didn't contribute, don't include their name).
