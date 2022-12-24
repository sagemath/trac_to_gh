# Issue 3323: [with patch, needs review] Enhanced error reporting for dependency errors in pbuild

archive/issues_003323.json:
```json
{
    "body": "Assignee: gfurnish\n\nKeywords: pbuild\n\nThis patch adds some better error handeling to pbuild - instead of dieing with a mysterious error, it will tell you the file from which a dependency that is missing is being imported from (if foo.pyx is trying to cimport bar and there is no bar.pxd, it will tell you that foo.pyx is missing bar.pxd).  It will also tell you if foo.pyx imports some file which imports bar.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3323\n\n",
    "created_at": "2008-05-28T15:49:04Z",
    "labels": [
        "pbuild",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.3",
    "title": "[with patch, needs review] Enhanced error reporting for dependency errors in pbuild",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3323",
    "user": "gfurnish"
}
```
Assignee: gfurnish

Keywords: pbuild

This patch adds some better error handeling to pbuild - instead of dieing with a mysterious error, it will tell you the file from which a dependency that is missing is being imported from (if foo.pyx is trying to cimport bar and there is no bar.pxd, it will tell you that foo.pyx is missing bar.pxd).  It will also tell you if foo.pyx imports some file which imports bar.


Issue created by migration from https://trac.sagemath.org/ticket/3323





---

archive/issue_comments_023036.json:
```json
{
    "body": "Attachment [trac_3323_extcode.patch](tarball://root/attachments/some-uuid/ticket3323/trac_3323_extcode.patch) by gfurnish created at 2008-05-28 15:49:18",
    "created_at": "2008-05-28T15:49:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3323",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3323#issuecomment-23036",
    "user": "gfurnish"
}
```

Attachment [trac_3323_extcode.patch](tarball://root/attachments/some-uuid/ticket3323/trac_3323_extcode.patch) by gfurnish created at 2008-05-28 15:49:18



---

archive/issue_comments_023037.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-05-28T15:49:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3323",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3323#issuecomment-23037",
    "user": "gfurnish"
}
```

Changing status from new to assigned.



---

archive/issue_comments_023038.json:
```json
{
    "body": "Patch looks good to me. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-28T23:36:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3323",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3323#issuecomment-23038",
    "user": "mabshoff"
}
```

Patch looks good to me. Positive review.

Cheers,

Michael



---

archive/issue_comments_023039.json:
```json
{
    "body": "Merged in Sage 3.0.3.alpha1",
    "created_at": "2008-05-29T01:10:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3323",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3323#issuecomment-23039",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.3.alpha1



---

archive/issue_comments_023040.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-29T01:10:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3323",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3323#issuecomment-23040",
    "user": "mabshoff"
}
```

Resolution: fixed
