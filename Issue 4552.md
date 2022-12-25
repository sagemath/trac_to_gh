# Issue 4552: notebook -- when email system on, registration is broken

archive/issues_004552.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  @wjp\n\nDepends on #4551\n\nIssue created by migration from https://trac.sagemath.org/ticket/4552\n\n",
    "created_at": "2008-11-19T18:00:43Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "notebook -- when email system on, registration is broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4552",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```
Assignee: boothby

CC:  @wjp

Depends on #4551

Issue created by migration from https://trac.sagemath.org/ticket/4552





---

archive/issue_comments_034053.json:
```json
{
    "body": "Attachment [sage-4552.patch](tarball://root/attachments/some-uuid/ticket4552/sage-4552.patch) by TimothyClemans created at 2008-11-19 18:11:32",
    "created_at": "2008-11-19T18:11:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4552#issuecomment-34053",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Attachment [sage-4552.patch](tarball://root/attachments/some-uuid/ticket4552/sage-4552.patch) by TimothyClemans created at 2008-11-19 18:11:32



---

archive/issue_comments_034054.json:
```json
{
    "body": "Timothy -- please describe the problem that this is supposed to fix.  \"Depends on #4551\" is insufficient.",
    "created_at": "2009-01-22T00:56:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4552#issuecomment-34054",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Timothy -- please describe the problem that this is supposed to fix.  "Depends on #4551" is insufficient.



---

archive/issue_comments_034055.json:
```json
{
    "body": "If the email config is set to True then registration doesn't work.",
    "created_at": "2009-01-22T00:59:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4552#issuecomment-34055",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

If the email config is set to True then registration doesn't work.



---

archive/issue_comments_034056.json:
```json
{
    "body": "Attachment [trac_4552-notebook_account_email.patch](tarball://root/attachments/some-uuid/ticket4552/trac_4552-notebook_account_email.patch) by @wjp created at 2009-09-01 18:40:58\n\nmodified patch without dependency on #4551",
    "created_at": "2009-09-01T18:40:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4552#issuecomment-34056",
    "user": "https://github.com/wjp"
}
```

Attachment [trac_4552-notebook_account_email.patch](tarball://root/attachments/some-uuid/ticket4552/trac_4552-notebook_account_email.patch) by @wjp created at 2009-09-01 18:40:58

modified patch without dependency on #4551



---

archive/issue_comments_034057.json:
```json
{
    "body": "I modified the attached patch to remove the dependency on #4551. (Only apply `trac_4552-notebook_account_email.patch`)\n\nTo elaborate on the problem a little bit: the problem was that the value of the 'email' input box was never read from the form. As a result, when the verification code tries to access it, the server gets a KeyError.\n\nFor what it's worth, I give a positive review to adding 'email' to 'input_boxes', which is how Timothy's patch fixes the problem.",
    "created_at": "2009-09-01T18:45:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4552#issuecomment-34057",
    "user": "https://github.com/wjp"
}
```

I modified the attached patch to remove the dependency on #4551. (Only apply `trac_4552-notebook_account_email.patch`)

To elaborate on the problem a little bit: the problem was that the value of the 'email' input box was never read from the form. As a result, when the verification code tries to access it, the server gets a KeyError.

For what it's worth, I give a positive review to adding 'email' to 'input_boxes', which is how Timothy's patch fixes the problem.



---

archive/issue_comments_034058.json:
```json
{
    "body": "It turns out the dependency on #4551 was really a dependency on #4135. Now that that has been merged, positive review.\n\nNote to release manager: apply only the _original_ patch (`sage-4552.patch`)",
    "created_at": "2009-09-07T09:52:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4552#issuecomment-34058",
    "user": "https://github.com/wjp"
}
```

It turns out the dependency on #4551 was really a dependency on #4135. Now that that has been merged, positive review.

Note to release manager: apply only the _original_ patch (`sage-4552.patch`)



---

archive/issue_events_010368.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-09-07T17:45:16Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4552",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4552#event-10368"
}
```



---

archive/issue_comments_034059.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-07T17:45:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4552#issuecomment-34059",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_034060.json:
```json
{
    "body": "Merged `sage-4552.patch`.",
    "created_at": "2009-09-07T17:45:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4552#issuecomment-34060",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged `sage-4552.patch`.
