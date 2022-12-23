# Issue 5757: [with patch, needs review] change nodoctest directive

archive/issues_005757.json:
```json
{
    "body": "Assignee: jhpalmieri\n\nWithout this patch, if the string 'nodoctest' is anywhere in the file, then the file is not doctested.  This changes it to only look at for 'nodoctest' in the first 50 characters of the file.\n\n(This is a patch to the 'scripts' repository.)\n\nIssue created by migration from https://trac.sagemath.org/ticket/5757\n\n",
    "created_at": "2009-04-11T17:47:59Z",
    "labels": [
        "doctest coverage",
        "minor",
        "bug"
    ],
    "title": "[with patch, needs review] change nodoctest directive",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5757",
    "user": "jhpalmieri"
}
```
Assignee: jhpalmieri

Without this patch, if the string 'nodoctest' is anywhere in the file, then the file is not doctested.  This changes it to only look at for 'nodoctest' in the first 50 characters of the file.

(This is a patch to the 'scripts' repository.)

Issue created by migration from https://trac.sagemath.org/ticket/5757





---

archive/issue_comments_044999.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-04-11T17:49:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5757",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5757#issuecomment-44999",
    "user": "jhpalmieri"
}
```

Attachment



---

archive/issue_comments_045000.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-13T01:57:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5757",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5757#issuecomment-45000",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_045001.json:
```json
{
    "body": "Merged in Sage 3.4.1.rc3.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-13T01:57:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5757",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5757#issuecomment-45001",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.1.rc3.

Cheers,

Michael
