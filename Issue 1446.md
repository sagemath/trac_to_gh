# Issue 1446: make check needs to error out on build failure instead of runnind doctests

Issue created by migration from https://trac.sagemath.org/ticket/1446

Original creator: mabshoff

Original creation time: 2007-12-10 08:06:39

Assignee: was

When invoking `make check` and the build fails make will start doctesting whatever sage install is in $PATH. That is obviously a bad thing.

Cheers,

Michael


---

Comment by jdemeyer created at 2013-02-08 19:27:42

Already fixed a while ago.


---

Comment by jdemeyer created at 2013-02-08 19:27:42

Resolution: worksforme
