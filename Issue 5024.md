# Issue 5024: [with spkg, needs review] Solaris 10: Do not create dynamic liblpack on non-Linux

Issue created by migration from https://trac.sagemath.org/ticket/5024

Original creator: mabshoff

Original creation time: 2009-01-19 11:07:40

Assignee: mabshoff

When we create a dynamic liblapack.so on non-Linux it often creates broken imports for numpy and scipy, so don't do it for now.

The atlas.spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.3/alpha0/atlas-3.8.2.p1.spkg

fixes the problem.

Cheers,

Michael



---

Comment by mabshoff created at 2009-01-19 11:07:47

Changing status from new to assigned.


---

Comment by mhansen created at 2009-01-19 11:33:10

Works for me.


---

Comment by mabshoff created at 2009-01-19 11:55:59

Resolution: fixed


---

Comment by mabshoff created at 2009-01-19 11:55:59

Merged in Sage 3.3.alpha0
