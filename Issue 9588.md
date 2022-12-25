# Issue 9588: Extend is_prime_power to negative exponents

archive/issues_009588.json:
```json
{
    "body": "Assignee: @aghitza\n\nKeywords: is_prime_power\n\nCurrently, is_prime_power only works on integers.  The attached simple patch will allow rational numbers as input as illustrated below.\n\n```\nsage: is_prime_power(1/2197)\nTrue\nsage: is_prime_power(1/100)\nFalse\nsage: is_prime_power(2/5)\nFalse\n```\n\nThis is also the behavior of Mathematica's PrimePowerQ function.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9588\n\n",
    "closed_at": "2010-07-26T02:24:43Z",
    "created_at": "2010-07-23T14:55:18Z",
    "labels": [
        "component: basic arithmetic",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "Extend is_prime_power to negative exponents",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9588",
    "user": "https://github.com/arminstraub"
}
```
Assignee: @aghitza

Keywords: is_prime_power

Currently, is_prime_power only works on integers.  The attached simple patch will allow rational numbers as input as illustrated below.

```
sage: is_prime_power(1/2197)
True
sage: is_prime_power(1/100)
False
sage: is_prime_power(2/5)
False
```

This is also the behavior of Mathematica's PrimePowerQ function.

Issue created by migration from https://trac.sagemath.org/ticket/9588





---

archive/issue_comments_092555.json:
```json
{
    "body": "Attachment [is_prime_power.patch](tarball://root/attachments/some-uuid/ticket9588/is_prime_power.patch) by @arminstraub created at 2010-07-23 15:10:58",
    "created_at": "2010-07-23T15:10:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9588#issuecomment-92555",
    "user": "https://github.com/arminstraub"
}
```

