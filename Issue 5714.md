# Issue 5714: Mod-2 matrix output does not show subdivisions

Issue created by migration from https://trac.sagemath.org/ticket/5714

Original creator: justin

Original creation time: 2009-04-08 19:06:54

Assignee: tbd

This was reported on sage-support.  The following shows what's going on:

```
sage: MS7=MatrixSpace(Integers(7),4,4)
sage: M=MS7.random_element()
sage: M.subdivide([2],[2])
sage: M

[6 1|3 4]
[4 4|0 5]
[---+---]
[4 2|2 6]
[5 6|3 3]
sage: MS2=MatrixSpace(Integers(2),4,4)
sage: N=MS2.random_element()
sage: N.subdivide([2],[2])
sage: N

[1 0 1 0]
[1 1 0 0]
[1 1 1 0]
[0 0 0 1]
```



---

Comment by justin created at 2009-04-08 19:14:10

As I mentioned on the list, the Matrix_mod2_dense class has its own str() method that just returns a string representation of the matrix without  taking subdivisions into account.

Removing that method seems to be benign, and lets the common print method for matrices take over, printing with subdivisions.

I have doctested the matrix directory without a problem.  Someone involved in the initial implementations might want to comment.

I'll attach a patch when the testing is complete (or try again if testing fails).


---

Comment by robertwb created at 2009-04-09 10:40:24

Resolution: duplicate
