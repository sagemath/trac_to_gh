# Issue 8544: Factor  polynomials over QQbar and AA

Issue created by migration from https://trac.sagemath.org/ticket/8544

Original creator: cremona

Original creation time: 2010-03-15 20:44:31

Assignee: AlexGhitza

CC:  zimmerma

Keywords: factor polynomial QQbar

QQbar and AA have root-finding but not polynomial factorization.

See the discussion at #8344, where a special case is dealt with and a possible solution outlined.


---

Attachment

Applies to 4.4.2


---

Comment by cremona created at 2010-05-26 20:02:36

Changing status from new to needs_review.


---

Comment by cremona created at 2010-05-26 20:02:36

The patch implements this, with tests.


---

Comment by zimmerma created at 2010-05-28 20:51:59

Changing status from needs_review to positive_review.


---

Comment by zimmerma created at 2010-05-28 20:51:59

John, this is nice work. All doctests pass, and I've played with the few examples you've added.
Paul


---

Comment by zimmerma created at 2010-05-28 20:52:33

Changing keywords from "factor polynomial QQbar" to "factor polynomial QQbar AA".


---

Comment by mhansen created at 2010-06-06 01:08:01

Resolution: fixed
