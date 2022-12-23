# Issue 873: sage -clone is rebuilding everything !

Issue created by migration from https://trac.sagemath.org/ticket/873

Original creator: was

Original creation time: 2007-10-13 05:49:12

Assignee: was

Doing "sage -clone foo" rebuild all the pyx files, which is terrible. 


---

Comment by was created at 2007-10-13 05:49:17

Changing status from new to assigned.


---

Comment by was created at 2007-10-13 05:49:29

Changing component from algebraic geometry to user interface.


---

Comment by cwitty created at 2007-10-13 07:02:26

fixes slow "-clone" (look for Cython-generated files, not Pyrex)


---

Attachment


---

Comment by was created at 2007-10-13 07:14:33

Resolution: fixed
