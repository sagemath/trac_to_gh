# Issue 5708: [with patch; needs review] solaris -- fix heilbronn.pyx (it turns out that our roundf is wrong)

archive/issues_005708.json:
```json
{
    "body": "Assignee: @craigcitro\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5708\n\n",
    "created_at": "2009-04-08T00:24:34Z",
    "labels": [
        "component: modular forms",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "[with patch; needs review] solaris -- fix heilbronn.pyx (it turns out that our roundf is wrong)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5708",
    "user": "https://github.com/williamstein"
}
```
Assignee: @craigcitro



Issue created by migration from https://trac.sagemath.org/ticket/5708





---

archive/issue_comments_044513.json:
```json
{
    "body": "Attachment [trac_5708.patch](tarball://root/attachments/some-uuid/ticket5708/trac_5708.patch) by @williamstein created at 2009-04-08 00:27:56",
    "created_at": "2009-04-08T00:27:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5708",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5708#issuecomment-44513",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_5708.patch](tarball://root/attachments/some-uuid/ticket5708/trac_5708.patch) by @williamstein created at 2009-04-08 00:27:56



---

archive/issue_comments_044514.json:
```json
{
    "body": "Positive review. The faulty roundf() substitute was for Solaris 9 and my fault :(\n\nCheers,\n\nMichael",
    "created_at": "2009-04-09T05:53:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5708",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5708#issuecomment-44514",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Positive review. The faulty roundf() substitute was for Solaris 9 and my fault :(

Cheers,

Michael



---

archive/issue_comments_044515.json:
```json
{
    "body": "Merged in Sage 3.4.1.rc2.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-09T06:09:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5708",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5708#issuecomment-44515",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.1.rc2.

Cheers,

Michael



---

archive/issue_comments_044516.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-09T06:09:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5708",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5708#issuecomment-44516",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
