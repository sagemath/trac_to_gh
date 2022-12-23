# Issue 1671: doctest: fix shapes.pyx fallout from #1666

Issue created by migration from https://trac.sagemath.org/ticket/1671

Original creator: mabshoff

Original creation time: 2008-01-03 17:26:58

Assignee: mabshoff

Due to Robert's work (#1666) I get a bunch of doctest failures like the following:

```
sage -t  devel/sage-main/sage/groups/perm_gps/cubegroup.py  
**********************************************************************
File "cubegroup.py", line 901:
    sage: C.show3d()
Expected nothing
Got:
    0.00166666666667
    0.00166666666667
    0.00166666666667
    0.00166666666667
    0.00166666666667
    0.00166666666667
    0.00166666666667
    0.00166666666667
    0.00166666666667
    0.00166666666667
    0.00166666666667
    0.00166666666667
**********************************************************************
```

I tracked this down to a print statement in `shapes.pyx`. I uncommented that line which fixes this issue.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-03 17:27:58

Resolution: fixed


---

Attachment

Applied to 2.9.2.alpha0.
