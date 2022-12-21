# Issue 8673: No KeyErrror raised when it should for FiniteWord_callable

Issue created by migration from Trac.

Original creator: slabbe

Original creation time: 2010-04-11 14:00:57

Assignee: slabbe

CC:  abmasse


```
Le 10-02-23, Paul Zimmermann a écrit :

sage: def f(n):
   return n^2

sage: w = Word(f,length=23)

sage: w[24]
576

Paul
```



---

Attachment


---

Comment by slabbe created at 2011-02-18 19:57:43

Changing status from new to needs_review.


---

Comment by abmasse created at 2011-02-18 20:38:53

Changing status from needs_review to positive_review.


---

Comment by abmasse created at 2011-02-18 20:38:53

Pretty straight-forward. All tests pass! Positive review.


---

Comment by jdemeyer created at 2011-03-25 12:31:06

Resolution: fixed
