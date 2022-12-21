# Issue 441: add sage-valgrind command line option analog to sage-gdb

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-08-18 18:50:23

Assignee: mabshoff

Integrate valgrind into sage so people can conveniently attempt to debug. This requires Sage's python to be build with the configure flag "--without-pymalloc" to prevent valgrind from reporting false positives because pymalloc mallocs large chunks of memory and returns fractions of the memory when the python interpreter requests memory.



---

Comment by mabshoff created at 2007-08-18 19:49:37

Basic support has been merged, but "./sage -valgrind -testall" ignores the -testall for now.


---

Comment by was created at 2007-08-19 07:04:27

Resolution: fixed
