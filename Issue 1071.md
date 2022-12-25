# Issue 1071: [with patch] IntegerVectors_nk

archive/issues_001071.json:
```json
{
    "body": "Assignee: @mwhansen\n\nCC:  sage-combinat\n\ncalling IntegerVectors.list after applying the attached patch is much faster now.\n\nold:\n\n```\nsage: time l1 = map(tuple, IntegerVectors(2, 60).list())\nCPU time: 5.01 s,  Wall time: 5.11 s\n```\n\n\nnew:\n\n```\nsage: time l1 = map(tuple, IntegerVectors(2, 60).list())\nCPU time: 0.20 s,  Wall time: 0.20 s\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1071\n\n",
    "created_at": "2007-11-02T22:48:35Z",
    "labels": [
        "component: combinatorics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.12",
    "title": "[with patch] IntegerVectors_nk",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1071",
    "user": "https://github.com/malb"
}
```
Assignee: @mwhansen

CC:  sage-combinat

calling IntegerVectors.list after applying the attached patch is much faster now.

old:

```
sage: time l1 = map(tuple, IntegerVectors(2, 60).list())
CPU time: 5.01 s,  Wall time: 5.11 s
```


new:

```
sage: time l1 = map(tuple, IntegerVectors(2, 60).list())
CPU time: 0.20 s,  Wall time: 0.20 s
```



Issue created by migration from https://trac.sagemath.org/ticket/1071





---

archive/issue_comments_006466.json:
```json
{
    "body": "Attachment [iv.patch](tarball://root/attachments/some-uuid/ticket1071/iv.patch) by @malb created at 2007-11-02 22:49:03",
    "created_at": "2007-11-02T22:49:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1071",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1071#issuecomment-6466",
    "user": "https://github.com/malb"
}
```

Attachment [iv.patch](tarball://root/attachments/some-uuid/ticket1071/iv.patch) by @malb created at 2007-11-02 22:49:03



---

archive/issue_comments_006467.json:
```json
{
    "body": "Attachment [1071.patch](tarball://root/attachments/some-uuid/ticket1071/1071.patch) by @mwhansen created at 2007-11-03 18:29:48",
    "created_at": "2007-11-03T18:29:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1071",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1071#issuecomment-6467",
    "user": "https://github.com/mwhansen"
}
```

Attachment [1071.patch](tarball://root/attachments/some-uuid/ticket1071/1071.patch) by @mwhansen created at 2007-11-03 18:29:48



---

archive/issue_comments_006468.json:
```json
{
    "body": "Updated patch attached.",
    "created_at": "2007-11-03T18:30:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1071",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1071#issuecomment-6468",
    "user": "https://github.com/mwhansen"
}
```

Updated patch attached.



---

archive/issue_comments_006469.json:
```json
{
    "body": "Please note that the cleaner version by mhansen is by a factor of three than the original submission:\n\n```\nthe untouched implementation\nsage: time l1 = map(tuple, IntegerVectors(2, 60).list())\nCPU times: user 5.06 s, sys: 0.11 s, total: 5.18 s\nWall time: 5.18\n```\n\n\nmhansen's implementation\n\n```\nsage: time l1 = map(tuple, IntegerVectors(2, 60, min_part=0).list())\nCPU time: 0.56 s,  Wall time: 0.57 s\n```\n\n\nmalb's original submission\n\n```\nsage: time l1 = map(tuple, IntegerVectors(2, 60).list())\nCPU time: 0.20 s,  Wall time: 0.20 s\n```\n\n\nI don't mean to push my original patch (which's problems were fixed by mhansen) but propose to optimise mhansen's patch eventually.",
    "created_at": "2007-11-05T11:04:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1071",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1071#issuecomment-6469",
    "user": "https://github.com/malb"
}
```

Please note that the cleaner version by mhansen is by a factor of three than the original submission:

```
the untouched implementation
sage: time l1 = map(tuple, IntegerVectors(2, 60).list())
CPU times: user 5.06 s, sys: 0.11 s, total: 5.18 s
Wall time: 5.18
```


mhansen's implementation

```
sage: time l1 = map(tuple, IntegerVectors(2, 60, min_part=0).list())
CPU time: 0.56 s,  Wall time: 0.57 s
```


malb's original submission

```
sage: time l1 = map(tuple, IntegerVectors(2, 60).list())
CPU time: 0.20 s,  Wall time: 0.20 s
```


I don't mean to push my original patch (which's problems were fixed by mhansen) but propose to optimise mhansen's patch eventually.



---

archive/issue_events_001193.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-11-06T22:19:50Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1071",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1071#event-1193"
}
```



---

archive/issue_comments_006470.json:
```json
{
    "body": "applied mhansen's patch to 2.8.12.rc0",
    "created_at": "2007-11-06T22:19:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1071",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1071#issuecomment-6470",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

applied mhansen's patch to 2.8.12.rc0



---

archive/issue_comments_006471.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-06T22:19:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1071",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1071#issuecomment-6471",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_006472.json:
```json
{
    "body": "Attachment [1071-final.patch](tarball://root/attachments/some-uuid/ticket1071/1071-final.patch) by @mwhansen created at 2007-11-06 23:19:27",
    "created_at": "2007-11-06T23:19:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1071",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1071#issuecomment-6472",
    "user": "https://github.com/mwhansen"
}
```

Attachment [1071-final.patch](tarball://root/attachments/some-uuid/ticket1071/1071-final.patch) by @mwhansen created at 2007-11-06 23:19:27



---

archive/issue_comments_006473.json:
```json
{
    "body": "Attachment [1071-final.2.patch](tarball://root/attachments/some-uuid/ticket1071/1071-final.2.patch) by @nthiery created at 2009-04-14 02:23:24",
    "created_at": "2009-04-14T02:23:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1071",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1071#issuecomment-6473",
    "user": "https://github.com/nthiery"
}
```

Attachment [1071-final.2.patch](tarball://root/attachments/some-uuid/ticket1071/1071-final.2.patch) by @nthiery created at 2009-04-14 02:23:24
