# Issue 4546: [with patch, needs review] redundant print in sage-doctest

Issue created by migration from https://trac.sagemath.org/ticket/4546

Original creator: burcin

Original creation time: 2008-11-18 10:39:56

Assignee: cwitty

An extra print statement seems to have snuck in the `sage-doctest` script. Attached patch removes it.


---

Comment by burcin created at 2008-11-18 10:41:34

remove extra print statement from sage-doctest


---

Attachment

Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-18 21:02:37

Resolution: fixed


---

Comment by mabshoff created at 2008-11-18 21:02:37

Merged in Sage 3.2.rc2
