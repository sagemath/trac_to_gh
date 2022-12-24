# Issue 8277: Using matrix() to convert between sparse and dense.

archive/issues_008277.json:
```json
{
    "body": "Assignee: hivert\n\nKeywords: sparse matrix conversion\n\nA call to `matrix` does not change the sparsity:\n\n```\n    sage: mat = matrix(ZZ, [[1,1],[1,1]], sparse=False)\n    sage: type(mat)\n    <type 'sage.matrix.matrix_integer_dense.Matrix_integer_dense'>\n    sage: mat2 = matrix(ZZ, mat, sparse=True)\n    sage: type(mat2)\n    <type 'sage.matrix.matrix_integer_dense.Matrix_integer_dense'>\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8277\n\n",
    "created_at": "2010-02-15T22:01:08Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-8.2",
    "title": "Using matrix() to convert between sparse and dense.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8277",
    "user": "hivert"
}
```
Assignee: hivert

Keywords: sparse matrix conversion

A call to `matrix` does not change the sparsity:

```
    sage: mat = matrix(ZZ, [[1,1],[1,1]], sparse=False)
    sage: type(mat)
    <type 'sage.matrix.matrix_integer_dense.Matrix_integer_dense'>
    sage: mat2 = matrix(ZZ, mat, sparse=True)
    sage: type(mat2)
    <type 'sage.matrix.matrix_integer_dense.Matrix_integer_dense'>
```


Issue created by migration from https://trac.sagemath.org/ticket/8277





---

archive/issue_comments_073297.json:
```json
{
    "body": "Changing component from algebra to linear algebra.",
    "created_at": "2010-09-02T10:50:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8277",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8277#issuecomment-73297",
    "user": "AlexGhitza"
}
```

Changing component from algebra to linear algebra.



---

archive/issue_comments_073298.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2018-03-01T15:00:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8277",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8277#issuecomment-73298",
    "user": "jdemeyer"
}
```

Resolution: duplicate



---

archive/issue_comments_073299.json:
```json
{
    "body": "Fixed in #24742.",
    "created_at": "2018-03-01T15:00:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8277",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8277#issuecomment-73299",
    "user": "jdemeyer"
}
```

Fixed in #24742.
