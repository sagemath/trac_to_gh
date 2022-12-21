# Issue 4395: Sage 3.1.4: magma related optional doctest failure in sage/rings/quotient_ring.py

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-10-30 16:56:35

Assignee: was


```
sage -t -long -optional devel/sage/sage/rings/quotient_ring.py
**********************************************************************
File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/tmp/quotient_ring.py", line 647:
    sage: Q._magma_() # optional requires Magma
Expected:
    Affine Algebra of rank 2 over GF(2)
    Graded Reverse Lexicographical Order
    Variables: x, y
    Quotient relations:
    [
    x^2 + x,
    y^2 + y
    ]
Got:
    Affine Algebra of rank 2 over GF(2)
    Graded Reverse Lexicographical Order
    Variables: x, y
    Quotient relations:
    [
    0,
    0
    ]
**********************************************************************
1 items had failures:
   1 of   5 in __main__.example_23
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/tmp/.doctest_quotient_ring.py
	 [5.4 s]
exit code: 1024
```



---

Comment by was created at 2008-10-30 20:43:51

Apply this after #4394


---

Comment by mabshoff created at 2008-10-31 16:46:53

Where is the patch?

Cheers,

Michael


---

Comment by mabshoff created at 2008-10-31 21:33:34

This patch (one it is here :)) also likely fixes the following problem:

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



---

Attachment

Positive review. It fixes the original problem reported, but not as I suspected the issue in 

```
devel/sage/sage/rings/polynomial/pbori.pyx
```

That issue is now #4482.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-09 17:39:42

Merged in Sage 3.2.rc0


---

Comment by mabshoff created at 2008-11-09 17:39:42

Resolution: fixed
