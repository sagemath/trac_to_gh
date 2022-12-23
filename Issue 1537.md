# Issue 1537: jmol triangulation/shadow weirdness

Issue created by migration from https://trac.sagemath.org/ticket/1537

Original creator: robertwb

Original creation time: 2007-12-16 10:34:55

Assignee: was

For example 

```
sage: from sage.plot.plot3d.all import *
sage: S = plot3d(lambda x, y: 1/(1+x^2+y^2), (-5,5), (-5,5), 'yellow')
sage: S.show(viewer='jmol')
```

or even

```
sage: S = plot3d(lambda x, y: 0, (-5,5), (-5,5), 'yellow')
sage: S.show(viewer='jmol')
```



---

Comment by robertwb created at 2007-12-16 10:35:22

Changing assignee from was to robertwb.


---

Comment by robertwb created at 2007-12-16 10:35:22

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-04-09 01:04:11

What is the status of this? It has been four months and a lot of work has gone into fixing various jmol related issues?

Cheers,

Michael


---

Comment by robertwb created at 2008-04-09 02:59:52

I believe this issue was fixed upstream, and I'm no longer seeing these issues so it is safe to close this patch.


---

Comment by mabshoff created at 2008-04-09 03:43:45

Resolution: fixed


---

Comment by mabshoff created at 2008-04-09 03:43:45

Closed as fixed upstream as per Robert's recommendation.
