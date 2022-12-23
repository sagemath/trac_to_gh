# Issue 474: make the -valgrind target more flexible, add massif support

Issue created by migration from https://trac.sagemath.org/ticket/474

Original creator: mabshoff

Original creation time: 2007-08-21 01:16:58

Assignee: mabshoff

At the moment the valgrind tool and flags are hardcoded in various scripts. So add checks for environment flag SAGE_VALGRIND_FLAGS to overwrite default.

To illustrate what you can do with other tools from the valgrind suite have a look at the two attached graphs created by the heap profiler massif.

It might also be nice to add a -valgrind to "sage -testall" to valgrind the whole test suite.

For two examples look at:

http://sage.math.washington.edu/home/mabshoff/massif.19869.ps
http://sage.math.washington.edu/home/mabshoff/massif.19966.ps


Cheers,

Michael


---

Comment by mabshoff created at 2007-08-21 01:17:41

Resolution: duplicate
