# Issue 1328: 2.8.14/Solaris: partitions_c.h compile fix - unclean

archive/issues_001328.json:
```json
{
    "body": "Assignee: mabshoff\n\nOn Solaris we need to apply the attached patch to make the partition code compile. This version breaks on non-Solaris, so it needs some trivial cleanup.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1328\n\n",
    "created_at": "2007-11-28T22:26:23Z",
    "labels": [
        "porting",
        "major",
        "bug"
    ],
    "title": "2.8.14/Solaris: partitions_c.h compile fix - unclean",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1328",
    "user": "mabshoff"
}
```
Assignee: mabshoff

On Solaris we need to apply the attached patch to make the partition code compile. This version breaks on non-Solaris, so it needs some trivial cleanup.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/1328





---

archive/issue_comments_008500.json:
```json
{
    "body": "Attachment [Sage-2.8.14-partitions_c.h-on-Solaris-unclean.patch](tarball://root/attachments/some-uuid/ticket1328/Sage-2.8.14-partitions_c.h-on-Solaris-unclean.patch) by mabshoff created at 2007-11-28 22:26:44",
    "created_at": "2007-11-28T22:26:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1328",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1328#issuecomment-8500",
    "user": "mabshoff"
}
```

Attachment [Sage-2.8.14-partitions_c.h-on-Solaris-unclean.patch](tarball://root/attachments/some-uuid/ticket1328/Sage-2.8.14-partitions_c.h-on-Solaris-unclean.patch) by mabshoff created at 2007-11-28 22:26:44



---

archive/issue_comments_008501.json:
```json
{
    "body": "There is a new unified patch at #1329. Do not apply this patch here.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-30T03:19:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1328",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1328#issuecomment-8501",
    "user": "mabshoff"
}
```

There is a new unified patch at #1329. Do not apply this patch here.

Cheers,

Michael



---

archive/issue_comments_008502.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-30T03:19:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1328",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1328#issuecomment-8502",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_008503.json:
```json
{
    "body": "Patch passes compile test and testall on non-Solaris.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-30T07:09:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1328",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1328#issuecomment-8503",
    "user": "mabshoff"
}
```

Patch passes compile test and testall on non-Solaris.

Cheers,

Michael



---

archive/issue_comments_008504.json:
```json
{
    "body": "tested that it doesn't break anyting on linux",
    "created_at": "2008-01-30T07:30:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1328",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1328#issuecomment-8504",
    "user": "jkantor"
}
```

tested that it doesn't break anyting on linux



---

archive/issue_comments_008505.json:
```json
{
    "body": "Merged Sage-2.10.1.rc2-Solaris-build-fixes-for-sage.spkg.patch from #1329 in Sage 2.10.1.rc3",
    "created_at": "2008-01-30T07:55:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1328",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1328#issuecomment-8505",
    "user": "mabshoff"
}
```

Merged Sage-2.10.1.rc2-Solaris-build-fixes-for-sage.spkg.patch from #1329 in Sage 2.10.1.rc3



---

archive/issue_comments_008506.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-30T07:55:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1328",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1328#issuecomment-8506",
    "user": "mabshoff"
}
```

Resolution: fixed
