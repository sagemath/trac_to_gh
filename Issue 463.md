# Issue 463: sage -upgrade:  make it more flexible

archive/issues_000463.json:
```json
{
    "body": "Assignee: @williamstein\n\n```\n[12:25] <william> interesting feature idea:\n[12:25] <william> extend the \"sage -upgrade\" command so you an give the directory or URL\n[12:26] <william> of any other installed version of SAGE, and it will pull everything from there.\n[12:26] <william> install any newer spkg's and pull from any active repo.\n[12:26] <malb> definitely nice for sysadmins I guess\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/463\n\n",
    "created_at": "2007-08-19T19:32:14Z",
    "labels": [
        "component: packages: standard"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.1",
    "title": "sage -upgrade:  make it more flexible",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/463",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

```
[12:25] <william> interesting feature idea:
[12:25] <william> extend the "sage -upgrade" command so you an give the directory or URL
[12:26] <william> of any other installed version of SAGE, and it will pull everything from there.
[12:26] <william> install any newer spkg's and pull from any active repo.
[12:26] <malb> definitely nice for sysadmins I guess
```

Issue created by migration from https://trac.sagemath.org/ticket/463





---

archive/issue_comments_002285.json:
```json
{
    "body": "Attachment [sage-463.patch](tarball://root/attachments/some-uuid/ticket463/sage-463.patch) by @williamstein created at 2008-11-27 01:24:31\n\nsomewhat orthogonal -- changes to use \"sage -br\" instead of \"sage -ba\" on upgrade.  apply to sage repo.",
    "created_at": "2008-11-27T01:24:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/463",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/463#issuecomment-2285",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-463.patch](tarball://root/attachments/some-uuid/ticket463/sage-463.patch) by @williamstein created at 2008-11-27 01:24:31

somewhat orthogonal -- changes to use "sage -br" instead of "sage -ba" on upgrade.  apply to sage repo.



---

archive/issue_comments_002286.json:
```json
{
    "body": "Attachment [scripts-463.patch](tarball://root/attachments/some-uuid/ticket463/scripts-463.patch) by @williamstein created at 2008-11-27 01:25:47\n\napply to the scripts repo.",
    "created_at": "2008-11-27T01:25:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/463",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/463#issuecomment-2286",
    "user": "https://github.com/williamstein"
}
```

Attachment [scripts-463.patch](tarball://root/attachments/some-uuid/ticket463/scripts-463.patch) by @williamstein created at 2008-11-27 01:25:47

apply to the scripts repo.



---

archive/issue_comments_002287.json:
```json
{
    "body": "To test this out try:\n\nOn an older sage install\n\n```\nsage -upgrade  # should do a standard upgrade to the latest version of sage\n```\n\nOn a new sage install\n\n```\nsage -upgrade http://sage.math.washington.edu/home/was/build/sage-3.2.1.alpha1\n```\nto upgrade to the latest devel version.",
    "created_at": "2008-11-27T01:27:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/463",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/463#issuecomment-2287",
    "user": "https://github.com/williamstein"
}
```

To test this out try:

On an older sage install

```
sage -upgrade  # should do a standard upgrade to the latest version of sage
```

On a new sage install

```
sage -upgrade http://sage.math.washington.edu/home/was/build/sage-3.2.1.alpha1
```
to upgrade to the latest devel version.



---

archive/issue_comments_002288.json:
```json
{
    "body": "Attachment [scripts-463-rebase-3.1.alpha1.patch](tarball://root/attachments/some-uuid/ticket463/scripts-463-rebase-3.1.alpha1.patch) by @williamstein created at 2008-11-27 01:45:43",
    "created_at": "2008-11-27T01:45:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/463",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/463#issuecomment-2288",
    "user": "https://github.com/williamstein"
}
```

Attachment [scripts-463-rebase-3.1.alpha1.patch](tarball://root/attachments/some-uuid/ticket463/scripts-463-rebase-3.1.alpha1.patch) by @williamstein created at 2008-11-27 01:45:43



---

archive/issue_comments_002289.json:
```json
{
    "body": "Attachment [scripts-463-rebase-3.2.1.alpha1-part2.patch](tarball://root/attachments/some-uuid/ticket463/scripts-463-rebase-3.2.1.alpha1-part2.patch) by @williamstein created at 2008-11-27 02:02:26\n\nApply these to 3.2.1.alpha1:\n\n```\nsage-463.patch \nscripts-463-rebase-3.1.alpha1.patch \nscripts-463-rebase-3.2.1.alpha1-part2.patch \n```",
    "created_at": "2008-11-27T02:02:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/463",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/463#issuecomment-2289",
    "user": "https://github.com/williamstein"
}
```

Attachment [scripts-463-rebase-3.2.1.alpha1-part2.patch](tarball://root/attachments/some-uuid/ticket463/scripts-463-rebase-3.2.1.alpha1-part2.patch) by @williamstein created at 2008-11-27 02:02:26

Apply these to 3.2.1.alpha1:

```
sage-463.patch 
scripts-463-rebase-3.1.alpha1.patch 
scripts-463-rebase-3.2.1.alpha1-part2.patch 
```



---

archive/issue_comments_002290.json:
```json
{
    "body": "The three patches listed above look good to me. \n\nAs William pointed out in IRC one can downgrade in which case a whole set of spkgs will be downloaded and then nothing is installed, but I am fine with that behavior. That might be fixed via some future ticket, but I don't think we should support downgrading. \n\nCheers,\n\nMichael",
    "created_at": "2008-11-27T03:29:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/463",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/463#issuecomment-2290",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The three patches listed above look good to me. 

As William pointed out in IRC one can downgrade in which case a whole set of spkgs will be downloaded and then nothing is installed, but I am fine with that behavior. That might be fixed via some future ticket, but I don't think we should support downgrading. 

Cheers,

Michael



---

archive/issue_comments_002291.json:
```json
{
    "body": "Merged in Sage 3.2.1.alpha2",
    "created_at": "2008-11-27T03:30:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/463",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/463#issuecomment-2291",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.1.alpha2



---

archive/issue_comments_002292.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-27T03:30:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/463",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/463#issuecomment-2292",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_001162.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-11-27T03:30:09Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/463",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/463#event-1162"
}
```



---

archive/issue_comments_002293.json:
```json
{
    "body": "Attachment [scripts-463-part3.patch](tarball://root/attachments/some-uuid/ticket463/scripts-463-part3.patch) by @williamstein created at 2008-11-27 05:14:06",
    "created_at": "2008-11-27T05:14:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/463",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/463#issuecomment-2293",
    "user": "https://github.com/williamstein"
}
```

Attachment [scripts-463-part3.patch](tarball://root/attachments/some-uuid/ticket463/scripts-463-part3.patch) by @williamstein created at 2008-11-27 05:14:06



---

archive/issue_comments_002294.json:
```json
{
    "body": "Attachment [sage-463-part2.patch](tarball://root/attachments/some-uuid/ticket463/sage-463-part2.patch) by mabshoff created at 2008-11-27 05:28:16\n\nMerged scripts-463-part3.patch and sage-463-part2.patch in Sage 3.2.1.alpah2",
    "created_at": "2008-11-27T05:28:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/463",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/463#issuecomment-2294",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [sage-463-part2.patch](tarball://root/attachments/some-uuid/ticket463/sage-463-part2.patch) by mabshoff created at 2008-11-27 05:28:16

Merged scripts-463-part3.patch and sage-463-part2.patch in Sage 3.2.1.alpah2



---

archive/issue_comments_002295.json:
```json
{
    "body": "And we merged on more fix: turn -br into -b\n\nCheers,\n\nMichael",
    "created_at": "2008-11-27T06:29:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/463",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/463#issuecomment-2295",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

And we merged on more fix: turn -br into -b

Cheers,

Michael
