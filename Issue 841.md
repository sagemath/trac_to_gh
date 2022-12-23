# Issue 841: hash() on algebraic reals is not stable

Issue created by migration from https://trac.sagemath.org/ticket/841

Original creator: cwitty

Original creation time: 2007-10-09 00:42:55

Assignee: cwitty

The hash() function applied to a single algebraic real may give different results at different times:

```
sage: foo = sqrt(AA(4))
sage: hash(foo)
-1289340516
sage: foo == 2
True
sage: hash(foo)
2105051955
```


(I plan to fix this problem very soon.)



---

Attachment

OK, here's a patch that makes hash() on algebraic reals stable.  New results after the patch:


```
sage: foo = sqrt(AA(4))
sage: hash(foo)
-1968313278
sage: foo == 2
True
sage: hash(foo)
-1968313278
```



---

Comment by cwitty created at 2007-10-09 01:03:52

Changing assignee from cwitty to tbd.


---

Comment by was created at 2007-10-13 07:10:03

Resolution: fixed
