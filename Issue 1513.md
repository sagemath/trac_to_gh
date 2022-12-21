# Issue 1513: FLINT install uses make -B, which isn't an option on (slightly) older make versions

Issue created by migration from Trac.

Original creator: craigcitro

Original creation time: 2007-12-14 23:21:40

Assignee: was

The title pretty much says it all. make 3.79.1 doesn't support make -B, and I'm likely not the only person with a slightly outdated version of make, so we should see if this can be switched around at all.


---

Comment by mabshoff created at 2007-12-14 23:27:54

The spkg at

http://sage.math.washington.edu/home/mabshoff/flint-1.02.p0.spkg

should fix the problem. I don't think we will need "-B" since we always build the check from a tree than only had the library build in it once.

Cheers,

Michael


---

Comment by mabshoff created at 2007-12-14 23:44:04

Changing status from new to assigned.


---

Comment by mabshoff created at 2007-12-14 23:44:04

Changing assignee from was to mabshoff.


---

Comment by mabshoff created at 2007-12-14 23:44:41

Resolution: fixed


---

Comment by mabshoff created at 2007-12-14 23:44:41

Merged in 2.9.rc0.
