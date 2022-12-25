# Issue 2164: add fast iterator for partitions

archive/issues_002164.json:
```json
{
    "body": "Assignee: @mwhansen\n\nCC:  sage-combinat\n\nwhich only returns lists rather than Partition_class objects.\n\n\nThis is also useful where you don't necessarily need the Partition_class object, you just need the values.\n\n\nBefore the patch:\n\n```\nsage: timeit a = Partitions(40).list()\n10 loops, best of 3: 1.4 s per loop\n```\n\n\nAfter the patch:\n\n```\nsage: timeit a = Partitions(40).list()\n10 loops, best of 3: 280 ms per loop\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2164\n\n",
    "created_at": "2008-02-14T23:15:56Z",
    "labels": [
        "component: combinatorics",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "add fast iterator for partitions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2164",
    "user": "https://github.com/mwhansen"
}
```
Assignee: @mwhansen

CC:  sage-combinat

which only returns lists rather than Partition_class objects.


This is also useful where you don't necessarily need the Partition_class object, you just need the values.


Before the patch:

```
sage: timeit a = Partitions(40).list()
10 loops, best of 3: 1.4 s per loop
```


After the patch:

```
sage: timeit a = Partitions(40).list()
10 loops, best of 3: 280 ms per loop
```


Issue created by migration from https://trac.sagemath.org/ticket/2164





---

archive/issue_comments_014181.json:
```json
{
    "body": "Attachment [2164.patch](tarball://root/attachments/some-uuid/ticket2164/2164.patch) by @mwhansen created at 2008-02-14 23:19:07",
    "created_at": "2008-02-14T23:19:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2164#issuecomment-14181",
    "user": "https://github.com/mwhansen"
}
```

Attachment [2164.patch](tarball://root/attachments/some-uuid/ticket2164/2164.patch) by @mwhansen created at 2008-02-14 23:19:07



---

archive/issue_comments_014182.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-02-14T23:19:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2164#issuecomment-14182",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_014183.json:
```json
{
    "body": "Attachment [2164-2.patch](tarball://root/attachments/some-uuid/ticket2164/2164-2.patch) by @mwhansen created at 2008-02-14 23:53:01",
    "created_at": "2008-02-14T23:53:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2164#issuecomment-14183",
    "user": "https://github.com/mwhansen"
}
```

Attachment [2164-2.patch](tarball://root/attachments/some-uuid/ticket2164/2164-2.patch) by @mwhansen created at 2008-02-14 23:53:01



---

archive/issue_comments_014184.json:
```json
{
    "body": "Apply both patches.",
    "created_at": "2008-02-14T23:53:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2164#issuecomment-14184",
    "user": "https://github.com/mwhansen"
}
```

Apply both patches.



---

archive/issue_comments_014185.json:
```json
{
    "body": "Looks fine to me.",
    "created_at": "2008-02-15T03:39:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2164#issuecomment-14185",
    "user": "https://github.com/ncalexan"
}
```

Looks fine to me.



---

archive/issue_comments_014186.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2008-02-15T03:39:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2164#issuecomment-14186",
    "user": "https://github.com/ncalexan"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_014187.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-15T05:00:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2164#issuecomment-14187",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_014188.json:
```json
{
    "body": "Merged in Sage 2.10.2.alpha0",
    "created_at": "2008-02-15T05:00:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2164#issuecomment-14188",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.2.alpha0
