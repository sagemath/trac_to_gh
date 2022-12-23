# Issue 8294: Copy is broken on 2x2 integer matrix (mutability is not set)

Issue created by migration from https://trac.sagemath.org/ticket/8294

Original creator: hivert

Original creation time: 2010-02-17 15:31:26

Assignee: h

Keywords: Matrix 2x2, mutability, copy


```
sage: M = sage.matrix.matrix_integer_2x2.MatrixSpace_ZZ_2x2()
sage: mat = M([3,4,5,6])
sage: mat.is_mutable()
True
sage: mat = copy(mat)
sage: mat.is_mutable()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/home/hivert/<ipython console> in <module>()

/usr/local/sage2/local/lib/python2.6/site-packages/sage/matrix/matrix0.so in sage.matrix.matrix0.Matrix.is_mutable (sage/matrix/matrix0.c:3928)()

AttributeError: 'NoneType' object has no attribute 'is_mutable'
```



---

Attachment

Should be ready for review.

Florent


---

Comment by hivert created at 2010-02-17 15:41:33

Changing assignee from h to hivert.


---

Comment by hivert created at 2010-02-17 15:41:44

Changing status from new to needs_review.


---

Comment by mraum created at 2010-02-20 13:02:46

Changing status from needs_review to positive_review.


---

Comment by mraum created at 2010-02-20 13:02:46

This applies cleanly and all tests pass. Positive review as is.
#8276 will follow soon.


---

Comment by hivert created at 2010-02-20 13:53:12

Replying to [comment:3 mraum]:
> This applies cleanly and all tests pass. Positive review as is.
> #8276 will follow soon.

Thanks a lot for this quick help !


---

Comment by mvngu created at 2010-03-03 14:27:07

Resolution: fixed
