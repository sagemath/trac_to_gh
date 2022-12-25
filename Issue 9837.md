# Issue 9837: Bugfix in WeylCharacterRing __call__ method

archive/issues_009837.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  sage-combinat\n\nThis addresses a bug that was reported here:\n\nhttp://groups.google.com/group/sage-combinat-devel/msg/252fd7fa0e297214\n\nThe `__call__` method of a Weyl Character ring, when `style=\"coroots\"` is specified, tries to interpret the arguments as the coroots of a weight; that weight\nis then the actual argument. However this is not appropriate if the argument is\nnot a tuple. Therefore this should be tested.\n\nThe patch implements the test.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9838\n\n",
    "created_at": "2010-08-29T19:03:03Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.1",
    "title": "Bugfix in WeylCharacterRing __call__ method",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9837",
    "user": "https://github.com/dwbump"
}
```
Assignee: @aghitza

CC:  sage-combinat

This addresses a bug that was reported here:

http://groups.google.com/group/sage-combinat-devel/msg/252fd7fa0e297214

The `__call__` method of a Weyl Character ring, when `style="coroots"` is specified, tries to interpret the arguments as the coroots of a weight; that weight
is then the actual argument. However this is not appropriate if the argument is
not a tuple. Therefore this should be tested.

The patch implements the test.

Issue created by migration from https://trac.sagemath.org/ticket/9838





---

archive/issue_comments_096922.json:
```json
{
    "body": "Changing assignee from @aghitza to @dwbump.",
    "created_at": "2010-08-29T19:08:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9837#issuecomment-96922",
    "user": "https://github.com/dwbump"
}
```

Changing assignee from @aghitza to @dwbump.



---

archive/issue_comments_096923.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-29T19:08:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9837#issuecomment-96923",
    "user": "https://github.com/dwbump"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_096924.json:
```json
{
    "body": "Changing component from algebra to group_theory.",
    "created_at": "2010-08-29T19:10:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9837#issuecomment-96924",
    "user": "https://github.com/dwbump"
}
```

Changing component from algebra to group_theory.



---

archive/issue_comments_096925.json:
```json
{
    "body": "Replying to [comment:3 bump]:\n\nThis is a bug fix. All tests pass!",
    "created_at": "2010-10-19T06:31:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9837#issuecomment-96925",
    "user": "https://github.com/anneschilling"
}
```

Replying to [comment:3 bump]:

This is a bug fix. All tests pass!



---

archive/issue_comments_096926.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-10-19T06:31:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9837#issuecomment-96926",
    "user": "https://github.com/anneschilling"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_096927.json:
```json
{
    "body": "Please change the commit message of the patch trac_9838.patch (use `hg qrefresh -e` for that).",
    "created_at": "2010-10-26T13:34:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9837#issuecomment-96927",
    "user": "https://github.com/jdemeyer"
}
```

Please change the commit message of the patch trac_9838.patch (use `hg qrefresh -e` for that).



---

archive/issue_comments_096928.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-10-26T13:34:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9837#issuecomment-96928",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_096929.json:
```json
{
    "body": "> Please change the commit message of the patch trac_9838.patch (use hg qrefresh -e for that).\n\nDone. -Dan",
    "created_at": "2010-10-26T15:19:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9837#issuecomment-96929",
    "user": "https://github.com/dwbump"
}
```

> Please change the commit message of the patch trac_9838.patch (use hg qrefresh -e for that).

Done. -Dan



---

archive/issue_comments_096930.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2010-10-26T15:19:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9837#issuecomment-96930",
    "user": "https://github.com/dwbump"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_096931.json:
```json
{
    "body": "Replying to [comment:7 bump]:\n> Done. -Dan\n\nSorry, the ticket number should also be in the first line of the commit message.",
    "created_at": "2010-10-27T08:52:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9837#issuecomment-96931",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:7 bump]:
> Done. -Dan

Sorry, the ticket number should also be in the first line of the commit message.



---

