# Issue 300: Consider filling out the blanks in Pyrex' PyObjects

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2007-02-28 21:46:47

Assignee: malb

Right now PyObject and PyTypeObjects are blackboxes in SageX/Pyrex. This is because they are declared without members in python.pxi or some file included from there. For some rare applications it might be useful to have direct access to the members of those structs. 


---

Comment by malb created at 2007-10-21 22:55:26

It never came up again, closing this for now.


---

Comment by malb created at 2007-10-21 22:55:26

Resolution: wontfix
