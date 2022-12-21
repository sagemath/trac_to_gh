# Issue 655: Wrap LinBox's Sparse Matrix Echelonizer over Finite Fields

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2007-09-14 09:22:40

Assignee: was

Apparently, LinBox can compute echelon forms for sparse matrices over finite fields. And it seems to be faster than what we have now:

SAGE:

```
sage: A = random_matrix(GF(127),10000,10000,density=0.0002,sparse=True)
sage: time A.echelonize()
CPU times: user 99.64 s, sys: 0.22 s, total: 99.85 s
```


LinBox:

```
matrix size :10000x10000
density = 0.0002
size before = 19981
Gaussian elimination (no reordering)...done (9.08057 s)
DONE
size after = 0 # Bug
```


I was told that `SparseMatrixBase::NoReordering` works but `InPlaceLinearPivoting` crashes.

Also, it claims to support GF(q) which is very very slow in SAGE right now.


---

Comment by malb created at 2007-09-15 14:27:40

Actually, the above is not a bug but the size actually is zero after application of the Gaussian elimination. LinBox clears rows it doesn't need anymore to save memory.

Also, `InPlaceLinearPivoting` does not crash if called correctly and is often faster than `NoReordering`.


---

Attachment


---

Comment by malb created at 2007-09-15 14:29:37

`sparsegfp.patch` requires http://sage.math.washington.edu/home/malb/pkgs/linbox-20070915.spkg and exposes some of LinBox's functionality for sparse matrices over GF(p) to SAGE. More to come.


---

Attachment


---

Comment by was created at 2007-09-21 00:08:19

Resolution: fixed
