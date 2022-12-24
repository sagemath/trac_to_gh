# Issue 4434: [with patch; needs review] hgmerge massively broken on os x

archive/issues_004434.json:
```json
{
    "body": "Assignee: mabshoff\n\nWhen doing a graphical 3-way merge under OS X, hgmerge is missing so one gets infinite loops or errors.  This is a major problem.\n\nThe spkg here:\n\nhttp://sage.math.washington.edu/home/was/patches/mercurial-1.01.p2.spkg\n\ndoes the following:\n\n* Added custom hgmerge script for OS X. For some reason no script at all was \n  copied over, which lead to (1) hg merge silently failing painfully for most\n  users, and (2) for users that run install_scripts, they would get a fork\n  bomb, since hgmerge would call sage -hgmerge which would call hgmerge \n  ad infintum.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4434\n\n",
    "created_at": "2008-11-04T04:41:23Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "[with patch; needs review] hgmerge massively broken on os x",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4434",
    "user": "was"
}
```
Assignee: mabshoff

When doing a graphical 3-way merge under OS X, hgmerge is missing so one gets infinite loops or errors.  This is a major problem.

The spkg here:

http://sage.math.washington.edu/home/was/patches/mercurial-1.01.p2.spkg

does the following:

* Added custom hgmerge script for OS X. For some reason no script at all was 
  copied over, which lead to (1) hg merge silently failing painfully for most
  users, and (2) for users that run install_scripts, they would get a fork
  bomb, since hgmerge would call sage -hgmerge which would call hgmerge 
  ad infintum.



Issue created by migration from https://trac.sagemath.org/ticket/4434





---

archive/issue_comments_032597.json:
```json
{
    "body": "Spkg looks good, but I checked in all outstanding changes.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-04T13:34:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4434#issuecomment-32597",
    "user": "mabshoff"
}
```

Spkg looks good, but I checked in all outstanding changes.

Cheers,

Michael



---

archive/issue_comments_032598.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-04T13:34:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4434#issuecomment-32598",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_032599.json:
```json
{
    "body": "Merged in Sage 3.2.alpha3",
    "created_at": "2008-11-04T13:34:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4434#issuecomment-32599",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.alpha3



---

archive/issue_comments_032600.json:
```json
{
    "body": "#11120 reverses this patch. Your comments would be greatly appreciated!",
    "created_at": "2011-04-04T16:45:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4434#issuecomment-32600",
    "user": "kini"
}
```

#11120 reverses this patch. Your comments would be greatly appreciated!
