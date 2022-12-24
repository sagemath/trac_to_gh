# Issue 3721: [with patch; needs review] Use SAGE_TESTDIR for dsage unit tests

archive/issues_003721.json:
```json
{
    "body": "Assignee: yi\n\ndsage tests currently ignore the SAGE_TESTDIR environment variable, resulting in permission denied errors for users who don't have write access to their Sage install.\n\nI've attached a patch to fix this.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3721\n\n",
    "created_at": "2008-07-25T05:31:34Z",
    "labels": [
        "dsage",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1",
    "title": "[with patch; needs review] Use SAGE_TESTDIR for dsage unit tests",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3721",
    "user": "tabbott"
}
```
Assignee: yi

dsage tests currently ignore the SAGE_TESTDIR environment variable, resulting in permission denied errors for users who don't have write access to their Sage install.

I've attached a patch to fix this.

Issue created by migration from https://trac.sagemath.org/ticket/3721





---

archive/issue_comments_026402.json:
```json
{
    "body": "Attachment [sage_scripts-dsage-testdir.patch](tarball://root/attachments/some-uuid/ticket3721/sage_scripts-dsage-testdir.patch) by mabshoff created at 2008-07-29 17:16:38",
    "created_at": "2008-07-29T17:16:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3721",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3721#issuecomment-26402",
    "user": "mabshoff"
}
```

Attachment [sage_scripts-dsage-testdir.patch](tarball://root/attachments/some-uuid/ticket3721/sage_scripts-dsage-testdir.patch) by mabshoff created at 2008-07-29 17:16:38



---

archive/issue_comments_026403.json:
```json
{
    "body": "Patch looks good to me. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-31T00:56:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3721",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3721#issuecomment-26403",
    "user": "mabshoff"
}
```

Patch looks good to me. Positive review.

Cheers,

Michael



---

archive/issue_comments_026404.json:
```json
{
    "body": "Merged in Sage 3.1.alpha0",
    "created_at": "2008-07-31T00:58:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3721",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3721#issuecomment-26404",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.alpha0



---

archive/issue_comments_026405.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-31T00:58:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3721",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3721#issuecomment-26405",
    "user": "mabshoff"
}
```

Resolution: fixed
