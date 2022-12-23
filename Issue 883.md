# Issue 883: 2.8.7-alpha0:doctest failure: sloane_functions.py assumes that ZZ(3.0) fails

Issue created by migration from https://trac.sagemath.org/ticket/883

Original creator: cwitty

Original creation time: 2007-10-13 20:11:56

Assignee: failure

Several of the doctests in sloane_functions.py assume that RR->ZZ coercion always fails.


---

Comment by was created at 2007-10-14 05:10:14

Resolution: fixed
