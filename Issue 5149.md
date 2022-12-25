# Issue 5149: [with patch; needs review] Cremona database -- fix a bug in handling of 990h

archive/issues_005149.json:
```json
{
    "body": "Assignee: @williamstein\n\nJohn mentioned that 990h3 is a special case in ticket #5138 -- I looked at the Cremona database code and found that there was one function where this special case isn't treated correctly.  I fixed that and added some doctests.  \n\nIssue created by migration from https://trac.sagemath.org/ticket/5149\n\n",
    "created_at": "2009-02-01T08:34:22Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "[with patch; needs review] Cremona database -- fix a bug in handling of 990h",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5149",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

John mentioned that 990h3 is a special case in ticket #5138 -- I looked at the Cremona database code and found that there was one function where this special case isn't treated correctly.  I fixed that and added some doctests.  

Issue created by migration from https://trac.sagemath.org/ticket/5149





---

archive/issue_comments_039321.json:
```json
{
    "body": "Attachment [trac_5149.patch](tarball://root/attachments/some-uuid/ticket5149/trac_5149.patch) by @JohnCremona created at 2009-02-01 10:59:51\n\nPatch applies cleanly to 3.33.alpha2 and all tests pass.  Code looks good, so pass!",
    "created_at": "2009-02-01T10:59:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5149",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5149#issuecomment-39321",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [trac_5149.patch](tarball://root/attachments/some-uuid/ticket5149/trac_5149.patch) by @JohnCremona created at 2009-02-01 10:59:51

Patch applies cleanly to 3.33.alpha2 and all tests pass.  Code looks good, so pass!



---

archive/issue_events_011930.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-02T02:56:56Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5149",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5149#event-11930"
}
```



---

archive/issue_comments_039322.json:
```json
{
    "body": "Merged in Sage 3.3.alpha4.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-02T02:56:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5149",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5149#issuecomment-39322",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha4.

Cheers,

Michael



---

archive/issue_comments_039323.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-02T02:56:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5149",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5149#issuecomment-39323",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
