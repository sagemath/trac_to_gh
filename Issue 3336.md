# Issue 3336: DyckWords(n) should use an iterator

archive/issues_003336.json:
```json
{
    "body": "Assignee: ddrake\n\nCC:  sage-combinat\n\nCurrently, DyckWords(n) creates a list, which uses a lot of memory and is slow. See [this sage-devel thread](http://groups.google.com/group/sage-devel/browse_thread/thread/8b739bb399f2e3d4).\n\nIssue created by migration from https://trac.sagemath.org/ticket/3336\n\n",
    "created_at": "2008-05-30T00:44:34Z",
    "labels": [
        "combinatorics",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.3",
    "title": "DyckWords(n) should use an iterator",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3336",
    "user": "ddrake"
}
```
Assignee: ddrake

CC:  sage-combinat

Currently, DyckWords(n) creates a list, which uses a lot of memory and is slow. See [this sage-devel thread](http://groups.google.com/group/sage-devel/browse_thread/thread/8b739bb399f2e3d4).

Issue created by migration from https://trac.sagemath.org/ticket/3336





---

archive/issue_comments_023120.json:
```json
{
    "body": "Patch attached.",
    "created_at": "2008-05-30T06:42:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3336",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3336#issuecomment-23120",
    "user": "ddrake"
}
```

Patch attached.



---

archive/issue_comments_023121.json:
```json
{
    "body": "Attachment [dyckword-3336.patch](tarball://root/attachments/some-uuid/ticket3336/dyckword-3336.patch) by mhansen created at 2008-05-31 03:53:44\n\nLooks good.  Thanks for this Dan!  I also added it to 2144.",
    "created_at": "2008-05-31T03:53:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3336",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3336#issuecomment-23121",
    "user": "mhansen"
}
```

Attachment [dyckword-3336.patch](tarball://root/attachments/some-uuid/ticket3336/dyckword-3336.patch) by mhansen created at 2008-05-31 03:53:44

Looks good.  Thanks for this Dan!  I also added it to 2144.



---

archive/issue_comments_023122.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-31T05:56:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3336",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3336#issuecomment-23122",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_023123.json:
```json
{
    "body": "Merged in Sage 3.0.3.alpha1",
    "created_at": "2008-05-31T05:56:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3336",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3336#issuecomment-23123",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.3.alpha1
