# Issue 916: [with patch] remove structure.sequence._combinations

archive/issues_000916.json:
```json
{
    "body": "Assignee: @malb\n\nCC:  sage-combinat\n\n`_combinations` does the same as `combinations_iterator` but is slower. The attached patch therefor removes it and replaces all calls to it by calls to `combinations_iterator`.\n\n```\nsage: time l1 = list(combinations_iterator(range(100),3))\nCPU times: user 0.91 s, sys: 0.01 s, total: 0.91 s\nWall time: 0.93\nsage: time l2 = list(_combinations(range(100),3))\nCPU times: user 3.96 s, sys: 0.13 s, total: 4.09 s\nWall time: 4.13\nsage: l1 == l2\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/916\n\n",
    "closed_at": "2007-10-23T19:46:34Z",
    "created_at": "2007-10-18T11:10:39Z",
    "labels": [
        "component: combinatorics",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.9",
    "title": "[with patch] remove structure.sequence._combinations",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/916",
    "user": "https://github.com/malb"
}
```
Assignee: @malb

CC:  sage-combinat

`_combinations` does the same as `combinations_iterator` but is slower. The attached patch therefor removes it and replaces all calls to it by calls to `combinations_iterator`.

```
sage: time l1 = list(combinations_iterator(range(100),3))
CPU times: user 0.91 s, sys: 0.01 s, total: 0.91 s
Wall time: 0.93
sage: time l2 = list(_combinations(range(100),3))
CPU times: user 3.96 s, sys: 0.13 s, total: 4.09 s
Wall time: 4.13
sage: l1 == l2
```

Issue created by migration from https://trac.sagemath.org/ticket/916





---

archive/issue_comments_005606.json:
```json
{
    "body": "Attachment [combinations.patch](tarball://root/attachments/some-uuid/ticket916/combinations.patch) by @williamstein created at 2007-10-21 03:35:46",
    "created_at": "2007-10-21T03:35:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/916",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/916#issuecomment-5606",
    "user": "https://github.com/williamstein"
}
```

Attachment [combinations.patch](tarball://root/attachments/some-uuid/ticket916/combinations.patch) by @williamstein created at 2007-10-21 03:35:46



---

archive/issue_events_002525.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-10-21T03:35:46Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/916",
    "milestone": "sage-2.8.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/916#event-2525"
}
```



---

archive/issue_comments_005607.json:
```json
{
    "body": "Changing assignee from @williamstein to @malb.",
    "created_at": "2007-10-21T22:44:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/916",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/916#issuecomment-5607",
    "user": "https://github.com/malb"
}
```

Changing assignee from @williamstein to @malb.



---

archive/issue_comments_005608.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-10-21T22:44:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/916",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/916#issuecomment-5608",
    "user": "https://github.com/malb"
}
```

Changing status from new to assigned.



---

archive/issue_events_002526.json:
```json
{
    "actor": "https://github.com/malb",
    "created_at": "2007-10-23T19:46:34Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/916",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/916#event-2526"
}
```



---

archive/issue_comments_005609.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-23T19:46:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/916",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/916#issuecomment-5609",
    "user": "https://github.com/malb"
}
```

Resolution: fixed



---

archive/issue_comments_005610.json:
```json
{
    "body": "applied to 2.8.9.alpha0",
    "created_at": "2007-10-23T19:46:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/916",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/916#issuecomment-5610",
    "user": "https://github.com/malb"
}
```

applied to 2.8.9.alpha0
