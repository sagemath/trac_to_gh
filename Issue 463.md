# Issue 463: sage -upgrade:  make it more flexible

archive/issues_000463.json:
```json
{
    "body": "Assignee: was\n\n\n```\n[12:25] <william> interesting feature idea:\n[12:25] <william> extend the \"sage -upgrade\" command so you an give the directory or URL\n[12:26] <william> of any other installed version of SAGE, and it will pull everything from there.\n[12:26] <william> install any newer spkg's and pull from any active repo.\n[12:26] <malb> definitely nice for sysadmins I guess\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/463\n\n",
    "created_at": "2007-08-19T19:32:14Z",
    "labels": [
        "packages: standard",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.1",
    "title": "sage -upgrade:  make it more flexible",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/463",
    "user": "was"
}
```
Assignee: was


```
[12:25] <william> interesting feature idea:
[12:25] <william> extend the "sage -upgrade" command so you an give the directory or URL
[12:26] <william> of any other installed version of SAGE, and it will pull everything from there.
[12:26] <william> install any newer spkg's and pull from any active repo.
[12:26] <malb> definitely nice for sysadmins I guess
```


Issue created by migration from https://trac.sagemath.org/ticket/463





---

archive/issue_comments_002295.json:
```json
{
    "body": "Attachment [sage-463.patch](tarball://root/attachments/some-uuid/ticket463/sage-463.patch) by was created at 2008-11-27 01:24:31\n\nsomewhat orthogonal -- changes to use \"sage -br\" instead of \"sage -ba\" on upgrade.  apply to sage repo.",
    "created_at": "2008-11-27T01:24:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/463",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/463#issuecomment-2295",
    "user": "was"
}
```

Attachment [sage-463.patch](tarball://root/attachments/some-uuid/ticket463/sage-463.patch) by was created at 2008-11-27 01:24:31

somewhat orthogonal -- changes to use "sage -br" instead of "sage -ba" on upgrade.  apply to sage repo.



---

archive/issue_comments_002296.json:
```json
{
    "body": "Attachment [scripts-463.patch](tarball://root/attachments/some-uuid/ticket463/scripts-463.patch) by was created at 2008-11-27 01:25:47\n\napply to the scripts repo.",
    "created_at": "2008-11-27T01:25:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/463",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/463#issuecomment-2296",
    "user": "was"
}
```

Attachment [scripts-463.patch](tarball://root/attachments/some-uuid/ticket463/scripts-463.patch) by was created at 2008-11-27 01:25:47

apply to the scripts repo.



---

archive/issue_comments_002297.json:
```json
{
    "body": "To test this out try:\n\nOn an older sage install\n\n```\nsage -upgrade  # should do a standard upgrade to the latest version of sage\n```\n\n\nOn a new sage install\n\n```\nsage -upgrade http://sage.math.washington.edu/home/was/build/sage-3.2.1.alpha1\n```\n\nto upgrade to the latest devel version.",
    "created_at": "2008-11-27T01:27:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/463",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/463#issuecomment-2297",
    "user": "was"
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

archive/issue_comments_002298.json:
```json
{
    "body": "Attachment [scripts-463-rebase-3.1.alpha1.patch](tarball://root/attachments/some-uuid/ticket463/scripts-463-rebase-3.1.alpha1.patch) by was created at 2008-11-27 01:45:43",
    "created_at": "2008-11-27T01:45:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/463",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/463#issuecomment-2298",
    "user": "was"
}
```

Attachment [scripts-463-rebase-3.1.alpha1.patch](tarball://root/attachments/some-uuid/ticket463/scripts-463-rebase-3.1.alpha1.patch) by was created at 2008-11-27 01:45:43



---

archive/issue_comments_002299.json:
```json
{
    "body": "Attachment [scripts-463-rebase-3.2.1.alpha1-part2.patch](tarball://root/attachments/some-uuid/ticket463/scripts-463-rebase-3.2.1.alpha1-part2.patch) by was created at 2008-11-27 02:02:26\n\nApply these to 3.2.1.alpha1:\n\n```\nsage-463.patch \nscripts-463-rebase-3.1.alpha1.patch \nscripts-463-rebase-3.2.1.alpha1-part2.patch \n```\n",
    "created_at": "2008-11-27T02:02:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/463",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/463#issuecomment-2299",
    "user": "was"
}
```

Attachment [scripts-463-rebase-3.2.1.alpha1-part2.patch](tarball://root/attachments/some-uuid/ticket463/scripts-463-rebase-3.2.1.alpha1-part2.patch) by was created at 2008-11-27 02:02:26

Apply these to 3.2.1.alpha1:

```
sage-463.patch 
scripts-463-rebase-3.1.alpha1.patch 
scripts-463-rebase-3.2.1.alpha1-part2.patch 
```




---

archive/issue_comments_002300.json:
```json
{
    "body": "The three patches listed above look good to me. \n\nAs William pointed out in IRC one can downgrade in which case a whole set of spkgs will be downloaded and then nothing is installed, but I am fine with that behavior. That might be fixed via some future ticket, but I don't think we should support downgrading. \n\nCheers,\n\nMichael",
    "created_at": "2008-11-27T03:29:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/463",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/463#issuecomment-2300",
    "user": "mabshoff"
}
```

The three patches listed above look good to me. 

As William pointed out in IRC one can downgrade in which case a whole set of spkgs will be downloaded and then nothing is installed, but I am fine with that behavior. That might be fixed via some future ticket, but I don't think we should support downgrading. 

Cheers,

Michael



---

archive/issue_comments_002301.json:
```json
{
    "body": "Merged in Sage 3.2.1.alpha2",
    "created_at": "2008-11-27T03:30:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/463",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/463#issuecomment-2301",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.1.alpha2



---

archive/issue_comments_002302.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-27T03:30:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/463",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/463#issuecomment-2302",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_002303.json:
```json
{
    "body": "Attachment [scripts-463-part3.patch](tarball://root/attachments/some-uuid/ticket463/scripts-463-part3.patch) by was created at 2008-11-27 05:14:06",
    "created_at": "2008-11-27T05:14:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/463",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/463#issuecomment-2303",
    "user": "was"
}
```

Attachment [scripts-463-part3.patch](tarball://root/attachments/some-uuid/ticket463/scripts-463-part3.patch) by was created at 2008-11-27 05:14:06



---

archive/issue_comments_002304.json:
```json
{
    "body": "Attachment [sage-463-part2.patch](tarball://root/attachments/some-uuid/ticket463/sage-463-part2.patch) by mabshoff created at 2008-11-27 05:28:16\n\nMerged scripts-463-part3.patch and sage-463-part2.patch in Sage 3.2.1.alpah2",
    "created_at": "2008-11-27T05:28:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/463",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/463#issuecomment-2304",
    "user": "mabshoff"
}
```

Attachment [sage-463-part2.patch](tarball://root/attachments/some-uuid/ticket463/sage-463-part2.patch) by mabshoff created at 2008-11-27 05:28:16

Merged scripts-463-part3.patch and sage-463-part2.patch in Sage 3.2.1.alpah2



---

archive/issue_comments_002305.json:
```json
{
    "body": "And we merged on more fix: turn -br into -b\n\nCheers,\n\nMichael",
    "created_at": "2008-11-27T06:29:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/463",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/463#issuecomment-2305",
    "user": "mabshoff"
}
```

And we merged on more fix: turn -br into -b

Cheers,

Michael
