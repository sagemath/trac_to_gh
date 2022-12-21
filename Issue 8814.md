# Issue 8814: Remove redundant checks for elliptic curve group structure

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2010-04-29 04:11:13

Assignee: cremona

CC:  cremona

These were doing nothing but slowing things down. 


---

Attachment

Before: 


```
sage: F.<a>=GF(101^3,'a')
sage: timeit("EllipticCurve([2*a^2 + 48*a + 27, 89*a^2 + 76*a + 24]).abelian_group()")
5 loops, best of 3: 1.37 s per loop
sage: timeit("EllipticCurve(GF(1009), [2, 1]).abelian_group()")
25 loops, best of 3: 21.1 ms per loop
```


After:


```
sage: F.<a>=GF(101^3,'a')
sage: timeit("EllipticCurve([2*a^2 + 48*a + 27, 89*a^2 + 76*a + 24]).abelian_group()")
5 loops, best of 3: 1.28 s per loop
sage: timeit("EllipticCurve(GF(1009), [2, 1]).abelian_group()")
5 loops, best of 3: 15.2 ms per loop
```


Of course, this is just low hanging fruit (I've gotten 40x or more speedup in EC point arithmetic alone via Cython) but every little bit helps.


---

Comment by robertwb created at 2010-04-29 04:15:35

Changing status from new to needs_review.


---

Comment by cremona created at 2010-04-29 07:42:50

Looks good, will test properly shortly...


---

Comment by cremona created at 2010-04-29 08:34:07

Applies to 4.4 and tests pass -- positive review!


---

Comment by cremona created at 2010-04-29 08:34:07

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-05-08 21:52:28

Resolution: fixed