archive/issue_comments_096932.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-10-27T08:52:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9837#issuecomment-96932",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_096933.json:
```json
{
    "body": "Attachment [trac_9838.patch](tarball://root/attachments/some-uuid/ticket9838/trac_9838.patch) by @dwbump created at 2010-10-27 16:25:02\n\n#9838: bugfix in WeylCharac terRing call method",
    "created_at": "2010-10-27T16:25:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9837#issuecomment-96933",
    "user": "https://github.com/dwbump"
}
```

Attachment [trac_9838.patch](tarball://root/attachments/some-uuid/ticket9838/trac_9838.patch) by @dwbump created at 2010-10-27 16:25:02

#9838: bugfix in WeylCharac terRing call method



---

archive/issue_comments_096934.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2010-10-27T16:26:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9837#issuecomment-96934",
    "user": "https://github.com/dwbump"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_096935.json:
```json
{
    "body": "> Sorry, the ticket number should also be in the first line of the commit message. \n\nDone.",
    "created_at": "2010-10-27T16:26:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9837#issuecomment-96935",
    "user": "https://github.com/dwbump"
}
```

> Sorry, the ticket number should also be in the first line of the commit message. 

Done.



---

archive/issue_comments_096936.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-11-01T10:11:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9837#issuecomment-96936",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_events_009959.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2010-11-01T10:11:20Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9837",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9837#event-9959"
}
```



---

archive/issue_comments_096937.json:
```json
{
    "body": "Changing status from closed to needs_work.",
    "created_at": "2010-11-02T15:34:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9837#issuecomment-96937",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from closed to needs_work.



---

archive/issue_events_009960.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2010-11-02T15:34:34Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/9837",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9837#event-9960"
}
```



---

archive/issue_comments_096938.json:
```json
{
    "body": "Due to a mistake by me (confusing #9838 with #9893), this ticket did not get merged in sage-4.6.1.alpha0.",
    "created_at": "2010-11-02T15:35:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9837#issuecomment-96938",
    "user": "https://github.com/jdemeyer"
}
```

Due to a mistake by me (confusing #9838 with #9893), this ticket did not get merged in sage-4.6.1.alpha0.



---

archive/issue_comments_096939.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2010-11-02T15:35:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9837#issuecomment-96939",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_096940.json:
```json
{
    "body": "The ticket is still described as resolved:fixed.\n\nI don't think I can revert the fixed status: trac admin has to do that.\n(It doesn't matter if this won't cause the release manager to\nforget the patch.)",
    "created_at": "2010-11-02T23:36:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9837#issuecomment-96940",
    "user": "https://github.com/dwbump"
}
```

The ticket is still described as resolved:fixed.

I don't think I can revert the fixed status: trac admin has to do that.
(It doesn't matter if this won't cause the release manager to
forget the patch.)



---

archive/issue_events_009961.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-11-04T11:43:33Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9837",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9837#event-9961"
}
```



---

archive/issue_comments_096941.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2010-11-04T11:43:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9837#issuecomment-96941",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from closed to new.



---

archive/issue_events_009962.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-11-04T11:43:42Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/9837",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9837#event-9962"
}
```



---

archive/issue_comments_096942.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2010-11-04T11:43:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9837#issuecomment-96942",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_096943.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-11-04T11:43:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9837#issuecomment-96943",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_096944.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-11-04T11:44:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9837#issuecomment-96944",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_096945.json:
```json
{
    "body": "Replying to [comment:13 bump]:\n> I don't think I can revert the fixed status: trac admin has to do that.\n\nDone.",
    "created_at": "2010-11-04T11:45:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9837#issuecomment-96945",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Replying to [comment:13 bump]:
> I don't think I can revert the fixed status: trac admin has to do that.

Done.



---

archive/issue_events_009963.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2010-11-10T22:20:13Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9837",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9837#event-9963"
}
```



---

archive/issue_comments_096946.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-11-10T22:20:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9837#issuecomment-96946",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
