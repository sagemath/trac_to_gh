# Issue 3303: [with patch; needs review] Add shared library to tachyon Debian package

archive/issues_003303.json:
```json
{
    "body": "Assignee: @timabbott\n\nCC:  f.r.bissey@massey.ac.nz\n\nI've attached a patch that adds a shared library to tachyon.\n\nMy patch includes the necessary changes to the Debian package.\n\nLooking at spkg-install, it looks like SAGE doesn't actually use the tachyon library, only the binary, so I'm not including any changes to the spkg-install system.\n\nOnce this gets merged, I'll email John Stone with the patch to tachyon upstream.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3303\n\n",
    "created_at": "2008-05-25T22:17:00Z",
    "labels": [
        "debian-package",
        "blocker",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.3",
    "title": "[with patch; needs review] Add shared library to tachyon Debian package",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3303",
    "user": "@timabbott"
}
```
Assignee: @timabbott

CC:  f.r.bissey@massey.ac.nz

I've attached a patch that adds a shared library to tachyon.

My patch includes the necessary changes to the Debian package.

Looking at spkg-install, it looks like SAGE doesn't actually use the tachyon library, only the binary, so I'm not including any changes to the spkg-install system.

Once this gets merged, I'll email John Stone with the patch to tachyon upstream.

Issue created by migration from https://trac.sagemath.org/ticket/3303





---

archive/issue_comments_022845.json:
```json
{
    "body": "Attachment [tachyon-debian-shared-library.patch](tarball://root/attachments/some-uuid/ticket3303/tachyon-debian-shared-library.patch) by @timabbott created at 2008-05-25 22:17:23",
    "created_at": "2008-05-25T22:17:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3303",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3303#issuecomment-22845",
    "user": "@timabbott"
}
```

Attachment [tachyon-debian-shared-library.patch](tarball://root/attachments/some-uuid/ticket3303/tachyon-debian-shared-library.patch) by @timabbott created at 2008-05-25 22:17:23



---

archive/issue_comments_022846.json:
```json
{
    "body": "Patch looks good to me and has been merged in \n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.3/alpha0/tachyon-0.98beta.p5.spkg\n\nwithout incrementing the patch number to avoid unneeded rebuilds.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-28T07:50:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3303",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3303#issuecomment-22846",
    "user": "mabshoff"
}
```

Patch looks good to me and has been merged in 

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.3/alpha0/tachyon-0.98beta.p5.spkg

without incrementing the patch number to avoid unneeded rebuilds.

Cheers,

Michael



---

archive/issue_comments_022847.json:
```json
{
    "body": "Merged in Sage 3.0.3.alpha0",
    "created_at": "2008-05-28T07:51:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3303",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3303#issuecomment-22847",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.3.alpha0



---

archive/issue_comments_022848.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-28T07:51:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3303",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3303#issuecomment-22848",
    "user": "mabshoff"
}
```

Resolution: fixed
