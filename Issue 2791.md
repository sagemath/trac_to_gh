# Issue 2791: [with patch; needs review] Build symmetrica with -fPIC on Debian

archive/issues_002791.json:
```json
{
    "body": "Assignee: @timabbott\n\nNow that the linbox bug is fixed, I tried to build SAGE itself, and am running into more -fPIC problems.  Attached is a patch to make symmetric build with -fPIC.\n\nThough really, we should fix the symmetrica build system.  \n\nIssue created by migration from https://trac.sagemath.org/ticket/2791\n\n",
    "created_at": "2008-04-03T06:15:23Z",
    "labels": [
        "debian-package",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "[with patch; needs review] Build symmetrica with -fPIC on Debian",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2791",
    "user": "@timabbott"
}
```
Assignee: @timabbott

Now that the linbox bug is fixed, I tried to build SAGE itself, and am running into more -fPIC problems.  Attached is a patch to make symmetric build with -fPIC.

Though really, we should fix the symmetrica build system.  

Issue created by migration from https://trac.sagemath.org/ticket/2791





---

archive/issue_comments_019171.json:
```json
{
    "body": "Attachment [symmetrica-amd64.patch](tarball://root/attachments/some-uuid/ticket2791/symmetrica-amd64.patch) by @timabbott created at 2008-04-03 06:15:45",
    "created_at": "2008-04-03T06:15:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2791#issuecomment-19171",
    "user": "@timabbott"
}
```

Attachment [symmetrica-amd64.patch](tarball://root/attachments/some-uuid/ticket2791/symmetrica-amd64.patch) by @timabbott created at 2008-04-03 06:15:45



---

archive/issue_comments_019172.json:
```json
{
    "body": "Patch looks good to me. The patch will be in the updated symmetrica-2.0.p2.spkg.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-03T11:25:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2791#issuecomment-19172",
    "user": "mabshoff"
}
```

Patch looks good to me. The patch will be in the updated symmetrica-2.0.p2.spkg.

Cheers,

Michael



---

archive/issue_comments_019173.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-03T11:25:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2791#issuecomment-19173",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_019174.json:
```json
{
    "body": "Merged in Sage 3.0.alpha1",
    "created_at": "2008-04-03T11:25:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2791#issuecomment-19174",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.alpha1
