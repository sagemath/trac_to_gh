# Issue 8114: doctest failure in `sage/libs/cremona/newforms.pyx` on 32-bit machines from #8042

archive/issues_008114.json:
```json
{
    "body": "Assignee: was\n\nCC:  aghitza\n\nI forgot to test my fix from #8042 on 32-bit platforms, and the fix causes doctest failures anywhere that `long` is smaller than 64 bits. I'm attaching a simple patch to fix this -- we just don't perform that test on 32-bit platforms.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8114\n\n",
    "created_at": "2010-01-28T22:28:32Z",
    "labels": [
        "interfaces",
        "major",
        "bug"
    ],
    "title": "doctest failure in `sage/libs/cremona/newforms.pyx` on 32-bit machines from #8042",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8114",
    "user": "craigcitro"
}
```
Assignee: was

CC:  aghitza

I forgot to test my fix from #8042 on 32-bit platforms, and the fix causes doctest failures anywhere that `long` is smaller than 64 bits. I'm attaching a simple patch to fix this -- we just don't perform that test on 32-bit platforms.

Issue created by migration from https://trac.sagemath.org/ticket/8114





---

archive/issue_comments_071237.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-01-28T22:32:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8114#issuecomment-71237",
    "user": "craigcitro"
}
```

Attachment



---

archive/issue_comments_071238.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-28T22:32:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8114#issuecomment-71238",
    "user": "craigcitro"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_071239.json:
```json
{
    "body": "With this patch applied, on 32-bit linux we have:\n\n\n```\nwstein@ubuntu32:/tmp/wstein/farm/sage-4.3.2.alpha0$         sage -t  -long \"devel/sage/sage/libs/cremona/newforms.pyx\"                                                                                        \n\nsage -t -long \"devel/sage/sage/libs/cremona/newforms.pyx\"   \n\n         [6.3 s]\n                \n```\n\n\nWhich is good.   However, I do not think the patch you posted explains very well what is going on.  It's not good for a user reading it.  I've posted an additional patch (apply after yours), which I think does a better job testing things and illustrating the issue.",
    "created_at": "2010-01-28T23:07:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8114#issuecomment-71239",
    "user": "was"
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

archive/issue_comments_071240.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2010-01-28T23:08:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8114#issuecomment-71240",
    "user": "was"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_071241.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-01-28T23:08:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8114#issuecomment-71241",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_071242.json:
```json
{
    "body": "Sure, that's fine. I was expecting that anyone who wanted to know what was going on would look at #8042, where there's an explanation -- but you're right, it wouldn't hurt to have at least some explanation in the code itself. (Basically, my rule of thumb is that anything in an `EXAMPLES` section needs a good explanation, but for things in the `TESTS` section, a pointer to a trac ticket is sufficient.)\n\nPositive review -- apply both patches. (William, I'm listing us both as authors and reviewers, since we each reviewed the other person's contribution.)",
    "created_at": "2010-01-28T23:13:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8114#issuecomment-71242",
    "user": "craigcitro"
}
```

Sure, that's fine. I was expecting that anyone who wanted to know what was going on would look at #8042, where there's an explanation -- but you're right, it wouldn't hurt to have at least some explanation in the code itself. (Basically, my rule of thumb is that anything in an `EXAMPLES` section needs a good explanation, but for things in the `TESTS` section, a pointer to a trac ticket is sufficient.)

Positive review -- apply both patches. (William, I'm listing us both as authors and reviewers, since we each reviewed the other person's contribution.)



---

archive/issue_comments_071243.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-28T23:13:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8114#issuecomment-71243",
    "user": "craigcitro"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_071244.json:
```json
{
    "body": "Merged in this order:\n\n1. [trac_8114.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8114/trac_8114.patch)\n2. [trac_8114-part2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8114/trac_8114-part2.patch)",
    "created_at": "2010-01-30T23:44:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8114#issuecomment-71244",
    "user": "mvngu"
}
```

Merged in this order:

1. [trac_8114.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8114/trac_8114.patch)
2. [trac_8114-part2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8114/trac_8114-part2.patch)



---

archive/issue_comments_071245.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-30T23:44:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8114#issuecomment-71245",
    "user": "mvngu"
}
```

Resolution: fixed
