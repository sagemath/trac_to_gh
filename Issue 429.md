# Issue 429: cannot create empty sparse matrix over reals

archive/issues_000429.json:
```json
{
    "body": "Assignee: @williamstein\n\nTry:\n\n```\nsage: A = Matrix(RR,2,2,sparse=True) \n<type 'exceptions.TypeError'>: Unable to convert x (='None')\nto real number.\n```\n\nwhile\n\n```\nsage: A = Matrix(GF(127),2,2,sparse=True)\n```\n\nworks.\n\nIssue created by migration from https://trac.sagemath.org/ticket/429\n\n",
    "created_at": "2007-08-15T16:53:44Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.2",
    "title": "cannot create empty sparse matrix over reals",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/429",
    "user": "https://github.com/malb"
}
```
Assignee: @williamstein

Try:

```
sage: A = Matrix(RR,2,2,sparse=True) 
<type 'exceptions.TypeError'>: Unable to convert x (='None')
to real number.
```

while

```
sage: A = Matrix(GF(127),2,2,sparse=True)
```

works.

Issue created by migration from https://trac.sagemath.org/ticket/429





---

archive/issue_comments_002143.json:
```json
{
    "body": "Oh, Complex numbers don't work, too.",
    "created_at": "2007-08-15T16:54:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/429",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/429#issuecomment-2143",
    "user": "https://github.com/malb"
}
```

Oh, Complex numbers don't work, too.



---

archive/issue_comments_002144.json:
```json
{
    "body": "fixed for sage-2.8.2.",
    "created_at": "2007-08-19T01:17:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/429",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/429#issuecomment-2144",
    "user": "https://github.com/williamstein"
}
```

fixed for sage-2.8.2.



---

archive/issue_comments_002145.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-08-19T01:17:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/429",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/429#issuecomment-2145",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_000456.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-08-19T01:17:36Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/429",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/429#event-456"
}
```
