# Issue 4144: [with patch, needs review] allow finite field elements in SBox constructor

archive/issues_004144.json:
```json
{
    "body": "Assignee: @malb\n\nKeywords: crypto, aes, sbox, mq\n\nmake it so that this works:\n\n\n```\nsage: sr = mq.SR(1,1,1,4, allow_zero_inversions=True)\nsage: S = mq.SBox([sr.sub_byte(e) for e in list(sr.k)])\nsage: S\n(6, 5, 2, 9, 4, 7, 3, 12, 14, 15, 10, 0, 8, 1, 13, 11)\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4144\n\n",
    "created_at": "2008-09-18T10:26:59Z",
    "labels": [
        "component: misc"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.1",
    "title": "[with patch, needs review] allow finite field elements in SBox constructor",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4144",
    "user": "https://github.com/malb"
}
```
Assignee: @malb

Keywords: crypto, aes, sbox, mq

make it so that this works:


```
sage: sr = mq.SR(1,1,1,4, allow_zero_inversions=True)
sage: S = mq.SBox([sr.sub_byte(e) for e in list(sr.k)])
sage: S
(6, 5, 2, 9, 4, 7, 3, 12, 14, 15, 10, 0, 8, 1, 13, 11)
```



Issue created by migration from https://trac.sagemath.org/ticket/4144





---

archive/issue_comments_030027.json:
```json
{
    "body": "Attachment [sbox_gfq.patch](tarball://root/attachments/some-uuid/ticket4144/sbox_gfq.patch) by @malb created at 2008-09-18 10:27:16",
    "created_at": "2008-09-18T10:27:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4144",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4144#issuecomment-30027",
    "user": "https://github.com/malb"
}
```

Attachment [sbox_gfq.patch](tarball://root/attachments/some-uuid/ticket4144/sbox_gfq.patch) by @malb created at 2008-09-18 10:27:16



---

archive/issue_comments_030028.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-09-20T15:47:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4144",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4144#issuecomment-30028",
    "user": "https://github.com/malb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_030029.json:
```json
{
    "body": "The code does something that looks reasonable, and doctests pass.  (I don't know enough crypto to be sure that this is a useful thing to do, so I'm relying on malb for that part.)\n\nPositive review.",
    "created_at": "2008-11-23T02:01:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4144",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4144#issuecomment-30029",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

The code does something that looks reasonable, and doctests pass.  (I don't know enough crypto to be sure that this is a useful thing to do, so I'm relying on malb for that part.)

Positive review.



---

archive/issue_comments_030030.json:
```json
{
    "body": "Merged in Sage 3.2.1.alpha0",
    "created_at": "2008-11-23T07:56:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4144",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4144#issuecomment-30030",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.1.alpha0



---

archive/issue_events_004382.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-11-23T07:56:15Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4144",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4144#event-4382"
}
```



---

archive/issue_comments_030031.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-23T07:56:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4144",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4144#issuecomment-30031",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
