# Issue 3610: __contains__ for RealIntervalFields does not work correctly.

archive/issues_003610.json:
```json
{
    "body": "Assignee: somebody\n\n\n```\nsage: (R(2.1) + R(2.2))^2 in R\nFalse\nsage: R = RealIntervalField(32)\nsage: a = (R(2.1) + R(2.2))^2 \nsage: a\n[18.489999987 .. 18.490000010]\nsage: a in R\nFalse\nsage: a.parent()\nReal Interval Field with 32 bits of precision\nsage: a == a\nFalse\n```\n\n\nThis is caused by the following code in which gets inherited from parent.pyx:\n\n```\n        try:\n            x2 = self(x)\n            return bool(x2 == x)\n        except TypeError:\n            return False\n```\n\n\nSince equality is not reflexive for RealIntervals, this doesn't work as intended.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3610\n\n",
    "created_at": "2008-07-08T17:41:30Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "__contains__ for RealIntervalFields does not work correctly.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3610",
    "user": "mhansen"
}
```
Assignee: somebody


```
sage: (R(2.1) + R(2.2))^2 in R
False
sage: R = RealIntervalField(32)
sage: a = (R(2.1) + R(2.2))^2 
sage: a
[18.489999987 .. 18.490000010]
sage: a in R
False
sage: a.parent()
Real Interval Field with 32 bits of precision
sage: a == a
False
```


This is caused by the following code in which gets inherited from parent.pyx:

```
        try:
            x2 = self(x)
            return bool(x2 == x)
        except TypeError:
            return False
```


Since equality is not reflexive for RealIntervals, this doesn't work as intended.

Issue created by migration from https://trac.sagemath.org/ticket/3610





---

archive/issue_comments_025497.json:
```json
{
    "body": "Attachment [trac3610.patch](tarball://root/attachments/some-uuid/ticket3610/trac3610.patch) by cwitty created at 2009-01-24 03:04:27",
    "created_at": "2009-01-24T03:04:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3610",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3610#issuecomment-25497",
    "user": "cwitty"
}
```

Attachment [trac3610.patch](tarball://root/attachments/some-uuid/ticket3610/trac3610.patch) by cwitty created at 2009-01-24 03:04:27



---

archive/issue_comments_025498.json:
```json
{
    "body": "Looks good to me, and is probably an worthwhile optimization as well.",
    "created_at": "2009-01-24T04:28:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3610",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3610#issuecomment-25498",
    "user": "robertwb"
}
```

Looks good to me, and is probably an worthwhile optimization as well.



---

archive/issue_comments_025499.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-24T19:31:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3610",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3610#issuecomment-25499",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_025500.json:
```json
{
    "body": "Merged in Sage 3.3.alpha2\n\nCheers,\n\nMichael",
    "created_at": "2009-01-24T19:31:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3610",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3610#issuecomment-25500",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha2

Cheers,

Michael
