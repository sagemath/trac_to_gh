# Issue 8507: all flag ignored for GF(107)(0).sqrt

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2010-03-12 05:59:18

Assignee: AlexGhitza


```
            sage: GF(107)(0).sqrt(all=True)
            0
```



---

Attachment


---

Comment by robertwb created at 2010-03-12 06:01:06

Changing status from new to needs_review.


---

Comment by mhansen created at 2010-03-12 19:02:49

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-03-12 19:02:49

Looks good to me.


---

Comment by robertwb created at 2010-03-15 19:18:33

This was exposed by #8505.


---

Comment by mvngu created at 2010-03-17 06:44:00

Resolution: fixed
