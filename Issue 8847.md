# Issue 8847: pynac.pyx use double precision special functions instead of long double

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2010-05-03 12:18:24

Assignee: tbd

Many systems such as cygwin don't have the long double version.  Plus, they are being applied to floats/doubles so the extra precision doesn't buy much.


---

Attachment


---

Comment by mhansen created at 2010-05-03 13:22:32

Changing status from new to needs_review.


---

Comment by burcin created at 2010-05-05 02:26:30

Changing status from needs_review to needs_work.


---

Comment by burcin created at 2010-05-05 02:26:30

This gives the following doctest failures on my 64-bit T9300 Core 2 Duo laptop, with `gcc (Gentoo 4.3.4 p1.0, pie-10.1.5) 4.3.4` and glibc-2.10.1. I have no idea what is relevant, so I give some random information. :)


```
**********************************************************************
File "/home/burcin/sage/sage-4.4.1.alpha2-patched/devel/sage-t/sage/functions/other.py", line 428:
    sage: gamma1(float(6))
Expected:
    120.0
Got:
    119.99999999999997
**********************************************************************
```


```
**********************************************************************
File "/home/burcin/sage/sage-4.4.1.alpha2-patched/devel/sage-t/sage/symbolic/expression.pyx", line 5318:
    sage: SR(10.0r).gamma()
Expected:
    362880.0
Got:
    362880.00000000047
**********************************************************************
```



---

Comment by burcin created at 2010-05-05 02:26:30

Changing keywords from "" to "pynac".


---

Comment by mhansen created at 2010-05-05 02:29:49

It'd be nice if we could just do like an ifdef in Cython.


---

Comment by burcin created at 2010-05-05 02:33:45

We can put the ifdef in `c_lib/include/ginac_wrapper.h` to define the long double versions on Cygwin. Initially, they could just wrap the double precision functions.


---

Comment by was created at 2010-05-26 01:39:58

Changing status from needs_work to needs_review.


---

Comment by was created at 2010-05-26 01:39:58

I just did something at runtime using a bint.  It's very simple, and will have a very minimal performance hit.


---

Comment by was created at 2010-05-26 01:41:03

apply only this (not the one below)


---

Attachment


---

Attachment


---

Comment by was created at 2010-05-26 02:52:08

Resolution: fixed
