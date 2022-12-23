# Issue 1805: improve doctest coverage for structure/factorization.py

Issue created by migration from https://trac.sagemath.org/ticket/1805

Original creator: was

Original creation time: 2008-01-17 19:58:11

Assignee: failure




---

Comment by was created at 2008-01-17 20:00:24

Before:

```
sage@modular:~/d/sage/sage/structure$ sage -coverage factorization.py 
----------------------------------------------------------------------
factorization.py
SCORE factorization.py: 28% (6 of 21)

Missing documentation:
	 * __init__(self, x, unit=None, cr=False, sort=True)
	 * _set_cr(self, cr)
	 * sort(self)
	 * _cmp(f,g)
	 * _cmp(f,g)
	 * _cmp(f,g)
	 * __reduce__(self)
	 * _cr(self)
	 * _repr_(self)
	 * _latex_(self)
	 * __pow__(self, n)
	 * __invert__(self)
	 * Factorization_deduce_unit(x, mul)


Missing doctests:
	 * unit_part(self)
	 * expand(self)

```


After:

```
teragon:structure was$ sage -coverage factorization.py
----------------------------------------------------------------------
factorization.py
SCORE factorization.py: 100% (22 of 22)
----------------------------------------------------------------------
```


and I fixed numerous conceptual bugs/mistakes in that file.


---

Comment by was created at 2008-01-17 20:00:24

Changing assignee from failure to was.


---

Comment by was created at 2008-01-17 20:00:24

Changing status from new to assigned.


---

Attachment

This is a preliminary patch.  I'm now doctesting all of sage-2.10 with this patch applied to see what else is broke.  I'll post another patch that fixes the problems later.


---

Attachment

this part 2 fixes some additional issues, typos, etc., I saw when proofreading my patch.


---

Comment by ncalexan created at 2008-01-20 06:58:23

Changing status from assigned to new.


---

Comment by ncalexan created at 2008-01-20 06:58:23

Changing assignee from was to ncalexan.


---

Comment by ncalexan created at 2008-01-20 06:58:23

I fixed 1804 not knowing that 1805 did a lot of the same work.  Damn!  They should both be applied but of course they need to be merged.  I'll try to do it tomorrow.


---

Comment by mabshoff created at 2008-02-18 14:25:44

Nick, can you give this another review?

Cheers,

Michael


---

Comment by was created at 2008-02-18 23:58:33

Yes, please review it.  My patch fixes a number of subtle serious bugs involving pickling factorizations, which could cause people problems.


---

Comment by gfurnish created at 2008-03-01 22:02:20

These patches don't import cleanly against current.  They also need the bug doctest removed.


---

Comment by was created at 2008-03-02 00:29:18

I've attached a brand new rebased patch which also fixes a critical bug in factorization (!) which may expose a bug in totallyrealfield, by the way.

I also changed factorizations to be immutable, as suggested by the referee, and they now no longer derive from list, so that __cmp__ works correctly.


---

Comment by was created at 2008-03-02 00:30:09

new rebased version


---

Attachment


---

Attachment


---

Comment by gfurnish created at 2008-03-02 06:35:43

sage -t  devel/sage-patch1805/build/sage/structure/factorization.py**********************************************************************
File "factorization.py", line 602:
    sage: F = factor(-2*x^2 - 1); F
Expected:
    (-2.0) * (1.0*x^2 + 0.5) * (1.0*x^2 + 1.11022302463e-16*x + 0.5)
Got:
    (-2.0) * (1.0*x^2 - 2.22044604925e-16*x + 0.5) * (1.0*x^2 + 0.5)
**********************************************************************

Positive review pending fix.


---

Comment by gfurnish created at 2008-03-02 06:36:38


```
sage -t  devel/sage-patch1805/build/sage/structure/factorization.py
**********************************************************************
File "factorization.py", line 602:
    sage: F = factor(-2*x^2 - 1); F
Expected:
    (-2.0) * (1.0*x^2 + 0.5) * (1.0*x^2 + 1.11022302463e-16*x + 0.5)
Got:
    (-2.0) * (1.0*x^2 - 2.22044604925e-16*x + 0.5) * (1.0*x^2 + 0.5)
**********************************************************************
```



---

Comment by gfurnish created at 2008-03-02 06:36:53

[[[
sage -t  devel/sage-patch1805/build/sage/structure/factorization.py
**********************************************************************
File "factorization.py", line 602:
    sage: F = factor(-2*x^2 - 1); F
Expected:
    (-2.0) * (1.0*x^2 + 0.5) * (1.0*x^2 + 1.11022302463e-16*x + 0.5)
Got:
    (-2.0) * (1.0*x^2 - 2.22044604925e-16*x + 0.5) * (1.0*x^2 + 0.5)
**********************************************************************
]]]


---

Comment by gfurnish created at 2008-03-02 06:37:35


```
sage -t  devel/sage-patch1805/build/sage/structure/factorization.py**********************************************************************
File "factorization.py", line 602:
    sage: F = factor(-2*x^2 - 1); F
Expected:
    (-2.0) * (1.0*x^2 + 0.5) * (1.0*x^2 + 1.11022302463e-16*x + 0.5)
Got:
    (-2.0) * (1.0*x^2 - 2.22044604925e-16*x + 0.5) * (1.0*x^2 + 0.5)
**********************************************************************
```



---

Comment by was created at 2008-03-02 08:06:18

this should be the final of four patches; it fixes one problem found by the referee (gfurnish)


---

Attachment

I attached the one small change requested.


---

Comment by mabshoff created at 2008-03-02 20:34:50

Resolution: fixed


---

Comment by mabshoff created at 2008-03-02 20:34:50

Merged in Sage 2.10.3.rc1