Attachment [is_prime_power.patch](tarball://root/attachments/some-uuid/ticket9588/is_prime_power.patch) by @arminstraub created at 2010-07-23 15:10:58



---

archive/issue_comments_092556.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-23T15:10:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9588#issuecomment-92556",
    "user": "https://github.com/arminstraub"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_092557.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-07-24T20:52:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9588#issuecomment-92557",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_092558.json:
```json
{
    "body": "Doesn't apply to sage-4.5.2.alpha0.  Could you update your patch?\n\nBy the way, you should look at the latest guidelines at http://groups.google.com/group/sage-release/browse_thread/thread/456f14fd92ee61a5 about commit messages and patch names.",
    "created_at": "2010-07-24T20:52:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9588#issuecomment-92558",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Doesn't apply to sage-4.5.2.alpha0.  Could you update your patch?

By the way, you should look at the latest guidelines at http://groups.google.com/group/sage-release/browse_thread/thread/456f14fd92ee61a5 about commit messages and patch names.



---

archive/issue_comments_092559.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-07-24T21:57:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9588#issuecomment-92559",
    "user": "https://github.com/arminstraub"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_092560.json:
```json
{
    "body": "Replying to [comment:2 cwitty]:\n\nThanks for the pointers.  Please let me know if I missed something else from the guidelines (it's my first patch).\n\n> Doesn't apply to sage-4.5.2.alpha0.  Could you update your patch?\n\n\nI downloaded the most recent available sage (4.5) and made a new patch.  Does this solve the issue?  If not, what can I do?",
    "created_at": "2010-07-24T22:00:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9588#issuecomment-92560",
    "user": "https://github.com/arminstraub"
}
```

Replying to [comment:2 cwitty]:

Thanks for the pointers.  Please let me know if I missed something else from the guidelines (it's my first patch).

> Doesn't apply to sage-4.5.2.alpha0.  Could you update your patch?


I downloaded the most recent available sage (4.5) and made a new patch.  Does this solve the issue?  If not, what can I do?



---

archive/issue_comments_092561.json:
```json
{
    "body": "Unfortunately, your patch conflicts with the patch from #9206, which was newly added to sage-4.5.2.alpha0.  You could download and build that release (read sage-release http://groups.google.com/group/sage-release/browse_thread/thread/cc0b1929f66e0658?hl=en for a pointer to the source); or you could apply the patch from #9206 to your copy of Sage, and then redo your patch on top of that.\n\nSorry you're having such a difficult time with your first patch -- but you have to expect the occasional patch conflict when you work in the fast-changing field of testing for prime powers :)\n(Just joking... the previous change to that code was in February 2009, so you're quite unlucky to have hit a time when somebody else was working on the same function.)",
    "created_at": "2010-07-24T22:21:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9588#issuecomment-92561",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Unfortunately, your patch conflicts with the patch from #9206, which was newly added to sage-4.5.2.alpha0.  You could download and build that release (read sage-release http://groups.google.com/group/sage-release/browse_thread/thread/cc0b1929f66e0658?hl=en for a pointer to the source); or you could apply the patch from #9206 to your copy of Sage, and then redo your patch on top of that.

Sorry you're having such a difficult time with your first patch -- but you have to expect the occasional patch conflict when you work in the fast-changing field of testing for prime powers :)
(Just joking... the previous change to that code was in February 2009, so you're quite unlucky to have hit a time when somebody else was working on the same function.)



---

archive/issue_comments_092562.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-07-24T22:21:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9588#issuecomment-92562",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_092563.json:
```json
{
    "body": "apply only this one -- depends on #9206",
    "created_at": "2010-07-24T23:47:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9588#issuecomment-92563",
    "user": "https://github.com/arminstraub"
}
```

apply only this one -- depends on #9206



---

archive/issue_comments_092564.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-07-24T23:48:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9588#issuecomment-92564",
    "user": "https://github.com/arminstraub"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_092565.json:
```json
{
    "body": "Attachment [9588_is_prime_power.patch](tarball://root/attachments/some-uuid/ticket9588/9588_is_prime_power.patch) by @arminstraub created at 2010-07-24 23:48:13",
    "created_at": "2010-07-24T23:48:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9588#issuecomment-92565",
    "user": "https://github.com/arminstraub"
}
```

Attachment [9588_is_prime_power.patch](tarball://root/attachments/some-uuid/ticket9588/9588_is_prime_power.patch) by @arminstraub created at 2010-07-24 23:48:13



---

archive/issue_comments_092566.json:
```json
{
    "body": "Replying to [comment:5 cwitty]:\n\nOk, thanks for the humorous explanation :)  I applied William's patch first, and adapted my patch---hopefully it works now!\n\nI did two things of which I'm not quite sure if that was the proper way: (1) when uploading the new patch I replaced the old one, and (2) I just removed the \"needs rebase\" work issue in the hope that I addressed it.  Let me know if either of those is considered bad practice.",
    "created_at": "2010-07-24T23:56:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9588#issuecomment-92566",
    "user": "https://github.com/arminstraub"
}
```

Replying to [comment:5 cwitty]:

Ok, thanks for the humorous explanation :)  I applied William's patch first, and adapted my patch---hopefully it works now!

I did two things of which I'm not quite sure if that was the proper way: (1) when uploading the new patch I replaced the old one, and (2) I just removed the "needs rebase" work issue in the hope that I addressed it.  Let me know if either of those is considered bad practice.



---

archive/issue_comments_092567.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-25T00:31:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9588#issuecomment-92567",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_023885.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/cwitty",
    "created_at": "2010-07-25T00:31:05Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9588",
    "milestone": "sage-4.5.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9588#event-23885"
}
```



---

archive/issue_comments_092568.json:
```json
{
    "body": "Code looks reasonable, doctests pass.  Positive review.\n\nArmin, thanks for sticking with this!  To answer your questions:\n\n(1) Opinions differ :) Sometimes it's nice to preserve the history of the patch, but it's also nice to make it easier for reviewers and the release manager by not having a whole sea of patches that they have to wade through to figure out which to apply.  In your case -- a simple rebase, where nobody will probably ever care about previous versions of the patch -- I'd say yes, replacing the old one is fine.\n\n(2) Yes, if you think you've addressed the work issue you should remove it.\n\nRelease manager: apply only the second patch.",
    "created_at": "2010-07-25T00:31:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9588#issuecomment-92568",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Code looks reasonable, doctests pass.  Positive review.

Armin, thanks for sticking with this!  To answer your questions:

(1) Opinions differ :) Sometimes it's nice to preserve the history of the patch, but it's also nice to make it easier for reviewers and the release manager by not having a whole sea of patches that they have to wade through to figure out which to apply.  In your case -- a simple rebase, where nobody will probably ever care about previous versions of the patch -- I'd say yes, replacing the old one is fine.

(2) Yes, if you think you've addressed the work issue you should remove it.

Release manager: apply only the second patch.



---

archive/issue_events_023886.json:
```json
{
    "actor": "https://github.com/dandrake",
    "created_at": "2010-07-26T02:24:43Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9588",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9588#event-23886"
}
```



---

archive/issue_comments_092569.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-26T02:24:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9588#issuecomment-92569",
    "user": "https://github.com/dandrake"
}
```

Resolution: fixed



---

archive/issue_comments_092570.json:
```json
{
    "body": "9588_is_prime_power.patch merged in 4.5.2.alpha0. I did hand-edit the patch a tiny bit: with your patch, the documentation says \"an integer rational number\", and I changed it to \"an integer or rational number\".",
    "created_at": "2010-07-26T02:24:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9588#issuecomment-92570",
    "user": "https://github.com/dandrake"
}
```

9588_is_prime_power.patch merged in 4.5.2.alpha0. I did hand-edit the patch a tiny bit: with your patch, the documentation says "an integer rational number", and I changed it to "an integer or rational number".
