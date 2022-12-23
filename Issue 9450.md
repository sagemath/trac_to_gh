# Issue 9450: Implement a factor() function for NumberFieldElement

Issue created by migration from https://trac.sagemath.org/ticket/9450

Original creator: jdemeyer

Original creation time: 2010-07-07 21:06:36

Assignee: davidloeffler

The attached patch implements a factor() function for number field elements.


---

Attachment


---

Comment by jdemeyer created at 2010-07-07 21:21:49

Changing status from new to needs_review.


---

Attachment

Apply after previous patch


---

Comment by cremona created at 2010-07-08 12:29:20

The patch applies and works fine.  I have changed the docstring a little, added a test for factoring 0 and simplified the code in a couple of places.  I also added an example in sage/rings/arith.py since the generic factor() function now works on number field elements!

Since I changed quite a lot, I have left this as "needs review".


---

Comment by mhansen created at 2010-07-11 01:15:24

John's changes look good to me.


---

Comment by mhansen created at 2010-07-11 01:15:24

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-07-20 07:53:15

Resolution: fixed
