# Issue 125: maxima doctest freezes

Issue created by migration from https://trac.sagemath.org/ticket/125

Original creator: dmharvey

Original creation time: 2006-10-11 00:12:51

Assignee: was

On a clean vanilla sage 1.4 install (running on sage.math), the doctest for `devel/sage-main/sage/interfaces/maxima.py` just freezes. SAGE never seems to pick up the timeout. I hit ctrl-c, and the doctests proceed normally after that.



---

Comment by was created at 2006-10-12 19:18:34

This is a very annoying bug that only happens on 64-bit linux.  I will have to carefully step through the problem.  It shouldn't be hard to fix though.


---

Comment by was created at 2007-01-12 22:58:57

fixed for a while...


---

Comment by was created at 2007-01-12 22:58:57

Resolution: fixed
