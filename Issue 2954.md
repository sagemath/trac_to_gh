# Issue 2954: [with spkg. needs review] ATLAS 3.8.1: Fix Itanium 2 detection on Itanium/gcc compiler flags on RHEL5/Itanium

Issue created by migration from https://trac.sagemath.org/ticket/2954

Original creator: mabshoff

Original creation time: 2008-04-19 04:00:01

Assignee: mabshoff

Itanium 2 on RHEL 5 and pretty much any other modern kernel is not properly detected. ATLAS also uses the -m64 flags which is not available on RHEL 5 on Itanium. The spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0/alpha6/atlas-3.8.1.p0.spkg

fixes both issues.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-19 04:00:07

Changing status from new to assigned.


---

Comment by was created at 2008-04-19 05:31:18

REPORT:

 Well I give #2954 a positive review if it builds and works for you.
I've read the patches.


---

Comment by mabshoff created at 2008-04-19 06:52:27

Build time on Itanium is quite bad, especially compared to x86-64, but I guess that it is partially the fault of gcc 4.1.1 I used.

Oh well,

Michael


---

Comment by mabshoff created at 2008-04-19 06:52:43

Merged in Sage 3.0.alpha6


---

Comment by mabshoff created at 2008-04-19 06:52:43

Resolution: fixed
