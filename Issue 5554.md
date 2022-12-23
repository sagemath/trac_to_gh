# Issue 5554: implement cholesky_decomposition for matrices other than RDF

archive/issues_005554.json:
```json
{
    "body": "Assignee: was\n\nCC:  jkantor wstein\n\nKeywords: cholesky decomposition RDF real\n\nThe attached patch\n\n* renames cholesky() to cholesky_decomposition()\n* improves the documentation\n* adds a helper function _cholesky_decomposition_() for specialization;\n* moves the GSL/scipy cholesky function to matrix_real_double_dense, where it belongs;\n* implements a generic Cholesky decomposition that works for arbitrary precision real and complex fields, where we generalize symmetric to Hermitian.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5554\n\n",
    "created_at": "2009-03-17T21:38:35Z",
    "labels": [
        "linear algebra",
        "major",
        "enhancement"
    ],
    "title": "implement cholesky_decomposition for matrices other than RDF",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5554",
    "user": "ncalexan"
}
```
Assignee: was

CC:  jkantor wstein

Keywords: cholesky decomposition RDF real

The attached patch

* renames cholesky() to cholesky_decomposition()
* improves the documentation
* adds a helper function _cholesky_decomposition_() for specialization;
* moves the GSL/scipy cholesky function to matrix_real_double_dense, where it belongs;
* implements a generic Cholesky decomposition that works for arbitrary precision real and complex fields, where we generalize symmetric to Hermitian.


Issue created by migration from https://trac.sagemath.org/ticket/5554





---

archive/issue_comments_043198.json:
```json
{
    "body": "Nicely done, great documentation, passes all tests.  Suggestions for improvements, in order of perceived importance.\n\n1.  Inputting a matrix over ZZ or QQ fails with the `ValueError` message about not being symmetric or positive definite, which is not an accurate error message in this case.  Should there be an attempt to coerce the matrix to RDF or CDF?  Inputting (trivial) symbolic matrices proceeds successfully (eg. [[x,y],[y,x]]).  Perhaps a coercion attempt above will cause a failure in this case, and this might be the right result?  Another interesting input is `matrix(2, [2, 2+i,2-i,4])` which is considered to be defined over SR, yet is handled properly by the routines here, or can be convrted to CDF for an accurate numerical result.\n\n2.  I think it would be safer to force the user to me more aware of the positive definite requirement.  I'd prefer to see a keyword argument like \"positive_definite=False\" added.  In other words, the default operation is to perform a check for positive-definiteness, but when the user knows the matrices at hand are positive-definite, the keyword can be invoked to bypass the check.  I think there are other examples like this in Sage (but I can't locate a good one at the moment).\n\n3.  A couple of places in the documentation could benefit from including the greater generality of matrices over the complex numbers, which this enhancement now allows.  Specifically:\n(a) docstring in matrix2.pyx could make it clear that `L^t` is the adjoint when the matrix has complex entries (rather than looking like just the transpose).\n(b) two error messages state that the matrix is \"not symmetric.\"  Could they say instead \"not symmetric (or not Hermitian)\"?\n\n4. Computing eigenvalues for matrices over a `RealField()` gives the warning message\n\n`UserWarning: Using generic algorithm for an inexact ring, which will probably give incorrect results due to numerical precision issues.`\n\nWould something similar be a good idea here for the generic algorithm?",
    "created_at": "2009-04-18T23:05:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5554",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5554#issuecomment-43198",
    "user": "rbeezer"
}
```

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

archive/issue_comments_043199.json:
```json
{
    "body": "Re (1): ncalexan says:  I think they should fail if you can't extract a square root.  And I *don't* think we should coerce anything.  Ever.\n\nImprovements 2, 3, and 4 have been moved to #6003.  So this now has a positive review.",
    "created_at": "2009-05-07T19:11:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5554",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5554#issuecomment-43199",
    "user": "rbeezer"
}
```

Re (1): ncalexan says:  I think they should fail if you can't extract a square root.  And I *don't* think we should coerce anything.  Ever.

Improvements 2, 3, and 4 have been moved to #6003.  So this now has a positive review.



---

archive/issue_comments_043200.json:
```json
{
    "body": "This needs work: cholesky() cannot just be deleted, it needs to be deprecated first.\n\nThe code looks very nice otherwise :)\n\nCheers,\n\nMichael",
    "created_at": "2009-05-14T05:32:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5554",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5554#issuecomment-43200",
    "user": "mabshoff"
}
```

This needs work: cholesky() cannot just be deleted, it needs to be deprecated first.

The code looks very nice otherwise :)

Cheers,

Michael



---

archive/issue_comments_043201.json:
```json
{
    "body": "Attachment\n\nOkay, this adds back cholesky, with a deprecation warning.  I'm returning this to positive review, since nothing else has changed.",
    "created_at": "2009-05-19T16:27:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5554",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5554#issuecomment-43201",
    "user": "ncalexan"
}
```

Attachment

Okay, this adds back cholesky, with a deprecation warning.  I'm returning this to positive review, since nothing else has changed.



---

archive/issue_comments_043202.json:
```json
{
    "body": "Merged trac_5554-cholesky-decomposition-2.patch in Sage 4.0.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-19T19:43:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5554",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5554#issuecomment-43202",
    "user": "mabshoff"
}
```

Merged trac_5554-cholesky-decomposition-2.patch in Sage 4.0.rc0.

Cheers,

Michael



---

archive/issue_comments_043203.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-19T19:43:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5554",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5554#issuecomment-43203",
    "user": "mabshoff"
}
```

Resolution: fixed
