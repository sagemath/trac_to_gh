# Issue 9837: Bugfix in WeylCharacterRing __call__ method

archive/issues_009837.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nCC:  sage-combinat\n\nThis addresses a bug that was reported here:\n\nhttp://groups.google.com/group/sage-combinat-devel/msg/252fd7fa0e297214\n\nThe `__call__` method of a Weyl Character ring, when `style=\"coroots\"` is specified, tries to interpret the arguments as the coroots of a weight; that weight\nis then the actual argument. However this is not appropriate if the argument is\nnot a tuple. Therefore this should be tested.\n\nThe patch implements the test.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9838\n\n",
    "created_at": "2010-08-29T19:03:03Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "title": "Bugfix in WeylCharacterRing __call__ method",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9837",
    "user": "bump"
}
```
Assignee: AlexGhitza

CC:  sage-combinat

This addresses a bug that was reported here:

http://groups.google.com/group/sage-combinat-devel/msg/252fd7fa0e297214

The `__call__` method of a Weyl Character ring, when `style="coroots"` is specified, tries to interpret the arguments as the coroots of a weight; that weight
is then the actual argument. However this is not appropriate if the argument is
not a tuple. Therefore this should be tested.

The patch implements the test.

Issue created by migration from https://trac.sagemath.org/ticket/9838





---

archive/issue_comments_097081.json:
```json
{
    "body": "Changing assignee from AlexGhitza to bump.",
    "created_at": "2010-08-29T19:08:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9837#issuecomment-97081",
    "user": "bump"
}
```

Changing assignee from AlexGhitza to bump.



---

archive/issue_comments_097082.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-29T19:08:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9837#issuecomment-97082",
    "user": "bump"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_097083.json:
```json
{
    "body": "Changing component from algebra to group_theory.",
    "created_at": "2010-08-29T19:10:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9837#issuecomment-97083",
    "user": "bump"
}
```

Changing component from algebra to group_theory.



---

archive/issue_comments_097084.json:
```json
{
    "body": "Replying to [comment:3 bump]:\n\nThis is a bug fix. All tests pass!",
    "created_at": "2010-10-19T06:31:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9837#issuecomment-97084",
    "user": "aschilling"
}
```

Replying to [comment:3 bump]:

This is a bug fix. All tests pass!



---

archive/issue_comments_097085.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-10-19T06:31:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9837#issuecomment-97085",
    "user": "aschilling"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_097086.json:
```json
{
    "body": "Please change the commit message of the patch trac_9838.patch (use `hg qrefresh -e` for that).",
    "created_at": "2010-10-26T13:34:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9837#issuecomment-97086",
    "user": "jdemeyer"
}
```

Please change the commit message of the patch trac_9838.patch (use `hg qrefresh -e` for that).



---

archive/issue_comments_097087.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-10-26T13:34:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9837#issuecomment-97087",
    "user": "jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_097088.json:
```json
{
    "body": "> Please change the commit message of the patch trac_9838.patch (use hg qrefresh -e for that).\n\nDone. -Dan",
    "created_at": "2010-10-26T15:19:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9837#issuecomment-97088",
    "user": "bump"
}
```

> Please change the commit message of the patch trac_9838.patch (use hg qrefresh -e for that).

Done. -Dan



---

archive/issue_comments_097089.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2010-10-26T15:19:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9837#issuecomment-97089",
    "user": "bump"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_097090.json:
```json
{
    "body": "Replying to [comment:7 bump]:\n> Done. -Dan\n\nSorry, the ticket number should also be in the first line of the commit message.",
    "created_at": "2010-10-27T08:52:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9837#issuecomment-97090",
    "user": "jdemeyer"
}
```

Replying to [comment:7 bump]:
> Done. -Dan

Sorry, the ticket number should also be in the first line of the commit message.



---

archive/issue_comments_097091.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-10-27T08:52:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9837#issuecomment-97091",
    "user": "jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_097092.json:
```json
{
    "body": "Attachment [trac_9838.patch](tarball://root/attachments/some-uuid/ticket9838/trac_9838.patch) by bump created at 2010-10-27 16:25:02\n\n#9838: bugfix in WeylCharac terRing call method",
    "created_at": "2010-10-27T16:25:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9837#issuecomment-97092",
    "user": "bump"
}
```

Attachment [trac_9838.patch](tarball://root/attachments/some-uuid/ticket9838/trac_9838.patch) by bump created at 2010-10-27 16:25:02

#9838: bugfix in WeylCharac terRing call method



---

archive/issue_comments_097093.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2010-10-27T16:26:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9837#issuecomment-97093",
    "user": "bump"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_097094.json:
```json
{
    "body": "> Sorry, the ticket number should also be in the first line of the commit message. \n\nDone.",
    "created_at": "2010-10-27T16:26:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9837#issuecomment-97094",
    "user": "bump"
}
```

> Sorry, the ticket number should also be in the first line of the commit message. 

Done.



---

archive/issue_comments_097095.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-11-01T10:11:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9837#issuecomment-97095",
    "user": "jdemeyer"
}
```

Resolution: fixed



---

archive/issue_comments_097096.json:
```json
{
    "body": "Changing status from closed to needs_work.",
    "created_at": "2010-11-02T15:34:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9837#issuecomment-97096",
    "user": "jdemeyer"
}
```

Changing status from closed to needs_work.



---

archive/issue_comments_097097.json:
```json
{
    "body": "Due to a mistake by me (confusing #9838 with #9893), this ticket did not get merged in sage-4.6.1.alpha0.",
    "created_at": "2010-11-02T15:35:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9837#issuecomment-97097",
    "user": "jdemeyer"
}
```

Due to a mistake by me (confusing #9838 with #9893), this ticket did not get merged in sage-4.6.1.alpha0.



---

archive/issue_comments_097098.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2010-11-02T15:35:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9837#issuecomment-97098",
    "user": "jdemeyer"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_097099.json:
```json
{
    "body": "The ticket is still described as resolved:fixed.\n\nI don't think I can revert the fixed status: trac admin has to do that.\n(It doesn't matter if this won't cause the release manager to\nforget the patch.)",
    "created_at": "2010-11-02T23:36:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9837#issuecomment-97099",
    "user": "bump"
}
```

The ticket is still described as resolved:fixed.

I don't think I can revert the fixed status: trac admin has to do that.
(It doesn't matter if this won't cause the release manager to
forget the patch.)



---

archive/issue_comments_097100.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2010-11-04T11:43:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9837#issuecomment-97100",
    "user": "mvngu"
}
```

Changing status from closed to new.



---

archive/issue_comments_097101.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2010-11-04T11:43:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9837#issuecomment-97101",
    "user": "mvngu"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_097102.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-11-04T11:43:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9837#issuecomment-97102",
    "user": "mvngu"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_097103.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-11-04T11:44:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9837#issuecomment-97103",
    "user": "mvngu"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_097104.json:
```json
{
    "body": "Replying to [comment:13 bump]:\n> I don't think I can revert the fixed status: trac admin has to do that.\n\nDone.",
    "created_at": "2010-11-04T11:45:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9837#issuecomment-97104",
    "user": "mvngu"
}
```

Replying to [comment:13 bump]:
> I don't think I can revert the fixed status: trac admin has to do that.

Done.



---

archive/issue_comments_097105.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-11-10T22:20:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9837#issuecomment-97105",
    "user": "jdemeyer"
}
```

Resolution: fixed
