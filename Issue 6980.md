# Issue 6980: add _nonzero_positions_by_column to sparse integer matrices

archive/issues_006980.json:
```json
{
    "body": "Assignee: was\n\nwe still use the dense version:\n\n```\nsage: time matrix(ZZ,5000,sparse=True)._nonzero_positions_by_column()\nCPU times: user 5.12 s, sys: 0.01 s, total: 5.14 s\nWall time: 5.19 s\n[]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6980\n\n",
    "created_at": "2009-09-21T22:20:34Z",
    "labels": [
        "linear algebra",
        "minor",
        "enhancement"
    ],
    "title": "add _nonzero_positions_by_column to sparse integer matrices",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6980",
    "user": "ylchapuy"
}
```
Assignee: was

we still use the dense version:

```
sage: time matrix(ZZ,5000,sparse=True)._nonzero_positions_by_column()
CPU times: user 5.12 s, sys: 0.01 s, total: 5.14 s
Wall time: 5.19 s
[]
```


Issue created by migration from https://trac.sagemath.org/ticket/6980





---

archive/issue_comments_057729.json:
```json
{
    "body": "Attachment\n\nAfter patching, we obtain what is expected:\n\n```\nsage: time matrix(ZZ,5000,sparse=True)._nonzero_positions_by_column()\nCPU times: user 0.01 s, sys: 0.00 s, total: 0.01 s\nWall time: 0.01 s\n[]\n```\n",
    "created_at": "2009-09-21T22:24:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6980#issuecomment-57729",
    "user": "ylchapuy"
}
```

Attachment

After patching, we obtain what is expected:

```
sage: time matrix(ZZ,5000,sparse=True)._nonzero_positions_by_column()
CPU times: user 0.01 s, sys: 0.00 s, total: 0.01 s
Wall time: 0.01 s
[]
```




---

archive/issue_comments_057730.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-25T06:32:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6980#issuecomment-57730",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_057731.json:
```json
{
    "body": "There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.",
    "created_at": "2009-09-27T10:28:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6980#issuecomment-57731",
    "user": "mvngu"
}
```

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
