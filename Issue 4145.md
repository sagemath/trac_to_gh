# Issue 4145: [with patch, needs review] linear codes list function is slow

archive/issues_004145.json:
```json
{
    "body": "Assignee: tbd\n\nBefore:\n\n```\nsage: G = ExtendedBinaryGolayCode()\nsage: time L = G.list()\nCPU times: user 16.24 s, sys: 0.32 s, total: 16.57 s\nWall time: 17.14 s\n```\n\n\nAfter:\n\n```\nsage: G = ExtendedBinaryGolayCode()\nsage: time L = G.list()\nCPU times: user 3.65 s, sys: 0.04 s, total: 3.68 s\nWall time: 3.71 s\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4145\n\n",
    "created_at": "2008-09-18T15:05:53Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.3",
    "title": "[with patch, needs review] linear codes list function is slow",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4145",
    "user": "https://github.com/rlmill"
}
```
Assignee: tbd

Before:

```
sage: G = ExtendedBinaryGolayCode()
sage: time L = G.list()
CPU times: user 16.24 s, sys: 0.32 s, total: 16.57 s
Wall time: 17.14 s
```


After:

```
sage: G = ExtendedBinaryGolayCode()
sage: time L = G.list()
CPU times: user 3.65 s, sys: 0.04 s, total: 3.68 s
Wall time: 3.71 s
```


Issue created by migration from https://trac.sagemath.org/ticket/4145





---

archive/issue_comments_030032.json:
```json
{
    "body": "Attachment [trac_4145-lin-codes-slow.patch](tarball://root/attachments/some-uuid/ticket4145/trac_4145-lin-codes-slow.patch) by @rlmill created at 2008-09-18 15:47:33\n\nThis may actually be a bugfix, see:\nhttp://trac.sagemath.org/sage_trac/ticket/4115#comment:13",
    "created_at": "2008-09-18T15:47:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4145",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4145#issuecomment-30032",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac_4145-lin-codes-slow.patch](tarball://root/attachments/some-uuid/ticket4145/trac_4145-lin-codes-slow.patch) by @rlmill created at 2008-09-18 15:47:33

This may actually be a bugfix, see:
http://trac.sagemath.org/sage_trac/ticket/4115#comment:13



---

archive/issue_comments_030033.json:
```json
{
    "body": "This is obviously correct (the code is 1 line). I didn't know about the list method for vector spaces but I'd not surprised that that list method is a great deal faster and more efficient that the current LinearCodes one.\n\nI have tested this does fix the comment 13 in #4115. Thanks Robert!",
    "created_at": "2008-09-18T17:07:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4145",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4145#issuecomment-30033",
    "user": "https://github.com/wdjoyner"
}
```

This is obviously correct (the code is 1 line). I didn't know about the list method for vector spaces but I'd not surprised that that list method is a great deal faster and more efficient that the current LinearCodes one.

I have tested this does fix the comment 13 in #4115. Thanks Robert!



---

archive/issue_comments_030034.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-19T00:48:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4145",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4145#issuecomment-30034",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_030035.json:
```json
{
    "body": "Merged in Sage 3.1.3.alpha0",
    "created_at": "2008-09-19T00:48:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4145",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4145#issuecomment-30035",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.3.alpha0



---

archive/issue_events_004383.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-09-19T00:48:07Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4145",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4145#event-4383"
}
```
