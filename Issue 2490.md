# Issue 2490: Faster matrix_from_rows_and_columns

Issue created by migration from https://trac.sagemath.org/ticket/2490

Original creator: jsp

Original creation time: 2008-03-12 11:58:03

Assignee: was

matrix_from_rows_and_columns could be made faster by using PY_TYPE_CHECK and pyrex-style for loops.

See also trac ticket #2397


---

Comment by dfdeshom created at 2008-03-12 12:47:23

Japp, I'm marking this as duplicate since it is a duplicate of #2372 . Reviews for #2372 welcome!


---

Comment by dfdeshom created at 2008-03-12 12:47:23

Resolution: duplicate
