# Issue 1462: speed up "sage -b" -- don't do anything cython stuff if no .pyx, .pxd, or .pxi file changes (not a dupe!)

Issue created by migration from https://trac.sagemath.org/ticket/1462

Original creator: was

Original creation time: 2007-12-11 20:17:38

Assignee: was

This is a very very simple patch that makes it so 

  sage -b

takes 1 seconds (on my mac laptop) instead of 10 seconds, so long as 
no Cython code has changed.  Otherwise it works just as before.

This is orthogonal to Bobby Moretti's patch for caching Cython dependencies.
Both should be used.

This is much simpler -- all it does is -- in 1/100th of a second (or so) compute a hash got from all cython-related files in the repo, and if that hasn't changed from last time, skip all cython-ing of code. 




---

Attachment


---

Comment by was created at 2007-12-12 15:55:20

I applied this for 2.9.


---

Comment by was created at 2007-12-12 15:55:20

Resolution: fixed


---

Attachment
