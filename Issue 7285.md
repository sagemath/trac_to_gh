# Issue 7285: remove hgmerge from list of installed scripts

archive/issues_007285.json:
```json
{
    "body": "Assignee: tbd\n\nMercurial no longer has an hgmerge script.  This if one does \n\n```\nsage: install_scripts('/usr/local/bin/')\n```\n\nwith sage right now then very bad things happen.  For starters, you get an hgmerge script that hangs, which means any time any file ever gets merged with mercurial, instead of getting a merge option, you get a hang.  Pretty confusing. \n\nIssue created by migration from https://trac.sagemath.org/ticket/7285\n\n",
    "created_at": "2009-10-25T03:47:15Z",
    "labels": [
        "algebra",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2.1",
    "title": "remove hgmerge from list of installed scripts",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7285",
    "user": "was"
}
```
Assignee: tbd

Mercurial no longer has an hgmerge script.  This if one does 

```
sage: install_scripts('/usr/local/bin/')
```

with sage right now then very bad things happen.  For starters, you get an hgmerge script that hangs, which means any time any file ever gets merged with mercurial, instead of getting a merge option, you get a hang.  Pretty confusing. 

Issue created by migration from https://trac.sagemath.org/ticket/7285





---

archive/issue_comments_060626.json:
```json
{
    "body": "Attachment [trac_7285.patch](tarball://root/attachments/some-uuid/ticket7285/trac_7285.patch) by was created at 2009-10-25 03:51:58",
    "created_at": "2009-10-25T03:51:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7285",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7285#issuecomment-60626",
    "user": "was"
}
```

Attachment [trac_7285.patch](tarball://root/attachments/some-uuid/ticket7285/trac_7285.patch) by was created at 2009-10-25 03:51:58



---

archive/issue_comments_060627.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-25T03:52:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7285",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7285#issuecomment-60627",
    "user": "was"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_060628.json:
```json
{
    "body": "Changing component from algebra to misc.",
    "created_at": "2009-10-25T03:52:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7285",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7285#issuecomment-60628",
    "user": "was"
}
```

Changing component from algebra to misc.



---

archive/issue_comments_060629.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-11-04T14:50:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7285",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7285#issuecomment-60629",
    "user": "mhansen"
}
```

Looks good to me.



---

archive/issue_comments_060630.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-04T14:50:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7285",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7285#issuecomment-60630",
    "user": "mhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_060631.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-06T04:11:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7285",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7285#issuecomment-60631",
    "user": "mhansen"
}
```

Resolution: fixed
