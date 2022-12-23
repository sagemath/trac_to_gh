# Issue 9701: NumberFieldElement should have a conversion to float

Issue created by migration from https://trac.sagemath.org/ticket/9701

Original creator: cwitty

Original creation time: 2010-08-07 00:37:10

Assignee: davidloeffler

The missing conversion from `NumberFieldElement` to float is the cause of this strangeness:


```
sage: RR(I*I)
-1.00000000000000
sage: float(I*I)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/cwitty/svn-ironpython/IronPython_Main/<ipython console> in <module>()

/home/cwitty/sage-4.5.2.alpha1/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.__float__ (sage/symbolic/expression.cpp:5205)()

TypeError: unable to simplify to float approximation
```


(I'll have a patch posted for this in a few minutes.)


---

Attachment

The attached patch adds the missing method and adds a doctest in symbolics where I originally saw the problem.

All doctests pass.


---

Comment by cwitty created at 2010-08-07 01:17:34

Changing status from new to needs_review.


---

Comment by davidloeffler created at 2010-09-23 10:04:45

Looks good to me.


---

Comment by davidloeffler created at 2010-09-23 10:04:45

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-09-29 04:23:21

Resolution: fixed
