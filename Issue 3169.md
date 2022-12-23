# Issue 3169: matrix augment and stack should take vectors

Issue created by migration from https://trac.sagemath.org/ticket/3169

Original creator: jason

Original creation time: 2008-05-12 22:21:56

Assignee: was

CC:  slelievre

It would be nice if these worked:


```
sage: m=matrix(3,range(9))
sage: v=vector([-1,-2,-3])
sage: m.augment(v)
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/home/grout/<ipython console> in <module>()

/home/grout/matrix1.pyx in sage.matrix.matrix1.Matrix.augment (sage/matrix/matrix1.c:7099)()

<type 'exceptions.TypeError'>: Argument 'other' has incorrect type (expected sage.matrix.matrix1.Matrix, got sage.modules.vector_integer_dense.Vector_integer_dense)
sage: m.stack(v)
---------------------------------------------------------------------------
<type 'exceptions.AttributeError'>        Traceback (most recent call last)

/home/grout/<ipython console> in <module>()

/home/grout/matrix_integer_dense.pyx in sage.matrix.matrix_integer_dense.Matrix_integer_dense.stack (sage/matrix/matrix_integer_dense.c:24661)()

<type 'exceptions.AttributeError'>: 'sage.modules.vector_integer_dense.Vector_integer_d' object has no attribute 'ncols'
```



---

Attachment


---

Comment by slelievre created at 2018-04-20 14:31:27

Implemented in #10424 and #10974.

The following now works, making this ticket obsolete.

```
sage: m = matrix(3, range(9))
sage: m
[0 1 2]
[3 4 5]
[6 7 8]
sage: v = vector([-1, -2, -3])
sage: m.augment(v)
[ 0  1  2 -1]
[ 3  4  5 -2]
[ 6  7  8 -3]
sage: m.stack(v)
[ 0  1  2]
[ 3  4  5]
[ 6  7  8]
[-1 -2 -3]
```


I am marking this ticket as duplicate/invalid/wontfix.


---

Comment by slelievre created at 2018-04-20 14:31:27

Changing keywords from "" to "augment".


---

Comment by slelievre created at 2018-04-20 14:31:27

Changing status from new to needs_review.


---

Comment by tscrim created at 2018-04-21 04:31:37

Changing status from needs_review to positive_review.


---

Comment by vdelecroix created at 2018-05-18 17:16:26

Resolution: wontfix


---

Comment by vdelecroix created at 2018-05-18 17:16:26

closing positively reviewed duplicates
