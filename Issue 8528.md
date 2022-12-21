# Issue 8528: type in an exception

Issue created by migration from Trac.

Original creator: ylchapuy

Original creation time: 2010-03-13 21:53:53

Assignee: burcin

here it is

```
sage: x.n()
Traceback (most recent call last)
...
TypeError: cannot evaluate symbolic expresssion numerically
                                         ^^^
```



---

Attachment

based on Sage 4.3.4.alpha1


---

Comment by mvngu created at 2010-03-14 00:40:08

Changing status from new to needs_review.


---

Comment by jhpalmieri created at 2010-03-14 05:49:49

Changing priority from trivial to minor.


---

Comment by jhpalmieri created at 2010-03-14 05:49:49

How about a doctest?  Here's a patch.  (Your patch gets a positive review.)


---

Comment by jhpalmieri created at 2010-03-14 05:50:15

apply on top of other patch


---

Attachment


---

Comment by mvngu created at 2010-03-14 06:23:43

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-03-14 22:39:31

Merged in this order:

 1. [trac_8528-typo.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8528/trac_8528-typo.patch)
 1. [trac_8528-doctests.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8528/trac_8528-doctests.patch)


---

Comment by mvngu created at 2010-03-14 22:39:31

Resolution: fixed
