# Issue 9148: [with patch, needs review] Fix deprecated sha module usage in wiki2html.py

archive/issues_009148.json:
```json
{
    "body": "Assignee: tba\n\nThe following patch replaces the deprecated sha module in sagenb/notebook/wiki2html.py to get rid of the following warning:\n\nDeprecationWarning: the sha module is deprecated; use the hashlib module instead\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9148\n\n",
    "created_at": "2010-06-05T11:02:03Z",
    "labels": [
        "notebook",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "[with patch, needs review] Fix deprecated sha module usage in wiki2html.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9148",
    "user": "cschwan"
}
```
Assignee: tba

The following patch replaces the deprecated sha module in sagenb/notebook/wiki2html.py to get rid of the following warning:

DeprecationWarning: the sha module is deprecated; use the hashlib module instead


Issue created by migration from https://trac.sagemath.org/ticket/9148





---

archive/issue_comments_085414.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-09-17T01:16:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9148",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9148#issuecomment-85414",
    "user": "mhansen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_085415.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2010-09-17T01:16:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9148",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9148#issuecomment-85415",
    "user": "mhansen"
}
```

Looks good to me.



---

archive/issue_comments_085416.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-17T01:16:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9148",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9148#issuecomment-85416",
    "user": "mhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_085417.json:
```json
{
    "body": "Could someone prepend the ticket number to the first line of the patch commit string and restore the positive review?",
    "created_at": "2010-09-18T07:47:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9148",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9148#issuecomment-85417",
    "user": "mpatel"
}
```

Could someone prepend the ticket number to the first line of the patch commit string and restore the positive review?



---

archive/issue_comments_085418.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-09-18T07:47:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9148",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9148#issuecomment-85418",
    "user": "mpatel"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_085419.json:
```json
{
    "body": "Attachment [sagenb-0.8-fix-deprecated-sha-module.patch](tarball://root/attachments/some-uuid/ticket9148/sagenb-0.8-fix-deprecated-sha-module.patch) by cschwan created at 2010-09-30 10:37:19",
    "created_at": "2010-09-30T10:37:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9148",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9148#issuecomment-85419",
    "user": "cschwan"
}
```

Attachment [sagenb-0.8-fix-deprecated-sha-module.patch](tarball://root/attachments/some-uuid/ticket9148/sagenb-0.8-fix-deprecated-sha-module.patch) by cschwan created at 2010-09-30 10:37:19



---

archive/issue_comments_085420.json:
```json
{
    "body": "Updated patch - contains the ticket number now.",
    "created_at": "2010-09-30T10:39:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9148",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9148#issuecomment-85420",
    "user": "cschwan"
}
```

Updated patch - contains the ticket number now.



---

archive/issue_comments_085421.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2010-09-30T10:49:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9148",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9148#issuecomment-85421",
    "user": "mpatel"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_085422.json:
```json
{
    "body": "Rebase to fix failed \"hunk\".  Apply only this patch.",
    "created_at": "2010-10-03T10:11:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9148",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9148#issuecomment-85422",
    "user": "mpatel"
}
```

Rebase to fix failed "hunk".  Apply only this patch.



---

archive/issue_comments_085423.json:
```json
{
    "body": "Attachment [sagenb-0.8-fix-deprecated-sha-module.2.patch](tarball://root/attachments/some-uuid/ticket9148/sagenb-0.8-fix-deprecated-sha-module.2.patch) by mpatel created at 2010-10-03 10:12:06\n\nI've attached a rebased patch that fixes a failed \"hunk.\"",
    "created_at": "2010-10-03T10:12:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9148",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9148#issuecomment-85423",
    "user": "mpatel"
}
```

Attachment [sagenb-0.8-fix-deprecated-sha-module.2.patch](tarball://root/attachments/some-uuid/ticket9148/sagenb-0.8-fix-deprecated-sha-module.2.patch) by mpatel created at 2010-10-03 10:12:06

I've attached a rebased patch that fixes a failed "hunk."



---

archive/issue_comments_085424.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-10-04T01:34:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9148",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9148#issuecomment-85424",
    "user": "mpatel"
}
```

Resolution: fixed
