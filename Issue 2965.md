# Issue 2965: extcode spkg build failure on Debian

archive/issues_002965.json:
```json
{
    "body": "Assignee: tabbott\n\nNow that there's a dist/debian directory in the extcode spkg, my Debian scripts try to build extcode as a separate package.  This doesn't work; I've attached a trivial patch to make this not happen.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2965\n\n",
    "created_at": "2008-04-20T04:02:32Z",
    "labels": [
        "debian-package",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "extcode spkg build failure on Debian",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2965",
    "user": "tabbott"
}
```
Assignee: tabbott

Now that there's a dist/debian directory in the extcode spkg, my Debian scripts try to build extcode as a separate package.  This doesn't work; I've attached a trivial patch to make this not happen.

Issue created by migration from https://trac.sagemath.org/ticket/2965





---

archive/issue_comments_020446.json:
```json
{
    "body": "Attachment [extcode-debian.patch](tarball://root/attachments/some-uuid/ticket2965/extcode-debian.patch) by tabbott created at 2008-04-20 04:07:25",
    "created_at": "2008-04-20T04:07:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2965#issuecomment-20446",
    "user": "tabbott"
}
```

Attachment [extcode-debian.patch](tarball://root/attachments/some-uuid/ticket2965/extcode-debian.patch) by tabbott created at 2008-04-20 04:07:25



---

archive/issue_comments_020447.json:
```json
{
    "body": "Patch looks good to me. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-20T04:17:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2965#issuecomment-20447",
    "user": "mabshoff"
}
```

Patch looks good to me. Positive review.

Cheers,

Michael



---

archive/issue_comments_020448.json:
```json
{
    "body": "Merged in Sage 3.0.rc0",
    "created_at": "2008-04-20T04:17:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2965#issuecomment-20448",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.rc0



---

archive/issue_comments_020449.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-20T04:17:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2965#issuecomment-20449",
    "user": "mabshoff"
}
```

Resolution: fixed
