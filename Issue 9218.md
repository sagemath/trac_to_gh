# Issue 9218: add a finance chapter to the sage reference manual

Issue created by migration from https://trac.sagemath.org/ticket/9218

Original creator: was

Original creation time: 2010-06-11 18:19:19

Assignee: mvngu




---

Attachment

The first patch adds the documentation.  However the docstrings are all pre-rest, so look like crap.  E.g., see 

    http://sage.math.washington.edu/home/wstein/build/sage-4.4.4.alpha0/devel/sage/doc/output/html/en/reference/finance.html

or just apply the patch, then do `sage -docbuild reference html` and look at `output/html/en/reference/` for yourself.

A second patch will fix all the formatting.


---

Attachment


---

Comment by mvngu created at 2010-06-12 22:00:26

Replying to [comment:1 was]:
> The first patch adds the documentation.  However the docstrings are all pre-rest, so look like crap. 

Not any more.




> A second patch will fix all the formatting. 

See my reviewer patch.


---

Comment by mvngu created at 2010-06-12 22:00:26

Changing status from new to needs_review.


---

Attachment

Apply this last.


---

Comment by kcrisman created at 2010-06-18 18:37:41

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2010-06-18 18:37:41

Looks good!  Apply in the order `finance_doc`, `reviewer`, and `typo`.  Also added Minh as an author, considering his patch is two orders of magnitude bigger than the original one.


---

Comment by mpatel created at 2010-07-21 09:56:17

Resolution: fixed
