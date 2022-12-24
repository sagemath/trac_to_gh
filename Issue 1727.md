# Issue 1727: truth value of inequalities not as expected

archive/issues_001727.json:
```json
{
    "body": "Assignee: @williamstein\n\nAs reported by ncalexan on IRC:\n\n\n```\nsage: bool(x == x)\nTrue\nsage: bool(x != x)\nTrue\nsage: bool(x > x)\nTrue\n```\n\n\nThis appears to be caused by `SymbolicEquation.__nonzero__()` assuming in various places that the operator of the equation is ==.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1727\n\n",
    "created_at": "2008-01-09T00:47:29Z",
    "labels": [
        "calculus",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10",
    "title": "truth value of inequalities not as expected",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1727",
    "user": "@wjp"
}
```
Assignee: @williamstein

As reported by ncalexan on IRC:


```
sage: bool(x == x)
True
sage: bool(x != x)
True
sage: bool(x > x)
True
```


This appears to be caused by `SymbolicEquation.__nonzero__()` assuming in various places that the operator of the equation is ==.

Issue created by migration from https://trac.sagemath.org/ticket/1727





---

archive/issue_comments_010932.json:
```json
{
    "body": "This is really serious.",
    "created_at": "2008-01-09T04:16:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1727#issuecomment-10932",
    "user": "@williamstein"
}
```

This is really serious.



---

archive/issue_comments_010933.json:
```json
{
    "body": "Changing priority from major to critical.",
    "created_at": "2008-01-09T04:16:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1727#issuecomment-10933",
    "user": "@williamstein"
}
```

Changing priority from major to critical.



---

archive/issue_comments_010934.json:
```json
{
    "body": "Changing assignee from @williamstein to @mwhansen.",
    "created_at": "2008-01-16T04:54:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1727#issuecomment-10934",
    "user": "@mwhansen"
}
```

Changing assignee from @williamstein to @mwhansen.



---

archive/issue_comments_010935.json:
```json
{
    "body": "Attachment [1727.patch](tarball://root/attachments/some-uuid/ticket1727/1727.patch) by @mwhansen created at 2008-01-16 04:54:52",
    "created_at": "2008-01-16T04:54:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1727#issuecomment-10935",
    "user": "@mwhansen"
}
```

Attachment [1727.patch](tarball://root/attachments/some-uuid/ticket1727/1727.patch) by @mwhansen created at 2008-01-16 04:54:52



---

archive/issue_comments_010936.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-16T04:54:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1727#issuecomment-10936",
    "user": "@mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_010937.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-01-16T05:09:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1727#issuecomment-10937",
    "user": "mabshoff"
}
```

Looks good to me.



---

archive/issue_comments_010938.json:
```json
{
    "body": "Merged in Sage 2.10.alpha4",
    "created_at": "2008-01-16T05:16:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1727#issuecomment-10938",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.alpha4



---

archive/issue_comments_010939.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-16T05:16:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1727#issuecomment-10939",
    "user": "mabshoff"
}
```

Resolution: fixed
