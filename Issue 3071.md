# Issue 3071: Using pbuild does not create site-packages sage symlink

archive/issues_003071.json:
```json
{
    "body": "Assignee: mabshoff\n\nKeywords: pbuild\n\nIf you use pbuild during the initial setup, it does not create the sage symlink in site-packages.  This can be fixed by performing:\nln -s devel/sage/build/sage/ local/lib/python/site-packages/sage\nduring the install process.  \n\nIssue created by migration from https://trac.sagemath.org/ticket/3071\n\n",
    "created_at": "2008-05-01T10:26:22Z",
    "labels": [
        "component: build",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.1",
    "title": "Using pbuild does not create site-packages sage symlink",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3071",
    "user": "https://github.com/garyfurnish"
}
```
Assignee: mabshoff

Keywords: pbuild

If you use pbuild during the initial setup, it does not create the sage symlink in site-packages.  This can be fixed by performing:
ln -s devel/sage/build/sage/ local/lib/python/site-packages/sage
during the install process.  

Issue created by migration from https://trac.sagemath.org/ticket/3071





---

archive/issue_comments_021154.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-05-02T00:18:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3071",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3071#issuecomment-21154",
    "user": "https://github.com/garyfurnish"
}
```

Changing status from new to assigned.



---

archive/issue_comments_021155.json:
```json
{
    "body": "The attached patch should fix this issue and the linking issues reported on the mailing list.  It also fixes the banner.",
    "created_at": "2008-05-02T00:18:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3071",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3071#issuecomment-21155",
    "user": "https://github.com/garyfurnish"
}
```

The attached patch should fix this issue and the linking issues reported on the mailing list.  It also fixes the banner.



---

archive/issue_comments_021156.json:
```json
{
    "body": "Changing assignee from mabshoff to @garyfurnish.",
    "created_at": "2008-05-02T00:18:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3071",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3071#issuecomment-21156",
    "user": "https://github.com/garyfurnish"
}
```

Changing assignee from mabshoff to @garyfurnish.



---

archive/issue_comments_021157.json:
```json
{
    "body": "Attachment [trac_3071.patch](tarball://root/attachments/some-uuid/ticket3071/trac_3071.patch) by @garyfurnish created at 2008-05-02 00:21:33",
    "created_at": "2008-05-02T00:21:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3071",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3071#issuecomment-21157",
    "user": "https://github.com/garyfurnish"
}
```

Attachment [trac_3071.patch](tarball://root/attachments/some-uuid/ticket3071/trac_3071.patch) by @garyfurnish created at 2008-05-02 00:21:33



---

archive/issue_comments_021158.json:
```json
{
    "body": "Attachment [trac_3071_2.patch](tarball://root/attachments/some-uuid/ticket3071/trac_3071_2.patch) by @wjp created at 2008-05-02 10:18:40",
    "created_at": "2008-05-02T10:18:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3071",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3071#issuecomment-21158",
    "user": "https://github.com/wjp"
}
```

Attachment [trac_3071_2.patch](tarball://root/attachments/some-uuid/ticket3071/trac_3071_2.patch) by @wjp created at 2008-05-02 10:18:40



---

archive/issue_comments_021159.json:
```json
{
    "body": "Merged in Sage 3.0.1.rc0",
    "created_at": "2008-05-02T12:02:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3071",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3071#issuecomment-21159",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.1.rc0



---

archive/issue_comments_021160.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-02T12:02:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3071",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3071#issuecomment-21160",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
