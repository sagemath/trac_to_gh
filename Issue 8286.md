# Issue 8286: sparse_rows and sparse_columns are broken for 0xn, nx0 matrices

archive/issues_008286.json:
```json
{
    "body": "Assignee: was\n\n\n```\nsage: mat = matrix(ZZ, 0, 1, sparse=True)\nsage: mat.nrows()\n0\nsage: mat.rows()\n[(0)]\nsage: mat = matrix(ZZ, 0, 1, sparse=False)\nsage: mat.nrows()\n0\nsage: mat.rows()\n[]\n```\n\nThe `rows` method should act the same regardless of the sparsity of the matrix, and when there are no rows, it should return an empty list.\n\nThe same thing happens with matrices defined over QQ or GF(2), so I'm guessing that the problem is with `sparse_rows` and `sparse_columns` in sage/matrix/matrix1.pyx.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8286\n\n",
    "created_at": "2010-02-16T21:37:28Z",
    "labels": [
        "linear algebra",
        "major",
        "bug"
    ],
    "title": "sparse_rows and sparse_columns are broken for 0xn, nx0 matrices",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8286",
    "user": "jhpalmieri"
}
```
Assignee: was


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

archive/issue_comments_073374.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-02-24T05:03:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8286",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8286#issuecomment-73374",
    "user": "rbeezer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_073375.json:
```json
{
    "body": "Hi John,\n\nI think this is an exact duplicate of #10714, which has a fix and has been merged. (I'd missed this ticket when I \"rediscovered\" this problem).  On 4.6.2.rc0 I now get:\n\n\n```\nsage: mat = matrix(ZZ, 0, 1, sparse=True)\nsage: mat.nrows()\n0\nsage: mat.rows()\n[]\n```\n\n\nI think we can close this as a duplicate?\n\nRob",
    "created_at": "2011-02-24T05:03:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8286",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8286#issuecomment-73375",
    "user": "rbeezer"
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

archive/issue_comments_073376.json:
```json
{
    "body": "Yes, it works for me now.",
    "created_at": "2011-02-24T06:15:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8286",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8286#issuecomment-73376",
    "user": "jhpalmieri"
}
```

Yes, it works for me now.



---

archive/issue_comments_073377.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2011-02-24T06:15:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8286",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8286#issuecomment-73377",
    "user": "jhpalmieri"
}
```

Resolution: duplicate
