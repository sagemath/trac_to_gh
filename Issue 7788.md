# Issue 7788: followup patch to #5396

Issue created by migration from https://trac.sagemath.org/ticket/7788

Original creator: rishi

Original creation time: 2009-12-29 16:45:25

Assignee: was

CC:  craigcitro cremona ylchapuy robertwb

I am attaching  patchs which adds to the documentation that the derivatives loose about half the precision. There is additional documentation to guide how many dirichlet coefficients are needed, at least for computing near the real axis.


---

Attachment


---

Attachment


---

Comment by rishi created at 2009-12-29 18:32:00

Changing status from new to needs_review.


---

Comment by rishi created at 2009-12-29 18:32:00

I finally figured out how to combine several commits


---

Comment by cremona created at 2009-12-30 16:17:03

I'm giving this a positive review, though the formatting of the docstrings in  lcalc_Lfunction.pyx is not correct so that sphinx would choke on these.  But at the moment this file is not included in the reference manual.  So rather than delay the merging of the lcalc wrapping, it seems reasonable to pass this as is and create a new TODO ticket for that.


---

Comment by cremona created at 2009-12-30 16:17:03

Changing status from needs_review to positive_review.


---

Comment by cremona created at 2010-01-17 18:16:39

I don't think it's helpful to have this tagged as "positive review" when it depends on #5396 which is still being worked on.  So I am switching it back to "needs work" and it can go to "needs review" after #5396 is positively reviewed.


---

Comment by cremona created at 2010-01-17 18:16:39

Changing status from positive_review to needs_work.


---

Comment by rishi created at 2010-01-17 19:03:41

John,

I put a new spkg in [#5396](http://trac.sagemath.org/sage_trac/ticket/5396)

I tested it on my computer and on sage.math. I believe this should work.

Rishi


---

Comment by rishi created at 2010-07-11 02:49:35

This patch is superseded by #8623. This ticket can be discarded.


---

Comment by rishi created at 2010-07-11 02:49:35

Resolution: fixed


---

Comment by mhansen created at 2010-07-11 03:34:33

Resolution changed from fixed to duplicate
