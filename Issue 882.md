# Issue 882: 2.8.7-alpha0: doctest failures due to RR->ZZ coercion patch

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2007-10-13 19:45:40

Assignee: somebody

2.8.6 behavior:

```
sage: 2.5 in ZZ
False
```


2.8.7-alpha0 behavior:

```
sage: 2.5 in ZZ
---------------------------------------------------------------------------
<type 'exceptions.ValueError'>            Traceback (most recent call last)

/home/cwitty/pre-sage/<ipython console> in <module>()

/home/cwitty/pre-sage/parent.pyx in parent.Parent.__contains__()

/home/cwitty/pre-sage/integer_ring.pyx in integer_ring.IntegerRing_class.__call__()

/home/cwitty/pre-sage/integer.pyx in integer.Integer.__init__()

/home/cwitty/pre-sage/real_mpfr.pyx in real_mpfr.RealNumber._integer_()

<type 'exceptions.ValueError'>: Attempt to coerce non-integral RealNumber to Integer
```


I'm pretty sure this is the underlying cause behind several 2.8.7-alpha0 doctest failures.

I have prepared a patch for this, which I will be testing shortly.


---

Attachment

I have attached a patch to change RR->ZZ coercion failure from ValueError to TypeError.  This fixes the doctest errors in sets/set.py and matrix/matrix_integer_dense.py.


---

Comment by was created at 2007-10-14 17:34:54

Resolution: fixed
