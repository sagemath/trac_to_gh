# Issue 8355: Fix hsv_to_rgb to take all 3 arguments

archive/issues_008355.json:
```json
{
    "body": "Assignee: was\n\nCC:  kcrisman\n\n\n```\nsage: hue(.5,.5,.5)\nTraceback (click to the left of this block for traceback)\n...\nTypeError: can't multiply sequence by non-int of type 'float'\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8355\n\n",
    "created_at": "2010-02-25T00:25:00Z",
    "labels": [
        "graphics",
        "minor",
        "bug"
    ],
    "title": "Fix hsv_to_rgb to take all 3 arguments",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8355",
    "user": "boothby"
}
```
Assignee: was

CC:  kcrisman


```
sage: hue(.5,.5,.5)
Traceback (click to the left of this block for traceback)
...
TypeError: can't multiply sequence by non-int of type 'float'
```


Issue created by migration from https://trac.sagemath.org/ticket/8355





---

archive/issue_comments_074623.json:
```json
{
    "body": "Attachment [8355-hue.patch](tarball://root/attachments/some-uuid/ticket8355/8355-hue.patch) by boothby created at 2010-04-02 00:31:57",
    "created_at": "2010-04-02T00:31:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8355#issuecomment-74623",
    "user": "boothby"
}
```

Attachment [8355-hue.patch](tarball://root/attachments/some-uuid/ticket8355/8355-hue.patch) by boothby created at 2010-04-02 00:31:57



---

archive/issue_comments_074624.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-02T00:31:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8355#issuecomment-74624",
    "user": "boothby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_074625.json:
```json
{
    "body": "Works for me.",
    "created_at": "2010-04-02T00:35:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8355#issuecomment-74625",
    "user": "boothby"
}
```

Works for me.



---

archive/issue_comments_074626.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-02T00:35:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8355#issuecomment-74626",
    "user": "boothby"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_074627.json:
```json
{
    "body": "This doesn't apply cleanly to me against 4.3.5.  Please rebase.",
    "created_at": "2010-04-15T22:16:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8355#issuecomment-74627",
    "user": "jhpalmieri"
}
```

This doesn't apply cleanly to me against 4.3.5.  Please rebase.



---

archive/issue_comments_074628.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-04-15T22:16:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8355#issuecomment-74628",
    "user": "jhpalmieri"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_074629.json:
```json
{
    "body": "Changing keywords from \"\" to \"beginner\".",
    "created_at": "2010-05-26T15:41:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8355#issuecomment-74629",
    "user": "jason"
}
```

Changing keywords from "" to "beginner".



---

archive/issue_comments_074630.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-01-09T00:03:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8355#issuecomment-74630",
    "user": "ryan"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_074631.json:
```json
{
    "body": "I think this has been fixed already.  Works in sage-4.6.0",
    "created_at": "2011-01-09T00:03:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8355#issuecomment-74631",
    "user": "ryan"
}
```

I think this has been fixed already.  Works in sage-4.6.0



---

archive/issue_comments_074632.json:
```json
{
    "body": "Confirmed.  But should we add a patch that confirms this, as in the previous patch?  This is because we now use the Python version of this, afaict.",
    "created_at": "2011-01-09T02:56:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8355#issuecomment-74632",
    "user": "kcrisman"
}
```

Confirmed.  But should we add a patch that confirms this, as in the previous patch?  This is because we now use the Python version of this, afaict.



---

archive/issue_comments_074633.json:
```json
{
    "body": "I've created a patch that confirms\n\n```\nsage: hue(.5,.5,.5)\n(0.25, 0.5, 0.5)\n```\n\nin the doctest of hue and applies to sage-4.6.1.rc1.",
    "created_at": "2011-01-09T22:41:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8355#issuecomment-74633",
    "user": "aly.deines"
}
```

I've created a patch that confirms

```
sage: hue(.5,.5,.5)
(0.25, 0.5, 0.5)
```

in the doctest of hue and applies to sage-4.6.1.rc1.



---

archive/issue_comments_074634.json:
```json
{
    "body": "hue doctest which applies to sage-4.6.1.rc1",
    "created_at": "2011-01-09T22:42:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8355#issuecomment-74634",
    "user": "aly.deines"
}
```

hue doctest which applies to sage-4.6.1.rc1



---

archive/issue_comments_074635.json:
```json
{
    "body": "Attachment [8355-hue.2.patch](tarball://root/attachments/some-uuid/ticket8355/8355-hue.2.patch) by wjp created at 2011-01-09 23:15:11\n\nLooks good to me.",
    "created_at": "2011-01-09T23:15:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8355#issuecomment-74635",
    "user": "wjp"
}
```

Attachment [8355-hue.2.patch](tarball://root/attachments/some-uuid/ticket8355/8355-hue.2.patch) by wjp created at 2011-01-09 23:15:11

Looks good to me.



---

archive/issue_comments_074636.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-01-09T23:15:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8355#issuecomment-74636",
    "user": "wjp"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_074637.json:
```json
{
    "body": "If these spellings of the author and reviewer aren't right, please correct them.",
    "created_at": "2011-01-10T13:58:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8355#issuecomment-74637",
    "user": "kcrisman"
}
```

If these spellings of the author and reviewer aren't right, please correct them.



---

archive/issue_comments_074638.json:
```json
{
    "body": "Well, up to you guys.  It just seemed to me that since there wasn't anything left to patch, maybe the older ones weren't relevant - but you can give credit where you feel it's due!",
    "created_at": "2011-01-11T17:42:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8355#issuecomment-74638",
    "user": "kcrisman"
}
```

Well, up to you guys.  It just seemed to me that since there wasn't anything left to patch, maybe the older ones weren't relevant - but you can give credit where you feel it's due!



---

archive/issue_comments_074639.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-01-17T20:52:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8355#issuecomment-74639",
    "user": "jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_074640.json:
```json
{
    "body": "Please add the **correct** ticket number to the commit message :-)",
    "created_at": "2011-01-17T20:52:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8355#issuecomment-74640",
    "user": "jdemeyer"
}
```

Please add the **correct** ticket number to the commit message :-)



---

archive/issue_comments_074641.json:
```json
{
    "body": "Use only this patch",
    "created_at": "2011-01-17T21:00:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8355#issuecomment-74641",
    "user": "kcrisman"
}
```

Use only this patch



---

archive/issue_comments_074642.json:
```json
{
    "body": "Attachment [8355-hue.2.2.patch](tarball://root/attachments/some-uuid/ticket8355/8355-hue.2.2.patch) by kcrisman created at 2011-01-17 21:01:16\n\nThis should fix this.  Apply only 8355-hue.2.2.patch",
    "created_at": "2011-01-17T21:01:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8355#issuecomment-74642",
    "user": "kcrisman"
}
```

Attachment [8355-hue.2.2.patch](tarball://root/attachments/some-uuid/ticket8355/8355-hue.2.2.patch) by kcrisman created at 2011-01-17 21:01:16

This should fix this.  Apply only 8355-hue.2.2.patch



---

archive/issue_comments_074643.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-01-17T21:01:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8355#issuecomment-74643",
    "user": "kcrisman"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_074644.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-01-17T21:01:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8355#issuecomment-74644",
    "user": "kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_074645.json:
```json
{
    "body": "I didn't have anything to do with the review of the patch going in... I think it's weird to get credit for this.",
    "created_at": "2011-01-17T21:17:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8355#issuecomment-74645",
    "user": "boothby"
}
```

I didn't have anything to do with the review of the patch going in... I think it's weird to get credit for this.



---

archive/issue_comments_074646.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-01-19T22:19:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8355#issuecomment-74646",
    "user": "jdemeyer"
}
```

Resolution: fixed
