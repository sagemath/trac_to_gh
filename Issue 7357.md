# Issue 7357: Add non-offset logarithmic integral, Li

archive/issues_007357.json:
```json
{
    "body": "Assignee: @burcin\n\nCC:  myurko @benjaminfjones\n\nAdd the logarithmic integral, Li, with integration starting at 0 rather than 2.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7357\n\n",
    "created_at": "2009-10-30T16:49:49Z",
    "labels": [
        "calculus",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Add non-offset logarithmic integral, Li",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7357",
    "user": "myurko"
}
```
Assignee: @burcin

CC:  myurko @benjaminfjones

Add the logarithmic integral, Li, with integration starting at 0 rather than 2.

Issue created by migration from https://trac.sagemath.org/ticket/7357





---

archive/issue_comments_061648.json:
```json
{
    "body": "Attachment [li(x).patch](tarball://root/attachments/some-uuid/ticket7357/li(x).patch) by myurko created at 2009-10-30 16:53:13",
    "created_at": "2009-10-30T16:53:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7357#issuecomment-61648",
    "user": "myurko"
}
```

Attachment [li(x).patch](tarball://root/attachments/some-uuid/ticket7357/li(x).patch) by myurko created at 2009-10-30 16:53:13



---

archive/issue_comments_061649.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-30T16:53:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7357#issuecomment-61649",
    "user": "myurko"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_061650.json:
```json
{
    "body": "This is nice, but like #3401, should have some doctests indicating it works for complex input (I assume it does).   The patch also depends on #3401.",
    "created_at": "2009-11-10T13:18:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7357#issuecomment-61650",
    "user": "@kcrisman"
}
```

This is nice, but like #3401, should have some doctests indicating it works for complex input (I assume it does).   The patch also depends on #3401.



---

archive/issue_comments_061651.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-11-10T13:18:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7357#issuecomment-61651",
    "user": "@kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_061652.json:
```json
{
    "body": "Attachment [non-offset-log-int.patch](tarball://root/attachments/some-uuid/ticket7357/non-offset-log-int.patch) by @kcrisman created at 2010-01-18 17:11:39\n\nThis patch adds these tests.  It still depends on the (newest) patch at #3401, and in fact gets rid of one final thing which was only needed by the previous implementation of Li.",
    "created_at": "2010-01-18T17:11:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7357#issuecomment-61652",
    "user": "@kcrisman"
}
```

Attachment [non-offset-log-int.patch](tarball://root/attachments/some-uuid/ticket7357/non-offset-log-int.patch) by @kcrisman created at 2010-01-18 17:11:39

This patch adds these tests.  It still depends on the (newest) patch at #3401, and in fact gets rid of one final thing which was only needed by the previous implementation of Li.



---

archive/issue_comments_061653.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-18T17:11:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7357#issuecomment-61653",
    "user": "@kcrisman"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_061654.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-18T17:12:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7357#issuecomment-61654",
    "user": "@kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_061655.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-01-18T18:19:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7357#issuecomment-61655",
    "user": "@burcin"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_061656.json:
```json
{
    "body": "This needs more work. See my comments about the prec parameter at comment:10:ticket:3401.\n\nTwo different functions whose names differ only in capitalization (`li` and `Li`) is also very confusing. We need to come up with a better name for this.",
    "created_at": "2010-01-18T18:19:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7357#issuecomment-61656",
    "user": "@burcin"
}
```

This needs more work. See my comments about the prec parameter at comment:10:ticket:3401.

Two different functions whose names differ only in capitalization (`li` and `Li`) is also very confusing. We need to come up with a better name for this.



---

archive/issue_comments_061657.json:
```json
{
    "body": "Changing keywords from \"\" to \"beginner\".",
    "created_at": "2010-08-28T16:15:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7357#issuecomment-61657",
    "user": "@burcin"
}
```

Changing keywords from "" to "beginner".



---

archive/issue_comments_061658.json:
```json
{
    "body": "This seems to be addressed in the context of a much bigger overhaul by #11143.  But there the name is... more complicated.",
    "created_at": "2011-10-09T01:28:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7357#issuecomment-61658",
    "user": "@kcrisman"
}
```

This seems to be addressed in the context of a much bigger overhaul by #11143.  But there the name is... more complicated.



---

archive/issue_comments_061659.json:
```json
{
    "body": "Yes, this would duplicate work done in #11143. The function added there is a fully symbolic function with numerical evaluation handled by mpmath. I think that is superior to the one defined here which is just a wrapper for the mpmath call. \n\nThe function added in #11143 is really a class called ``Function_exp_integral_li`` and it has an alias ``exp_integral_li`` to match the other exponential integrals. #11143 also moves all the exponential integrals to a new module under sage/functions so this would conflict with that design decision too.",
    "created_at": "2011-10-09T01:41:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7357#issuecomment-61659",
    "user": "@benjaminfjones"
}
```

Yes, this would duplicate work done in #11143. The function added there is a fully symbolic function with numerical evaluation handled by mpmath. I think that is superior to the one defined here which is just a wrapper for the mpmath call. 

The function added in #11143 is really a class called ``Function_exp_integral_li`` and it has an alias ``exp_integral_li`` to match the other exponential integrals. #11143 also moves all the exponential integrals to a new module under sage/functions so this would conflict with that design decision too.



---

archive/issue_comments_061660.json:
```json
{
    "body": "So this can be closed as duplicate, correct?  Except I really would love it to be called `Li` instead of something horribly long... either way, feel free to review this as positive; I'm changing the milestone.",
    "created_at": "2011-10-10T02:17:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7357#issuecomment-61660",
    "user": "@kcrisman"
}
```

So this can be closed as duplicate, correct?  Except I really would love it to be called `Li` instead of something horribly long... either way, feel free to review this as positive; I'm changing the milestone.



---

archive/issue_comments_061661.json:
```json
{
    "body": "This is definitely and definitively duplicated by the much more comprehensive #11143.",
    "created_at": "2012-05-26T17:19:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7357#issuecomment-61661",
    "user": "@kcrisman"
}
```

This is definitely and definitively duplicated by the much more comprehensive #11143.



---

archive/issue_comments_061662.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2012-05-26T17:19:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7357#issuecomment-61662",
    "user": "@kcrisman"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_061663.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2012-06-19T13:28:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7357#issuecomment-61663",
    "user": "@jdemeyer"
}
```

Resolution: duplicate
