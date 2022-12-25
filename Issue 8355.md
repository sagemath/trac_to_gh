# Issue 8355: Fix hsv_to_rgb to take all 3 arguments

archive/issues_008355.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @kcrisman\n\n\n```\nsage: hue(.5,.5,.5)\nTraceback (click to the left of this block for traceback)\n...\nTypeError: can't multiply sequence by non-int of type 'float'\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8355\n\n",
    "created_at": "2010-02-25T00:25:00Z",
    "labels": [
        "component: graphics",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.2",
    "title": "Fix hsv_to_rgb to take all 3 arguments",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8355",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```
Assignee: @williamstein

CC:  @kcrisman


```
sage: hue(.5,.5,.5)
Traceback (click to the left of this block for traceback)
...
TypeError: can't multiply sequence by non-int of type 'float'
```


Issue created by migration from https://trac.sagemath.org/ticket/8355





---

archive/issue_comments_074499.json:
```json
{
    "body": "Attachment [8355-hue.patch](tarball://root/attachments/some-uuid/ticket8355/8355-hue.patch) by boothby created at 2010-04-02 00:31:57",
    "created_at": "2010-04-02T00:31:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8355#issuecomment-74499",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Attachment [8355-hue.patch](tarball://root/attachments/some-uuid/ticket8355/8355-hue.patch) by boothby created at 2010-04-02 00:31:57



---

archive/issue_comments_074500.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-02T00:31:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8355#issuecomment-74500",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_074501.json:
```json
{
    "body": "Works for me.",
    "created_at": "2010-04-02T00:35:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8355#issuecomment-74501",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Works for me.



---

archive/issue_comments_074502.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-02T00:35:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8355#issuecomment-74502",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_074503.json:
```json
{
    "body": "This doesn't apply cleanly to me against 4.3.5.  Please rebase.",
    "created_at": "2010-04-15T22:16:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8355#issuecomment-74503",
    "user": "https://github.com/jhpalmieri"
}
```

This doesn't apply cleanly to me against 4.3.5.  Please rebase.



---

archive/issue_comments_074504.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-04-15T22:16:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8355#issuecomment-74504",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_074505.json:
```json
{
    "body": "Changing keywords from \"\" to \"beginner\".",
    "created_at": "2010-05-26T15:41:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8355#issuecomment-74505",
    "user": "https://github.com/jasongrout"
}
```

Changing keywords from "" to "beginner".



---

archive/issue_comments_074506.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-01-09T00:03:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8355#issuecomment-74506",
    "user": "https://trac.sagemath.org/admin/accounts/users/ryan"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_074507.json:
```json
{
    "body": "I think this has been fixed already.  Works in sage-4.6.0",
    "created_at": "2011-01-09T00:03:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8355#issuecomment-74507",
    "user": "https://trac.sagemath.org/admin/accounts/users/ryan"
}
```

I think this has been fixed already.  Works in sage-4.6.0



---

archive/issue_comments_074508.json:
```json
{
    "body": "Confirmed.  But should we add a patch that confirms this, as in the previous patch?  This is because we now use the Python version of this, afaict.",
    "created_at": "2011-01-09T02:56:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8355#issuecomment-74508",
    "user": "https://github.com/kcrisman"
}
```

Confirmed.  But should we add a patch that confirms this, as in the previous patch?  This is because we now use the Python version of this, afaict.



---

archive/issue_comments_074509.json:
```json
{
    "body": "I've created a patch that confirms\n\n```\nsage: hue(.5,.5,.5)\n(0.25, 0.5, 0.5)\n```\n\nin the doctest of hue and applies to sage-4.6.1.rc1.",
    "created_at": "2011-01-09T22:41:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8355#issuecomment-74509",
    "user": "https://github.com/adeines"
}
```

I've created a patch that confirms

```
sage: hue(.5,.5,.5)
(0.25, 0.5, 0.5)
```

in the doctest of hue and applies to sage-4.6.1.rc1.



---

archive/issue_comments_074510.json:
```json
{
    "body": "hue doctest which applies to sage-4.6.1.rc1",
    "created_at": "2011-01-09T22:42:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8355#issuecomment-74510",
    "user": "https://github.com/adeines"
}
```

hue doctest which applies to sage-4.6.1.rc1



---

archive/issue_comments_074511.json:
```json
{
    "body": "Attachment [8355-hue.2.patch](tarball://root/attachments/some-uuid/ticket8355/8355-hue.2.patch) by @wjp created at 2011-01-09 23:15:11\n\nLooks good to me.",
    "created_at": "2011-01-09T23:15:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8355#issuecomment-74511",
    "user": "https://github.com/wjp"
}
```

Attachment [8355-hue.2.patch](tarball://root/attachments/some-uuid/ticket8355/8355-hue.2.patch) by @wjp created at 2011-01-09 23:15:11

Looks good to me.



---

archive/issue_comments_074512.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-01-09T23:15:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8355#issuecomment-74512",
    "user": "https://github.com/wjp"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_074513.json:
```json
{
    "body": "If these spellings of the author and reviewer aren't right, please correct them.",
    "created_at": "2011-01-10T13:58:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8355#issuecomment-74513",
    "user": "https://github.com/kcrisman"
}
```

If these spellings of the author and reviewer aren't right, please correct them.



---

archive/issue_comments_074514.json:
```json
{
    "body": "Well, up to you guys.  It just seemed to me that since there wasn't anything left to patch, maybe the older ones weren't relevant - but you can give credit where you feel it's due!",
    "created_at": "2011-01-11T17:42:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8355#issuecomment-74514",
    "user": "https://github.com/kcrisman"
}
```

Well, up to you guys.  It just seemed to me that since there wasn't anything left to patch, maybe the older ones weren't relevant - but you can give credit where you feel it's due!



---

archive/issue_comments_074515.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-01-17T20:52:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8355#issuecomment-74515",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_074516.json:
```json
{
    "body": "Please add the **correct** ticket number to the commit message :-)",
    "created_at": "2011-01-17T20:52:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8355#issuecomment-74516",
    "user": "https://github.com/jdemeyer"
}
```

Please add the **correct** ticket number to the commit message :-)



---

archive/issue_comments_074517.json:
```json
{
    "body": "Use only this patch",
    "created_at": "2011-01-17T21:00:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8355#issuecomment-74517",
    "user": "https://github.com/kcrisman"
}
```

Use only this patch



---

archive/issue_comments_074518.json:
```json
{
    "body": "Attachment [8355-hue.2.2.patch](tarball://root/attachments/some-uuid/ticket8355/8355-hue.2.2.patch) by @kcrisman created at 2011-01-17 21:01:16\n\nThis should fix this.  Apply only 8355-hue.2.2.patch",
    "created_at": "2011-01-17T21:01:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8355#issuecomment-74518",
    "user": "https://github.com/kcrisman"
}
```

Attachment [8355-hue.2.2.patch](tarball://root/attachments/some-uuid/ticket8355/8355-hue.2.2.patch) by @kcrisman created at 2011-01-17 21:01:16

This should fix this.  Apply only 8355-hue.2.2.patch



---

archive/issue_comments_074519.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-01-17T21:01:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8355#issuecomment-74519",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_074520.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-01-17T21:01:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8355#issuecomment-74520",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_074521.json:
```json
{
    "body": "I didn't have anything to do with the review of the patch going in... I think it's weird to get credit for this.",
    "created_at": "2011-01-17T21:17:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8355#issuecomment-74521",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

I didn't have anything to do with the review of the patch going in... I think it's weird to get credit for this.



---

archive/issue_comments_074522.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-01-19T22:19:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8355#issuecomment-74522",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_events_008545.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-01-19T22:19:30Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8355",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8355#event-8545"
}
```
