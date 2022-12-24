# Issue 6301: implement the Hadamard product of two matrices

archive/issues_006301.json:
```json
{
    "body": "Assignee: was\n\nCC:  rbeezer ylchapuy\n\nKeywords: Hadamard matrix product\n\nThat is, given a matrix A and another matrix B (of the same dimensions), form C such that C[i, j] = A[i, j] * B[i, j].\n\nIssue created by migration from https://trac.sagemath.org/ticket/6301\n\n",
    "created_at": "2009-06-15T16:12:18Z",
    "labels": [
        "linear algebra",
        "minor",
        "bug"
    ],
    "title": "implement the Hadamard product of two matrices",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6301",
    "user": "ncalexan"
}
```
Assignee: was

CC:  rbeezer ylchapuy

Keywords: Hadamard matrix product

That is, given a matrix A and another matrix B (of the same dimensions), form C such that C[i, j] = A[i, j] * B[i, j].

Issue created by migration from https://trac.sagemath.org/ticket/6301





---

archive/issue_comments_050265.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-07-14T22:32:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6301#issuecomment-50265",
    "user": "rbeezer"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_050266.json:
```json
{
    "body": "Patch overview:\n\n`elementwise_product()` in `matrix2.pyx` checks inputs for proper sizes, and coerces base rings, etc.\n\nThen two versions of `_elementwise_product()` (in `matrix_dense.pyx` and `matrix_sparse.pyx`) take over and do the actual work in what should be a fairly efficient manner, given the generality implied.  \n\nMore efficient implementations are certainly possible for more specialized classes.  The intent here is to begin with a correct and general implementation that is moderately efficient, primarily to make the functionality available in Sage.",
    "created_at": "2009-07-14T22:32:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6301#issuecomment-50266",
    "user": "rbeezer"
}
```

Patch overview:

`elementwise_product()` in `matrix2.pyx` checks inputs for proper sizes, and coerces base rings, etc.

Then two versions of `_elementwise_product()` (in `matrix_dense.pyx` and `matrix_sparse.pyx`) take over and do the actual work in what should be a fairly efficient manner, given the generality implied.  

More efficient implementations are certainly possible for more specialized classes.  The intent here is to begin with a correct and general implementation that is moderately efficient, primarily to make the functionality available in Sage.



---

archive/issue_comments_050267.json:
```json
{
    "body": "Changing keywords from \"Hadamard matrix product\" to \"elementwise Hadamard matrix product\".",
    "created_at": "2009-07-14T22:32:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6301#issuecomment-50267",
    "user": "rbeezer"
}
```

Changing keywords from "Hadamard matrix product" to "elementwise Hadamard matrix product".



---

archive/issue_comments_050268.json:
```json
{
    "body": "Attachment [trac_6301_elementwise_matrix_product.patch](tarball://root/attachments/some-uuid/ticket6301/trac_6301_elementwise_matrix_product.patch) by rbeezer created at 2009-07-14 22:33:02",
    "created_at": "2009-07-14T22:33:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6301#issuecomment-50268",
    "user": "rbeezer"
}
```

Attachment [trac_6301_elementwise_matrix_product.patch](tarball://root/attachments/some-uuid/ticket6301/trac_6301_elementwise_matrix_product.patch) by rbeezer created at 2009-07-14 22:33:02



---

archive/issue_comments_050269.json:
```json
{
    "body": "Nice work!  This all looks great.  Doctests in these files pass as well.  Positive review.",
    "created_at": "2009-07-19T07:25:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6301#issuecomment-50269",
    "user": "jason"
}
```

Nice work!  This all looks great.  Doctests in these files pass as well.  Positive review.



---

archive/issue_comments_050270.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-19T14:50:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6301#issuecomment-50270",
    "user": "mvngu"
}
```

Resolution: fixed
