# Issue 7752: RAM is not free after deleting a worksheet

archive/issues_007752.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @williamstein acleone @qed777\n\nTotal RAM use does not decrease after deleting a worksheet. In the Trash section, it appears as (running).\n\nI suggest the page is stopped, then deleted, as usually someone deleting a worksheet does not plan on working on it further.\n\nWhen I have to correct a lot of worksheets from the students, I upload one, correct it, save it, and delete it, but RAM eventually gets collapsed.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7752\n\n",
    "created_at": "2009-12-23T14:16:30Z",
    "labels": [
        "component: notebook",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "RAM is not free after deleting a worksheet",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7752",
    "user": "https://trac.sagemath.org/admin/accounts/users/pang"
}
```
Assignee: @williamstein

CC:  @williamstein acleone @qed777

Total RAM use does not decrease after deleting a worksheet. In the Trash section, it appears as (running).

I suggest the page is stopped, then deleted, as usually someone deleting a worksheet does not plan on working on it further.

When I have to correct a lot of worksheets from the students, I upload one, correct it, save it, and delete it, but RAM eventually gets collapsed.

Issue created by migration from https://trac.sagemath.org/ticket/7752





---

archive/issue_comments_066648.json:
```json
{
    "body": "Attachment [trac_7752-delete-worksheet-quit.patch](tarball://root/attachments/some-uuid/ticket7752/trac_7752-delete-worksheet-quit.patch) by @TimDumol created at 2010-01-19 10:42:08\n\nQuits a worksheet only if the only user viewing the worksheet is the person trashing it.",
    "created_at": "2010-01-19T10:42:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7752",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7752#issuecomment-66648",
    "user": "https://github.com/TimDumol"
}
```

Attachment [trac_7752-delete-worksheet-quit.patch](tarball://root/attachments/some-uuid/ticket7752/trac_7752-delete-worksheet-quit.patch) by @TimDumol created at 2010-01-19 10:42:08

Quits a worksheet only if the only user viewing the worksheet is the person trashing it.



---

archive/issue_events_018541.json:
```json
{
    "actor": "https://github.com/TimDumol",
    "created_at": "2010-01-19T10:43:00Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7752",
    "milestone": "sage-4.3.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7752#event-18541"
}
```



---

archive/issue_comments_066649.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-19T10:43:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7752",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7752#issuecomment-66649",
    "user": "https://github.com/TimDumol"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_066650.json:
```json
{
    "body": "This should do the trick. It only quits a worksheet if the only user viewing it is the person trashing it, as it may otherwise ruin other people's sessions.",
    "created_at": "2010-01-19T10:43:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7752",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7752#issuecomment-66650",
    "user": "https://github.com/TimDumol"
}
```

This should do the trick. It only quits a worksheet if the only user viewing it is the person trashing it, as it may otherwise ruin other people's sessions.



---

archive/issue_comments_066651.json:
```json
{
    "body": "LGTM.",
    "created_at": "2010-01-19T12:53:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7752",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7752#issuecomment-66651",
    "user": "https://trac.sagemath.org/admin/accounts/users/acleone"
}
```

LGTM.



---

archive/issue_comments_066652.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-19T12:53:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7752",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7752#issuecomment-66652",
    "user": "https://trac.sagemath.org/admin/accounts/users/acleone"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_066653.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-25T01:01:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7752",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7752#issuecomment-66653",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_018542.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-01-25T01:01:58Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7752",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7752#event-18542"
}
```
