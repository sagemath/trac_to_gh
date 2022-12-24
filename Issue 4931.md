# Issue 4931: [with patch, needs review] Sage 3.2.3.final: Fix various Solaris 10 build issues in the Sage library

archive/issues_004931.json:
```json
{
    "body": "Assignee: mabshoff\n\nThere are a couple buglets in the Sage library that cause build issues on Solaris. The attached patch fixes those.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4931\n\n",
    "created_at": "2009-01-03T04:47:39Z",
    "labels": [
        "porting: Solaris",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.3",
    "title": "[with patch, needs review] Sage 3.2.3.final: Fix various Solaris 10 build issues in the Sage library",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4931",
    "user": "mabshoff"
}
```
Assignee: mabshoff

There are a couple buglets in the Sage library that cause build issues on Solaris. The attached patch fixes those.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/4931





---

archive/issue_comments_037405.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-03T04:47:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4931#issuecomment-37405",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_037406.json:
```json
{
    "body": "I read the patch.  Positive review if it still works on linux.",
    "created_at": "2009-01-03T04:53:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4931#issuecomment-37406",
    "user": "@williamstein"
}
```

I read the patch.  Positive review if it still works on linux.



---

archive/issue_comments_037407.json:
```json
{
    "body": "Attachment [trac_4931.patch](tarball://root/attachments/some-uuid/ticket4931/trac_4931.patch) by mabshoff created at 2009-01-03 05:51:22",
    "created_at": "2009-01-03T05:51:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4931#issuecomment-37407",
    "user": "mabshoff"
}
```

Attachment [trac_4931.patch](tarball://root/attachments/some-uuid/ticket4931/trac_4931.patch) by mabshoff created at 2009-01-03 05:51:22



---

archive/issue_comments_037408.json:
```json
{
    "body": "I found some major breakage exposed by actually looking at the code. See #4932. \n\nWith the attached referee followup patch this gets positive review.",
    "created_at": "2009-01-03T06:32:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4931#issuecomment-37408",
    "user": "@williamstein"
}
```

I found some major breakage exposed by actually looking at the code. See #4932. 

With the attached referee followup patch this gets positive review.



---

archive/issue_comments_037409.json:
```json
{
    "body": "Attachment [trac_4931_ref.patch](tarball://root/attachments/some-uuid/ticket4931/trac_4931_ref.patch) by @williamstein created at 2009-01-03 06:33:56",
    "created_at": "2009-01-03T06:33:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4931#issuecomment-37409",
    "user": "@williamstein"
}
```

Attachment [trac_4931_ref.patch](tarball://root/attachments/some-uuid/ticket4931/trac_4931_ref.patch) by @williamstein created at 2009-01-03 06:33:56



---

archive/issue_comments_037410.json:
```json
{
    "body": "The referee patch passes doctests.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-03T06:42:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4931#issuecomment-37410",
    "user": "mabshoff"
}
```

The referee patch passes doctests.

Cheers,

Michael



---

archive/issue_comments_037411.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-03T06:43:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4931#issuecomment-37411",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_037412.json:
```json
{
    "body": "Merged both patches in Sage 3.2.3.final",
    "created_at": "2009-01-03T06:43:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4931#issuecomment-37412",
    "user": "mabshoff"
}
```

Merged both patches in Sage 3.2.3.final
