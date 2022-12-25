# Issue 3412: sage-3.0.3.alpha2 -- two files that are ? in repo in fresh build

archive/issues_003412.json:
```json
{
    "body": "Assignee: cwitty\n\nAfter building sage-3.0.3.alpha2:\n\n```\nsage: hg_sage()\ncd \"/home/was/build/sage-3.0.3.alpha2/devel/sage\" && hg status\n? sage/misc/allocator.h\n? sage/server/notebook/a.txt\n0\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/3412\n\n",
    "created_at": "2008-06-13T14:16:21Z",
    "labels": [
        "component: misc",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.3",
    "title": "sage-3.0.3.alpha2 -- two files that are ? in repo in fresh build",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3412",
    "user": "https://github.com/williamstein"
}
```
Assignee: cwitty

After building sage-3.0.3.alpha2:

```
sage: hg_sage()
cd "/home/was/build/sage-3.0.3.alpha2/devel/sage" && hg status
? sage/misc/allocator.h
? sage/server/notebook/a.txt
0
```

Issue created by migration from https://trac.sagemath.org/ticket/3412





---

archive/issue_comments_023883.json:
```json
{
    "body": "This is the real blocker for 3.0.3 without somebody working on this as far as I know.\n\nCheers,\n\nMichael",
    "created_at": "2008-06-15T19:10:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3412",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3412#issuecomment-23883",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This is the real blocker for 3.0.3 without somebody working on this as far as I know.

Cheers,

Michael



---

archive/issue_events_007693.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-06-15T19:10:48Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3412",
    "milestone": "sage-3.0.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3412#event-7693"
}
```



---

archive/issue_comments_023884.json:
```json
{
    "body": "Attachment [sage-3412.patch](tarball://root/attachments/some-uuid/ticket3412/sage-3412.patch) by @williamstein created at 2008-06-16 04:15:57",
    "created_at": "2008-06-16T04:15:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3412",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3412#issuecomment-23884",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-3412.patch](tarball://root/attachments/some-uuid/ticket3412/sage-3412.patch) by @williamstein created at 2008-06-16 04:15:57



---

archive/issue_comments_023885.json:
```json
{
    "body": "Patch looks good to me. There is another file in tree after running doctests, but we will deal with that one on a different ticket. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-06-16T18:29:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3412",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3412#issuecomment-23885",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Patch looks good to me. There is another file in tree after running doctests, but we will deal with that one on a different ticket. Positive review.

Cheers,

Michael



---

archive/issue_comments_023886.json:
```json
{
    "body": "Merged in Sage 3.0.3.rc0",
    "created_at": "2008-06-16T18:30:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3412",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3412#issuecomment-23886",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.3.rc0



---

archive/issue_comments_023887.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-16T18:30:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3412",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3412#issuecomment-23887",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_007694.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-06-16T18:30:07Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3412",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3412#event-7694"
}
```
