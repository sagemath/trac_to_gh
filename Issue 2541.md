# Issue 2541: [with patch, needs review] Fixes bugs in binary_codes.pyx

archive/issues_002541.json:
```json
{
    "body": "Assignee: @rlmill\n\nThis also makes the automorphism group calculator return the size of the group.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2541\n\n",
    "created_at": "2008-03-16T03:05:25Z",
    "labels": [
        "component: coding theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.4",
    "title": "[with patch, needs review] Fixes bugs in binary_codes.pyx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2541",
    "user": "https://github.com/rlmill"
}
```
Assignee: @rlmill

This also makes the automorphism group calculator return the size of the group.

Issue created by migration from https://trac.sagemath.org/ticket/2541





---

archive/issue_comments_017290.json:
```json
{
    "body": "Attachment [2541-binary_code.patch](tarball://root/attachments/some-uuid/ticket2541/2541-binary_code.patch) by @rlmill created at 2008-03-16 03:23:03\n\nThis may fix one of the issues mentioned in #2514. At the very least it adds doctests that show that if there still is a problem, it isn't in `binary_code.pyx`.",
    "created_at": "2008-03-16T03:23:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2541",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2541#issuecomment-17290",
    "user": "https://github.com/rlmill"
}
```

Attachment [2541-binary_code.patch](tarball://root/attachments/some-uuid/ticket2541/2541-binary_code.patch) by @rlmill created at 2008-03-16 03:23:03

This may fix one of the issues mentioned in #2514. At the very least it adds doctests that show that if there still is a problem, it isn't in `binary_code.pyx`.



---

archive/issue_comments_017291.json:
```json
{
    "body": "Applies and passes tests for me.",
    "created_at": "2008-03-16T03:41:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2541",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2541#issuecomment-17291",
    "user": "https://github.com/mwhansen"
}
```

Applies and passes tests for me.



---

archive/issue_comments_017292.json:
```json
{
    "body": "I will remove the colorful language once I merge this patch :)\n\nCheers,\n\nMichael",
    "created_at": "2008-03-16T04:15:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2541",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2541#issuecomment-17292",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I will remove the colorful language once I merge this patch :)

Cheers,

Michael



---

archive/issue_comments_017293.json:
```json
{
    "body": "Merged in Sage 2.10.4.rc0 (minus one line ;)",
    "created_at": "2008-03-16T04:39:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2541",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2541#issuecomment-17293",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.4.rc0 (minus one line ;)



---

archive/issue_comments_017294.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-16T04:39:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2541",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2541#issuecomment-17294",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
