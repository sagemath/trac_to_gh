# Issue 5554: implement cholesky_decomposition for matrices other than RDF

Issue created by migration from Trac.

Original creator: ncalexan

Original creation time: 2009-03-17 21:38:35

Assignee: was

CC:  jkantor wstein

Keywords: cholesky decomposition RDF real

The attached patch

 * renames cholesky() to cholesky_decomposition()
 * improves the documentation
 * adds a helper function _cholesky_decomposition_() for specialization;
 * moves the GSL/scipy cholesky function to matrix_real_double_dense, where it belongs;
 * implements a generic Cholesky decomposition that works for arbitrary precision real and complex fields, where we generalize symmetric to Hermitian.



---

Comment by rbeezer created at 2009-04-18 23:05:10

Nicely done, great documentation, passes all tests.  Suggestions for improvements, in order of perceived importance.

1.  Inputting a matrix over ZZ or QQ fails with the `ValueError` message about not being symmetric or positive definite, which is not an accurate error message in this case.  Should there be an attempt to coerce the matrix to RDF or CDF?  Inputting (trivial) symbolic matrices proceeds successfully (eg. [[x,y],[y,x]]).  Perhaps a coercion attempt above will cause a failure in this case, and this might be the right result?  Another interesting input is `matrix(2, [2, 2+i,2-i,4])` which is considered to be defined over SR, yet is handled properly by the routines here, or can be convrted to CDF for an accurate numerical result.

2.  I think it would be safer to force the user to me more aware of the positive definite requirement.  I'd prefer to see a keyword argument like "positive_definite=False" added.  In other words, the default operation is to perform a check for positive-definiteness, but when the user knows the matrices at hand are positive-definite, the keyword can be invoked to bypass the check.  I think there are other examples like this in Sage (but I can't locate a good one at the moment).

3.  A couple of places in the documentation could benefit from including the greater generality of matrices over the complex numbers, which this enhancement now allows.  Specifically:
(a) docstring in matrix2.pyx could make it clear that `L^t` is the adjoint when the matrix has complex entries (rather than looking like just the transpose).
(b) two error messages state that the matrix is "not symmetric."  Could they say instead "not symmetric (or not Hermitian)"?

4. Computing eigenvalues for matrices over a `RealField()` gives the warning message

`UserWarning: Using generic algorithm for an inexact ring, which will probably give incorrect results due to numerical precision issues.`

Would something similar be a good idea here for the generic algorithm?


---

Comment by rbeezer created at 2009-05-07 19:11:52

Re (1): ncalexan says:  I think they should fail if you can't extract a square root.  And I *don't* think we should coerce anything.  Ever.

Improvements 2, 3, and 4 have been moved to #6003.  So this now has a positive review.


---

Comment by mabshoff created at 2009-05-14 05:32:25

This needs work: cholesky() cannot just be deleted, it needs to be deprecated first.

The code looks very nice otherwise :)

Cheers,

Michael


---

Attachment

Okay, this adds back cholesky, with a deprecation warning.  I'm returning this to positive review, since nothing else has changed.


---

Comment by mabshoff created at 2009-05-19 19:43:21

Merged trac_5554-cholesky-decomposition-2.patch in Sage 4.0.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-19 19:43:21

Resolution: fixed
