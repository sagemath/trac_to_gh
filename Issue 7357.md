# Issue 7357: Add non-offset logarithmic integral, Li

archive/issues_007357.json:
```json
{
    "body": "Assignee: @burcin\n\nCC:  myurko @benjaminfjones\n\nAdd the logarithmic integral, Li, with integration starting at 0 rather than 2.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7357\n\n",
    "created_at": "2009-10-30T16:49:49Z",
    "labels": [
        "component: calculus",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Add non-offset logarithmic integral, Li",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7357",
    "user": "https://trac.sagemath.org/admin/accounts/users/myurko"
}
```
Assignee: @burcin

CC:  myurko @benjaminfjones

Add the logarithmic integral, Li, with integration starting at 0 rather than 2.

Issue created by migration from https://trac.sagemath.org/ticket/7357





---

archive/issue_comments_061535.json:
```json
{
    "body": "Attachment [li(x).patch](tarball://root/attachments/some-uuid/ticket7357/li(x).patch) by myurko created at 2009-10-30 16:53:13",
    "created_at": "2009-10-30T16:53:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7357#issuecomment-61535",
    "user": "https://trac.sagemath.org/admin/accounts/users/myurko"
}
```

Attachment [li(x).patch](tarball://root/attachments/some-uuid/ticket7357/li(x).patch) by myurko created at 2009-10-30 16:53:13



---

archive/issue_comments_061536.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-30T16:53:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7357#issuecomment-61536",
    "user": "https://trac.sagemath.org/admin/accounts/users/myurko"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_061537.json:
```json
{
    "body": "This is nice, but like #3401, should have some doctests indicating it works for complex input (I assume it does).   The patch also depends on #3401.",
    "created_at": "2009-11-10T13:18:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7357#issuecomment-61537",
    "user": "https://github.com/kcrisman"
}
```

This is nice, but like #3401, should have some doctests indicating it works for complex input (I assume it does).   The patch also depends on #3401.



---

archive/issue_comments_061538.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-11-10T13:18:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7357#issuecomment-61538",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_061539.json:
```json
{
    "body": "Attachment [non-offset-log-int.patch](tarball://root/attachments/some-uuid/ticket7357/non-offset-log-int.patch) by @kcrisman created at 2010-01-18 17:11:39\n\nThis patch adds these tests.  It still depends on the (newest) patch at #3401, and in fact gets rid of one final thing which was only needed by the previous implementation of Li.",
    "created_at": "2010-01-18T17:11:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7357#issuecomment-61539",
    "user": "https://github.com/kcrisman"
}
```

Attachment [non-offset-log-int.patch](tarball://root/attachments/some-uuid/ticket7357/non-offset-log-int.patch) by @kcrisman created at 2010-01-18 17:11:39

This patch adds these tests.  It still depends on the (newest) patch at #3401, and in fact gets rid of one final thing which was only needed by the previous implementation of Li.



---

archive/issue_comments_061540.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-18T17:11:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7357#issuecomment-61540",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_061541.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-18T17:12:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7357#issuecomment-61541",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_061542.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-01-18T18:19:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7357#issuecomment-61542",
    "user": "https://github.com/burcin"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_061543.json:
```json
{
    "body": "This needs more work. See my comments about the prec parameter at comment:10:ticket:3401.\n\nTwo different functions whose names differ only in capitalization (`li` and `Li`) is also very confusing. We need to come up with a better name for this.",
    "created_at": "2010-01-18T18:19:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7357#issuecomment-61543",
    "user": "https://github.com/burcin"
}
```

This needs more work. See my comments about the prec parameter at comment:10:ticket:3401.

Two different functions whose names differ only in capitalization (`li` and `Li`) is also very confusing. We need to come up with a better name for this.



---

archive/issue_comments_061544.json:
```json
{
    "body": "Changing keywords from \"\" to \"beginner\".",
    "created_at": "2010-08-28T16:15:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7357#issuecomment-61544",
    "user": "https://github.com/burcin"
}
```

Changing keywords from "" to "beginner".



---

archive/issue_comments_061545.json:
```json
{
    "body": "This seems to be addressed in the context of a much bigger overhaul by #11143.  But there the name is... more complicated.",
    "created_at": "2011-10-09T01:28:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7357#issuecomment-61545",
    "user": "https://github.com/kcrisman"
}
```

This seems to be addressed in the context of a much bigger overhaul by #11143.  But there the name is... more complicated.



---

archive/issue_comments_061546.json:
```json
{
    "body": "Yes, this would duplicate work done in #11143. The function added there is a fully symbolic function with numerical evaluation handled by mpmath. I think that is superior to the one defined here which is just a wrapper for the mpmath call. \n\nThe function added in #11143 is really a class called ``Function_exp_integral_li`` and it has an alias ``exp_integral_li`` to match the other exponential integrals. #11143 also moves all the exponential integrals to a new module under sage/functions so this would conflict with that design decision too.",
    "created_at": "2011-10-09T01:41:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7357#issuecomment-61546",
    "user": "https://github.com/benjaminfjones"
}
```

Yes, this would duplicate work done in #11143. The function added there is a fully symbolic function with numerical evaluation handled by mpmath. I think that is superior to the one defined here which is just a wrapper for the mpmath call. 

The function added in #11143 is really a class called ``Function_exp_integral_li`` and it has an alias ``exp_integral_li`` to match the other exponential integrals. #11143 also moves all the exponential integrals to a new module under sage/functions so this would conflict with that design decision too.



---

archive/issue_comments_061547.json:
```json
{
    "body": "So this can be closed as duplicate, correct?  Except I really would love it to be called `Li` instead of something horribly long... either way, feel free to review this as positive; I'm changing the milestone.",
    "created_at": "2011-10-10T02:17:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7357#issuecomment-61547",
    "user": "https://github.com/kcrisman"
}
```

So this can be closed as duplicate, correct?  Except I really would love it to be called `Li` instead of something horribly long... either way, feel free to review this as positive; I'm changing the milestone.



---

archive/issue_comments_061548.json:
```json
{
    "body": "This is definitely and definitively duplicated by the much more comprehensive #11143.",
    "created_at": "2012-05-26T17:19:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7357#issuecomment-61548",
    "user": "https://github.com/kcrisman"
}
```

This is definitely and definitively duplicated by the much more comprehensive #11143.



---

archive/issue_comments_061549.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2012-05-26T17:19:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7357#issuecomment-61549",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_events_007580.json:
```json
{
    "actor": "@jdemeyer",
    "created_at": "2012-06-19T13:28:24Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7357",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7357#event-7580"
}
```



---

archive/issue_comments_061550.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2012-06-19T13:28:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7357#issuecomment-61550",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: duplicate
