# Issue 4006: [with patch, needs review] Remove unused code in sage/libs/pari/functional.py

archive/issues_004006.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4006\n\n",
    "created_at": "2008-08-30T19:05:49Z",
    "labels": [
        "component: interfaces",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "[with patch, needs review] Remove unused code in sage/libs/pari/functional.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4006",
    "user": "https://github.com/mwhansen"
}
```
Assignee: @williamstein



Issue created by migration from https://trac.sagemath.org/ticket/4006





---

archive/issue_comments_028867.json:
```json
{
    "body": "Attachment [trac_4006.patch](tarball://root/attachments/some-uuid/ticket4006/trac_4006.patch) by @mwhansen created at 2008-08-30 20:01:45\n\nThis code is totally broken due to the imports at the top.  Plus, it's old, untested, and a bit crufty.",
    "created_at": "2008-08-30T20:01:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4006",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4006#issuecomment-28867",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_4006.patch](tarball://root/attachments/some-uuid/ticket4006/trac_4006.patch) by @mwhansen created at 2008-08-30 20:01:45

This code is totally broken due to the imports at the top.  Plus, it's old, untested, and a bit crufty.



---

archive/issue_comments_028868.json:
```json
{
    "body": "Replying to [comment:1 mhansen]:\n> This code is totally broken due to the imports at the top.  Plus, it's old, untested, and a bit crufty.\n\n+1. Should anybody want this code he/she has to resubmit it. It has been broken since at least Sage 0.10.12, so good riddance. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-30T22:24:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4006",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4006#issuecomment-28868",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:1 mhansen]:
> This code is totally broken due to the imports at the top.  Plus, it's old, untested, and a bit crufty.

+1. Should anybody want this code he/she has to resubmit it. It has been broken since at least Sage 0.10.12, so good riddance. Positive review.

Cheers,

Michael



---

archive/issue_events_009176.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-08-30T22:46:20Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4006",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4006#event-9176"
}
```



---

archive/issue_comments_028869.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-30T22:46:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4006",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4006#issuecomment-28869",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_028870.json:
```json
{
    "body": "Merged in Sage 3.1.2.alpha3",
    "created_at": "2008-08-30T22:46:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4006",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4006#issuecomment-28870",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.2.alpha3
