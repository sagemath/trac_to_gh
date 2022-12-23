# Issue 1632: update sqlite to 3.5.4

Issue created by migration from https://trac.sagemath.org/ticket/1632

Original creator: mabshoff

Original creation time: 2007-12-29 04:44:08

Assignee: mabshoff




---

Comment by mabshoff created at 2007-12-29 04:44:14

Changing status from new to assigned.


---

Comment by mhansen created at 2009-06-04 21:06:14

Resolution: invalid


---

Comment by mhansen created at 2009-06-04 21:06:14

Since sqlite3 is included in the Python standard library, that is the version we should use.  Also, we don't include a separate sqlite spkg anymore.
