# Issue 3012: animate.py: convert not being found is an annoying debug message - fix that

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-04-23 22:07:43

Assignee: mabshoff

Bjake Hammersholt Roune reported:

```
> [...]
 sage -t  devel/sage/sage/plot/animate.py                    sh:
 convert: command
  not found
```

Hide it or test if it exists before running it. This should be easy to fix.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-23 22:08:50

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-09-29 22:26:54

This is a duplicate of #767. Closed.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-29 22:26:54

Resolution: duplicate
