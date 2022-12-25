# Issue 8277: Using matrix() to convert between sparse and dense.

archive/issues_008277.json:
```json
{
    "body": "Assignee: @hivert\n\nKeywords: sparse matrix conversion\n\nA call to `matrix` does not change the sparsity:\n\n```\n    sage: mat = matrix(ZZ, [[1,1],[1,1]], sparse=False)\n    sage: type(mat)\n    <type 'sage.matrix.matrix_integer_dense.Matrix_integer_dense'>\n    sage: mat2 = matrix(ZZ, mat, sparse=True)\n    sage: type(mat2)\n    <type 'sage.matrix.matrix_integer_dense.Matrix_integer_dense'>\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8277\n\n",
    "created_at": "2010-02-15T22:01:08Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-8.2",
    "title": "Using matrix() to convert between sparse and dense.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8277",
    "user": "https://github.com/hivert"
}
```
Assignee: @hivert

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

archive/issue_comments_073174.json:
```json
{
    "body": "Changing component from algebra to linear algebra.",
    "created_at": "2010-09-02T10:50:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8277",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8277#issuecomment-73174",
    "user": "https://github.com/aghitza"
}
```

Changing component from algebra to linear algebra.



---

archive/issue_events_019800.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8277",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8277#event-19800"
}
```



---

archive/issue_events_019801.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8277",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8277#event-19801"
}
```



---

archive/issue_events_019802.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8277",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8277#event-19802"
}
```



---

archive/issue_events_019803.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8277",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8277#event-19803"
}
```



---

archive/issue_events_019804.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8277",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8277#event-19804"
}
```



---

archive/issue_events_019805.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8277",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8277#event-19805"
}
```



---

archive/issue_events_019806.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8277",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8277#event-19806"
}
```



---

archive/issue_events_019807.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2018-03-01T15:00:46Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8277",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8277#event-19807"
}
```



---

archive/issue_events_019808.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2018-03-01T15:00:46Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8277",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8277#event-19808"
}
```



---

archive/issue_events_019809.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2018-03-01T15:00:46Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8277",
    "milestone": "sage-8.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8277#event-19809"
}
```



---

archive/issue_comments_073175.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2018-03-01T15:00:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8277",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8277#issuecomment-73175",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: duplicate



---

archive/issue_comments_073176.json:
```json
{
    "body": "Fixed in #24742.",
    "created_at": "2018-03-01T15:00:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8277",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8277#issuecomment-73176",
    "user": "https://github.com/jdemeyer"
}
```

Fixed in #24742.
