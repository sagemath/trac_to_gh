# Issue 1821: Update FLINT to 1.0.6

Issue created by migration from https://trac.sagemath.org/ticket/1821

Original creator: mabshoff

Original creation time: 2008-01-18 01:04:04

Assignee: mabshoff


```
FLINT 1.0.6 fixes the issue on the teragrid machine. It's just a
workaround. I've no idea what was really wrong. It might be that when
they implemented the builtin they forgot about arithmetic shift
issues. At any rate it seems to be broken only when you ask for the
number of bits of 0. The patch just treats this as a special case. The
tests now pass on that machine, and still pass on sage.math.

At first I thought it had to do with the fact that the builtin returns
an int, which is 32 bits, whilst a long is 64 bits. But I was unable
to fix it under this assumption.

http://www.flintlib.org/

Bill.
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-01-18 01:04:28

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-01-19 18:58:00

The updated spkg is at

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.1/alpha0/flint-1.06.spkg

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-19 19:52:48

Resolution: fixed


---

Comment by mabshoff created at 2008-01-19 19:52:48

Merged in Sage 2.10.1.alpha0
