# Issue 8716: Modular forms of level GammaH

Issue created by migration from Trac.

Original creator: davidloeffler

Original creation time: 2010-04-19 16:53:25

Assignee: craigcitro

We have code for modular symbols on GammaH groups but the code for modular forms is little more than stubs. Here's a patch that should fix that.


---

Attachment

patch against 4.4.alpha0


---

Comment by davidloeffler created at 2010-04-19 20:44:11

Changing status from new to needs_review.


---

Comment by rlm created at 2010-12-06 10:46:19

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-12-06 10:46:19

This patch applies fine to sage-4.6.1.alpha2 and passes all long doctests. The code looks good as well, and I think this should be merged.


---

Comment by jdemeyer created at 2010-12-06 13:15:37

Tested also against sage-4.6.1.alpha3 on sage.math.washington.edu


---

Comment by davidloeffler created at 2010-12-12 14:34:24

apply over previous patch


---

Attachment

Oops, my bad: this patch causes an error when building the documentation, due to a silly latex mistake in one of the docstrings. Here's a tiny patch which fixes that. Robert, would you mind taking a quick look to OK it?


---

Comment by davidloeffler created at 2010-12-12 14:36:00

Changing status from positive_review to needs_work.


---

Comment by davidloeffler created at 2010-12-12 14:36:07

Changing status from needs_work to needs_review.


---

Comment by rlm created at 2010-12-13 11:28:42

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-12-13 11:28:42

Oops!


---

Comment by davidloeffler created at 2010-12-31 14:29:20


```
Apply trac_8716-gamma_h_modforms.patch, trac_8716-docfix.patch
```


(FAO PatchBot)


---

Comment by jdemeyer created at 2011-01-25 08:14:18

Resolution: fixed
