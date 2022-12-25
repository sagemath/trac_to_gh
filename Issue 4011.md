# Issue 4011: [with patch, positive review] notebook -- copying a worksheet on worksheet listings page results in the new worksheet being listed as running

archive/issues_004011.json:
```json
{
    "body": "Assignee: @mwhansen\n\nWhy is the new worksheet, copy of another worksheet, running? It hasn't been accessed by the user.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4011\n\n",
    "closed_at": "2009-03-24T23:26:00Z",
    "created_at": "2008-08-31T01:08:02Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "[with patch, positive review] notebook -- copying a worksheet on worksheet listings page results in the new worksheet being listed as running",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4011",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```
Assignee: @mwhansen

Why is the new worksheet, copy of another worksheet, running? It hasn't been accessed by the user.

Issue created by migration from https://trac.sagemath.org/ticket/4011





---

archive/issue_comments_028886.json:
```json
{
    "body": "Please delete sage-4011_1.patch.\n\nPatch sage-4011_1.patch doesn't seem to resolve the problem.",
    "created_at": "2008-09-09T16:25:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4011",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4011#issuecomment-28886",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Please delete sage-4011_1.patch.

Patch sage-4011_1.patch doesn't seem to resolve the problem.



---

archive/issue_comments_028887.json:
```json
{
    "body": "Attachment [trac_4011.patch](tarball://root/attachments/some-uuid/ticket4011/trac_4011.patch) by @mwhansen created at 2009-01-24 06:20:35",
    "created_at": "2009-01-24T06:20:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4011",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4011#issuecomment-28887",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_4011.patch](tarball://root/attachments/some-uuid/ticket4011/trac_4011.patch) by @mwhansen created at 2009-01-24 06:20:35



---

archive/issue_comments_028888.json:
```json
{
    "body": "I've added a test to my Selenium test suite for this since it requires the Javascript to run.",
    "created_at": "2009-01-24T06:21:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4011",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4011#issuecomment-28888",
    "user": "https://github.com/mwhansen"
}
```

I've added a test to my Selenium test suite for this since it requires the Javascript to run.



---

archive/issue_comments_028889.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-24T06:21:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4011",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4011#issuecomment-28889",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_028890.json:
```json
{
    "body": "Changing assignee from boothby to @mwhansen.",
    "created_at": "2009-01-24T06:21:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4011",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4011#issuecomment-28890",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from boothby to @mwhansen.



---

archive/issue_comments_028891.json:
```json
{
    "body": "This might be really nitpicky, but can we make the code not have a double negative?  I.e., `if no_load is in ctx`, rather than `if no_load not in ctx`.  Having a double negative makes the code a bit more confusing.",
    "created_at": "2009-02-07T17:43:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4011",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4011#issuecomment-28891",
    "user": "https://github.com/jasongrout"
}
```

This might be really nitpicky, but can we make the code not have a double negative?  I.e., `if no_load is in ctx`, rather than `if no_load not in ctx`.  Having a double negative makes the code a bit more confusing.



---

archive/issue_comments_028892.json:
```json
{
    "body": "And if you're modifying the patch anyway, you might fix the typo in the docs in js.py for this function: worsheet -> worksheet.",
    "created_at": "2009-02-07T17:45:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4011",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4011#issuecomment-28892",
    "user": "https://github.com/jasongrout"
}
```

And if you're modifying the patch anyway, you might fix the typo in the docs in js.py for this function: worsheet -> worksheet.



---

archive/issue_comments_028893.json:
```json
{
    "body": "Attachment [trac_4135.2.patch](tarball://root/attachments/some-uuid/ticket4011/trac_4135.2.patch) by TimothyClemans created at 2009-03-16 19:58:10",
    "created_at": "2009-03-16T19:58:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4011",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4011#issuecomment-28893",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Attachment [trac_4135.2.patch](tarball://root/attachments/some-uuid/ticket4011/trac_4135.2.patch) by TimothyClemans created at 2009-03-16 19:58:10



---

archive/issue_comments_028894.json:
```json
{
    "body": "Attachment [trac_4011.2.patch](tarball://root/attachments/some-uuid/ticket4011/trac_4011.2.patch) by TimothyClemans created at 2009-03-16 19:59:22\n\nApply trac_4011.2.patch",
    "created_at": "2009-03-16T19:59:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4011",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4011#issuecomment-28894",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Attachment [trac_4011.2.patch](tarball://root/attachments/some-uuid/ticket4011/trac_4011.2.patch) by TimothyClemans created at 2009-03-16 19:59:22

Apply trac_4011.2.patch



---

archive/issue_events_009182.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-03-24T23:26:00Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4011",
    "milestone": "sage-3.4.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4011#event-9182"
}
```



---

archive/issue_comments_028895.json:
```json
{
    "body": "Merged trac_4011.2.patch in Sage 3.4.1.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-24T23:26:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4011",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4011#issuecomment-28895",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged trac_4011.2.patch in Sage 3.4.1.alpha0.

Cheers,

Michael



---

archive/issue_comments_028896.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-24T23:26:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4011",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4011#issuecomment-28896",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_009183.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-03-24T23:26:00Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4011",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4011#event-9183"
}
```
