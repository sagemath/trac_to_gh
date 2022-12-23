# Issue 497: add minpoly command to finite field elements

Issue created by migration from https://trac.sagemath.org/ticket/497

Original creator: was

Original creation time: 2007-08-27 22:15:51

Assignee: pablo

Make it so a.minpoly() works when a is in a finite field.


---

Comment by pdenapo created at 2007-09-01 21:02:06

Changing assignee from pablo to pdenapo.


---

Comment by pdenapo created at 2007-09-01 21:02:06

Changing status from new to assigned.


---

Attachment

Here is an updated version of my patch. It also adds a default variable name 'x' to charpoly.


---

Comment by was created at 2007-09-02 05:49:22

Resolution: fixed
