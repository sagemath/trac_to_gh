# Issue 8491: incorret latex produced for some symbolic expressions

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2010-03-10 17:23:44

Assignee: AlexGhitza

CC:  robert.marik


```
sage: f = 6.5/x
sage: latex(f)
\frac{1}{x}
```



---

Comment by mhansen created at 2010-03-10 17:24:08

Changing priority from major to blocker.


---

Comment by mhansen created at 2010-03-10 17:24:08

Changing assignee from AlexGhitza to burcin.


---

Comment by mhansen created at 2010-03-10 17:24:08

Changing component from algebra to symbolics.


---

Comment by burcin created at 2010-03-10 22:05:10

Changing status from new to needs_review.


---

Attachment


---

Comment by robert.marik created at 2010-03-11 12:37:15

Changing status from needs_review to positive_review.


---

Comment by robert.marik created at 2010-03-11 12:37:15

Works for me, seems good, doctests passed, solves the problem. 

Positive review


---

Comment by mvngu created at 2010-03-12 04:52:17

Resolution: fixed
