# Issue 9927: vectors from numpy arrays don't always work

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2010-09-17 02:00:19

Assignee: jason, was

CC:  rbeezer

From Victor Miller:


```

sage: import numpy
sage: a = numpy.array([1,2,3])
sage: v = vector(a)

Traceback (click to the left of this block for traceback)
...
TypeError: unsupported operand type(s) for ** or pow(): 'NoneType' and
'int'
```




---

Comment by jason created at 2010-09-17 02:07:23

Changing status from new to needs_review.


---

Attachment


---

Comment by jason created at 2010-09-17 02:08:51

The problem was that we were falling through to the last case (R**len(v)), but R was never prepared (i.e., was None) because the else statement was tied to the numpy check, not the dict check.


---

Comment by mhansen created at 2010-09-17 04:08:57

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-09-17 04:08:57

Looks good to me.


---

Comment by mpatel created at 2010-09-28 10:58:24

Resolution: fixed
