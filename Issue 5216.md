# Issue 5216: Update bzip2 to 1.0.5 release

archive/issues_005216.json:
```json
{
    "body": "Assignee: mabshoff\n\nThis is a security issue:\n\n```\nVersion 1.0.5 removes a potential security vulnerability (CERT-FI 20469 \nas it applies to bzip2) in versions 1.0.4 and earlier, so all users are \nrecommended to upgrade immediately.\n```\n\nand we have been shipping an vulnerable bzip2 release for a while. So upgrade :)\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5216\n\n",
    "created_at": "2009-02-09T12:23:44Z",
    "labels": [
        "component: packages: standard",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "Update bzip2 to 1.0.5 release",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5216",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

This is a security issue:

```
Version 1.0.5 removes a potential security vulnerability (CERT-FI 20469 
as it applies to bzip2) in versions 1.0.4 and earlier, so all users are 
recommended to upgrade immediately.
```

and we have been shipping an vulnerable bzip2 release for a while. So upgrade :)

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/5216





---

archive/issue_comments_039882.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-02-09T12:25:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5216",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5216#issuecomment-39882",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_039883.json:
```json
{
    "body": "Changing status from assigned to new.",
    "created_at": "2009-02-15T06:22:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5216",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5216#issuecomment-39883",
    "user": "https://github.com/mwhansen"
}
```

Changing status from assigned to new.



---

archive/issue_comments_039884.json:
```json
{
    "body": "Changing assignee from mabshoff to @mwhansen.",
    "created_at": "2009-02-15T06:22:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5216",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5216#issuecomment-39884",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from mabshoff to @mwhansen.



---

archive/issue_comments_039885.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-02-15T06:22:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5216",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5216#issuecomment-39885",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_039886.json:
```json
{
    "body": "Attachment [trac_5216-spkg-base.patch](tarball://root/attachments/some-uuid/ticket5216/trac_5216-spkg-base.patch) by mabshoff created at 2009-02-20 14:21:18\n\nThis is Mike's patch slightly modified",
    "created_at": "2009-02-20T14:21:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5216",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5216#issuecomment-39886",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_5216-spkg-base.patch](tarball://root/attachments/some-uuid/ticket5216/trac_5216-spkg-base.patch) by mabshoff created at 2009-02-20 14:21:18

This is Mike's patch slightly modified



---

archive/issue_comments_039887.json:
```json
{
    "body": "The new bzip2 tarball is at\n\n  http://sage.math.washington.edu/home/mabshoff/release-cycles-3.3/rc3/bzip2-1.0.5.tar.gz\n\nNote that we should move the bzip2 code to an spkg soon.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-20T14:22:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5216",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5216#issuecomment-39887",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The new bzip2 tarball is at

  http://sage.math.washington.edu/home/mabshoff/release-cycles-3.3/rc3/bzip2-1.0.5.tar.gz

Note that we should move the bzip2 code to an spkg soon.

Cheers,

Michael



---

archive/issue_comments_039888.json:
```json
{
    "body": "Positive review. Thanks Mike.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-20T14:26:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5216",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5216#issuecomment-39888",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Positive review. Thanks Mike.

Cheers,

Michael



---

archive/issue_comments_039889.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-20T14:26:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5216",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5216#issuecomment-39889",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_039890.json:
```json
{
    "body": "Merged in Sage 3.3.r3.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-20T14:26:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5216",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5216#issuecomment-39890",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.r3.

Cheers,

Michael
