# Issue 5476: dimension of jacobian of curves broken

archive/issues_005476.json:
```json
{
    "body": "Assignee: was\n\n\n```\nsage: k.<a> = GF(9); R.<x> = k[]\nsage: HyperellipticCurve(x^3 + x - 1, x+a).jacobian().dimension()\nboom!\n```\n\n\nThis was found during Alex G.'s talk at Sage Days 14.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5476\n\n",
    "created_at": "2009-03-10T22:02:08Z",
    "labels": [
        "algebraic geometry",
        "major",
        "bug"
    ],
    "title": "dimension of jacobian of curves broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5476",
    "user": "was"
}
```
Assignee: was


```
sage: k.<a> = GF(9); R.<x> = k[]
sage: HyperellipticCurve(x^3 + x - 1, x+a).jacobian().dimension()
boom!
```


This was found during Alex G.'s talk at Sage Days 14.

Issue created by migration from https://trac.sagemath.org/ticket/5476





---

archive/issue_comments_042477.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-03-10T22:03:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5476#issuecomment-42477",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_042478.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-03-11T03:30:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5476#issuecomment-42478",
    "user": "mhansen"
}
```

Looks good to me.



---

archive/issue_comments_042479.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-11T03:45:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5476#issuecomment-42479",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_042480.json:
```json
{
    "body": "Merged in Sage 3.4.final.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-11T03:45:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5476#issuecomment-42480",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.final.

Cheers,

Michael
