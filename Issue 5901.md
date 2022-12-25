# Issue 5901: [with patch, needs review] Avoid permission denied error message when testing with non-writeable sage install

archive/issues_005901.json:
```json
{
    "body": "Assignee: @timabbott\n\nThis is a patch to fix the fact that running sage tests prints a permission denied error writing to test.log when you don't have write access to the Sage installation.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5901\n\n",
    "created_at": "2009-04-26T05:47:24Z",
    "labels": [
        "component: debian-package",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5",
    "title": "[with patch, needs review] Avoid permission denied error message when testing with non-writeable sage install",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5901",
    "user": "https://github.com/timabbott"
}
```
Assignee: @timabbott

This is a patch to fix the fact that running sage tests prints a permission denied error writing to test.log when you don't have write access to the Sage installation.


Issue created by migration from https://trac.sagemath.org/ticket/5901





---

archive/issue_comments_046558.json:
```json
{
    "body": "Attachment [sage_scripts-maketest.patch](tarball://root/attachments/some-uuid/ticket5901/sage_scripts-maketest.patch) by @TimDumol created at 2010-04-18 13:31:21\n\nI don't think this is applicable anymore. As far as I know, the testing is done in the user's home folder. Making $SAGE_ROOT unwritable didn't give me any permission errors either.",
    "created_at": "2010-04-18T13:31:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5901",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5901#issuecomment-46558",
    "user": "https://github.com/TimDumol"
}
```

Attachment [sage_scripts-maketest.patch](tarball://root/attachments/some-uuid/ticket5901/sage_scripts-maketest.patch) by @TimDumol created at 2010-04-18 13:31:21

I don't think this is applicable anymore. As far as I know, the testing is done in the user's home folder. Making $SAGE_ROOT unwritable didn't give me any permission errors either.



---

archive/issue_comments_046559.json:
```json
{
    "body": "My bad, I thought this was for sage-test. Looks good to me.",
    "created_at": "2010-06-23T11:11:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5901",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5901#issuecomment-46559",
    "user": "https://github.com/TimDumol"
}
```

My bad, I thought this was for sage-test. Looks good to me.



---

archive/issue_comments_046560.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-23T11:11:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5901",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5901#issuecomment-46560",
    "user": "https://github.com/TimDumol"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_006155.json:
```json
{
    "actor": "@rlmill",
    "created_at": "2010-06-25T15:42:30Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5901",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5901#event-6155"
}
```



---

archive/issue_comments_046561.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-25T15:42:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5901",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5901#issuecomment-46561",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed
