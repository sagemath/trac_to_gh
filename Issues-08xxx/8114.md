# Issue 8114: doctest failure in `sage/libs/cremona/newforms.pyx` on 32-bit machines from #8042

archive/issues_008114.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  aghitza\n\nI forgot to test my fix from #8042 on 32-bit platforms, and the fix causes doctest failures anywhere that `long` is smaller than 64 bits. I'm attaching a simple patch to fix this -- we just don't perform that test on 32-bit platforms.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8114\n\n",
    "closed_at": "2010-01-30T23:44:10Z",
    "created_at": "2010-01-28T22:28:32Z",
    "labels": [
        "component: interfaces",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "doctest failure in `sage/libs/cremona/newforms.pyx` on 32-bit machines from #8042",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8114",
    "user": "https://github.com/craigcitro"
}
```
Assignee: @williamstein

CC:  aghitza

I forgot to test my fix from #8042 on 32-bit platforms, and the fix causes doctest failures anywhere that `long` is smaller than 64 bits. I'm attaching a simple patch to fix this -- we just don't perform that test on 32-bit platforms.

Issue created by migration from https://trac.sagemath.org/ticket/8114





---

archive/issue_comments_071116.json:
```json
{
    "body": "Attachment [trac_8114.patch](tarball://root/attachments/some-uuid/ticket8114/trac_8114.patch) by @craigcitro created at 2010-01-28 22:32:21",
    "created_at": "2010-01-28T22:32:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8114#issuecomment-71116",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac_8114.patch](tarball://root/attachments/some-uuid/ticket8114/trac_8114.patch) by @craigcitro created at 2010-01-28 22:32:21



---

archive/issue_comments_071117.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-28T22:32:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8114#issuecomment-71117",
    "user": "https://github.com/craigcitro"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_071118.json:
```json
{
    "body": "With this patch applied, on 32-bit linux we have:\n\n```\nwstein@ubuntu32:/tmp/wstein/farm/sage-4.3.2.alpha0$         sage -t  -long \"devel/sage/sage/libs/cremona/newforms.pyx\"                                                                                        \n\nsage -t -long \"devel/sage/sage/libs/cremona/newforms.pyx\"   \n\n         [6.3 s]\n                \n```\n\nWhich is good.   However, I do not think the patch you posted explains very well what is going on.  It's not good for a user reading it.  I've posted an additional patch (apply after yours), which I think does a better job testing things and illustrating the issue.",
    "created_at": "2010-01-28T23:07:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8114#issuecomment-71118",
    "user": "https://github.com/williamstein"
}
```

With this patch applied, on 32-bit linux we have:

```
wstein@ubuntu32:/tmp/wstein/farm/sage-4.3.2.alpha0$         sage -t  -long "devel/sage/sage/libs/cremona/newforms.pyx"                                                                                        

sage -t -long "devel/sage/sage/libs/cremona/newforms.pyx"   

         [6.3 s]
                
```

Which is good.   However, I do not think the patch you posted explains very well what is going on.  It's not good for a user reading it.  I've posted an additional patch (apply after yours), which I think does a better job testing things and illustrating the issue.



---

archive/issue_comments_071119.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2010-01-28T23:08:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8114#issuecomment-71119",
    "user": "https://github.com/williamstein"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_071120.json:
```json
{
    "body": "Attachment [trac_8114-part2.patch](tarball://root/attachments/some-uuid/ticket8114/trac_8114-part2.patch) by @williamstein created at 2010-01-28 23:08:54",
    "created_at": "2010-01-28T23:08:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8114#issuecomment-71120",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_8114-part2.patch](tarball://root/attachments/some-uuid/ticket8114/trac_8114-part2.patch) by @williamstein created at 2010-01-28 23:08:54



---

archive/issue_comments_071121.json:
```json
{
    "body": "Sure, that's fine. I was expecting that anyone who wanted to know what was going on would look at #8042, where there's an explanation -- but you're right, it wouldn't hurt to have at least some explanation in the code itself. (Basically, my rule of thumb is that anything in an `EXAMPLES` section needs a good explanation, but for things in the `TESTS` section, a pointer to a trac ticket is sufficient.)\n\nPositive review -- apply both patches. (William, I'm listing us both as authors and reviewers, since we each reviewed the other person's contribution.)",
    "created_at": "2010-01-28T23:13:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8114#issuecomment-71121",
    "user": "https://github.com/craigcitro"
}
```

Sure, that's fine. I was expecting that anyone who wanted to know what was going on would look at #8042, where there's an explanation -- but you're right, it wouldn't hurt to have at least some explanation in the code itself. (Basically, my rule of thumb is that anything in an `EXAMPLES` section needs a good explanation, but for things in the `TESTS` section, a pointer to a trac ticket is sufficient.)

Positive review -- apply both patches. (William, I'm listing us both as authors and reviewers, since we each reviewed the other person's contribution.)



---

archive/issue_comments_071122.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-28T23:13:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8114#issuecomment-71122",
    "user": "https://github.com/craigcitro"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_019428.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-01-30T23:44:10Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8114",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8114#event-19428"
}
```



---

archive/issue_comments_071123.json:
```json
{
    "body": "Merged in this order:\n\n1. [trac_8114.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8114/trac_8114.patch)\n2. [trac_8114-part2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8114/trac_8114-part2.patch)",
    "created_at": "2010-01-30T23:44:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8114#issuecomment-71123",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged in this order:

1. [trac_8114.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8114/trac_8114.patch)
2. [trac_8114-part2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8114/trac_8114-part2.patch)



---

archive/issue_comments_071124.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-30T23:44:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8114#issuecomment-71124",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
