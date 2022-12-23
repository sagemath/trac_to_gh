# Issue 5408: Matrix kernel with PARI algorithm passes wrong type

Issue created by migration from https://trac.sagemath.org/ticket/5408

Original creator: rbeezer

Original creation time: 2009-03-01 06:26:56

Assignee: rbeezer

Keywords: kernel, PARI

Using the PARI kernel algorithm returns a PARI object which is unpacked as a list with the rows given as tuples.  When this is passed to hermite_form() the object is not of the right type.


```
sage: a = matrix(ZZ, [[1,2],[2,4]])
sage: a.kernel(algorithm='pari')
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/home/rob/.sage/temp/wave/8545/_home_rob__sage_init_sage_0.py in <module>()

/opt/sage-3.3/local/lib/python2.5/site-packages/sage/matrix/matrix_integer_dense.so in sage.matrix.matrix_integer_dense.Matrix_integer_dense.kernel (sage/matrix/matrix_integer_dense.c:16256)()

AttributeError: 'list' object has no attribute 'hermite_form'
```



---

Attachment


---

Comment by rbeezer created at 2009-03-01 23:59:41

Replying to [comment:1 rbeezer]:

matrix_dense_integer._kernel_gens_using_pari() now returns a matrix, when it previously returned a list of tuples, which always caused the calling routine (kernel_matrix) to choke.  Two comments:

1.  I may change the name of this routine as part of http://trac.sagemath.org/sage_trac/ticket/5381

2.  I've tried to be careful about sending back an empty matrix with the right dimensions when the matrix has full rank.  I suspect there are other places that could use changes like this.

Apply this patch before http://trac.sagemath.org/sage_trac/ticket/5381


---

Comment by cremona created at 2009-03-07 17:05:48

Review: Looks good, applies ok to 3.4.alpha0 and tests in sage/matrix (plus a whole lot of other random kernel tests I did) pass fine.


---

Comment by mabshoff created at 2009-03-08 06:16:41

Merged in Sage 3.4.rc1.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-08 06:16:41

Resolution: fixed
