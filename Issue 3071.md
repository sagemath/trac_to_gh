# Issue 3071: Using pbuild does not create site-packages sage symlink

archive/issues_003071.json:
```json
{
    "body": "Assignee: mabshoff\n\nKeywords: pbuild\n\nIf you use pbuild during the initial setup, it does not create the sage symlink in site-packages.  This can be fixed by performing:\nln -s devel/sage/build/sage/ local/lib/python/site-packages/sage\nduring the install process.  \n\nIssue created by migration from https://trac.sagemath.org/ticket/3071\n\n",
    "created_at": "2008-05-01T10:26:22Z",
    "labels": [
        "build",
        "blocker",
        "bug"
    ],
    "title": "Using pbuild does not create site-packages sage symlink",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3071",
    "user": "gfurnish"
}
```
Assignee: mabshoff

Keywords: pbuild

If you use pbuild during the initial setup, it does not create the sage symlink in site-packages.  This can be fixed by performing:
ln -s devel/sage/build/sage/ local/lib/python/site-packages/sage
during the install process.  

Issue created by migration from https://trac.sagemath.org/ticket/3071





---

archive/issue_comments_021198.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-05-02T00:18:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3071",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3071#issuecomment-21198",
    "user": "gfurnish"
}
```

Changing status from new to assigned.



---

archive/issue_comments_021199.json:
```json
{
    "body": "The attached patch should fix this issue and the linking issues reported on the mailing list.  It also fixes the banner.",
    "created_at": "2008-05-02T00:18:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3071",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3071#issuecomment-21199",
    "user": "gfurnish"
}
```

The attached patch should fix this issue and the linking issues reported on the mailing list.  It also fixes the banner.



---

archive/issue_comments_021200.json:
```json
{
    "body": "Changing assignee from mabshoff to gfurnish.",
    "created_at": "2008-05-02T00:18:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3071",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3071#issuecomment-21200",
    "user": "gfurnish"
}
```

Changing assignee from mabshoff to gfurnish.



---

archive/issue_comments_021201.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-05-02T00:21:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3071",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3071#issuecomment-21201",
    "user": "gfurnish"
}
```

Attachment



---

archive/issue_comments_021202.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-05-02T10:18:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3071",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3071#issuecomment-21202",
    "user": "wjp"
}
```

Attachment



---

archive/issue_comments_021203.json:
```json
{
    "body": "Merged in Sage 3.0.1.rc0",
    "created_at": "2008-05-02T12:02:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3071",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3071#issuecomment-21203",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.1.rc0



---

archive/issue_comments_021204.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-02T12:02:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3071",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3071#issuecomment-21204",
    "user": "mabshoff"
}
```

Resolution: fixed
