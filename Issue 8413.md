# Issue 8413: Add "Unknown" truth value

Issue created by migration from https://trac.sagemath.org/ticket/8413

Original creator: hivert

Original creation time: 2010-03-01 23:05:49

Assignee: hivert

CC:  robertwb

Keywords: Unknown Boolean

As discussed on [sage-devel](http://groups.google.com/group/sage-devel/t/5d9c32390ffe3c96) it could be good to have an "Unkown" value in sage which semantic is a truth value. Here are the intended truth table:

```
      and             or
    F  U  T         F  U  T
 F [F, F, F]     F [F, U, T]
 U [F, U, U]     U [U, U, T]
 T [F, U, T]     T [T, T, T]
```

Unfortunately, without [PEP 335](http://www.python.org/dev/peps/pep-0335/), there is no way to achieve this with python's "and" and "or".


---

Attachment


---

Comment by hivert created at 2010-03-02 11:10:21

Changing status from new to needs_review.


---

Comment by nthiery created at 2010-04-16 21:41:13

For the record: all test pass.


---

Comment by robertwb created at 2010-06-22 23:50:17

Changing status from needs_review to positive_review.


---

Comment by robertwb created at 2010-06-22 23:50:17

Looks good.


---

Comment by ddrake created at 2010-07-22 07:35:47

Resolution: fixed
