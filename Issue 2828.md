# Issue 2828: get doctest coverage for combinat/ to 100%

archive/issues_002828.json:
```json
{
    "body": "Assignee: @mwhansen\n\nCC:  sage-combinat\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2828\n\n",
    "created_at": "2008-04-06T10:09:16Z",
    "labels": [
        "component: combinatorics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "get doctest coverage for combinat/ to 100%",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2828",
    "user": "https://github.com/mwhansen"
}
```
Assignee: @mwhansen

CC:  sage-combinat



Issue created by migration from https://trac.sagemath.org/ticket/2828





---

archive/issue_comments_019371.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-04-06T10:15:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2828#issuecomment-19371",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_019372.json:
```json
{
    "body": "Ignore lint.patch.  2828.patch is the one to be reviewed.",
    "created_at": "2008-04-06T10:16:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2828#issuecomment-19372",
    "user": "https://github.com/mwhansen"
}
```

Ignore lint.patch.  2828.patch is the one to be reviewed.



---

archive/issue_comments_019373.json:
```json
{
    "body": "Attachment [2828.patch](tarball://root/attachments/some-uuid/ticket2828/2828.patch) by @mwhansen created at 2008-04-06 10:36:42\n\nNote that this patch is based against 3.0.alpha2.",
    "created_at": "2008-04-06T10:36:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2828#issuecomment-19373",
    "user": "https://github.com/mwhansen"
}
```

Attachment [2828.patch](tarball://root/attachments/some-uuid/ticket2828/2828.patch) by @mwhansen created at 2008-04-06 10:36:42

Note that this patch is based against 3.0.alpha2.



---

archive/issue_comments_019374.json:
```json
{
    "body": "**Review**\n* patch applies cleanly\n* patch looks good but I'm not an expert on the subject matter\n* coverage is indeed 100% as advertised\n* doctests pass\n* some small issues are:\n  * some \"possibly wrong\"s are reported, see `trac_2828_fixes.patch`\n  * one typo, see `trac_2828_fixes.patch`\n  * a couple of classes don't have `loads(dumps(s))` doctests\n* However, this shouldn't stop the patch from being applied. \n* I say apply asap, don't let this big patch bitrot.\n\nI provide a partial fix for the issues mentioned above. The patch does not fix all issues because I ran out of steam.",
    "created_at": "2008-04-06T13:14:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2828#issuecomment-19374",
    "user": "https://github.com/malb"
}
```

**Review**
* patch applies cleanly
* patch looks good but I'm not an expert on the subject matter
* coverage is indeed 100% as advertised
* doctests pass
* some small issues are:
  * some "possibly wrong"s are reported, see `trac_2828_fixes.patch`
  * one typo, see `trac_2828_fixes.patch`
  * a couple of classes don't have `loads(dumps(s))` doctests
* However, this shouldn't stop the patch from being applied. 
* I say apply asap, don't let this big patch bitrot.

I provide a partial fix for the issues mentioned above. The patch does not fix all issues because I ran out of steam.



---

archive/issue_comments_019375.json:
```json
{
    "body": "Attachment [trac_2828_fixes.patch](tarball://root/attachments/some-uuid/ticket2828/trac_2828_fixes.patch) by mabshoff created at 2008-04-06 14:09:32\n\nMerged in Sage 3.0.alpha2",
    "created_at": "2008-04-06T14:09:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2828#issuecomment-19375",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_2828_fixes.patch](tarball://root/attachments/some-uuid/ticket2828/trac_2828_fixes.patch) by mabshoff created at 2008-04-06 14:09:32

Merged in Sage 3.0.alpha2



---

archive/issue_comments_019376.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-06T14:09:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2828#issuecomment-19376",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
