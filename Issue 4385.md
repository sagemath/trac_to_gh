# Issue 4385: Sage 3.1.4: optional doctest failure in sage/rings/polynomial/multi_polynomial.pyx

Issue created by migration from https://trac.sagemath.org/ticket/4385

Original creator: mabshoff

Original creation time: 2008-10-30 04:16:25

Assignee: mhampton


```
sage -t -long -optional devel/sage/sage/rings/polynomial/multi_polynomial.pyx
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.alpha1/tmp/multi_polynomial.py", line 712:
    sage: P
Expected:
    A Polyhedron with 4 vertices.
Got:
    A Polyhedron with 3 vertices.
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.alpha1/tmp/multi_polynomial.py", line 721:
    sage: R(1).newton_polytope()
Expected:
    A Polyhedron with 1 vertices.
Got:
    A Polyhedron with 1 vertex.
**********************************************************************
```



---

Comment by mhampton created at 2008-10-31 12:37:00

simple fixes


---

Attachment

This is very simple, those optional tests just hadn't been hit in a while and the output needed to be changed.  The "vertices" to "vertex" was just a grammatical fix.  The 4 vertices to 3 is because Polyhedron objects now remove redundant vertices immediately.


---

Comment by mhampton created at 2008-10-31 12:38:56

Changing priority from major to minor.


---

Comment by mabshoff created at 2008-10-31 12:49:15

Patch looks good to me. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-10-31 13:50:12

Merged in Sage 3.2.alpha2


---

Comment by mabshoff created at 2008-10-31 13:50:12

Resolution: fixed
