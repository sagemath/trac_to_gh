# Issue 838: doctest runner should share SAGE initialization using fork()

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2007-10-07 17:03:12

Assignee: failure

CC:  gfurnish

On my machine, every file that gets doctested takes 0.8s for initializing SAGE (before it even gets to running the tests).  It would be nice if this overhead could be eliminated somehow; and I think it might be possible, by having a single process do the SAGE initialization, then fork() before doctesting a particular file.  (This sort of architecture might also make it easier to implement #639.)


---

Comment by mabshoff created at 2008-12-05 04:51:05

This is not a dupe of #4699, but seems closely related since -tp 1 would basically work that way.

Cheers,

Michael


---

Comment by roed created at 2012-02-06 03:50:46

This will be resolved by #12415.


---

Comment by jdemeyer created at 2013-02-08 13:55:52

Resolution: duplicate
