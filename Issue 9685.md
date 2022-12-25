# Issue 9685: constructor for the all ones matrix

archive/issues_009685.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @jdemeyer\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9685\n\n",
    "created_at": "2010-08-04T13:30:38Z",
    "labels": [
        "component: user interface",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.1",
    "title": "constructor for the all ones matrix",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9685",
    "user": "https://github.com/rlmill"
}
```
Assignee: @williamstein

CC:  @jdemeyer



Issue created by migration from https://trac.sagemath.org/ticket/9685





---

archive/issue_comments_093990.json:
```json
{
    "body": "Attachment [trac_9685.patch](tarball://root/attachments/some-uuid/ticket9685/trac_9685.patch) by @rlmill created at 2010-08-04 13:34:03",
    "created_at": "2010-08-04T13:34:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9685#issuecomment-93990",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac_9685.patch](tarball://root/attachments/some-uuid/ticket9685/trac_9685.patch) by @rlmill created at 2010-08-04 13:34:03



---

archive/issue_comments_093991.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-04T13:34:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9685#issuecomment-93991",
    "user": "https://github.com/rlmill"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_093992.json:
```json
{
    "body": "Worked for me and behaves consistently with similar functions such as zero_matrix().  The sparse matrix option is not too useful here (since the matrix gets filled with ones), but I guess it's best to be consistent with similar functions, which the patch is.",
    "created_at": "2010-11-03T05:46:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9685#issuecomment-93992",
    "user": "https://trac.sagemath.org/admin/accounts/users/flawrence"
}
```

Worked for me and behaves consistently with similar functions such as zero_matrix().  The sparse matrix option is not too useful here (since the matrix gets filled with ones), but I guess it's best to be consistent with similar functions, which the patch is.



---

archive/issue_comments_093993.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-11-03T05:46:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9685#issuecomment-93993",
    "user": "https://trac.sagemath.org/admin/accounts/users/flawrence"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_093994.json:
```json
{
    "body": "When applying this to sage-4.6.1.alpha0, I get\n\n```\npatching file sage/matrix/constructor.py\nHunk #1 succeeded at 1348 with fuzz 2 (offset 363 lines).\n```\n\nSo the patch succeeds, but it's probably better if it gets rebased properly.",
    "created_at": "2010-11-03T10:47:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9685#issuecomment-93994",
    "user": "https://github.com/jdemeyer"
}
```

When applying this to sage-4.6.1.alpha0, I get

```
patching file sage/matrix/constructor.py
Hunk #1 succeeded at 1348 with fuzz 2 (offset 363 lines).
```

So the patch succeeds, but it's probably better if it gets rebased properly.



---

archive/issue_comments_093995.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-11-03T10:47:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9685#issuecomment-93995",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_093996.json:
```json
{
    "body": "If I rebased it, would someone else then have to review it?",
    "created_at": "2010-11-04T01:13:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9685#issuecomment-93996",
    "user": "https://trac.sagemath.org/admin/accounts/users/flawrence"
}
```

If I rebased it, would someone else then have to review it?



---

archive/issue_comments_093997.json:
```json
{
    "body": "Replying to [comment:4 flawrence]:\n> If I rebased it, would someone else then have to review it?\n\nI could easily review your rebasing.",
    "created_at": "2010-11-04T08:22:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9685#issuecomment-93997",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:4 flawrence]:
> If I rebased it, would someone else then have to review it?

I could easily review your rebasing.



---

archive/issue_comments_093998.json:
```json
{
    "body": "rebased version of original patch",
    "created_at": "2010-11-04T10:17:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9685#issuecomment-93998",
    "user": "https://trac.sagemath.org/admin/accounts/users/flawrence"
}
```

rebased version of original patch



---

archive/issue_comments_093999.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-11-04T10:17:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9685#issuecomment-93999",
    "user": "https://trac.sagemath.org/admin/accounts/users/flawrence"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_094000.json:
```json
{
    "body": "Attachment [trac_9685-rebased.patch](tarball://root/attachments/some-uuid/ticket9685/trac_9685-rebased.patch) by flawrence created at 2010-11-04 10:17:55",
    "created_at": "2010-11-04T10:17:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9685#issuecomment-94000",
    "user": "https://trac.sagemath.org/admin/accounts/users/flawrence"
}
```

Attachment [trac_9685-rebased.patch](tarball://root/attachments/some-uuid/ticket9685/trac_9685-rebased.patch) by flawrence created at 2010-11-04 10:17:55



---

archive/issue_comments_094001.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-11-04T15:46:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9685#issuecomment-94001",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_094002.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-11-10T22:19:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9685#issuecomment-94002",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_events_009817.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2010-11-10T22:19:59Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9685",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9685#event-9817"
}
```
