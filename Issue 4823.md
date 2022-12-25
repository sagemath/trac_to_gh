# Issue 4823: [with patch, needs review]

archive/issues_004823.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @ClementPernet\n\nThe fix at #3887 computes way to many primes, making det and hnf very slow. The attached patch resolves this issue and still gives correct output. \n\nIssue created by migration from https://trac.sagemath.org/ticket/4823\n\n",
    "created_at": "2008-12-18T00:26:15Z",
    "labels": [
        "component: linear algebra",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.2",
    "title": "[with patch, needs review]",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4823",
    "user": "https://github.com/robertwb"
}
```
Assignee: @williamstein

CC:  @ClementPernet

The fix at #3887 computes way to many primes, making det and hnf very slow. The attached patch resolves this issue and still gives correct output. 

Issue created by migration from https://trac.sagemath.org/ticket/4823





---

archive/issue_comments_036496.json:
```json
{
    "body": "Attachment [4823-faster-fix.patch](tarball://root/attachments/some-uuid/ticket4823/4823-faster-fix.patch) by @robertwb created at 2008-12-18 00:27:01",
    "created_at": "2008-12-18T00:27:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4823",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4823#issuecomment-36496",
    "user": "https://github.com/robertwb"
}
```

Attachment [4823-faster-fix.patch](tarball://root/attachments/some-uuid/ticket4823/4823-faster-fix.patch) by @robertwb created at 2008-12-18 00:27:01



---

archive/issue_comments_036497.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-18T00:30:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4823",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4823#issuecomment-36497",
    "user": "https://github.com/ClementPernet"
}
```

Resolution: fixed



---

archive/issue_events_011058.json:
```json
{
    "actor": "https://github.com/ClementPernet",
    "created_at": "2008-12-18T00:30:34Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4823",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4823#event-11058"
}
```



---

archive/issue_comments_036498.json:
```json
{
    "body": "Patch looks correct and passes doctests.",
    "created_at": "2008-12-18T00:30:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4823",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4823#issuecomment-36498",
    "user": "https://github.com/ClementPernet"
}
```

Patch looks correct and passes doctests.



---

archive/issue_comments_036499.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-12-18T00:37:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4823",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4823#issuecomment-36499",
    "user": "https://github.com/craigcitro"
}
```

Changing status from closed to reopened.



---

archive/issue_events_011059.json:
```json
{
    "actor": "https://github.com/craigcitro",
    "created_at": "2008-12-18T00:37:27Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/4823",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4823#event-11059"
}
```



---

archive/issue_comments_036500.json:
```json
{
    "body": "I think we need to leave this as \"open\" until mabshoff merges the patch.",
    "created_at": "2008-12-18T00:37:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4823",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4823#issuecomment-36500",
    "user": "https://github.com/craigcitro"
}
```

I think we need to leave this as "open" until mabshoff merges the patch.



---

archive/issue_comments_036501.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2008-12-18T00:37:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4823",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4823#issuecomment-36501",
    "user": "https://github.com/craigcitro"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_036502.json:
```json
{
    "body": "Changing priority from critical to blocker.",
    "created_at": "2008-12-18T01:12:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4823",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4823#issuecomment-36502",
    "user": "https://github.com/williamstein"
}
```

Changing priority from critical to blocker.



---

archive/issue_comments_036503.json:
```json
{
    "body": "How about a title for this ticket?\n\nCheers,\n\nMichael",
    "created_at": "2008-12-18T06:24:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4823",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4823#issuecomment-36503",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

How about a title for this ticket?

Cheers,

Michael



---

archive/issue_comments_036504.json:
```json
{
    "body": "Merged in Sage 3.2.2.rc2",
    "created_at": "2008-12-18T14:58:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4823",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4823#issuecomment-36504",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.2.rc2



---

archive/issue_events_011060.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-12-18T14:58:40Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4823",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4823#event-11060"
}
```



---

archive/issue_comments_036505.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-18T14:58:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4823",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4823#issuecomment-36505",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
