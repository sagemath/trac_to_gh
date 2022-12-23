# Issue 4998: OSX64: build Singulat with "--with-malloc=system"

Issue created by migration from https://trac.sagemath.org/ticket/4998

Original creator: mabshoff

Original creation time: 2009-01-17 15:52:10

Assignee: mabshoff

Using the mmap default leads to segfaults at starup since omalloc is not properly initialized.

Spkg coming up.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-17 15:52:16

Changing status from new to assigned.


---

Comment by mabshoff created at 2009-01-22 19:14:01

Spkg is at

http://sage.math.washington.edu/home/mabshoff/spkgs/singular-3-0-4-4-20080711.p3.spkg

Cheers,

Michael


---

Comment by rlm created at 2009-01-22 20:25:05

+1


---

Comment by mabshoff created at 2009-01-23 00:26:57

Resolution: fixed


---

Comment by mabshoff created at 2009-01-23 00:26:57

Merged in Sage 3.3.alpha1
