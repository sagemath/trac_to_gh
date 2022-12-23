# Issue 917: [with patch] Matrix.minors

archive/issues_000917.json:
```json
{
    "body": "Assignee: was\n\nThe attached patch implements a method to return the list of all k-minors of a matrix A.\n\nLet A be an m x n matrix and k an integer with 0 < k, k <= m, and\nk <= n. A k x k minor of A is the determinant of a k x k matrix\nobtained from A by deleting m - k rows and n - k columns.\n\nThe returned list is sorted in lexicographical row major ordering,\ne.g., if A is a 3 x 3 matrix then the minors returned are with\nfor these rows/columns:  [ [0, 1]x[0, 1], [0, 1]x[0, 2],\n[0, 1]x[1, 2], [0, 2]x[0, 1], [0, 2]x[0, 2], [0, 2]x[1, 2],\n[1, 2]x[0, 1], [1, 2]x[0, 2], [1, 2]x[1, 2] ].\n\nNote I am not sure if this method is too trivial or too specialised to be included with SAGE. I am submitting it here such that others can decide on that.\n\nIssue created by migration from https://trac.sagemath.org/ticket/917\n\n",
    "created_at": "2007-10-18T11:26:55Z",
    "labels": [
        "linear algebra",
        "trivial",
        "enhancement"
    ],
    "title": "[with patch] Matrix.minors",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/917",
    "user": "malb"
}
```
Assignee: was

The attached patch implements a method to return the list of all k-minors of a matrix A.

Let A be an m x n matrix and k an integer with 0 < k, k <= m, and
k <= n. A k x k minor of A is the determinant of a k x k matrix
obtained from A by deleting m - k rows and n - k columns.

The returned list is sorted in lexicographical row major ordering,
e.g., if A is a 3 x 3 matrix then the minors returned are with
for these rows/columns:  [ [0, 1]x[0, 1], [0, 1]x[0, 2],
[0, 1]x[1, 2], [0, 2]x[0, 1], [0, 2]x[0, 2], [0, 2]x[1, 2],
[1, 2]x[0, 1], [1, 2]x[0, 2], [1, 2]x[1, 2] ].

Note I am not sure if this method is too trivial or too specialised to be included with SAGE. I am submitting it here such that others can decide on that.

Issue created by migration from https://trac.sagemath.org/ticket/917





---

archive/issue_comments_005629.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-21T01:15:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/917",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/917#issuecomment-5629",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_005630.json:
```json
{
    "body": "Attachment\n\nThis should definitely go in.",
    "created_at": "2007-10-21T01:15:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/917",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/917#issuecomment-5630",
    "user": "was"
}
```

Attachment

This should definitely go in.
