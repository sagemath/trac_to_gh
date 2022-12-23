# Issue 9178: attrcall: add missing hash function

Issue created by migration from https://trac.sagemath.org/ticket/9178

Original creator: nthiery

Original creation time: 2010-06-07 15:23:23

Assignee: nthiery

CC:  sage-combinat mhansen

Keywords: attrcall, hash

This patch implements `attrcall.__hash__`. Its absence caused the
following misbehavior:


```
    sage: x = attrcall("blah")
    sage: y = attrcall("blah")
    sage: x == y
    True
    sage: hash(x) == hash(y)
    False
```


which in particular broke unique representation and pickling of some
crystals (see #8911).



---

Attachment


---

Comment by nthiery created at 2010-06-07 15:26:00

Changing status from new to needs_review.


---

Comment by mhansen created at 2010-06-07 15:28:39

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-06-07 15:28:39

Looks good to me.


---

Comment by mhansen created at 2010-06-09 02:31:14

Resolution: fixed
