# Issue 5354: [with patch, needs review] stop paying attention to <stdlib.h> RAND_MAX (should fix problems on Solaris)

archive/issues_005354.json:
```json
{
    "body": "Assignee: mabshoff\n\nThe randstate framework always provides 31-bit random numbers regardless of platform, so RAND_MAX should be ignored.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5354\n\n",
    "created_at": "2009-02-24T02:21:00Z",
    "labels": [
        "component: porting: solaris",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4",
    "title": "[with patch, needs review] stop paying attention to <stdlib.h> RAND_MAX (should fix problems on Solaris)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5354",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: mabshoff

The randstate framework always provides 31-bit random numbers regardless of platform, so RAND_MAX should be ignored.

Issue created by migration from https://trac.sagemath.org/ticket/5354





---

archive/issue_comments_041171.json:
```json
{
    "body": "Attachment [ignore-rand-max.patch](tarball://root/attachments/some-uuid/ticket5354/ignore-rand-max.patch) by cwitty created at 2009-02-24 02:21:20",
    "created_at": "2009-02-24T02:21:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5354",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5354#issuecomment-41171",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Attachment [ignore-rand-max.patch](tarball://root/attachments/some-uuid/ticket5354/ignore-rand-max.patch) by cwitty created at 2009-02-24 02:21:20



---

archive/issue_comments_041172.json:
```json
{
    "body": "Nice. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-24T07:15:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5354",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5354#issuecomment-41172",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Nice. Positive review.

Cheers,

Michael



---

archive/issue_comments_041173.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-24T19:50:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5354",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5354#issuecomment-41173",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_041174.json:
```json
{
    "body": "Merged in Sage 3.4.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-24T19:50:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5354",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5354#issuecomment-41174",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.alpha0.

Cheers,

Michael
