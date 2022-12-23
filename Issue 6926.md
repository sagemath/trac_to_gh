# Issue 6926: multiple bugs in plotting symbolic expressions

Issue created by migration from https://trac.sagemath.org/ticket/6926

Original creator: was

Original creation time: 2009-09-12 19:27:44

Assignee: was

CC:  rlm

This is a bug:

```
sage: plot(abs(exp(i*x)), xmin=1,xmax=2)
Traceback (most recent call last):
...
TypeError: float() argument must be a string or a number
```

The above should never happen, since the outputs of the function should be floats.   

Doing the obvious workaround yields another totally different bug!

```
sage: plot(lambda x: float(abs(exp(i*x))), xmin=1,xmax=2)
Traceback (most recent call last):
...
ZeroDivisionError: float division
```


The above ZeroDivisionError comes from trying incorrectly to scale the y-axis!

The following works, where we do two things explicitly, both of which should be completely automatic. 

```
sage: plot(lambda x: float(abs(exp(i*x))), xmin=1,xmax=2, ymin=0,ymax=1)
```


This was reported by Andi Walz on sage-support.


---

Comment by jason created at 2009-09-12 19:49:48

The second bug is fixed in the latest alpha of Sage.  It was fixed by moving the axes drawing to matplotlib by #5448.


---

Comment by jason created at 2010-01-17 10:32:52

The first bug is now fixed, I believe by #7614.  This ticket can be closed as fixed now.


---

Comment by jason created at 2010-01-17 10:32:52

Changing status from new to needs_review.


---

Comment by jason created at 2010-01-17 11:00:20

Resolution: fixed
