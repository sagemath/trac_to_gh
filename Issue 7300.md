# Issue 7300: Display tight constraints

Issue created by migration from https://trac.sagemath.org/ticket/7300

Original creator: ncohen

Original creation time: 2009-10-25 19:42:04

Assignee: jkantor

It is often useful when solving linear programs to see which constraints are tight.... And so there should be a way to do it in Sage !!!


---

Comment by ncohen created at 2010-09-06 11:12:39

Changing component from numerical to linear programming.


---

Comment by mkoeppe created at 2016-04-03 19:50:32

Perhaps there should be a `MixedIntegerLinearProgram` method similar to `get_values` that retrieves the values of the constraint functions at the current solution; its input should be the same as the input to `constraints`.

Note also that some backends already have support for getting this kind of information, for example GLPK has `get_row_prim`.
