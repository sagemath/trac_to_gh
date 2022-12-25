# Issue 2414: there should be a conversion from X.fraction_field() to X (esp. for multivariate polynomials)

archive/issues_002414.json:
```json
{
    "body": "Assignee: somebody\n\n\n```\nsage: R.<x,y> = QQ[]\nsage: R(x/y*y)\n```\n\ngoes boom; it should return x.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2414\n\n",
    "created_at": "2008-03-07T02:29:19Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "there should be a conversion from X.fraction_field() to X (esp. for multivariate polynomials)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2414",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
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

archive/issue_comments_016250.json:
```json
{
    "body": "I cannot reproduce this in 2.10.4.  Has it really just been fixed in the last two weeks?",
    "created_at": "2008-03-19T12:26:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2414#issuecomment-16250",
    "user": "https://trac.sagemath.org/admin/accounts/users/jbmohler"
}
```

I cannot reproduce this in 2.10.4.  Has it really just been fixed in the last two weeks?



---

archive/issue_comments_016251.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-21T06:20:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2414#issuecomment-16251",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Resolution: fixed



---

archive/issue_comments_016252.json:
```json
{
    "body": "Yes, this example was fixed in 2.10.3 by #1186, and I can't find any other examples with problems, so I'm declaring this bug fixed.",
    "created_at": "2008-03-21T06:20:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2414#issuecomment-16252",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Yes, this example was fixed in 2.10.3 by #1186, and I can't find any other examples with problems, so I'm declaring this bug fixed.



---

archive/issue_events_002590.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/cwitty",
    "created_at": "2008-03-21T06:20:03Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2414",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2414#event-2590"
}
```
