# Issue 5434: [with patch, needs review] .shift() of a zero polynomial is broken

archive/issues_005434.json:
```json
{
    "body": "Assignee: cwitty\n\n\n```\nsage: K.<x> = RDF[]\nsage: K(0).shift(3).is_zero()\nFalse\nsage: K.<x> = RR[]\nsage: K(0).shift(3).is_zero()\nFalse\nsage: K.<x> = AA[]\nsage: K(0).shift(3).is_zero()\nFalse\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5434\n\n",
    "created_at": "2009-03-04T04:02:25Z",
    "labels": [
        "basic arithmetic",
        "critical",
        "bug"
    ],
    "title": "[with patch, needs review] .shift() of a zero polynomial is broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5434",
    "user": "cwitty"
}
```
Assignee: cwitty


```
sage: K.<x> = RDF[]
sage: K(0).shift(3).is_zero()
False
sage: K.<x> = RR[]
sage: K(0).shift(3).is_zero()
False
sage: K.<x> = AA[]
sage: K(0).shift(3).is_zero()
False
```



Issue created by migration from https://trac.sagemath.org/ticket/5434





---

archive/issue_comments_042042.json:
```json
{
    "body": "Attachment\n\nExcellent.  Thanks!",
    "created_at": "2009-03-04T07:04:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5434#issuecomment-42042",
    "user": "was"
}
```

Attachment

Excellent.  Thanks!



---

archive/issue_comments_042043.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-05T00:07:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5434#issuecomment-42043",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_042044.json:
```json
{
    "body": "Merged in Sage 3.4.rc1.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-05T00:07:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5434#issuecomment-42044",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.rc1.

Cheers,

Michael
