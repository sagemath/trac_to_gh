# Issue 1071: [with patch] IntegerVectors_nk

archive/issues_001071.json:
```json
{
    "body": "Assignee: mhansen\n\nCC:  sage-combinat\n\ncalling IntegerVectors.list after applying the attached patch is much faster now.\n\nold:\n\n```\nsage: time l1 = map(tuple, IntegerVectors(2, 60).list())\nCPU time: 5.01 s,  Wall time: 5.11 s\n```\n\n\nnew:\n\n```\nsage: time l1 = map(tuple, IntegerVectors(2, 60).list())\nCPU time: 0.20 s,  Wall time: 0.20 s\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1071\n\n",
    "created_at": "2007-11-02T22:48:35Z",
    "labels": [
        "combinatorics",
        "major",
        "enhancement"
    ],
    "title": "[with patch] IntegerVectors_nk",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1071",
    "user": "malb"
}
```
Assignee: mhansen

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

archive/issue_comments_006486.json:
```json
{
    "body": "Attachment [iv.patch](tarball://root/attachments/some-uuid/ticket1071/iv.patch) by malb created at 2007-11-02 22:49:03",
    "created_at": "2007-11-02T22:49:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1071",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1071#issuecomment-6486",
    "user": "malb"
}
```

Attachment [iv.patch](tarball://root/attachments/some-uuid/ticket1071/iv.patch) by malb created at 2007-11-02 22:49:03



---

archive/issue_comments_006487.json:
```json
{
    "body": "Attachment [1071.patch](tarball://root/attachments/some-uuid/ticket1071/1071.patch) by mhansen created at 2007-11-03 18:29:48",
    "created_at": "2007-11-03T18:29:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1071",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1071#issuecomment-6487",
    "user": "mhansen"
}
```

Attachment [1071.patch](tarball://root/attachments/some-uuid/ticket1071/1071.patch) by mhansen created at 2007-11-03 18:29:48



---

archive/issue_comments_006488.json:
```json
{
    "body": "Updated patch attached.",
    "created_at": "2007-11-03T18:30:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1071",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1071#issuecomment-6488",
    "user": "mhansen"
}
```

Updated patch attached.



---

archive/issue_comments_006489.json:
```json
{
    "body": "Please note that the cleaner version by mhansen is by a factor of three than the original submission:\n\n```\nthe untouched implementation\nsage: time l1 = map(tuple, IntegerVectors(2, 60).list())\nCPU times: user 5.06 s, sys: 0.11 s, total: 5.18 s\nWall time: 5.18\n```\n\n\nmhansen's implementation\n\n```\nsage: time l1 = map(tuple, IntegerVectors(2, 60, min_part=0).list())\nCPU time: 0.56 s,  Wall time: 0.57 s\n```\n\n\nmalb's original submission\n\n```\nsage: time l1 = map(tuple, IntegerVectors(2, 60).list())\nCPU time: 0.20 s,  Wall time: 0.20 s\n```\n\n\nI don't mean to push my original patch (which's problems were fixed by mhansen) but propose to optimise mhansen's patch eventually.",
    "created_at": "2007-11-05T11:04:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1071",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1071#issuecomment-6489",
    "user": "malb"
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

archive/issue_comments_006490.json:
```json
{
    "body": "applied mhansen's patch to 2.8.12.rc0",
    "created_at": "2007-11-06T22:19:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1071",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1071#issuecomment-6490",
    "user": "mabshoff"
}
```

applied mhansen's patch to 2.8.12.rc0



---

archive/issue_comments_006491.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-06T22:19:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1071",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1071#issuecomment-6491",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_006492.json:
```json
{
    "body": "Attachment [1071-final.patch](tarball://root/attachments/some-uuid/ticket1071/1071-final.patch) by mhansen created at 2007-11-06 23:19:27",
    "created_at": "2007-11-06T23:19:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1071",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1071#issuecomment-6492",
    "user": "mhansen"
}
```

Attachment [1071-final.patch](tarball://root/attachments/some-uuid/ticket1071/1071-final.patch) by mhansen created at 2007-11-06 23:19:27



---

archive/issue_comments_006493.json:
```json
{
    "body": "Attachment [1071-final.2.patch](tarball://root/attachments/some-uuid/ticket1071/1071-final.2.patch) by nthiery created at 2009-04-14 02:23:24",
    "created_at": "2009-04-14T02:23:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1071",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1071#issuecomment-6493",
    "user": "nthiery"
}
```

Attachment [1071-final.2.patch](tarball://root/attachments/some-uuid/ticket1071/1071-final.2.patch) by nthiery created at 2009-04-14 02:23:24
