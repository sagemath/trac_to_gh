# Issue 2414: there should be a conversion from X.fraction_field() to X (esp. for multivariate polynomials)

archive/issues_002414.json:
```json
{
    "body": "Assignee: somebody\n\n\n```\nsage: R.<x,y> = QQ[]\nsage: R(x/y*y)\n```\n\ngoes boom; it should return x.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2414\n\n",
    "created_at": "2008-03-07T02:29:19Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "there should be a conversion from X.fraction_field() to X (esp. for multivariate polynomials)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2414",
    "user": "cwitty"
}
```
Assignee: somebody


```
sage: R.<x,y> = QQ[]
sage: R(x/y*y)
```

goes boom; it should return x.

Issue created by migration from https://trac.sagemath.org/ticket/2414





---

archive/issue_comments_016285.json:
```json
{
    "body": "I cannot reproduce this in 2.10.4.  Has it really just been fixed in the last two weeks?",
    "created_at": "2008-03-19T12:26:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2414#issuecomment-16285",
    "user": "jbmohler"
}
```

I cannot reproduce this in 2.10.4.  Has it really just been fixed in the last two weeks?



---

archive/issue_comments_016286.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-21T06:20:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2414#issuecomment-16286",
    "user": "cwitty"
}
```

Resolution: fixed



---

archive/issue_comments_016287.json:
```json
{
    "body": "Yes, this example was fixed in 2.10.3 by #1186, and I can't find any other examples with problems, so I'm declaring this bug fixed.",
    "created_at": "2008-03-21T06:20:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2414#issuecomment-16287",
    "user": "cwitty"
}
```

Yes, this example was fixed in 2.10.3 by #1186, and I can't find any other examples with problems, so I'm declaring this bug fixed.
