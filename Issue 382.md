# Issue 382: Unitialized variable in error message

Issue created by migration from https://trac.sagemath.org/ticket/382

Original creator: justin

Original creation time: 2007-05-29 04:23:16

Assignee: was

In "databases/db_class_polynomials.py:_dbpath()", the "NYI" error for level>1 refers
to the variable 's'; it should be 'level'. 

Bundle attached.



---

Comment by justin created at 2007-05-29 04:25:27

OK, Trac blew chunks when I tried to attach the bundle.  I'm sending it out of band, to William.


---

Comment by was created at 2007-05-31 13:48:27

Resolution: fixed


---

Comment by was created at 2007-05-31 13:48:27

I applied the patch.
