# Issue 809: [with patch] class_graph fixes

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2007-10-03 15:47:17

Assignee: was

class_graph as introduced recently, gives false results, i.e. it doesn't return a real representation of the SAGE inheritance tree. The attached patch is supposed to fix that by using Python's built-in functionality directly rather than using string parsing.


---

Attachment


---

Comment by was created at 2007-10-04 03:13:57

Resolution: fixed


---

Comment by was created at 2007-10-04 03:14:09

Changing component from algebraic geometry to user interface.
