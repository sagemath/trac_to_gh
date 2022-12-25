# Issue 1505: make M4RI a shared library

archive/issues_001505.json:
```json
{
    "body": "Assignee: @malb\n\nWe are not the only ones anymore who use M4RI, PolyBoRi (which deputs in Sage 2.9) also uses M4RI. Thus we should make M4RI a shared library to not duplicate code/memory.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1505\n\n",
    "created_at": "2007-12-14T12:41:26Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9.1",
    "title": "make M4RI a shared library",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1505",
    "user": "https://github.com/malb"
}
```
Assignee: @malb

We are not the only ones anymore who use M4RI, PolyBoRi (which deputs in Sage 2.9) also uses M4RI. Thus we should make M4RI a shared library to not duplicate code/memory.

Issue created by migration from https://trac.sagemath.org/ticket/1505





---

archive/issue_comments_009615.json:
```json
{
    "body": "spkg here:\n\n   http://sage.math.washington.edu/home/malb/pkgs/libm4ri-20071216.spkg\n\nstand-alone shared lib:\n\n   http://sage.math.washington.edu/home/malb/pkgs/libm4ri-1.0.0.tar.gz\n\npatch for Sage:\n\n   attached",
    "created_at": "2007-12-16T15:02:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1505",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1505#issuecomment-9615",
    "user": "https://github.com/malb"
}
```

spkg here:

   http://sage.math.washington.edu/home/malb/pkgs/libm4ri-20071216.spkg

stand-alone shared lib:

   http://sage.math.washington.edu/home/malb/pkgs/libm4ri-1.0.0.tar.gz

patch for Sage:

   attached



---

archive/issue_comments_009616.json:
```json
{
    "body": "Attachment [removing_m4ri.patch](tarball://root/attachments/some-uuid/ticket1505/removing_m4ri.patch) by @malb created at 2007-12-16 15:03:16",
    "created_at": "2007-12-16T15:03:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1505",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1505#issuecomment-9616",
    "user": "https://github.com/malb"
}
```

Attachment [removing_m4ri.patch](tarball://root/attachments/some-uuid/ticket1505/removing_m4ri.patch) by @malb created at 2007-12-16 15:03:16



---

archive/issue_comments_009617.json:
```json
{
    "body": "oh, 'make test' passes on 64-bit Linux.",
    "created_at": "2007-12-16T15:03:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1505",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1505#issuecomment-9617",
    "user": "https://github.com/malb"
}
```

oh, 'make test' passes on 64-bit Linux.



---

archive/issue_events_001659.json:
```json
{
    "actor": "@rlmill",
    "created_at": "2007-12-22T18:53:22Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1505",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1505#event-1659"
}
```



---

archive/issue_comments_009618.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-22T18:53:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1505",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1505#issuecomment-9618",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed



---

archive/issue_comments_009619.json:
```json
{
    "body": "merged in 2.9.1 rc0",
    "created_at": "2007-12-22T18:53:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1505",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1505#issuecomment-9619",
    "user": "https://github.com/rlmill"
}
```

merged in 2.9.1 rc0
