# Issue 8071: Trivial kernel of a matrix over non-fields are broken

Issue created by migration from Trac.

Original creator: rbeezer

Original creation time: 2010-01-26 04:48:34

Assignee: was

CC:  jason

Matrices with zero rows or zero columns, over rings that are not fields, try to construct vector spaces as return values.  The return value should be built as a `FreeModule` which seems to promote the result to a vector space when the ring is a field.


```
sage: A=matrix(Integers(6),[])
sage: A.right_kernel()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/rob/.sage/temp/wave/21471/_home_rob__sage_init_sage_0.py in <module>()

/sage/four-three/local/lib/python2.6/site-packages/sage/matrix/matrix2.so in sage.matrix.matrix2.Matrix.right_kernel (sage/matrix/matrix2.c:12440)()

/sage/four-three/local/lib/python2.6/site-packages/sage/modules/free_module.pyc in VectorSpace(K, dimension, sparse, inner_product_matrix)
    400     """
    401     if not K.is_field():
--> 402         raise TypeError, "Argument K (= %s) must be a field." % K
    403     if not sparse in (True,False):
    404         raise TypeError, "Argument sparse (= %s) must be a boolean."%sparse

TypeError: Argument K (= Ring of integers modulo 6) must be a field.
```


Patch is in-progress.


---

Comment by rbeezer created at 2010-01-27 05:51:12

This patch adds a new helper function to compute the right kernel of a matrix in the trivial cases of zero rows or zero columns.  When the ring is not a field or a PID, it is not always possible to create the submodule needed as a return value.  So in these cases it gives an informative error message (which is the response to the bug).

This function has been called in four places, and various doctests have been added.  This is the first step in refactoring and cleaning up some of the matrix code for kernels of matrices.


---

Comment by rbeezer created at 2010-01-27 05:51:12

Changing status from new to needs_review.


---

Attachment

Patch applies cleanly, looks good, doctests pass. The only nitpick I have is: shouldn't `:meth:`sage.modules.free_module.VectorSpace`` be `class:...`?

If that's fixed then this patch gets a positive review.


---

Comment by rbeezer created at 2010-04-06 03:08:17

Fixes class/meth in docstring


---

Attachment

Replying to [comment:3 malb]:
> Patch applies cleanly, looks good, doctests pass. The only nitpick I have is: shouldn't `:meth:`sage.modules.free_module.VectorSpace`` be `class:...`?
> 
> If that's fixed then this patch gets a positive review.

Hi Martin,

Thanks for the review on this one.  New patch contains everything, plus two changes in the docstring for `_right_kernel_trivial()` in `sage/matrix/matrix2.py` - both substitute "class" for "meth".  I am forever making that mistake - thanks for catching these.

Release manager - apply only the "dash-2" patch.

Rob


---

Comment by malb created at 2010-04-06 08:50:05

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-04-15 06:02:50

Merged in 4.4.alpha0:

 - trac_8071-matrix-kernels-trivially-2.patch


---

Comment by jhpalmieri created at 2010-04-15 06:02:50

Resolution: fixed
