# Issue 8508: max is broken on symbolic input

Issue created by migration from https://trac.sagemath.org/ticket/8508

Original creator: zimmerma

Original creation time: 2010-03-12 17:19:56

Assignee: burcin

cf http://groups.google.com/group/sage-support/msg/55dafb49058a55c6

```
sage: var('y');
sage: max(x,y)
x
sage: max(y,x)
y
```

We expect both to give `max(x,y)` of course.


---

Comment by burcin created at 2010-03-12 18:07:20

Resolution: duplicate


---

Comment by burcin created at 2010-03-12 18:07:20

This is a duplicate of #6949.
