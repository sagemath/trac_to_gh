# Issue 7370: fix FiniteFieldIterator

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2009-11-01 17:06:29

Assignee: AlexGhitza

CC:  ylchapuy

This should work


```
sage: K = GF(11^5,'a')
sage: K.list()
```



---

Attachment


---

Comment by ylchapuy created at 2009-11-01 18:12:40

I guess it was a needs review...


---

Comment by ylchapuy created at 2009-11-01 18:12:40

Changing status from new to needs_review.


---

Comment by ylchapuy created at 2009-11-01 18:13:19

Here is my positive review now


---

Comment by ylchapuy created at 2009-11-01 18:13:19

Changing status from needs_review to positive_review.


---

Comment by rbeezer created at 2009-11-02 00:07:14

Release manager:  please mark #7372 as obsolete when you merge this.


---

Comment by mhansen created at 2009-11-02 04:20:07

Resolution: fixed
