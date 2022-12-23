# Issue 1516: jmol spkg, use from notebook and command line

Issue created by migration from https://trac.sagemath.org/ticket/1516

Original creator: robertwb

Original creation time: 2007-12-15 02:18:58

Assignee: was




---

Comment by robertwb created at 2007-12-15 02:19:03

Changing assignee from was to robertwb.


---

Comment by robertwb created at 2007-12-15 02:19:03

Changing status from new to assigned.


---

Attachment

See spkg at http://sage.math.washington.edu/home/robertwb/3d/jmol-11.2.14.spkg

Note, this is 14MB, but it is just the full Jmol bundle which has about 4MB docs, 6MB source, and 3M redundant applet binaries, not all of which we may want to include. 

I realize the bundle has other patches from other tickets (e.g. #1533), but these are needed.


---

Comment by robertwb created at 2007-12-16 10:31:20

Examples

```
sage: from sage.plot.plot3d.all import *
sage: S = plot3d(lambda x, y: abs(zeta(x+y*i)), (-3,3), (-3,3), ['red','blue'])
sage: S.show(viewer='jmol')
sage: (S + axes3d(5)).show(viewer='jmol')
```



---

Comment by mabshoff created at 2008-01-05 14:29:46

Resolution: fixed


---

Comment by mabshoff created at 2008-01-05 14:29:46

This was merged some time in 2.9.2.X.

Cheers,

Michael
