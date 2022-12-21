# Issue 4482: Sage 3.2.rc0: optional Magma doctest failure in devel/sage/sage/rings/polynomial/pbori.pyx

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-11-09 17:37:22

Assignee: was

#4395 fixes a similar issue, but the following still fails after applying that patch:

```
sage -t -long -optional devel/sage/sage/rings/polynomial/pbori.pyx
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.3.final/tmp/pbori.py", line 988:
    sage: B._magma_() # optional requires magma
Expected:
    Affine Algebra of rank 3 over GF(2)
    Lexicographical Order
    Variables: x, y, z
    Quotient relations:
    [
    x^2 + x,
    y^2 + y,
    z^2 + z
    ]
Got:
    Affine Algebra of rank 3 over GF(2)
    Lexicographical Order
    Variables: x, y, z
    Quotient relations:
    [
    0,
    0,
    0
    ]
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.3.final/tmp/pbori.py", line 1024:
    sage: B._magma_() # optional requires magma, indirect doctest
Expected:
    Affine Algebra of rank 3 over GF(2)
    Lexicographical Order
    Variables: x, y, z
    Quotient relations:
    [
    x^2 + x,
    y^2 + y,
    z^2 + z
    ]
Got:
    Affine Algebra of rank 3 over GF(2)
    Lexicographical Order
    Variables: x, y, z
    Quotient relations:
    [
    0,
    0,
    0
    ]
**********************************************************************
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-11-24 22:54:48

Resolution: fixed


---

Comment by mabshoff created at 2008-11-24 22:54:48

Fixed in Sage 3.2.1.alpha1 via #4601.

Cheers,

Michael
