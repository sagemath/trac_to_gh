# Issue 7479: sage fails to integrate identity

Issue created by migration from Trac.

Original creator: ggrafendorfer

Original creation time: 2009-11-17 11:40:01

Assignee: burcin

32-bit Intel core duo, debian lenny, sage-4.2.1:


georg`@`HILBERT:~$ sage
----------------------------------------------------------------------
| Sage Version 4.2.1, Release Date: 009-11-14                      |
----------------------------------------------------------------------
sage: f(x)=x
| Type notebook() for the GUI, and license() for information.        |
sage: integrate(f,x,0,1)

sage0

sage: integrate(f,x,0,1)

sage7

sage: integrate(f,x,0,1)

sage12

sage: integrate(f,x,0,1)

sage17

sage: integrate(f,x,0,1).n()

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/georg/<ipython console> in <module>()

/mnt/data/georg/.system/bin/sage/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.n (sage/symbolic/expression.cpp:15863)()

/mnt/data/georg/.system/bin/sage/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.pyobject (sage/symbolic/expression.cpp:2701)()

TypeError: self must be a numeric expression



---

Attachment


---

Comment by mhansen created at 2009-11-17 12:19:06

Changing status from new to needs_review.


---

Comment by kcrisman created at 2009-11-17 20:22:24

Positive review except there is no doctest to indicate that one can now integrate f(x)=x!  It works:

```
sage: integrate(f,x,0,1)
1/2
```

So maybe this should be put in somewhere in sage/calculus/calculus.py in tests, or wherever you think is most appropriate.


---

Comment by kcrisman created at 2009-11-17 20:22:24

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-11-18 04:22:23

On the other hand, there is a doctest for the cause of the problem.


---

Comment by kcrisman created at 2009-11-18 14:02:15

Based on 4.2.1, apply only this patch


---

Attachment

I still feel safer putting it in there (for instance, if we switch to using Maxima as an ECL library this sort of thing could also break but for a different reason), so please apply this patch with the extra doctest.


---

Comment by mhansen created at 2009-11-19 10:18:55

Resolution: fixed
