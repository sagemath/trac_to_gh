# Issue 8136: fix ref manual issues in linear_code.py

Issue created by migration from https://trac.sagemath.org/ticket/8136

Original creator: jhpalmieri

Original creation time: 2010-01-31 06:48:52

Assignee: wdj

CC:  spancratz

Building the reference manual in 4.3.2.alpha0 produces some warnings for the file linear_code.py, I think coming from #6486.  The attached patch fixes them.



---

Attachment


---

Comment by wdj created at 2010-01-31 15:04:52

I'll referee this, unless someone beats me to it. Thanks very much for fixing this up!


---

Comment by wdj created at 2010-01-31 17:52:51

Changing status from new to needs_review.


---

Comment by wdj created at 2010-01-31 17:53:29

Changing status from needs_review to positive_review.


---

Comment by wdj created at 2010-01-31 17:53:29

This applied fine to 4.3.2.a0 and pased sage -testall except for apparently unrelated failures on a mac 10.6.2.

Positive review.


---

Comment by mvngu created at 2010-02-02 00:27:13

Thank you very much for this, John! The total number of warnings resulting from building the HTML version of the reference manual is now 151.


---

Comment by mvngu created at 2010-02-02 00:27:13

Resolution: fixed
