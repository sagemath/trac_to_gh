# Issue 7977: explain how to use the MATH block and automatic numbering with hash-dot

Issue created by migration from https://trac.sagemath.org/ticket/7977

Original creator: mvngu

Original creation time: 2010-01-18 14:18:22

Assignee: mvngu

See this [sage-combinat-devel](http://groups.google.com/group/sage-combinat-devel/browse_thread/thread/3a846ce7ba9fdb1f) thread:

```
Is there anywhere strict specification/possibilities for the docstring
of functions ? My only source was the devel guide but it does not
mention the ".. math:" ReST tag and contains two different conventions
for the OUTPUT part of the docstrings 
```



---

Comment by mvngu created at 2010-01-18 14:20:35

based on Sage 4.3.1.rc0


---

Attachment


---

Comment by mvngu created at 2010-01-18 14:21:11

Changing status from new to needs_review.


---

Comment by jhpalmieri created at 2010-01-18 16:46:18

apply on top of the other patch


---

Attachment

Looks good to me.  I've attached a tiny patch fixing two typos unrelated to mvngu's patch.


---

Comment by jhpalmieri created at 2010-01-18 16:48:14

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-01-19 00:07:50

Resolution: fixed
