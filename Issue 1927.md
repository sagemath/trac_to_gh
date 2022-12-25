# Issue 1927: dots in symbolic variable names should not be allowed, etc. (probably easy to fix)

archive/issues_001927.json:
```json
{
    "body": "Assignee: @williamstein\n\nVariable names made with the var command should be valid identifiers, but\n\n```\nsage: var('.foo')\n.foo\nsage: var('.foo/x')\n.foo/x\n```\n\n\nThanks to janwil for pointing this out. \n\nIssue created by migration from https://trac.sagemath.org/ticket/1927\n\n",
    "created_at": "2008-01-25T17:21:18Z",
    "labels": [
        "component: calculus",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "dots in symbolic variable names should not be allowed, etc. (probably easy to fix)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1927",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

Variable names made with the var command should be valid identifiers, but

```
sage: var('.foo')
.foo
sage: var('.foo/x')
.foo/x
```


Thanks to janwil for pointing this out. 

Issue created by migration from https://trac.sagemath.org/ticket/1927





---

archive/issue_comments_012202.json:
```json
{
    "body": "Changing assignee from @williamstein to @mwhansen.",
    "created_at": "2008-02-01T03:34:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1927",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1927#issuecomment-12202",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from @williamstein to @mwhansen.



---

archive/issue_comments_012203.json:
```json
{
    "body": "Attachment [1927.patch](tarball://root/attachments/some-uuid/ticket1927/1927.patch) by @mwhansen created at 2008-02-01 03:34:42",
    "created_at": "2008-02-01T03:34:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1927",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1927#issuecomment-12203",
    "user": "https://github.com/mwhansen"
}
```

Attachment [1927.patch](tarball://root/attachments/some-uuid/ticket1927/1927.patch) by @mwhansen created at 2008-02-01 03:34:42



---

archive/issue_comments_012204.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-02-01T03:34:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1927",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1927#issuecomment-12204",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_012205.json:
```json
{
    "body": "Doctests are good.  Apply.",
    "created_at": "2008-02-15T04:42:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1927",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1927#issuecomment-12205",
    "user": "https://github.com/ncalexan"
}
```

Doctests are good.  Apply.



---

archive/issue_comments_012206.json:
```json
{
    "body": "Merged in Sage 2.10.2.alpha0",
    "created_at": "2008-02-15T04:48:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1927",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1927#issuecomment-12206",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.2.alpha0



---

archive/issue_events_002084.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-02-15T04:48:43Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1927",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1927#event-2084"
}
```



---

archive/issue_comments_012207.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-15T04:48:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1927",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1927#issuecomment-12207",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
