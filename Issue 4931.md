# Issue 4931: [with patch, needs review] Sage 3.2.3.final: Fix various Solaris 10 build issues in the Sage library

archive/issues_004931.json:
```json
{
    "body": "Assignee: mabshoff\n\nThere are a couple buglets in the Sage library that cause build issues on Solaris. The attached patch fixes those.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4931\n\n",
    "created_at": "2009-01-03T04:47:39Z",
    "labels": [
        "component: porting: solaris",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.3",
    "title": "[with patch, needs review] Sage 3.2.3.final: Fix various Solaris 10 build issues in the Sage library",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4931",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

There are a couple buglets in the Sage library that cause build issues on Solaris. The attached patch fixes those.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/4931





---

archive/issue_comments_037333.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-03T04:47:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4931#issuecomment-37333",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_037334.json:
```json
{
    "body": "I read the patch.  Positive review if it still works on linux.",
    "created_at": "2009-01-03T04:53:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4931#issuecomment-37334",
    "user": "https://github.com/williamstein"
}
```

I read the patch.  Positive review if it still works on linux.



---

archive/issue_comments_037335.json:
```json
{
    "body": "Attachment [trac_4931.patch](tarball://root/attachments/some-uuid/ticket4931/trac_4931.patch) by mabshoff created at 2009-01-03 05:51:22",
    "created_at": "2009-01-03T05:51:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4931#issuecomment-37335",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_4931.patch](tarball://root/attachments/some-uuid/ticket4931/trac_4931.patch) by mabshoff created at 2009-01-03 05:51:22



---

archive/issue_comments_037336.json:
```json
{
    "body": "I found some major breakage exposed by actually looking at the code. See #4932. \n\nWith the attached referee followup patch this gets positive review.",
    "created_at": "2009-01-03T06:32:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4931#issuecomment-37336",
    "user": "https://github.com/williamstein"
}
```

I found some major breakage exposed by actually looking at the code. See #4932. 

With the attached referee followup patch this gets positive review.



---

archive/issue_comments_037337.json:
```json
{
    "body": "Attachment [trac_4931_ref.patch](tarball://root/attachments/some-uuid/ticket4931/trac_4931_ref.patch) by @williamstein created at 2009-01-03 06:33:56",
    "created_at": "2009-01-03T06:33:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4931#issuecomment-37337",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_4931_ref.patch](tarball://root/attachments/some-uuid/ticket4931/trac_4931_ref.patch) by @williamstein created at 2009-01-03 06:33:56



---

archive/issue_comments_037338.json:
```json
{
    "body": "The referee patch passes doctests.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-03T06:42:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4931#issuecomment-37338",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The referee patch passes doctests.

Cheers,

Michael



---

archive/issue_events_011352.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-03T06:43:03Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4931",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4931#event-11352"
}
```



---

archive/issue_comments_037339.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-03T06:43:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4931#issuecomment-37339",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_037340.json:
```json
{
    "body": "Merged both patches in Sage 3.2.3.final",
    "created_at": "2009-01-03T06:43:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4931#issuecomment-37340",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged both patches in Sage 3.2.3.final
