# Issue 1927: dots in symbolic variable names should not be allowed, etc. (probably easy to fix)

archive/issues_001927.json:
```json
{
    "body": "Assignee: was\n\nVariable names made with the var command should be valid identifiers, but\n\n```\nsage: var('.foo')\n.foo\nsage: var('.foo/x')\n.foo/x\n```\n\n\nThanks to janwil for pointing this out. \n\nIssue created by migration from https://trac.sagemath.org/ticket/1927\n\n",
    "created_at": "2008-01-25T17:21:18Z",
    "labels": [
        "calculus",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "dots in symbolic variable names should not be allowed, etc. (probably easy to fix)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1927",
    "user": "was"
}
```
Assignee: was

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

archive/issue_comments_012232.json:
```json
{
    "body": "Changing assignee from was to mhansen.",
    "created_at": "2008-02-01T03:34:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1927",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1927#issuecomment-12232",
    "user": "mhansen"
}
```

Changing assignee from was to mhansen.



---

archive/issue_comments_012233.json:
```json
{
    "body": "Attachment [1927.patch](tarball://root/attachments/some-uuid/ticket1927/1927.patch) by mhansen created at 2008-02-01 03:34:42",
    "created_at": "2008-02-01T03:34:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1927",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1927#issuecomment-12233",
    "user": "mhansen"
}
```

Attachment [1927.patch](tarball://root/attachments/some-uuid/ticket1927/1927.patch) by mhansen created at 2008-02-01 03:34:42



---

archive/issue_comments_012234.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-02-01T03:34:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1927",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1927#issuecomment-12234",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_012235.json:
```json
{
    "body": "Doctests are good.  Apply.",
    "created_at": "2008-02-15T04:42:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1927",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1927#issuecomment-12235",
    "user": "ncalexan"
}
```

Doctests are good.  Apply.



---

archive/issue_comments_012236.json:
```json
{
    "body": "Merged in Sage 2.10.2.alpha0",
    "created_at": "2008-02-15T04:48:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1927",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1927#issuecomment-12236",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.2.alpha0



---

archive/issue_comments_012237.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-15T04:48:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1927",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1927#issuecomment-12237",
    "user": "mabshoff"
}
```

Resolution: fixed
