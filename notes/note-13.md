# Note 07

## The call stack

When your program calls a function, the program's execution pauses at the
calling point, the function runs until it returns, and then execution resumes
just past the calling point.

Behind the scenes, a structure called a call stack helps manage function calls
and returns.  The call stack consists of frames.  Among other data, each frame
stores any local variables, including parameters, associated with each active
function.  A function is considered active if it is either currently running or
if its execution is paused.
