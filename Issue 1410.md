# Issue 1410: fix leftover issues from removal of mwrank.spkg

Issue created by migration from https://trac.sagemath.org/ticket/1410

Original creator: mabshoff

Original creation time: 2007-12-06 13:17:34

Assignee: mabshoff

ToDo:
  * delete $SAGE_LOCAL/include/mwrank
  * strip the mwrank binaries? Also make them link dynamically?
    mwrank unstripped: 12 mb, stripped 2.2MB
  * delete $SAGE_LOCAL/lib/libmwrank.[so|dylib]

Cheers,

Michael


---

Comment by mabshoff created at 2007-12-06 13:17:45

Changing status from new to assigned.


---

Comment by mabshoff created at 2007-12-06 16:55:01

As far as I can tell the spkg at

http://sage.math.washington.edu/home/mabshoff/cremona-20071124.p4.spkg

fixes all the above issues. But it certainly can stand some more testing.

Cheers,

Michael


---

Comment by mabshoff created at 2007-12-06 16:55:49

The patch isn't very clean, but it works ;)


---

Comment by mabshoff created at 2007-12-06 17:46:59

Resolution: fixed


---

Attachment

Merged in 2.9.alpha1. Doctests and builds fine in Linux and OSX.
