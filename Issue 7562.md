# Issue 7562: Another (new?) binomial bug

archive/issues_007562.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  hgranath\n\nFrom sage-devel:\n\n```\nIn [143]: [binomial(1,1),binomial(1,2),binomial(1,3),binomial(1,4)] \nOut[143]: [1, 0, 0, 0] \nIn [144]: [binomial(1.0,1),binomial(1.0,2),binomial(1.0,3),binomial \n(1.0,4)] \nOut[144]: [1.00000000000000, 0.000000000000000, NaN, NaN] \n```\n\nThe problem is this:\n\n```\nsage: x = RealNumber('1.0')\nsage: P = x.parent()\nsage: P\nReal Field with 53 bits of precision\nsage: gamma(x+1)/gamma(P(Integer(4)+1))/gamma(x-Integer(4)+1)\nNaN\nsage: gamma(x-Integer(4)+1)\nNaN\n```\n\nSo we'll have to put in yet another check...\n\nIssue created by migration from https://trac.sagemath.org/ticket/7562\n\n",
    "created_at": "2009-11-30T18:16:36Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "Another (new?) binomial bug",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7562",
    "user": "https://github.com/kcrisman"
}
```
Assignee: @aghitza

CC:  hgranath

From sage-devel:

```
In [143]: [binomial(1,1),binomial(1,2),binomial(1,3),binomial(1,4)] 
Out[143]: [1, 0, 0, 0] 
In [144]: [binomial(1.0,1),binomial(1.0,2),binomial(1.0,3),binomial 
(1.0,4)] 
Out[144]: [1.00000000000000, 0.000000000000000, NaN, NaN] 
```

The problem is this:

```
sage: x = RealNumber('1.0')
sage: P = x.parent()
sage: P
Real Field with 53 bits of precision
sage: gamma(x+1)/gamma(P(Integer(4)+1))/gamma(x-Integer(4)+1)
NaN
sage: gamma(x-Integer(4)+1)
NaN
```

So we'll have to put in yet another check...

Issue created by migration from https://trac.sagemath.org/ticket/7562





---

archive/issue_comments_064221.json:
```json
{
    "body": "Here is a patch that should fix this issue. Note that for x a\nnegative floating point integer we hit gamma function poles both\nin the numerator and denominator. An alternative formula is used\nin the patch to avoid this.\n\nBy the way, is the cc field above supposed to notify me by mail?\nI did not get any.",
    "created_at": "2009-12-02T06:13:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7562",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7562#issuecomment-64221",
    "user": "https://trac.sagemath.org/admin/accounts/users/hgranath"
}
```

Here is a patch that should fix this issue. Note that for x a
negative floating point integer we hit gamma function poles both
in the numerator and denominator. An alternative formula is used
in the patch to avoid this.

By the way, is the cc field above supposed to notify me by mail?
I did not get any.



---

archive/issue_comments_064222.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-02T06:13:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7562",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7562#issuecomment-64222",
    "user": "https://trac.sagemath.org/admin/accounts/users/hgranath"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_064223.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-12-02T06:56:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7562",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7562#issuecomment-64223",
    "user": "https://trac.sagemath.org/admin/accounts/users/hgranath"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_064224.json:
```json
{
    "body": "Sorry, my patch is off for negative x. I will send an updated patch later.",
    "created_at": "2009-12-02T06:56:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7562",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7562#issuecomment-64224",
    "user": "https://trac.sagemath.org/admin/accounts/users/hgranath"
}
```

Sorry, my patch is off for negative x. I will send an updated patch later.



---

archive/issue_comments_064225.json:
```json
{
    "body": "> By the way, is the cc field above supposed to notify me by mail?\n> I did not get any.\n\nYes, and it does usually work, but perhaps you don't have a correct email associated to your account.  I don't know how to fix this, you may want to ask on sage-devel.",
    "created_at": "2009-12-02T14:19:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7562",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7562#issuecomment-64225",
    "user": "https://github.com/kcrisman"
}
```

> By the way, is the cc field above supposed to notify me by mail?
> I did not get any.

Yes, and it does usually work, but perhaps you don't have a correct email associated to your account.  I don't know how to fix this, you may want to ask on sage-devel.



---

archive/issue_comments_064226.json:
```json
{
    "body": "Replying to [comment:3 kcrisman]:\n\n> Yes, and it does usually work, but perhaps you don't have a correct email associated to your account.  I don't know how to fix this, you may want to ask on sage-devel.\n\nThanks for the info, I found some place to enter my email so probably it will work now.",
    "created_at": "2009-12-02T14:53:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7562",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7562#issuecomment-64226",
    "user": "https://trac.sagemath.org/admin/accounts/users/hgranath"
}
```

Replying to [comment:3 kcrisman]:

> Yes, and it does usually work, but perhaps you don't have a correct email associated to your account.  I don't know how to fix this, you may want to ask on sage-devel.

Thanks for the info, I found some place to enter my email so probably it will work now.



---

archive/issue_comments_064227.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-12-02T20:03:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7562",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7562#issuecomment-64227",
    "user": "https://trac.sagemath.org/admin/accounts/users/hgranath"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_064228.json:
```json
{
    "body": "This seems to work fine, and agrees with integer calculations.  Obviously passes tests.\n\nBut:\n\n```\nsage: binomial(0,0)\n1\nsage: binomial(0.,0)\nNaN\n```\n\n\nI don't know which is the usual convention, but they should probably agree.",
    "created_at": "2009-12-04T15:48:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7562",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7562#issuecomment-64228",
    "user": "https://github.com/kcrisman"
}
```

This seems to work fine, and agrees with integer calculations.  Obviously passes tests.

But:

```
sage: binomial(0,0)
1
sage: binomial(0.,0)
NaN
```


I don't know which is the usual convention, but they should probably agree.



---

archive/issue_comments_064229.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-12-04T15:48:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7562",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7562#issuecomment-64229",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_064230.json:
```json
{
    "body": "Attachment [trac_7562.patch](tarball://root/attachments/some-uuid/ticket7562/trac_7562.patch) by hgranath created at 2009-12-04 16:11:48\n\nNew breakpoint",
    "created_at": "2009-12-04T16:11:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7562",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7562#issuecomment-64230",
    "user": "https://trac.sagemath.org/admin/accounts/users/hgranath"
}
```

Attachment [trac_7562.patch](tarball://root/attachments/some-uuid/ticket7562/trac_7562.patch) by hgranath created at 2009-12-04 16:11:48

New breakpoint



---

archive/issue_comments_064231.json:
```json
{
    "body": "Thanks for spotting this, new version is up.",
    "created_at": "2009-12-04T16:13:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7562",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7562#issuecomment-64231",
    "user": "https://trac.sagemath.org/admin/accounts/users/hgranath"
}
```

Thanks for spotting this, new version is up.



---

archive/issue_comments_064232.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-12-04T16:13:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7562",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7562#issuecomment-64232",
    "user": "https://trac.sagemath.org/admin/accounts/users/hgranath"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_064233.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-04T17:45:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7562",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7562#issuecomment-64233",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_064234.json:
```json
{
    "body": "Great, positive review!",
    "created_at": "2009-12-04T17:45:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7562",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7562#issuecomment-64234",
    "user": "https://github.com/kcrisman"
}
```

Great, positive review!



---

archive/issue_comments_064235.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-06T08:51:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7562",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7562#issuecomment-64235",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_007791.json:
```json
{
    "actor": "@mwhansen",
    "created_at": "2009-12-06T08:51:53Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7562",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7562#event-7791"
}
```
