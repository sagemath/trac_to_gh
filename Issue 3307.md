# Issue 3307: [with patch; needs review] Move genus2reduction to /usr/lib for Debian package

archive/issues_003307.json:
```json
{
    "body": "Assignee: tabbott\n\nI've attached a patch that moves genus2reduction to /usr/lib in my Debian package because it's not a program you run directly and doesn't have a man page.  The patch also fixes all the other minor issues with the package I'm aware of.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3307\n\n",
    "created_at": "2008-05-26T04:24:51Z",
    "labels": [
        "debian-package",
        "blocker",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.3",
    "title": "[with patch; needs review] Move genus2reduction to /usr/lib for Debian package",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3307",
    "user": "tabbott"
}
```
Assignee: tabbott

I've attached a patch that moves genus2reduction to /usr/lib in my Debian package because it's not a program you run directly and doesn't have a man page.  The patch also fixes all the other minor issues with the package I'm aware of.

Issue created by migration from https://trac.sagemath.org/ticket/3307





---

archive/issue_comments_022877.json:
```json
{
    "body": "Attachment [genus2reduction-lib.patch](tarball://root/attachments/some-uuid/ticket3307/genus2reduction-lib.patch) by tabbott created at 2008-05-26 04:25:03",
    "created_at": "2008-05-26T04:25:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3307",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3307#issuecomment-22877",
    "user": "tabbott"
}
```

Attachment [genus2reduction-lib.patch](tarball://root/attachments/some-uuid/ticket3307/genus2reduction-lib.patch) by tabbott created at 2008-05-26 04:25:03



---

archive/issue_comments_022878.json:
```json
{
    "body": "Patch looks good to me. I have slipped it into\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.3/alpha0/genus2reduction-0.3.p3.spkg\n\nwithout incrementing the patch level to avoid rebuilds.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-28T06:41:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3307",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3307#issuecomment-22878",
    "user": "mabshoff"
}
```

Patch looks good to me. I have slipped it into

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.3/alpha0/genus2reduction-0.3.p3.spkg

without incrementing the patch level to avoid rebuilds.

Cheers,

Michael



---

archive/issue_comments_022879.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-28T06:41:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3307",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3307#issuecomment-22879",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_022880.json:
```json
{
    "body": "Merged in Sage 3.0.3.alpha0",
    "created_at": "2008-05-28T06:41:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3307",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3307#issuecomment-22880",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.3.alpha0
