# Issue 1148: valuation doesn't work for rational numbers

Issue created by migration from https://trac.sagemath.org/ticket/1148

Original creator: dmharvey

Original creation time: 2007-11-11 16:50:33

Assignee: somebody

It would be nice if `valuation(3/5, 5)` returned -1, but it does this:


```
sage: valuation(3/5, 5)
---------------------------------------------------------------------------
<type 'exceptions.ZeroDivisionError'>     Traceback (most recent call last)

/Users/david/series/<ipython console> in <module>()

/Users/david/sage-2.8.12/local/lib/python2.5/site-packages/sage/rings/arith.py in valuation(m, p)
    425     r=0
    426     power=p
--> 427     while m%power==0:
    428         r += 1
    429         power *= p

/Users/david/series/rational.pyx in sage.rings.rational.Rational.__mod__()

/Users/david/series/integer.pyx in sage.rings.integer.Integer.inverse_mod()

<type 'exceptions.ZeroDivisionError'>: Inverse does not exist.
```




---

Comment by dmharvey created at 2007-11-16 01:13:30

Changing status from new to assigned.


---

Comment by dmharvey created at 2007-11-16 01:13:30

Changing assignee from somebody to dmharvey.


---

Attachment

fixed it


---

Attachment


---

Comment by cwitty created at 2007-11-27 04:51:52

I tried the combination of 1148.hg and 1148-more.patch patch against 2.8.14.  The source code looks reasonable, and doctesting arith.py and rational.pyx (the two files touched by the change) both succeed.  (I did not try testall.)

In other words, looks good to me.


---

Comment by mabshoff created at 2007-12-01 18:51:29

Merged in 2.8.15.alpha1.


---

Comment by mabshoff created at 2007-12-01 18:51:29

Resolution: fixed
