# Issue 6031: [with spkg, needs review] ntl-5.4.2.p7.spkg: Fix gcc 4.4.0 compilation problem, add spkg-check target

Issue created by migration from https://trac.sagemath.org/ticket/6031

Original creator: mabshoff

Original creation time: 2009-05-12 16:39:26

Assignee: mabshoff

NTL 5.4.2 needs a minimal header fix to build with gcc 4.4. While at it I also added a spkg-check target. 

The spkg is at 

   http://sage.math.washington.edu/home/mabshoff/release-cycles-4.0/alpha0/ntl-5.4.2.p7.spkg

Tested on Linux and 64 bit OSX.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-12 16:39:31

Changing status from new to assigned.


---

Comment by malb created at 2009-05-12 17:48:08

looks good, doctests pass.


---

Comment by mabshoff created at 2009-05-12 18:17:07

Merged in Sage 4.0.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-12 18:17:07

Resolution: fixed
