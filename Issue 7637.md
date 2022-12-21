# Issue 7637: Default dictionary in MixedIntegerLinearProgram

Issue created by migration from Trac.

Original creator: ncohen

Original creation time: 2009-12-09 12:27:25

Assignee: jkantor

CC:  malb

Martin Albrecht requested this functionality for his code, and it would also simplify mine. For short linear programs, of when some global variables do not require the creation of a new dictionary of variables ( from which only one field would be used ), this trick is good enough !

Nathann


---

Comment by malb created at 2009-12-09 15:01:43

* `try: foo except AttributeError:` seems to be favoured in the Python community over `hasattr`. It is also faster if the attribute does in fact exist.
 * Why do you call `__getitem__()` instead of using the normal syntax `[x]`?


---

Comment by ncohen created at 2009-12-09 17:42:01

Done !


---

Comment by ncohen created at 2009-12-09 17:42:01

Changing status from new to needs_review.


---

Attachment


---

Comment by malb created at 2009-12-09 20:55:55

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-12-14 15:51:31

Resolution: fixed
