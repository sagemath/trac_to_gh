# Issue 604: Number field element memory leak

Issue created by migration from Trac.

Original creator: jbmohler

Original creation time: 2007-09-06 21:44:29

Assignee: was

The NTL structures in the number field are leaking.

The attached patch fixes this and some other matters with multiplication and division -- actually making them use NTL.


---

Attachment


---

Comment by was created at 2007-09-07 04:43:27

Resolution: fixed
