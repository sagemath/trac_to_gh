# Issue 7521: typo in optional doctest for R interface

Issue created by migration from Trac.

Original creator: kcrisman

Original creation time: 2009-11-24 01:00:30

Assignee: tbd

CC:  jason mhansen


```
sage: r.install_package('Hmisc')       #optional 
```

makes no sense, because the command is install_packages().


---

Attachment

Based on 4.2.1


---

Comment by kcrisman created at 2009-12-14 15:49:20

Changing status from new to needs_review.


---

Comment by kcrisman created at 2009-12-14 15:49:20

This should apply ok to newer versions, though.  Please note that Hmisc has been replaced with a package which depends only on R itself, in addition to fixing the doctest. 

This should be VERY easy to review.


---

Comment by mhansen created at 2009-12-14 15:51:05

Something looks weird with the character encoding in the patch.


---

Comment by kcrisman created at 2009-12-14 16:28:35

You're right.  I'm not sure how to fix that; what the original looks like is in the attached file.  I don't know how to deal with that, since I can't actually create those kind of quotes on my computer.  Would it be enough to just replace the weird stuff in line 385 with `aaMI'?


---

Attachment


---

Comment by kcrisman created at 2010-01-25 19:20:00

As far as I can tell, we can also now remove the warnings for Mac in this function. New patch coming up - hopefully without weird character issues.


---

Comment by kcrisman created at 2010-01-25 19:20:00

Changing status from needs_review to needs_work.


---

Attachment

Based on 4.3.1, sort of depends on spkg in #6532


---

Comment by kcrisman created at 2010-01-25 19:37:28

Changing status from needs_work to needs_review.


---

Comment by mvngu created at 2010-01-25 23:51:44

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-01-25 23:51:44

Looks good to me.


---

Comment by mvngu created at 2010-01-25 23:52:39

Resolution: fixed


---

Comment by mvngu created at 2010-01-25 23:52:39

Merged [trac_7521-R-typo-take2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7521/trac_7521-R-typo-take2.patch).
