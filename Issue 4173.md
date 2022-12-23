# Issue 4173: [with spkg, needs review] Solaris: fix cddlib build problem on Solaris x86

Issue created by migration from https://trac.sagemath.org/ticket/4173

Original creator: mabshoff

Original creation time: 2008-09-23 06:41:00

Assignee: mabshoff

LL and SS are reserved numerical constants on Solaris, but cddlib uses them in allface.c The spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.3/alpha1/cddlib-094b.p3.spkg

renames them so that the spkg now builds out of the box on Solaris.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-23 06:41:07

Changing status from new to assigned.


---

Comment by mhansen created at 2008-09-23 21:25:01

Looks good to me.


---

Comment by mabshoff created at 2008-09-23 22:01:36

Merged in Sage 3.1.3.alpha1


---

Comment by mabshoff created at 2008-09-23 22:01:36

Resolution: fixed
