# Issue 9355: 100% coverage for quadratic_forms

Issue created by migration from https://trac.sagemath.org/ticket/9355

Original creator: annahaensch

Original creation time: 2010-06-27 21:48:38

Assignee: mvngu




---

Attachment


---

Comment by annahaensch created at 2010-06-27 21:51:58

Changing status from new to needs_review.


---

Comment by davidloeffler created at 2010-06-28 17:46:25

Changing status from needs_review to needs_work.


---

Comment by davidloeffler created at 2010-06-28 17:46:25

I tried this, and it is fine as far as it goes but `sage -coverage` still grumbles about the lack of a `TestSuite.run()` doctest in genera/genus.py. In fact the two classes in that file don't derive from SageObject (although they probably should), so the TestSuite machinery doesn't work on them; but it would be good to have loads/dumps doctests for these classes. With those added I would be happy for this to go in.

(A much bigger step forward would be adding the quadratic forms code to the reference manual, but that's a separate issue.)


---

Attachment

Apply on top of trac_9355.patch


---

Comment by annahaensch created at 2010-06-29 06:26:35

Changing status from needs_work to needs_review.


---

Comment by davidloeffler created at 2010-06-29 07:55:27

Changing status from needs_review to positive_review.


---

Comment by davidloeffler created at 2010-06-29 07:55:27

OK, that looks fine.


---

Comment by davidloeffler created at 2010-06-29 07:55:54

Changing keywords from "" to "quadratic forms".


---

Comment by mpatel created at 2010-07-21 10:07:30

Resolution: fixed
