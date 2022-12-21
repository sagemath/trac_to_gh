# Issue 5183: issues with elementary_divisors for sparse integer matrices

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2009-02-04 23:51:15

Assignee: was

CC:  davidloeffler

Keywords: elementary_divisor, sparse, dense

Two things: 

1. the conventions for elementary_divisors are different in Pari's implementation (called in matrix_integer_dense.pyx) compared to the generic PID implementation (in matrix2.pyx):

```
sage: mat = matrix(ZZ, 3, 2, [1, 0, 0, 1, 0, 0], sparse=True)
sage: mat.elementary_divisors()
[1, 1]
sage: mat.dense_matrix().elementary_divisors()
[1, 1, 0]
```


2. if the elementary divisors of a sparse matrix are not all 0 or 1 (at least I think that's the issue), I get an error:

```
sage: mat = matrix(ZZ, 3, 2, range(6), sparse=True)
sage: sage: mat.elementary_divisors()                    
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
...
TypeError: unable to coerce <class 'sage.rings.ideal.Ideal_pid'> to an integer
```

I get the same error for `mat.smith_form()`.  This is a problem with the Smith normal form stuff in matrix2.pyx, I think.



---

Comment by jhpalmieri created at 2010-02-20 00:49:52

Resolution: worksforme


---

Comment by jhpalmieri created at 2010-02-20 00:49:52

These two examples seem to work now, so I think we can close this.
