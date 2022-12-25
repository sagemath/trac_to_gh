# Issue 1407: deciding that generators don't generate an order in some extensions can be way way too slow.

archive/issues_001407.json:
```json
{
    "body": "Assignee: @williamstein\n\nConsider this:\n\n```\nsage: P.<a,b,c> = QQ[2^(1/2), 2^(1/3), 2^(1/5)]\nsage: P.order([1,a])\n*should* go boom very quickly... but runs forever and runs out of RAM\n```\n\nIn the situation above, a satisfies only a quadratic polynomial so \nthere is no possible way it will generate an order in a degree 8 field,\nsince the index [O_K : ZZ[a]] is clearly infinite.   Sage should\nquickly detect this and give an error message, but doesn't for some\nreason. \n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1407\n\n",
    "created_at": "2007-12-06T04:02:24Z",
    "labels": [
        "component: number theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9",
    "title": "deciding that generators don't generate an order in some extensions can be way way too slow.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1407",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

Consider this:

```
sage: P.<a,b,c> = QQ[2^(1/2), 2^(1/3), 2^(1/5)]
sage: P.order([1,a])
*should* go boom very quickly... but runs forever and runs out of RAM
```

In the situation above, a satisfies only a quadratic polynomial so 
there is no possible way it will generate an order in a degree 8 field,
since the index [O_K : ZZ[a]] is clearly infinite.   Sage should
quickly detect this and give an error message, but doesn't for some
reason. 


Issue created by migration from https://trac.sagemath.org/ticket/1407





---

archive/issue_comments_009056.json:
```json
{
    "body": "Attachment [trac1407.patch](tarball://root/attachments/some-uuid/ticket1407/trac1407.patch) by @williamstein created at 2007-12-06 15:30:37",
    "created_at": "2007-12-06T15:30:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1407#issuecomment-9056",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac1407.patch](tarball://root/attachments/some-uuid/ticket1407/trac1407.patch) by @williamstein created at 2007-12-06 15:30:37



---

archive/issue_comments_009057.json:
```json
{
    "body": "Attachment [trac_1407-2.patch](tarball://root/attachments/some-uuid/ticket1407/trac_1407-2.patch) by @craigcitro created at 2007-12-15 11:52:34\n\nMinor doctest touchups.",
    "created_at": "2007-12-15T11:52:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1407#issuecomment-9057",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac_1407-2.patch](tarball://root/attachments/some-uuid/ticket1407/trac_1407-2.patch) by @craigcitro created at 2007-12-15 11:52:34

Minor doctest touchups.



---

archive/issue_events_003630.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-15T11:57:19Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1407",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1407#event-3630"
}
```



---

archive/issue_comments_009058.json:
```json
{
    "body": "Merged in 2.9.rc0.",
    "created_at": "2007-12-15T11:57:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1407#issuecomment-9058",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in 2.9.rc0.



---

archive/issue_comments_009059.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-15T11:57:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1407#issuecomment-9059",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
