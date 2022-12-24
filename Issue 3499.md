# Issue 3499: [with patch, needs review] cyclotomic linear algebra: multiplying 1x1 identity matrix by anything fails

archive/issues_003499.json:
```json
{
    "body": "Assignee: @craigcitro\n\nThis fails:\n\n\n```\nsage: N1 = Matrix(CyclotomicField(6), 1, [1])\nsage: cf6 = CyclotomicField(6) ; z6 = cf6.0\nsage: N2 = Matrix(CyclotomicField(6), 1, 5, [0,1,z6,-z6,-z6+1])\nsage: N1*N2\n[         0          1      zeta6     -zeta6 -zeta6 + 1]\n```\n\n\nThe attached patch fixes it.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3499\n\n",
    "created_at": "2008-06-24T00:23:31Z",
    "labels": [
        "linear algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.4",
    "title": "[with patch, needs review] cyclotomic linear algebra: multiplying 1x1 identity matrix by anything fails",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3499",
    "user": "@craigcitro"
}
```
Assignee: @craigcitro

This fails:


```
sage: N1 = Matrix(CyclotomicField(6), 1, [1])
sage: cf6 = CyclotomicField(6) ; z6 = cf6.0
sage: N2 = Matrix(CyclotomicField(6), 1, 5, [0,1,z6,-z6,-z6+1])
sage: N1*N2
[         0          1      zeta6     -zeta6 -zeta6 + 1]
```


The attached patch fixes it.

Issue created by migration from https://trac.sagemath.org/ticket/3499





---

archive/issue_comments_024682.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-06-24T00:26:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3499",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3499#issuecomment-24682",
    "user": "@craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_comments_024683.json:
```json
{
    "body": "Attachment [trac-3499.2.patch](tarball://root/attachments/some-uuid/ticket3499/trac-3499.2.patch) by @craigcitro created at 2008-06-24 00:26:42\n\nI just realized that this may depend on trac #3495. Sorry.",
    "created_at": "2008-06-24T00:26:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3499",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3499#issuecomment-24683",
    "user": "@craigcitro"
}
```

Attachment [trac-3499.2.patch](tarball://root/attachments/some-uuid/ticket3499/trac-3499.2.patch) by @craigcitro created at 2008-06-24 00:26:42

I just realized that this may depend on trac #3495. Sorry.



---

archive/issue_comments_024684.json:
```json
{
    "body": "\n```\nsage: N1 = Matrix(CyclotomicField(6), 1, [1]) \nsage: cf6 = CyclotomicField(6) ; z6 = cf6.0 \nsage: N2 = Matrix(CyclotomicField(6), 1, 5, [0,1,z6,-z6,-z6+1]) \nsage: N1*N2\n[         0          1      zeta6     -zeta6 -zeta6 + 1]\nsage: N1 *N1\n[1]\nsage: N1 = Matrix(CyclotomicField(6), 1, [-1]) \nsage: N1 *N2\n---------------------------------------------------------------------------\nIndexError                                Traceback (most recent call last)\n\n/Users/was/<ipython console> in <module>()\n\n/Users/was/element.pyx in sage.structure.element.Matrix.__mul__ (sage/structure/element.c:11499)()\n\n/Users/was/coerce.pyx in sage.structure.coerce.CoercionModel_cache_maps.bin_op_c (sage/structure/coerce.c:5061)()\n\n/Users/was/action.pyx in sage.categories.action.Action._call_c (sage/categories/action.c:1682)()\n\n/Users/was/action.pyx in sage.matrix.action.MatrixMatrixAction._call_c_impl (sage/matrix/action.c:1934)()\n\n/Users/was/matrix_cyclo_dense.pyx in sage.matrix.matrix_cyclo_dense.Matrix_cyclo_dense._matrix_times_matrix_c_impl (sage/matrix/matrix_cyclo_dense.c:3257)()\n\n/Users/was/matrix_integer_dense.pyx in sage.matrix.matrix_integer_dense._lift_crt (sage/matrix/matrix_integer_dense.c:26974)()\n\nIndexError: list index out of range\n```\n",
    "created_at": "2008-06-24T00:47:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3499",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3499#issuecomment-24684",
    "user": "@williamstein"
}
```


```
sage: N1 = Matrix(CyclotomicField(6), 1, [1]) 
sage: cf6 = CyclotomicField(6) ; z6 = cf6.0 
sage: N2 = Matrix(CyclotomicField(6), 1, 5, [0,1,z6,-z6,-z6+1]) 
sage: N1*N2
[         0          1      zeta6     -zeta6 -zeta6 + 1]
sage: N1 *N1
[1]
sage: N1 = Matrix(CyclotomicField(6), 1, [-1]) 
sage: N1 *N2
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)

/Users/was/<ipython console> in <module>()

/Users/was/element.pyx in sage.structure.element.Matrix.__mul__ (sage/structure/element.c:11499)()

/Users/was/coerce.pyx in sage.structure.coerce.CoercionModel_cache_maps.bin_op_c (sage/structure/coerce.c:5061)()

/Users/was/action.pyx in sage.categories.action.Action._call_c (sage/categories/action.c:1682)()

/Users/was/action.pyx in sage.matrix.action.MatrixMatrixAction._call_c_impl (sage/matrix/action.c:1934)()

/Users/was/matrix_cyclo_dense.pyx in sage.matrix.matrix_cyclo_dense.Matrix_cyclo_dense._matrix_times_matrix_c_impl (sage/matrix/matrix_cyclo_dense.c:3257)()

/Users/was/matrix_integer_dense.pyx in sage.matrix.matrix_integer_dense._lift_crt (sage/matrix/matrix_integer_dense.c:26974)()

IndexError: list index out of range
```




---

archive/issue_comments_024685.json:
```json
{
    "body": "part 2",
    "created_at": "2008-06-24T01:07:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3499",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3499#issuecomment-24685",
    "user": "@craigcitro"
}
```

part 2



---

archive/issue_comments_024686.json:
```json
{
    "body": "Attachment [trac-3499-2.patch](tarball://root/attachments/some-uuid/ticket3499/trac-3499-2.patch) by @williamstein created at 2008-06-24 03:08:50",
    "created_at": "2008-06-24T03:08:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3499",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3499#issuecomment-24686",
    "user": "@williamstein"
}
```

Attachment [trac-3499-2.patch](tarball://root/attachments/some-uuid/ticket3499/trac-3499-2.patch) by @williamstein created at 2008-06-24 03:08:50



---

archive/issue_comments_024687.json:
```json
{
    "body": "REPORT:  Very good.  Michael -- apply both patches.",
    "created_at": "2008-06-24T03:09:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3499",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3499#issuecomment-24687",
    "user": "@williamstein"
}
```

REPORT:  Very good.  Michael -- apply both patches.



---

archive/issue_comments_024688.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-24T03:39:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3499",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3499#issuecomment-24688",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_024689.json:
```json
{
    "body": "Merged both patches in Sage 3.0.4.alpha1",
    "created_at": "2008-06-24T03:39:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3499",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3499#issuecomment-24689",
    "user": "mabshoff"
}
```

Merged both patches in Sage 3.0.4.alpha1
