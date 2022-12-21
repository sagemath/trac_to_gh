# Issue 9313: delete padic_height.py

Issue created by migration from Trac.

Original creator: wuthrich

Original creation time: 2010-06-22 17:11:36

Assignee: cremona

CC:  wstein

This file, implementing an interface for the p-adic height computation in MAGMA, is deprecated for a long time and no one is using it any more. This should be deleted now.


---

Comment by davidloeffler created at 2010-06-29 09:16:01

patch against 4.4.4


---

Comment by davidloeffler created at 2010-06-29 09:16:25

Changing status from new to needs_review.


---

Attachment

Here's a patch.


---

Comment by weigandt created at 2010-06-30 03:25:14

Changing status from needs_review to positive_review.


---

Comment by weigandt created at 2010-06-30 03:25:14

Looks fine. Doctests check out.


---

Comment by wuthrich created at 2010-06-30 04:02:36

Agree (though I have not run the tests). Moreover I can confirm that the author, William Stein, is happy that this is deleted.

Thanks, Jamie and David.


---

Comment by mpatel created at 2010-07-20 07:18:07

Resolution: fixed
