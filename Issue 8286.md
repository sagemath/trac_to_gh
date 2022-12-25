# Issue 8286: sparse_rows and sparse_columns are broken for 0xn, nx0 matrices

archive/issues_008286.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nsage: mat = matrix(ZZ, 0, 1, sparse=True)\nsage: mat.nrows()\n0\nsage: mat.rows()\n[(0)]\nsage: mat = matrix(ZZ, 0, 1, sparse=False)\nsage: mat.nrows()\n0\nsage: mat.rows()\n[]\n```\n\nThe `rows` method should act the same regardless of the sparsity of the matrix, and when there are no rows, it should return an empty list.\n\nThe same thing happens with matrices defined over QQ or GF(2), so I'm guessing that the problem is with `sparse_rows` and `sparse_columns` in sage/matrix/matrix1.pyx.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8286\n\n",
    "created_at": "2010-02-16T21:37:28Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "sparse_rows and sparse_columns are broken for 0xn, nx0 matrices",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8286",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: @williamstein


```
sage: mat = matrix(ZZ, 0, 1, sparse=True)
sage: mat.nrows()
0
sage: mat.rows()
[(0)]
sage: mat = matrix(ZZ, 0, 1, sparse=False)
sage: mat.nrows()
0
sage: mat.rows()
[]
```

The `rows` method should act the same regardless of the sparsity of the matrix, and when there are no rows, it should return an empty list.

The same thing happens with matrices defined over QQ or GF(2), so I'm guessing that the problem is with `sparse_rows` and `sparse_columns` in sage/matrix/matrix1.pyx.


Issue created by migration from https://trac.sagemath.org/ticket/8286





---

archive/issue_comments_073251.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-02-24T05:03:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8286",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8286#issuecomment-73251",
    "user": "https://github.com/rbeezer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_073252.json:
```json
{
    "body": "Hi John,\n\nI think this is an exact duplicate of #10714, which has a fix and has been merged. (I'd missed this ticket when I \"rediscovered\" this problem).  On 4.6.2.rc0 I now get:\n\n\n```\nsage: mat = matrix(ZZ, 0, 1, sparse=True)\nsage: mat.nrows()\n0\nsage: mat.rows()\n[]\n```\n\n\nI think we can close this as a duplicate?\n\nRob",
    "created_at": "2011-02-24T05:03:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8286",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8286#issuecomment-73252",
    "user": "https://github.com/rbeezer"
}
```

Hi John,

I think this is an exact duplicate of #10714, which has a fix and has been merged. (I'd missed this ticket when I "rediscovered" this problem).  On 4.6.2.rc0 I now get:


```
sage: mat = matrix(ZZ, 0, 1, sparse=True)
sage: mat.nrows()
0
sage: mat.rows()
[]
```


I think we can close this as a duplicate?

Rob



---

archive/issue_comments_073253.json:
```json
{
    "body": "Yes, it works for me now.",
    "created_at": "2011-02-24T06:15:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8286",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8286#issuecomment-73253",
    "user": "https://github.com/jhpalmieri"
}
```

Yes, it works for me now.



---

archive/issue_comments_073254.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2011-02-24T06:15:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8286",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8286#issuecomment-73254",
    "user": "https://github.com/jhpalmieri"
}
```

Resolution: duplicate
