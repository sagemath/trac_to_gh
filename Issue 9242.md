# Issue 9242: Add docstrings and tests for sage/rings/ideal_monoid.py

Issue created by migration from https://trac.sagemath.org/ticket/9242

Original creator: davidloeffler

Original creation time: 2010-06-15 08:51:44

Assignee: mvngu

Keywords: docstring, doctest, ideals


```
----------------------------------------------------------------------
ideal_monoid.py
ERROR: Please add a `TestSuite(s).run()` doctest.
SCORE ideal_monoid.py: 0% (0 of 6)

Missing documentation:
         * IdealMonoid(R):
         * __init__(self, R):
         * _repr_(self):
         * ring(self):
         * __call__(self, x):
         * _coerce_impl(self, x):

----------------------------------------------------------------------
```



---

Comment by davidloeffler created at 2010-06-15 09:18:18

Here's a patch which gets coverage up to 100%, but one `TestSuite` test fails.


---

Comment by davidloeffler created at 2010-06-15 09:18:18

Changing status from new to needs_review.


---

Comment by AlexGhitza created at 2010-06-15 10:22:21

Changing status from needs_review to needs_work.


---

Comment by AlexGhitza created at 2010-06-15 10:22:21

There is a doctest failure in `structure/coerce.pyx` which is caused by this patch:


```
sage -t -long "devel/sage/sage/structure/coerce.pyx"        
**********************************************************************
File "/mnt/usb1/scratch/ghitza/sage-4.4.4.alpha0-boxen.math.washington.edu-x86_64-Linux/devel/sage/sage/structure/coerce.pyx", line 357:
    sage: cm.exception_stack()
Expected:
    [(<class 'sage.structure.coerce_exceptions.CoercionException'>, CoercionException("BUG: the base_extend method must be defined for 'Monoid of ideals of Integer Ring' (class '<class 'sage.rings.ideal_monoid.IdealMonoid_c'>')",), <traceback object at ...>), (<type 'exceptions.TypeError'>,  TypeError("no common canonical parent for objects with parents: 'Rational Field' and 'Finite Field of size 3'",),  <traceback object at ...>)]
Got:
    [(<class 'sage.structure.coerce_exceptions.CoercionException'>, CoercionException(AttributeError("'IdealMonoid_c_with_category' object has no attribute 'base_extend'",),), <traceback object at 0x1049ea8>), (<type 'exceptions.TypeError'>, TypeError("no common canonical parent for objects with parents: 'Rational Field' and 'Finite Field of size 3'",), <traceback object at 0x1049c20>)]
```


I don't know what's going on.


---

Comment by davidloeffler created at 2010-06-15 10:42:20

patch against 4.4.4.alpha0


---

Comment by davidloeffler created at 2010-06-15 10:44:10

Changing status from needs_work to needs_review.


---

Attachment

It's harmess (if you look, the exception stack is actually identical, just with slightly different string representation for some of the classes). I've uploaded a new patch.


---

Comment by AlexGhitza created at 2010-06-15 11:36:03

Changing status from needs_review to positive_review.


---

Comment by AlexGhitza created at 2010-06-15 11:36:03

Great.  I'm happy with this; the category fix can be on a new ticket.


---

Comment by was created at 2010-06-22 04:36:54

Milestone sage-4.4.5 deleted


---

Comment by ddrake created at 2010-07-22 07:49:52

Resolution: fixed
