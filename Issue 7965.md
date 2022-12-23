# Issue 7965: quo_rem attribute error (probably easy to fix?)

Issue created by migration from https://trac.sagemath.org/ticket/7965

Original creator: was

Original creation time: 2010-01-17 10:37:46

Assignee: AlexGhitza

CC:  mjo


```
sage: 5.quo_rem(2/3)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/virtual/scratch/wstein/build/sage-4.3.1.rc0/<ipython console> in <module>()

/virtual/scratch/wstein/build/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sage/rings/integer.so in sage.rings.integer.Integer.quo_rem (sage/rings/integer.c:16710)()

/virtual/scratch/wstein/build/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.FieldElement.quo_rem (sage/structure/element.c:15715)()

AttributeError: 'sage.rings.rational.Rational' object has no attribute '_parent'
```



---

Comment by mjo created at 2012-01-13 19:00:29

Changing status from new to needs_review.


---

Comment by mjo created at 2012-01-13 19:00:29

This looks fixed, at least for the rationals. I've added a doctest and changed the description of the `other` input which was weird anyway.


---

Comment by mstreng created at 2012-01-16 19:09:46

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-01-17 16:00:53

Rebased to #10596, added one test.


---

Comment by jdemeyer created at 2012-01-17 16:00:53

Changing status from positive_review to needs_work.


---

Attachment

Add a doctest with the example from the description.


---

Comment by jdemeyer created at 2012-01-17 16:01:10

Changing status from needs_work to needs_review.


---

Comment by mjo created at 2012-01-17 18:25:32

The ticket number is missing from the commit message, but I suppose that's how you want it? The new patch applies and tests cleanly.


---

Comment by mjo created at 2012-01-17 18:25:32

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-01-18 08:14:36

Resolution: fixed
