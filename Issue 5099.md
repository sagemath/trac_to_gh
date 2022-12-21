# Issue 5099: rank for mod n sparse matrices is broken

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2009-01-25 16:46:23

Assignee: was

Keywords: sparse, rank

On both sage.math (sage 3.2.3) and on my iMac (sage 3.3.alpha1), running

```
matrix(GF(3), 0, 0, {}).rank()
```

is broken: sometimes I get 0, sometimes I get 1, sometimes I get `RuntimeError`. Same goes for 

```
matrix(GF(3), 0, 0, sparse=True).rank()
```

and 

```
matrix(GF(3), 0, 10, sparse=True).rank()
```

For what it's worth, `matrix(GF(3), 10, 0, sparse=True).rank()` seems okay.




---

Comment by hivert created at 2009-02-26 20:05:27

I Just discovered this problem, otherwise I would had taken care of it in #5256. This problem is very likely to occur for other kind of matrices. I suggest to expand `test_trivial_matrices_inverse` (from `sage.matrix.matrix_space`) which already tests `det`,`is_invertible` and `inverse` to also test the `rank` method. 

If you need it, I can also investigate further...

Cheers,

Florent


---

Comment by hivert created at 2009-02-26 21:33:57

Changing assignee from was to hivert.


---

Comment by hivert created at 2009-02-26 21:33:57

Changing status from new to assigned.


---

Attachment

Patch proposal


---

Comment by hivert created at 2009-03-01 22:14:35

The patch should solve the problem and check the rank methods for trivial matrices of other type. For Q[x,y] the rank is not implemented and can't be tested. I tested it as non implemented to ensure that it will be correctly tested if someone implement it. 

Author of the patch: Florent Hivert


---

Comment by jhpalmieri created at 2009-03-03 19:39:33

This fixes my problem.  Positive review.


---

Comment by mabshoff created at 2009-03-05 00:45:39

Merged in Sage 3.4.rc1.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-05 00:45:39

Resolution: fixed
