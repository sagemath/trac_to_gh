# Issue 9647: instructive example for mip.pyx

archive/issues_009647.json:
```json
{
    "body": "Assignee: jason, jkantor\n\nCC:  @kcrisman @nathanncohen\n\nAdd an example from sage-support to the head of mip.pyx [see here](http://groups.google.com/group/sage-support/browse_thread/thread/e5ebaf0f6f657ab2).\n\nIssue created by migration from https://trac.sagemath.org/ticket/9647\n\n",
    "created_at": "2010-07-30T17:06:42Z",
    "labels": [
        "component: numerical",
        "trivial"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.3",
    "title": "instructive example for mip.pyx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9647",
    "user": "https://github.com/haraldschilly"
}
```
Assignee: jason, jkantor

CC:  @kcrisman @nathanncohen

Add an example from sage-support to the head of mip.pyx [see here](http://groups.google.com/group/sage-support/browse_thread/thread/e5ebaf0f6f657ab2).

Issue created by migration from https://trac.sagemath.org/ticket/9647





---

archive/issue_comments_093385.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-30T17:19:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9647",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9647#issuecomment-93385",
    "user": "https://github.com/haraldschilly"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_093386.json:
```json
{
    "body": "I can't comment on the correctness, obviously, but if the formatting works out right, this is exactly the kind of thing I was envisioning.  Great documentation and explanation - I hope someone reviews it soon!",
    "created_at": "2010-07-30T19:13:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9647",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9647#issuecomment-93386",
    "user": "https://github.com/kcrisman"
}
```

I can't comment on the correctness, obviously, but if the formatting works out right, this is exactly the kind of thing I was envisioning.  Great documentation and explanation - I hope someone reviews it soon!



---

archive/issue_comments_093387.json:
```json
{
    "body": "I've added a general introduction chapter, but suddenly the `:meth:~`Class.method`` references to methods no longer work. I don't know why.",
    "created_at": "2010-07-30T21:48:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9647",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9647#issuecomment-93387",
    "user": "https://github.com/haraldschilly"
}
```

I've added a general introduction chapter, but suddenly the `:meth:~`Class.method`` references to methods no longer work. I don't know why.



---

archive/issue_comments_093388.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-07-30T21:48:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9647",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9647#issuecomment-93388",
    "user": "https://github.com/haraldschilly"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_093389.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-07-31T12:11:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9647",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9647#issuecomment-93389",
    "user": "https://github.com/haraldschilly"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_093390.json:
```json
{
    "body": "Hello !!! Everything seems nice, but could you please add in the example one or two inequalities ? All the constraints in this case are equalities, which is a bit unusual with LP... Anyway people would understand that it is indeed possible to write an equality with two inequalities, while the opposite is not true... :-)\n\nNathann",
    "created_at": "2010-07-31T14:28:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9647",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9647#issuecomment-93390",
    "user": "https://github.com/nathanncohen"
}
```

Hello !!! Everything seems nice, but could you please add in the example one or two inequalities ? All the constraints in this case are equalities, which is a bit unusual with LP... Anyway people would understand that it is indeed possible to write an equality with two inequalities, while the opposite is not true... :-)

Nathann



---

archive/issue_comments_093391.json:
```json
{
    "body": "w_3 >= 1 is an inequality, but it's probably not explicit enough... wait a sec.",
    "created_at": "2010-07-31T14:29:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9647",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9647#issuecomment-93391",
    "user": "https://github.com/haraldschilly"
}
```

w_3 >= 1 is an inequality, but it's probably not explicit enough... wait a sec.



---

archive/issue_comments_093392.json:
```json
{
    "body": "How about now? I've intentionally avoided to set the lower bound of w_3 to 1 and instead used an inequality just because of that. I think that's ok now.",
    "created_at": "2010-07-31T14:34:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9647",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9647#issuecomment-93392",
    "user": "https://github.com/haraldschilly"
}
```

How about now? I've intentionally avoided to set the lower bound of w_3 to 1 and instead used an inequality just because of that. I think that's ok now.



---

archive/issue_comments_093393.json:
```json
{
    "body": "Hmmm.. I don't want an inequality \"on principle\"... I thought it would be nice for the users to see among your system of equalities some inequality... When they look at this system of equations they can think \"ok, my own system fits\". If they only see equalities and don't read the full text, they may not notice it is possible... Well, it's up to you ! If you don't this it sound, just say so, your ticket already dserves a positive review :-)\n\nNathann",
    "created_at": "2010-07-31T14:42:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9647",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9647#issuecomment-93393",
    "user": "https://github.com/nathanncohen"
}
```

Hmmm.. I don't want an inequality "on principle"... I thought it would be nice for the users to see among your system of equalities some inequality... When they look at this system of equations they can think "ok, my own system fits". If they only see equalities and don't read the full text, they may not notice it is possible... Well, it's up to you ! If you don't this it sound, just say so, your ticket already dserves a positive review :-)

Nathann



---

archive/issue_comments_093394.json:
```json
{
    "body": "Attachment [9647-example-MILP.patch](tarball://root/attachments/some-uuid/ticket9647/9647-example-MILP.patch) by @haraldschilly created at 2010-07-31 14:54:25\n\nok, you are probably right.",
    "created_at": "2010-07-31T14:54:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9647",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9647#issuecomment-93394",
    "user": "https://github.com/haraldschilly"
}
```

Attachment [9647-example-MILP.patch](tarball://root/attachments/some-uuid/ticket9647/9647-example-MILP.patch) by @haraldschilly created at 2010-07-31 14:54:25

ok, you are probably right.



---

archive/issue_comments_093395.json:
```json
{
    "body": "Sorryyyyyy !! I know it feels a bit artificial.... With a bit of luck we should have a proper tutorial for LP in Sage soon anyway... Thank you for your paaaaaatch !!! :-)\n\nNathann",
    "created_at": "2010-07-31T14:57:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9647",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9647#issuecomment-93395",
    "user": "https://github.com/nathanncohen"
}
```

Sorryyyyyy !! I know it feels a bit artificial.... With a bit of luck we should have a proper tutorial for LP in Sage soon anyway... Thank you for your paaaaaatch !!! :-)

Nathann



---

archive/issue_comments_093396.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-31T14:57:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9647",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9647#issuecomment-93396",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_093397.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-08-09T09:40:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9647",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9647#issuecomment-93397",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_009783.json:
```json
{
    "actor": "@qed777",
    "created_at": "2010-08-09T09:40:18Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9647",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9647#event-9783"
}
```
