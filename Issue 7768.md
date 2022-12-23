# Issue 7768: PDF version of reference manual fails to build in Sage 4.3

Issue created by migration from https://trac.sagemath.org/ticket/7768

Original creator: mvngu

Original creation time: 2009-12-26 13:33:58

Assignee: mvngu

Keywords: reference manual

With Sage 4.3, building the PDF version of the reference manual hangs at the line:

```
! Missing $ inserted.
<inserted text> 
                $
l.164972 $\mbox{min_bound} 
                           \leq \mbox{linear_function} \leq \mbox{max_bound}$
```

This is due to the docstring of the method `constraints()` in `sage/numerical/mip.pyx`. The attached patch should fix the docstring formatting and allow the PDF version of the reference manual to build successfully.


---

Attachment

based on Sage 4.3


---

Comment by mvngu created at 2009-12-26 13:38:55

Changing status from new to needs_review.


---

Comment by jhpalmieri created at 2009-12-26 16:17:01

Without the patch, the PDF build crashes.  With the patch it succeeds.  Both the PDF and html versions look good with the patch.


---

Comment by jhpalmieri created at 2009-12-26 16:17:01

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-01-03 21:24:04

Resolution: fixed
