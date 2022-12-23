# Issue 6430: Cython problem with hashing Laurent series elements over CDF

Issue created by migration from https://trac.sagemath.org/ticket/6430

Original creator: ncalexan

Original creation time: 2009-06-27 04:37:25

Assignee: malb

CC:  mhansen

Keywords: hash Laurent series


```
sage: hash(1/CDF[['t']].gen())
-2
sage: hash(1/CDF[['t']].gen()^2)
---------------------------------------------------------------------------
SystemError                               Traceback (most recent call last)

/Users/ncalexan/Documents/School/period_matrix/riemann_surface.py in <module>()

SystemError: error return without exception set
```



---

Comment by chapoton created at 2018-08-22 18:48:02

Changing status from new to needs_review.


---

Comment by chapoton created at 2018-08-22 18:48:02

works fine in 8.4.b1


---

Comment by tscrim created at 2018-08-22 22:22:50

Confirmed.


---

Comment by tscrim created at 2018-08-22 22:22:50

Changing status from needs_review to positive_review.


---

Comment by embray created at 2019-02-26 13:58:00

Presuming these are all correctly reviewed as either duplicate, invalid, or wontfix.


---

Comment by embray created at 2019-02-26 13:58:00

Resolution: invalid
