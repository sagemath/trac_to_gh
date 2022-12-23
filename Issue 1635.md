# Issue 1635: Singular.spkg relatated: lib->LIB link issue on OSX

Issue created by migration from https://trac.sagemath.org/ticket/1635

Original creator: mabshoff

Original creation time: 2007-12-29 06:19:21

Assignee: mabshoff

The problem has come up a couple times on sage-devel: The OSX binary Sage tar-ball contains a link case sensitive link lib->LIB that is caused by the singular.spkg. I believe it is to accomodate some issue with Singular's high level libraries. We should just skip creating that link on OSX and all should be fine.

Cheers,

Michael


---

Comment by mabshoff created at 2007-12-31 10:23:53

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-01-02 21:44:13

The following spkg fixes the issue by avoiding creating a `lib->LIB` link:

 * http://sage.math.washington.edu/home/mabshoff/singular-3-0-4-1-20071209.p0.spkg

I tested the resulting bdist and it no longer shows the issue on an OSX 10.4 box with default file system options.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-02 21:49:20

Oops, I mean 

 * http://sage.math.washington.edu/home/mabshoff/singular-3-0-4-1-20071209.p1.spkg

Sorry for the confusion.

Cheers,

Michael


---

Comment by mhansen created at 2008-01-03 07:19:57

This builds fine for me.


---

Comment by mabshoff created at 2008-01-03 13:51:20

Merged in 2.9.2.alpha0


---

Comment by mabshoff created at 2008-01-03 13:51:20

Resolution: fixed
