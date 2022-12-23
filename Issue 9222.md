# Issue 9222: improve doctest coverage of databases/conway.py

Issue created by migration from https://trac.sagemath.org/ticket/9222

Original creator: AlexGhitza

Original creation time: 2010-06-12 07:09:15

Assignee: tbd

CC:  mvngu

Keywords: conway polynomial database

As of sage-4.4.3:


```
----------------------------------------------------------------------
conway.py
ERROR: Please add a `TestSuite(s).run()` doctest.
SCORE conway.py: 0% (0 of 7)

Missing documentation:
	 * _init(self):
	 * __repr__(self):
	 * polynomial(self, p, n):
	 * has_polynomial(self, p, n):
	 * primes(self):
	 * degrees(self, p):


Missing doctests:
	 * __init__(self, read_only=True):

----------------------------------------------------------------------
```



---

Comment by AlexGhitza created at 2010-06-12 08:11:50

Changing status from new to needs_review.


---

Comment by AlexGhitza created at 2010-06-12 08:11:50

After the patch:


```
ERROR: Please add a `TestSuite(s).run()` doctest.
SCORE conway.py: 85% (6 of 7)

Missing documentation:
	 * _init(self):
```


I'm not convinced a `TestSuite` test makes sense here (and I have tried to put one in and got a pickling-related error).  Also, I'm not sure what `_init(self)` is meant to be doing, so I'm leaving it alone for now.


---

Comment by davidloeffler created at 2010-06-14 10:32:43

Looks fine to me. Tests pass and the documentation builds OK. I agree that the _init method isn't something one can reasonably doctest!


---

Comment by davidloeffler created at 2010-06-14 10:32:43

Changing status from needs_review to positive_review.


---

Comment by ddrake created at 2010-07-22 02:31:27

Changing status from positive_review to needs_work.


---

Comment by ddrake created at 2010-07-22 02:31:27

Please include ticket numbers in the commit strings of your patches!


---

Comment by AlexGhitza created at 2010-07-22 03:12:03

Changing status from needs_work to positive_review.


---

Attachment

Done.


---

Comment by ddrake created at 2010-07-22 07:46:53

Resolution: fixed


---

Comment by ddrake created at 2010-07-22 07:46:53

Replying to [comment:6 AlexGhitza]:
> Done.

Thanks!
