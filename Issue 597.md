# Issue 597: Why are single-argument arithmetic functions in the coercion model?

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2007-09-06 00:52:14

Assignee: somebody

Is there any advantage to having _neg_c/_neg_/_neg_c_imple as opposed to overriding __neg__? 


---

Comment by robertwb created at 2008-11-14 07:12:48

Now that cpdef methods are used, one can just implement `__neg__` and `__inverse__`, we don't need this infrastructure for unary operations (and it slows them down). 

We should do a full search of the source.


---

Comment by mhansen created at 2008-11-14 08:56:35

Resolution: duplicate


---

Comment by mhansen created at 2008-11-14 08:56:35

This is a now duplicate of #2072, which is more recent.
