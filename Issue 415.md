# Issue 415: ZZ.random_element(0)

Issue created by migration from Trac.

Original creator: nbruin

Original creation time: 2007-08-09 19:53:56

Assignee: somebody

ZZ.random_element(0)

produces an uncaught FPE and hence crashes sage.


---

Comment by malb created at 2007-08-09 21:29:06

hg patch


---

Attachment

fixed in attached patch.


---

Comment by malb created at 2007-08-09 21:29:57

Resolution: fixed
