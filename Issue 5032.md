# Issue 5032: dividing a sparse matrix by a scalar gives a dense matrix, but multiplying gives a sparse one

archive/issues_005032.json:
```json
{
    "body": "Assignee: @williamstein\n\nThis is a bug:\n\n```\nsage: A = matrix(ZZ, 2, [1..4], sparse=True)\nsage: type(A*1)\n<type 'sage.matrix.matrix_integer_sparse.Matrix_integer_sparse'>\nsage: type(A/1)\n<type 'sage.matrix.matrix_rational_dense.Matrix_rational_dense'>\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/5032\n\n",
    "created_at": "2009-01-20T05:59:45Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "dividing a sparse matrix by a scalar gives a dense matrix, but multiplying gives a sparse one",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5032",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

This is a bug:

```
sage: A = matrix(ZZ, 2, [1..4], sparse=True)
sage: type(A*1)
<type 'sage.matrix.matrix_integer_sparse.Matrix_integer_sparse'>
sage: type(A/1)
<type 'sage.matrix.matrix_rational_dense.Matrix_rational_dense'>
```

Issue created by migration from https://trac.sagemath.org/ticket/5032





---

archive/issue_comments_038252.json:
```json
{
    "body": "This is because it creates the matrix space over the fraction field when division is done, and I agree that it is a bug that the sparce flag doesn't get passed on. In contrast \n\n```\nsage: A = matrix(QQ, 2, [1..4], sparse=True)\nsage: type(A)\n<type 'sage.matrix.matrix_rational_sparse.Matrix_rational_sparse'>\nsage: type(A/1)\n<type 'sage.matrix.matrix_rational_sparse.Matrix_rational_sparse'>\n```\n\nWhat needs to change is \n\n```\nFile:           /Users/robert/sage/sage-3.1.3/local/lib/python2.5/site-packages/sage/matrix/matrix_space.py\nDefinition:     MS.construction(self)\nSource:\n    def construction(self):\n        from sage.categories.pushout import MatrixFunctor\n        return MatrixFunctor(self.__nrows, self.__ncols), self.base_ring()\n```\n\nIt should read\n\n```\n        return MatrixFunctor(self.__nrows, self.__ncols, is_sparse=self.is_sparse), self.base_ring()\n```",
    "created_at": "2009-01-20T07:04:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5032",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5032#issuecomment-38252",
    "user": "https://github.com/robertwb"
}
```

This is because it creates the matrix space over the fraction field when division is done, and I agree that it is a bug that the sparce flag doesn't get passed on. In contrast 

```
sage: A = matrix(QQ, 2, [1..4], sparse=True)
sage: type(A)
<type 'sage.matrix.matrix_rational_sparse.Matrix_rational_sparse'>
sage: type(A/1)
<type 'sage.matrix.matrix_rational_sparse.Matrix_rational_sparse'>
```

What needs to change is 

```
File:           /Users/robert/sage/sage-3.1.3/local/lib/python2.5/site-packages/sage/matrix/matrix_space.py
Definition:     MS.construction(self)
Source:
    def construction(self):
        from sage.categories.pushout import MatrixFunctor
        return MatrixFunctor(self.__nrows, self.__ncols), self.base_ring()
```

It should read

```
        return MatrixFunctor(self.__nrows, self.__ncols, is_sparse=self.is_sparse), self.base_ring()
```



---

archive/issue_comments_038253.json:
```json
{
    "body": "Attachment [5032-sparce-matrix.patch](tarball://root/attachments/some-uuid/ticket5032/5032-sparce-matrix.patch) by @robertwb created at 2009-01-23 04:19:53",
    "created_at": "2009-01-23T04:19:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5032",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5032#issuecomment-38253",
    "user": "https://github.com/robertwb"
}
```

Attachment [5032-sparce-matrix.patch](tarball://root/attachments/some-uuid/ticket5032/5032-sparce-matrix.patch) by @robertwb created at 2009-01-23 04:19:53



---

archive/issue_comments_038254.json:
```json
{
    "body": "I was right in the middle of tracking this down when you posted the patch, so I figured I'd review it right away. ;)",
    "created_at": "2009-01-23T15:02:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5032",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5032#issuecomment-38254",
    "user": "https://github.com/rlmill"
}
```

I was right in the middle of tracking this down when you posted the patch, so I figured I'd review it right away. ;)



---

archive/issue_events_011609.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-24T14:31:31Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5032",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5032#event-11609"
}
```



---

archive/issue_comments_038255.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-24T14:31:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5032",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5032#issuecomment-38255",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_038256.json:
```json
{
    "body": "Merged in Sage 3.3.alpha2",
    "created_at": "2009-01-24T14:31:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5032",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5032#issuecomment-38256",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha2
