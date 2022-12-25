# Issue 5467: The sage/macaulay2 interface doesn't work at all on large input

archive/issues_005467.json:
```json
{
    "body": "Assignee: @mwhansen\n\nON OS X and Linux with Macaulay 1.2.\n\n```\nteragon:~ wstein$ sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: macaulay2(10^10000)\nsage0\nsage: macaulay2(10^10000)\nsage1\nsage: macaulay2(10^10000)\nsage2\n```\n| Sage Version 3.4.alpha0, Release Date: 2009-02-24                  |\n| Type notebook() for the GUI, and license() for information.        |\nSee also #7897 and #7915.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5467\n\n",
    "closed_at": "2010-07-21T03:30:21Z",
    "created_at": "2009-03-10T18:03:16Z",
    "labels": [
        "component: interfaces",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "The sage/macaulay2 interface doesn't work at all on large input",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5467",
    "user": "https://github.com/williamstein"
}
```
Assignee: @mwhansen

ON OS X and Linux with Macaulay 1.2.

```
teragon:~ wstein$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: macaulay2(10^10000)
sage0
sage: macaulay2(10^10000)
sage1
sage: macaulay2(10^10000)
sage2
```
| Sage Version 3.4.alpha0, Release Date: 2009-02-24                  |
| Type notebook() for the GUI, and license() for information.        |
See also #7897 and #7915.

Issue created by migration from https://trac.sagemath.org/ticket/5467





---

archive/issue_events_012775.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-03-10T19:20:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5467",
    "milestone": "sage-3.4.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5467#event-12775"
}
```



---

archive/issue_comments_042351.json:
```json
{
    "body": "This is a trivial fix - the problem was in a wrong file loading command passed to Macaulay2.\n\nThe tests in the modified function pass (although optional tests for the whole file give a bunch of unrelated mistakes).",
    "created_at": "2010-01-09T07:29:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5467#issuecomment-42351",
    "user": "https://github.com/novoselt"
}
```

This is a trivial fix - the problem was in a wrong file loading command passed to Macaulay2.

The tests in the modified function pass (although optional tests for the whole file give a bunch of unrelated mistakes).



---

archive/issue_comments_042352.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-09T07:29:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5467#issuecomment-42352",
    "user": "https://github.com/novoselt"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_042353.json:
```json
{
    "body": "Must be applied after the first patch.",
    "created_at": "2010-01-09T20:41:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5467#issuecomment-42353",
    "user": "https://github.com/novoselt"
}
```

Must be applied after the first patch.



---

archive/issue_comments_042354.json:
```json
{
    "body": "Attachment [5467_long_input_to_Macaulay2_second_part.patch](tarball://root/attachments/some-uuid/ticket5467/5467_long_input_to_Macaulay2_second_part.patch) by @novoselt created at 2010-01-09 20:42:36\n\nI managed to make a trivial mistake in this trivial fix - one of the test lines was not marked with #optional. Now it is.",
    "created_at": "2010-01-09T20:42:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5467#issuecomment-42354",
    "user": "https://github.com/novoselt"
}
```

Attachment [5467_long_input_to_Macaulay2_second_part.patch](tarball://root/attachments/some-uuid/ticket5467/5467_long_input_to_Macaulay2_second_part.patch) by @novoselt created at 2010-01-09 20:42:36

I managed to make a trivial mistake in this trivial fix - one of the test lines was not marked with #optional. Now it is.



---

archive/issue_comments_042355.json:
```json
{
    "body": "Converged patches into a single one and made the commit message of standard form.",
    "created_at": "2010-01-31T23:02:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5467#issuecomment-42355",
    "user": "https://github.com/novoselt"
}
```

Converged patches into a single one and made the commit message of standard form.



---

archive/issue_comments_042356.json:
```json
{
    "body": "Only this patch should be applied.",
    "created_at": "2010-01-31T23:04:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5467#issuecomment-42356",
    "user": "https://github.com/novoselt"
}
```

Only this patch should be applied.



---

archive/issue_comments_042357.json:
```json
{
    "body": "Attachment [5467_long_input_to_Macaulay2.patch](tarball://root/attachments/some-uuid/ticket5467/5467_long_input_to_Macaulay2.patch) by @novoselt created at 2010-02-07 17:02:33",
    "created_at": "2010-02-07T17:02:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5467#issuecomment-42357",
    "user": "https://github.com/novoselt"
}
```

Attachment [5467_long_input_to_Macaulay2.patch](tarball://root/attachments/some-uuid/ticket5467/5467_long_input_to_Macaulay2.patch) by @novoselt created at 2010-02-07 17:02:33



---

archive/issue_comments_042358.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-09T01:03:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5467#issuecomment-42358",
    "user": "https://github.com/mwhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_042359.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2010-07-09T01:03:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5467#issuecomment-42359",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.



---

archive/issue_comments_042360.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-21T03:30:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5467#issuecomment-42360",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_012776.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-07-21T03:30:21Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5467",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5467#event-12776"
}
```
