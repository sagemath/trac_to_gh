# Issue 5223: [with patch; needs review] silly bug in flint wrapper makes it a factor of 10 slower for division of a polynomial by an integer

Issue created by migration from https://trac.sagemath.org/ticket/5223

Original creator: was

Original creation time: 2009-02-09 20:03:19

Assignee: somebody

CC:  roed

BEFORE:

```
sage: R.<x> = ZZ['x']
sage: f = 389*R.random_element(1000)
sage: timeit('f//389')
625 loops, best of 3: 228 µs per loop
```


AFTER:

```
sage: R.<x> = ZZ['x']
sage: f = 389*R.random_element(1000)
sage: timeit('f//389')
625 loops, best of 3: 48.3 µs per loop
```


The bug was doing the shortcut case, but then not returning and hence doing the long case *as well*.




---

Attachment

Patch looks good. Fixes obvious mistake on my part. :)


---

Comment by mabshoff created at 2009-02-10 07:13:23

This patch causes the following doctest failure:

```
mabshoff@sage:/scratch/mabshoff/sage-3.3.rc0$ ./sage -t -long devel/sage/sage/rings/polynomial/padics/polynomial_padic_capped_relative_dense.py
sage -t -long "devel/sage/sage/rings/polynomial/padics/polynomial_padic_capped_relative_dense.py"
**********************************************************************
File "/scratch/mabshoff/sage-3.3.rc0/devel/sage/sage/rings/polynomial/padics/polynomial_padic_capped_relative_dense.py", line 592:
    sage: b = a.rshift_coeffs(1); b
Expected:
    (O(13^3))*t^2 + (1 + O(13^2))*t + (13 + O(13^5))
Got:
    (O(13^3))*t^2 + (9 + 8*13 + O(13^2))*t + (7 + 12*13 + 7*13^2 + 6*13^3 + O(13^4))
**********************************************************************
File "/scratch/mabshoff/sage-3.3.rc0/devel/sage/sage/rings/polynomial/padics/polynomial_padic_capped_relative_dense.py", line 594:
    sage: b.list()
Expected:
    [13 + O(13^5), 1 + O(13^2), O(13^3)]
Got:
    [7 + 12*13 + 7*13^2 + 6*13^3 + O(13^4), 9 + 8*13 + O(13^2), O(13^3)]
**********************************************************************
File "/scratch/mabshoff/sage-3.3.rc0/devel/sage/sage/rings/polynomial/padics/polynomial_padic_capped_relative_dense.py", line 596:
    sage: b = a.rshift_coeffs(2); b
Expected:
    (O(13^2))*t^2 + (O(13))*t + (1 + O(13^4))
Got:
    (O(13^2))*t^2 + (7 + O(13))*t + (8 + 3*13 + 10*13^2 + 9*13^3 + O(13^4))
**********************************************************************
File "/scratch/mabshoff/sage-3.3.rc0/devel/sage/sage/rings/polynomial/padics/polynomial_padic_capped_relative_dense.py", line 598:
    sage: b.list()
Expected:
    [1 + O(13^4), O(13), O(13^2)]
Got:
    [8 + 3*13 + 10*13^2 + 9*13^3 + O(13^4), 7 + O(13), O(13^2)]
**********************************************************************
```


Cheers,

Michael


---

Comment by mabshoff created at 2009-02-20 07:42:52

Bumped to 3.4.1.

Cheers,

Michael


---

Attachment


---

Comment by burcin created at 2009-03-15 13:43:13

Wrong function was called for scalar division in the existing code, so we returned wrong results if division was not exact. Using `fmpz_poly_scalar_div_mpz()` fixes this problem and removes the limit on the size of the divisor. I didn't measure it's effects on speed.

All tests under sage/rings/polynomial pass with attachment:trac_5223.take2.patch.


---

Comment by burcin created at 2009-03-15 13:43:13

Changing assignee from somebody to burcin.


---

Comment by burcin created at 2009-03-15 13:43:13

Changing status from new to assigned.


---

Comment by robertwb created at 2009-03-17 00:04:56

Looks good to me, even gets the degree right when the higher terms are truncated away.


---

Comment by mabshoff created at 2009-03-20 20:14:59

Merged trac_5223.take2.patch in Sage 3.4.1.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-20 20:14:59

Resolution: fixed
