# Issue 3039: [with patch; needs review] Improve auto-generated version numbers for Debian packages

archive/issues_003039.json:
```json
{
    "body": "Assignee: @timabbott\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3039\n\n",
    "created_at": "2008-04-27T02:36:29Z",
    "labels": [
        "debian-package",
        "blocker",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.1",
    "title": "[with patch; needs review] Improve auto-generated version numbers for Debian packages",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3039",
    "user": "@timabbott"
}
```
Assignee: @timabbott



Issue created by migration from https://trac.sagemath.org/ticket/3039





---

archive/issue_comments_020910.json:
```json
{
    "body": "Attachment [sage-debsource-versions.patch](tarball://root/attachments/some-uuid/ticket3039/sage-debsource-versions.patch) by @timabbott created at 2008-04-27 02:36:34",
    "created_at": "2008-04-27T02:36:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3039#issuecomment-20910",
    "user": "@timabbott"
}
```

Attachment [sage-debsource-versions.patch](tarball://root/attachments/some-uuid/ticket3039/sage-debsource-versions.patch) by @timabbott created at 2008-04-27 02:36:34



---

archive/issue_comments_020911.json:
```json
{
    "body": "Oops, forgot the text.\n\nThis patch changes the auto-generated versions for Debian packages so that \n1) alpha and rc versions are lower than the final versions (by appending ~ before them)\n2) the Debian revisions start with 0 (so that if Debian comes out with its own version of the same version of the package, the Debian version number will be higher)\n3) the Debian version numbers include sage in them so that it's obvious from the version number that this is a package that may have been modified for use with SAGE.",
    "created_at": "2008-04-27T02:39:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3039#issuecomment-20911",
    "user": "@timabbott"
}
```

Oops, forgot the text.

This patch changes the auto-generated versions for Debian packages so that 
1) alpha and rc versions are lower than the final versions (by appending ~ before them)
2) the Debian revisions start with 0 (so that if Debian comes out with its own version of the same version of the package, the Debian version number will be higher)
3) the Debian version numbers include sage in them so that it's obvious from the version number that this is a package that may have been modified for use with SAGE.



---

archive/issue_comments_020912.json:
```json
{
    "body": "Patch looks good to me and applies cleanly. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-27T02:48:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3039#issuecomment-20912",
    "user": "mabshoff"
}
```

Patch looks good to me and applies cleanly. Positive review.

Cheers,

Michael



---

archive/issue_comments_020913.json:
```json
{
    "body": "Merged in Sage 3.0.1.alpha1",
    "created_at": "2008-04-27T02:48:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3039#issuecomment-20913",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.1.alpha1



---

archive/issue_comments_020914.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-27T02:48:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3039#issuecomment-20914",
    "user": "mabshoff"
}
```

Resolution: fixed
