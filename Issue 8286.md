# Issue 8286: sparse_rows and sparse_columns are broken for 0xn, nx0 matrices

Issue created by migration from https://trac.sagemath.org/ticket/8286

Original creator: jhpalmieri

Original creation time: 2010-02-16 21:37:28

Assignee: was


```
sage: mat = matrix(ZZ, 0, 1, sparse=True)
sage: mat.nrows()
0
sage: mat.rows()
[(0)]
sage: mat = matrix(ZZ, 0, 1, sparse=False)
sage: mat.nrows()
0
sage: mat.rows()
[]
```

The `rows` method should act the same regardless of the sparsity of the matrix, and when there are no rows, it should return an empty list.

The same thing happens with matrices defined over QQ or GF(2), so I'm guessing that the problem is with `sparse_rows` and `sparse_columns` in sage/matrix/matrix1.pyx.



---

Comment by rbeezer created at 2011-02-24 05:03:45

Changing status from new to needs_review.


---

Comment by rbeezer created at 2011-02-24 05:03:45

Hi John,

I think this is an exact duplicate of #10714, which has a fix and has been merged. (I'd missed this ticket when I "rediscovered" this problem).  On 4.6.2.rc0 I now get:


```
sage: mat = matrix(ZZ, 0, 1, sparse=True)
sage: mat.nrows()
0
sage: mat.rows()
[]
```


I think we can close this as a duplicate?

Rob


---

Comment by jhpalmieri created at 2011-02-24 06:15:14

Yes, it works for me now.


---

Comment by jhpalmieri created at 2011-02-24 06:15:14

Resolution: duplicate
