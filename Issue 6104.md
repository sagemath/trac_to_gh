# Issue 6104: [with spkg, needs review] Fix Solaris specific build issue for libfplll.spkg

Issue created by migration from https://trac.sagemath.org/ticket/6104

Original creator: mabshoff

Original creation time: 2009-05-21 04:26:44

Assignee: mabshoff

dpe.h was not including some headers for finite() and also due to system header differences there are template scope issues with NAN. The spkg at 

http://sage.math.washington.edu/home/mabshoff/release-cycles-4.0/rc0/libfplll-3.0.12.p0.spkg

works around that.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-21 04:27:16

Changing status from new to assigned.


---

Comment by was created at 2009-05-28 06:49:30

Resolution: fixed
