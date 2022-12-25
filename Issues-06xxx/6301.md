# Issue 6301: [with patch, positive review] implement the Hadamard product of two matrices

archive/issues_006301.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @rbeezer ylchapuy\n\nKeywords: elementwise Hadamard matrix product\n\nThat is, given a matrix A and another matrix B (of the same dimensions), form C such that C[i, j] = A[i, j] * B[i, j].\n\nIssue created by migration from https://trac.sagemath.org/ticket/6301\n\n",
    "closed_at": "2009-07-19T14:50:06Z",
    "created_at": "2009-06-15T16:12:18Z",
    "labels": [
        "component: linear algebra",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "[with patch, positive review] implement the Hadamard product of two matrices",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6301",
    "user": "https://github.com/ncalexan"
}
```
Assignee: @williamstein

CC:  @rbeezer ylchapuy

Keywords: elementwise Hadamard matrix product

That is, given a matrix A and another matrix B (of the same dimensions), form C such that C[i, j] = A[i, j] * B[i, j].

Issue created by migration from https://trac.sagemath.org/ticket/6301





---

archive/issue_comments_050169.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-07-14T22:32:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6301#issuecomment-50169",
    "user": "https://github.com/rbeezer"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_050170.json:
```json
{
    "body": "Patch overview:\n\n`elementwise_product()` in `matrix2.pyx` checks inputs for proper sizes, and coerces base rings, etc.\n\nThen two versions of `_elementwise_product()` (in `matrix_dense.pyx` and `matrix_sparse.pyx`) take over and do the actual work in what should be a fairly efficient manner, given the generality implied.  \n\nMore efficient implementations are certainly possible for more specialized classes.  The intent here is to begin with a correct and general implementation that is moderately efficient, primarily to make the functionality available in Sage.",
    "created_at": "2009-07-14T22:32:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6301#issuecomment-50170",
    "user": "https://github.com/rbeezer"
}
```

Patch overview:

`elementwise_product()` in `matrix2.pyx` checks inputs for proper sizes, and coerces base rings, etc.

Then two versions of `_elementwise_product()` (in `matrix_dense.pyx` and `matrix_sparse.pyx`) take over and do the actual work in what should be a fairly efficient manner, given the generality implied.  

More efficient implementations are certainly possible for more specialized classes.  The intent here is to begin with a correct and general implementation that is moderately efficient, primarily to make the functionality available in Sage.



---

archive/issue_comments_050171.json:
```json
{
    "body": "Changing keywords from \"Hadamard matrix product\" to \"elementwise Hadamard matrix product\".",
    "created_at": "2009-07-14T22:32:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6301#issuecomment-50171",
    "user": "https://github.com/rbeezer"
}
```

Changing keywords from "Hadamard matrix product" to "elementwise Hadamard matrix product".



---

archive/issue_comments_050172.json:
```json
{
    "body": "Attachment [trac_6301_elementwise_matrix_product.patch](tarball://root/attachments/some-uuid/ticket6301/trac_6301_elementwise_matrix_product.patch) by @rbeezer created at 2009-07-14 22:33:02",
    "created_at": "2009-07-14T22:33:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6301#issuecomment-50172",
    "user": "https://github.com/rbeezer"
}
```

Attachment [trac_6301_elementwise_matrix_product.patch](tarball://root/attachments/some-uuid/ticket6301/trac_6301_elementwise_matrix_product.patch) by @rbeezer created at 2009-07-14 22:33:02



---

archive/issue_comments_050173.json:
```json
{
    "body": "Nice work!  This all looks great.  Doctests in these files pass as well.  Positive review.",
    "created_at": "2009-07-19T07:25:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6301#issuecomment-50173",
    "user": "https://github.com/jasongrout"
}
```

Nice work!  This all looks great.  Doctests in these files pass as well.  Positive review.



---

archive/issue_events_014732.json:
```json
{
    "actor": "https://github.com/jasongrout",
    "created_at": "2009-07-19T07:37:01Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6301",
    "milestone": "sage-4.1.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6301#event-14732"
}
```



---

archive/issue_events_014733.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-07-19T14:50:06Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6301",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6301#event-14733"
}
```



---

archive/issue_comments_050174.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-19T14:50:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6301#issuecomment-50174",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
