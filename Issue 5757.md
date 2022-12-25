# Issue 5757: [with patch, needs review] change nodoctest directive

archive/issues_005757.json:
```json
{
    "body": "Assignee: @jhpalmieri\n\nWithout this patch, if the string 'nodoctest' is anywhere in the file, then the file is not doctested.  This changes it to only look at for 'nodoctest' in the first 50 characters of the file.\n\n(This is a patch to the 'scripts' repository.)\n\nIssue created by migration from https://trac.sagemath.org/ticket/5757\n\n",
    "created_at": "2009-04-11T17:47:59Z",
    "labels": [
        "component: doctest coverage",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "[with patch, needs review] change nodoctest directive",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5757",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: @jhpalmieri

Without this patch, if the string 'nodoctest' is anywhere in the file, then the file is not doctested.  This changes it to only look at for 'nodoctest' in the first 50 characters of the file.

(This is a patch to the 'scripts' repository.)

Issue created by migration from https://trac.sagemath.org/ticket/5757





---

archive/issue_comments_044914.json:
```json
{
    "body": "Attachment [scripts-nodoctest.patch](tarball://root/attachments/some-uuid/ticket5757/scripts-nodoctest.patch) by @jhpalmieri created at 2009-04-11 17:49:32",
    "created_at": "2009-04-11T17:49:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5757",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5757#issuecomment-44914",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [scripts-nodoctest.patch](tarball://root/attachments/some-uuid/ticket5757/scripts-nodoctest.patch) by @jhpalmieri created at 2009-04-11 17:49:32



---

archive/issue_comments_044915.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-13T01:57:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5757",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5757#issuecomment-44915",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_044916.json:
```json
{
    "body": "Merged in Sage 3.4.1.rc3.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-13T01:57:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5757",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5757#issuecomment-44916",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.1.rc3.

Cheers,

Michael
