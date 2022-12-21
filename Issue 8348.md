# Issue 8348: find_root only works in fixed (double) precision

Issue created by migration from Trac.

Original creator: zimmerma

Original creation time: 2010-02-24 16:23:17

Assignee: AlexGhitza

CC:  was

How can one approximate the root of an equation in arbitrary
precision? For example I want the root of log(x+2) = x to
50 digits of precision:

```
sage: (log(x+2)-x).find_root(1,2)
1.1461932206205643
sage: (log(x+2)-x).find_root(1,2,prec=150)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/users/caramel/zimmerma/try/<ipython console> in <module>()

/usr/local/sage-core2/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.find_root (sage/symbolic/expression.cpp:24383)()

TypeError: find_root() got an unexpected keyword argument 'prec'
```



---

Comment by jason created at 2010-03-17 05:06:30

This is about adding capability not currently present, so should be an enhancement.


---

Comment by jason created at 2010-03-17 05:06:30

Changing type from defect to enhancement.


---

Comment by zimmerma created at 2010-03-17 07:37:23

> This is about adding capability not currently present, so should be an enhancement. 

I do not agree. The documentation does not say that `find_root` only works in double precision,
thus this is a defect (at least of the documentation). Do you agree with that?


---

Comment by jason created at 2010-03-17 16:25:20

The docs for find_root don't imply that it uses arbitrary precision to me, so I agree it's an omission, but not a bug (i.e., it doesn't claim one thing and do another).  The only mention of precision in the docs (in the xtol and rtol parameters) implies that things work with double precision.

But this is a minor point.  I was trying to clean up the large number of tickets that are classified as "bugs" (which to me means things that Sage claims should work, but don't).

In this case, the error returned indicates that find_root knows nothing about a prec argument, which is appropriate.

I've switched it back so we don't waste any more time fretting about how to classify this ticket.


---

Comment by jason created at 2010-03-17 16:25:20

Changing type from enhancement to defect.


---

Comment by zimmerma created at 2013-08-24 07:58:12

Changing status from new to needs_review.


---

Comment by zimmerma created at 2013-08-24 07:58:12

Changing type from defect to enhancement.


---

Attachment

the attached patch (produced against Sage 5.9) adds documentation to `find_root`.
Note: I found out that `find_root` is duplicated in `numerical/optimize.py` and in `symbolic/expression.pyx`, which is unfortunate.

Paul


---

Comment by mmezzarobba created at 2014-01-29 07:18:09

LGTM.

Replying to [comment:6 zimmerma]:
> Note: I found out that `find_root` is duplicated in `numerical/optimize.py` and in `symbolic/expression.pyx`, which is unfortunate.

Only (part of) the documentation is duplicated; one of the function is a wrapper for the other. It is unfortunate indeed, but that's a problem that occurs everywhere in Sage, so I don't think it really makes sense to open a ticket for that particular instance.
----
New commits:


---

Comment by mmezzarobba created at 2014-01-29 07:18:09

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-02-01 15:17:03

Resolution: fixed
