# Issue 5216: Update bzip2 to 1.0.5 release

archive/issues_005216.json:
```json
{
    "body": "Assignee: mabshoff\n\nThis is a security issue:\n\n```\nVersion 1.0.5 removes a potential security vulnerability (CERT-FI 20469 \nas it applies to bzip2) in versions 1.0.4 and earlier, so all users are \nrecommended to upgrade immediately.\n```\n\nand we have been shipping an vulnerable bzip2 release for a while. So upgrade :)\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5216\n\n",
    "created_at": "2009-02-09T12:23:44Z",
    "labels": [
        "packages: standard",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "Update bzip2 to 1.0.5 release",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5216",
    "user": "mabshoff"
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

archive/issue_comments_039960.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-02-09T12:25:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5216",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5216#issuecomment-39960",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_039961.json:
```json
{
    "body": "Changing status from assigned to new.",
    "created_at": "2009-02-15T06:22:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5216",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5216#issuecomment-39961",
    "user": "mhansen"
}
```

Changing status from assigned to new.



---

archive/issue_comments_039962.json:
```json
{
    "body": "Changing assignee from mabshoff to mhansen.",
    "created_at": "2009-02-15T06:22:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5216",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5216#issuecomment-39962",
    "user": "mhansen"
}
```

Changing assignee from mabshoff to mhansen.



---

archive/issue_comments_039963.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-02-15T06:22:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5216",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5216#issuecomment-39963",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_039964.json:
```json
{
    "body": "Attachment [trac_5216-spkg-base.patch](tarball://root/attachments/some-uuid/ticket5216/trac_5216-spkg-base.patch) by mabshoff created at 2009-02-20 14:21:18\n\nThis is Mike's patch slightly modified",
    "created_at": "2009-02-20T14:21:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5216",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5216#issuecomment-39964",
    "user": "mabshoff"
}
```

Attachment [trac_5216-spkg-base.patch](tarball://root/attachments/some-uuid/ticket5216/trac_5216-spkg-base.patch) by mabshoff created at 2009-02-20 14:21:18

This is Mike's patch slightly modified



---

archive/issue_comments_039965.json:
```json
{
    "body": "The new bzip2 tarball is at\n\n  http://sage.math.washington.edu/home/mabshoff/release-cycles-3.3/rc3/bzip2-1.0.5.tar.gz\n\nNote that we should move the bzip2 code to an spkg soon.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-20T14:22:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5216",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5216#issuecomment-39965",
    "user": "mabshoff"
}
```

The new bzip2 tarball is at

  http://sage.math.washington.edu/home/mabshoff/release-cycles-3.3/rc3/bzip2-1.0.5.tar.gz

Note that we should move the bzip2 code to an spkg soon.

Cheers,

Michael



---

archive/issue_comments_039966.json:
```json
{
    "body": "Positive review. Thanks Mike.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-20T14:26:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5216",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5216#issuecomment-39966",
    "user": "mabshoff"
}
```

Positive review. Thanks Mike.

Cheers,

Michael



---

archive/issue_comments_039967.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-20T14:26:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5216",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5216#issuecomment-39967",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_039968.json:
```json
{
    "body": "Merged in Sage 3.3.r3.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-20T14:26:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5216",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5216#issuecomment-39968",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.r3.

Cheers,

Michael
