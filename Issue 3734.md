# Issue 3734: inverse() fails for 0 by 0 matrices

archive/issues_003734.json:
```json
{
    "body": "Assignee: was\n\nAs reported to sage-devel on 2008-07-19:\n\n\n```\nPuzzle question:  find a matrix with rank 0 but determinant 1:\n\nsage: type(M)\n<type 'sage.matrix.matrix_generic_dense.Matrix_generic_dense'>\nsage: M.rank()\n0\nsage: M.determinant()\n1.00000000000000\n\nAnswer:  M is 0x0:\nsage: M\n[]\nsage: [M.nrows(), M.ncols()]\n[0, 0]\n\nNow I am happy with all that (since I am computing regulators of\nelliptic curves which may have rank 0).  And with this:\nsage: M.is_invertible()\nTrue\nbut then disappointed by this:\nsage: M.inverse()\n---------------------------------------------------------------------------\nIndexError                                Traceback (most recent call last)\n\n/home/john/sage-3.0.4/<ipython console> in <module>()\n\n/home/john/sage-3.0.4/matrix2.pyx in\nsage.matrix.matrix2.Matrix.inverse (sage/matrix/matrix2.c:19932)()\n\n/home/john/sage-3.0.4/matrix0.pyx in\nsage.matrix.matrix0.Matrix.__invert__ (sage/matrix/matrix0.c:14525)()\n\n/home/john/sage-3.0.4/matrix0.pyx in\nsage.matrix.matrix0.Matrix.__getitem__ (sage/matrix/matrix0.c:3129)()\n\nIndexError: matrix index out of range\n```\n\n\nThe matrix inversion code should catch this case and return the same matrix.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3734\n\n",
    "created_at": "2008-07-28T09:36:29Z",
    "labels": [
        "linear algebra",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1",
    "title": "inverse() fails for 0 by 0 matrices",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3734",
    "user": "cremona"
}
```
Assignee: was

As reported to sage-devel on 2008-07-19:


```
Puzzle question:  find a matrix with rank 0 but determinant 1:

sage: type(M)
<type 'sage.matrix.matrix_generic_dense.Matrix_generic_dense'>
sage: M.rank()
0
sage: M.determinant()
1.00000000000000

Answer:  M is 0x0:
sage: M
[]
sage: [M.nrows(), M.ncols()]
[0, 0]

Now I am happy with all that (since I am computing regulators of
elliptic curves which may have rank 0).  And with this:
sage: M.is_invertible()
True
but then disappointed by this:
sage: M.inverse()
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)

/home/john/sage-3.0.4/<ipython console> in <module>()

/home/john/sage-3.0.4/matrix2.pyx in
sage.matrix.matrix2.Matrix.inverse (sage/matrix/matrix2.c:19932)()

/home/john/sage-3.0.4/matrix0.pyx in
sage.matrix.matrix0.Matrix.__invert__ (sage/matrix/matrix0.c:14525)()

/home/john/sage-3.0.4/matrix0.pyx in
sage.matrix.matrix0.Matrix.__getitem__ (sage/matrix/matrix0.c:3129)()

IndexError: matrix index out of range
```


The matrix inversion code should catch this case and return the same matrix.


Issue created by migration from https://trac.sagemath.org/ticket/3734





---

archive/issue_comments_026509.json:
```json
{
    "body": "Attachment [sage-trac3734.patch](tarball://root/attachments/some-uuid/ticket3734/sage-trac3734.patch) by cremona created at 2008-07-29 00:36:25",
    "created_at": "2008-07-29T00:36:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3734",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3734#issuecomment-26509",
    "user": "cremona"
}
```

Attachment [sage-trac3734.patch](tarball://root/attachments/some-uuid/ticket3734/sage-trac3734.patch) by cremona created at 2008-07-29 00:36:25



---

archive/issue_comments_026510.json:
```json
{
    "body": "Before:\n\n```\nsage: MatrixSpace(ZZ,0,0)(0).inverse()  \n[]\nsage: MatrixSpace(QQ,0,0)(0).inverse()\n[]\nsage: MatrixSpace(RR,0,0)(0).inverse()\n---------------------------------------------------------------------------\nIndexError                                Traceback (most recent call last)\n\n/home/john/sage-3.0.4/<ipython console> in <module>()\n\n/home/john/sage-3.0.4/matrix2.pyx in sage.matrix.matrix2.Matrix.inverse (sage/matrix/matrix2.c:19932)()\n\n/home/john/sage-3.0.4/matrix0.pyx in sage.matrix.matrix0.Matrix.__invert__ (sage/matrix/matrix0.c:14525)()\n\n/home/john/sage-3.0.4/matrix0.pyx in sage.matrix.matrix0.Matrix.__getitem__ (sage/matrix/matrix0.c:3129)()\n\nIndexError: matrix index out of range\n```\n\n\nAfter applying sage-trac3734.patch:\n\n```\nsage: MatrixSpace(ZZ,0,0)(0).inverse()\n[]\nsage: MatrixSpace(QQ,0,0)(0).inverse()\n[]\nsage: MatrixSpace(RR,0,0)(0).inverse()\n[]\n```\n\n\nPatch was based on 3.0.4",
    "created_at": "2008-07-29T00:37:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3734",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3734#issuecomment-26510",
    "user": "cremona"
}
```

Before:

```
sage: MatrixSpace(ZZ,0,0)(0).inverse()  
[]
sage: MatrixSpace(QQ,0,0)(0).inverse()
[]
sage: MatrixSpace(RR,0,0)(0).inverse()
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)

/home/john/sage-3.0.4/<ipython console> in <module>()

/home/john/sage-3.0.4/matrix2.pyx in sage.matrix.matrix2.Matrix.inverse (sage/matrix/matrix2.c:19932)()

/home/john/sage-3.0.4/matrix0.pyx in sage.matrix.matrix0.Matrix.__invert__ (sage/matrix/matrix0.c:14525)()

/home/john/sage-3.0.4/matrix0.pyx in sage.matrix.matrix0.Matrix.__getitem__ (sage/matrix/matrix0.c:3129)()

IndexError: matrix index out of range
```


After applying sage-trac3734.patch:

```
sage: MatrixSpace(ZZ,0,0)(0).inverse()
[]
sage: MatrixSpace(QQ,0,0)(0).inverse()
[]
sage: MatrixSpace(RR,0,0)(0).inverse()
[]
```


Patch was based on 3.0.4



---

archive/issue_comments_026511.json:
```json
{
    "body": "Patch looks good to me.",
    "created_at": "2008-07-30T17:04:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3734",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3734#issuecomment-26511",
    "user": "dfdeshom"
}
```

Patch looks good to me.



---

archive/issue_comments_026512.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-30T22:49:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3734",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3734#issuecomment-26512",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_026513.json:
```json
{
    "body": "Merged in Sage 3.1.alpha0",
    "created_at": "2008-07-30T22:49:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3734",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3734#issuecomment-26513",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.alpha0
