# Issue 3064: empty matrices: density() function throws a ZeroDivisionError

archive/issues_003064.json:
```json
{
    "body": "Assignee: was\n\n\n```\nsage: a = matrix([])\n\nsage: a.density()\n---------------------------------------------------------------------------\n\n\n<type 'exceptions.ZeroDivisionError'>: Rational division by zero\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3064\n\n",
    "created_at": "2008-04-30T15:12:48Z",
    "labels": [
        "linear algebra",
        "major",
        "bug"
    ],
    "title": "empty matrices: density() function throws a ZeroDivisionError",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3064",
    "user": "dfdeshom"
}
```
Assignee: was


```
sage: a = matrix([])

sage: a.density()
---------------------------------------------------------------------------


<type 'exceptions.ZeroDivisionError'>: Rational division by zero
```


Issue created by migration from https://trac.sagemath.org/ticket/3064





---

archive/issue_comments_021152.json:
```json
{
    "body": "Attachment\n\nPatch attached.",
    "created_at": "2008-04-30T18:17:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3064#issuecomment-21152",
    "user": "dfdeshom"
}
```

Attachment

Patch attached.



---

archive/issue_comments_021153.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-01T05:45:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3064#issuecomment-21153",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_021154.json:
```json
{
    "body": "Merged in Sage 3.0.1.alpha1",
    "created_at": "2008-05-01T05:45:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3064#issuecomment-21154",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.1.alpha1
