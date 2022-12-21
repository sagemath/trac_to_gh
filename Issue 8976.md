# Issue 8976: squarefree_part() fails on Python types

Issue created by migration from Trac.

Original creator: leif

Original creation time: 2010-05-15 23:54:38

Assignee: jason

Keywords: squarefree_part()


```
sage: squarefree_part(216)
6
sage: squarefree_part(216r)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/home/leif/sage-4.4.1.rc0/devel/sage-8799/<ipython console> in <module>()

/home/leif/sage-4.4.1.rc0/local/lib/python2.6/site-packages/sage/misc/functional.pyc in squarefree_part(x)
   1478         pass
   1479     F = factor(x)
-> 1480     n = x.parent()(1)
   1481     for p, e in F:
   1482         if e%2 != 0:

AttributeError: 'int' object has no attribute 'parent'
```




---

Comment by leif created at 2010-05-16 00:00:01

Changing status from new to needs_info.


---

Comment by leif created at 2010-05-16 00:00:01

This is easy to fix, but I'm not sure if one should simply replace

```
n = x.parent()(1)
```

by

```
n = parent(x)(1)
```

or e.g. test for `isinstance(x,(int,long,float))` instead.


---

Comment by leif created at 2010-05-16 00:12:08

Btw, wouldn't it be convenient to have `squarefree_prime_divisors()` (i.e. a generator/list of just those prime factors with exponent=1), too?

(Currently, there's only `squarefree_divisors()`.)


---

Comment by leif created at 2010-05-16 01:26:17

This patch implements my first suggestion. Based on 4.4.2.rc0.


---

Comment by leif created at 2010-05-16 01:27:55

Changing status from needs_info to needs_review.


---

Attachment


---

Comment by leif created at 2010-05-26 16:42:35

Changing keywords from "squarefree_part()" to "squarefree_part(), beginner".


---

Comment by rlm created at 2010-06-17 21:41:51

Changing status from needs_review to positive_review.


---

Comment by ddrake created at 2010-07-22 07:40:41

Resolution: fixed
