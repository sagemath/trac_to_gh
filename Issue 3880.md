# Issue 3880: Bad behavior of arrows

Issue created by migration from https://trac.sagemath.org/ticket/3880

Original creator: itolkov

Original creation time: 2008-08-16 19:22:55

Assignee: was

According to the arrow documentation,

```
An arrow from (xmin, ymin) to (xmax, ymax).
```


However, the current behavior is an arrow from (xmin, ymin) to (xmin + xmax, ymin + ymax).

For example:

```
sage: arrow((1, 1), (-1,-1))
```

will draw an arrow from (1,1) to (0,0).


---

Comment by itolkov created at 2008-08-16 19:25:52

According to the docs on matplotlib:

> patches.FancyArrow(x, y, dx, dy, ...

Fixing the line where this constructor is called should solve the problem.


---

Comment by rlm created at 2008-08-18 23:47:07

This should be taken care of at the same time as #3877.


---

Comment by rlm created at 2008-08-19 01:22:42

Jason is right, this is orthogonal to #3877. Shame on Alex for using such a stupid syntax as (xmin, ymin) to denote the tail coordinates of an arrow.


---

Attachment


---

Comment by mabshoff created at 2008-08-19 01:39:15

Patch looks good to me. Rlm explained to me what needed fixing.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-19 02:03:18

Resolution: fixed


---

Comment by mabshoff created at 2008-08-19 02:03:18

Merged in Sage 3.1.2.alpha0


---

Attachment
