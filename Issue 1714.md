# Issue 1714: [with patch, needs review] allow keyword arguments for remote sage methods (sage0)

archive/issues_001714.json:
```json
{
    "body": "Assignee: @williamstein\n\nkeyword arguments were not passed through to the remote sage instance now they are.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1714\n\n",
    "created_at": "2008-01-07T15:37:02Z",
    "labels": [
        "component: interfaces",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "[with patch, needs review] allow keyword arguments for remote sage methods (sage0)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1714",
    "user": "https://github.com/malb"
}
```
Assignee: @williamstein

keyword arguments were not passed through to the remote sage instance now they are.

Issue created by migration from https://trac.sagemath.org/ticket/1714





---

archive/issue_comments_010837.json:
```json
{
    "body": "Attachment [sage0_keywords.patch](tarball://root/attachments/some-uuid/ticket1714/sage0_keywords.patch) by mabshoff created at 2008-01-21 05:55:55\n\nSince #1843 has been merged this patch needs to be revisited now.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-21T05:55:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1714#issuecomment-10837",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [sage0_keywords.patch](tarball://root/attachments/some-uuid/ticket1714/sage0_keywords.patch) by mabshoff created at 2008-01-21 05:55:55

Since #1843 has been merged this patch needs to be revisited now.

Cheers,

Michael



---

archive/issue_comments_010838.json:
```json
{
    "body": "rebased patch against 2.10.1.rc2 (without cputime method)",
    "created_at": "2008-01-29T16:24:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1714#issuecomment-10838",
    "user": "https://github.com/malb"
}
```

rebased patch against 2.10.1.rc2 (without cputime method)



---

archive/issue_comments_010839.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2008-01-29T16:24:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1714#issuecomment-10839",
    "user": "https://github.com/malb"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_010840.json:
```json
{
    "body": "Attachment [sage0_keywords.2.patch](tarball://root/attachments/some-uuid/ticket1714/sage0_keywords.2.patch) by @malb created at 2008-01-29 16:24:52\n\nThe new attached patch `sage0_keywords.2.patch` which replaces the old patch applies cleanly against `2.10.1.rc2`.",
    "created_at": "2008-01-29T16:24:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1714#issuecomment-10840",
    "user": "https://github.com/malb"
}
```

Attachment [sage0_keywords.2.patch](tarball://root/attachments/some-uuid/ticket1714/sage0_keywords.2.patch) by @malb created at 2008-01-29 16:24:52

The new attached patch `sage0_keywords.2.patch` which replaces the old patch applies cleanly against `2.10.1.rc2`.



---

archive/issue_comments_010841.json:
```json
{
    "body": "Second patch looks fine, I say apply.\n\nThere are no docstrings, but is this code even doctested?  I don't know.",
    "created_at": "2008-02-14T23:38:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1714#issuecomment-10841",
    "user": "https://github.com/ncalexan"
}
```

Second patch looks fine, I say apply.

There are no docstrings, but is this code even doctested?  I don't know.



---

archive/issue_comments_010842.json:
```json
{
    "body": "Merged sage0_keywords.2.patch in Sage 2.10.2.alpha0",
    "created_at": "2008-02-15T00:24:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1714#issuecomment-10842",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged sage0_keywords.2.patch in Sage 2.10.2.alpha0



---

archive/issue_events_001873.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-02-15T00:24:38Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1714",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1714#event-1873"
}
```



---

archive/issue_comments_010843.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-15T00:24:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1714#issuecomment-10843",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
