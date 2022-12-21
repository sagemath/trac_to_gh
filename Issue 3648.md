# Issue 3648: [with patch, needs review] complex(pari(...)) fails

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2008-07-12 16:23:14

Assignee: somebody

Pari gen objects should have a `__complex__` method, so that complex(...) works on them.


---

Attachment


---

Attachment


---

Comment by dmharvey created at 2008-07-14 04:55:05

I've added a further doctest to cover the case when "complex" doesn't make sense.

cwitty: if you're happy with that, this has a positive review from me.


---

Comment by cwitty created at 2008-07-16 04:04:42

dmharvey's patch looks good to me, and doctests pass in sage/libs/pari.


---

Comment by mabshoff created at 2008-07-16 04:45:27

Resolution: fixed


---

Comment by mabshoff created at 2008-07-16 04:45:27

Merged in Sage 3.0.6.alpha0
