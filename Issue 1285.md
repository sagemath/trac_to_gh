# Issue 1285: implement substitution of subexpression  in calculus

Issue created by migration from Trac.

Original creator: certik

Original creation time: 2007-11-26 22:36:21

Assignee: was

e.subs(x, y) needs to work, where "x" is an expression and "y" is an expression.
and it substitutes x for y.

some tests from SymPy:

http://hg.sympy.org/sympy/file/d77f6c3b50bb/sympy/core/tests/test_subs.py

This is needed for the limit algorithm to work.


---

Comment by mhansen created at 2007-11-26 22:37:23

Changing status from new to assigned.


---

Comment by mhansen created at 2007-11-26 22:37:23

Changing assignee from was to mhansen.


---

Comment by rlm created at 2007-12-22 18:28:05

Resolution: duplicate
