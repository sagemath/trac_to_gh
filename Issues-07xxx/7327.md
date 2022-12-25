# Issue 7327: Make integrate accept a variable range as a tuple

archive/issues_007327.json:
```json
{
    "body": "Assignee: @burcin\n\nCC:  @kcrisman\n\nIt is inconsistent with plot and other functions that this just hangs:\n\n```\nintegrate(sin(x), (x,0,1))\n```\n\nThis patch takes care of this.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7327\n\n",
    "closed_at": "2009-11-06T05:10:58Z",
    "created_at": "2009-10-28T00:24:05Z",
    "labels": [
        "component: calculus",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2.1",
    "title": "Make integrate accept a variable range as a tuple",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7327",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @burcin

CC:  @kcrisman

It is inconsistent with plot and other functions that this just hangs:

```
integrate(sin(x), (x,0,1))
```

This patch takes care of this.


Issue created by migration from https://trac.sagemath.org/ticket/7327





---

archive/issue_comments_061165.json:
```json
{
    "body": "Attachment [trac-7327-integrate-range.patch](tarball://root/attachments/some-uuid/ticket7327/trac-7327-integrate-range.patch) by @jasongrout created at 2009-10-28 00:38:54",
    "created_at": "2009-10-28T00:38:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7327",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7327#issuecomment-61165",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-7327-integrate-range.patch](tarball://root/attachments/some-uuid/ticket7327/trac-7327-integrate-range.patch) by @jasongrout created at 2009-10-28 00:38:54



---

archive/issue_comments_061166.json:
```json
{
    "body": "This is a duplicate of #6816.  The tests for one of these should be incorporated in the other - probably in this one, since it has some doc upgrades - and probably also the check for too many arguments in the tuple.",
    "created_at": "2009-10-28T01:14:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7327",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7327#issuecomment-61166",
    "user": "https://github.com/kcrisman"
}
```

This is a duplicate of #6816.  The tests for one of these should be incorporated in the other - probably in this one, since it has some doc upgrades - and probably also the check for too many arguments in the tuple.



---

archive/issue_comments_061167.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2009-10-28T01:14:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7327",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7327#issuecomment-61167",
    "user": "https://github.com/kcrisman"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_061168.json:
```json
{
    "body": "Based on Sage 4.2",
    "created_at": "2009-11-05T17:43:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7327",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7327#issuecomment-61168",
    "user": "https://github.com/kcrisman"
}
```

Based on Sage 4.2



---

archive/issue_comments_061169.json:
```json
{
    "body": "Attachment [trac_7327-updated.patch](tarball://root/attachments/some-uuid/ticket7327/trac_7327-updated.patch) by @kcrisman created at 2009-11-05 17:45:16\n\nUpdated patch includes the issues mentioned in previous comment, is ready for review.  Positive review to the parts I didn't write.",
    "created_at": "2009-11-05T17:45:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7327",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7327#issuecomment-61169",
    "user": "https://github.com/kcrisman"
}
```

Attachment [trac_7327-updated.patch](tarball://root/attachments/some-uuid/ticket7327/trac_7327-updated.patch) by @kcrisman created at 2009-11-05 17:45:16

Updated patch includes the issues mentioned in previous comment, is ready for review.  Positive review to the parts I didn't write.



---

archive/issue_comments_061170.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-11-05T17:45:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7327",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7327#issuecomment-61170",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_061171.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-11-06T05:10:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7327",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7327#issuecomment-61171",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.



---

archive/issue_comments_061172.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-06T05:10:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7327",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7327#issuecomment-61172",
    "user": "https://github.com/mwhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_017347.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-11-06T05:10:58Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7327",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7327#event-17347"
}
```



---

archive/issue_comments_061173.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-06T05:10:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7327",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7327#issuecomment-61173",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_comments_061174.json:
```json
{
    "body": "Just an update - it turns out the original integral reported in #6816 is not, in fact, convergent.  Fixing this doctest so something mathematically correct happens will be done in #7745, since Maxima 5.20.1 simply returns that integral now, as opposed to giving 0.",
    "created_at": "2009-12-22T16:29:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7327",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7327#issuecomment-61174",
    "user": "https://github.com/kcrisman"
}
```

Just an update - it turns out the original integral reported in #6816 is not, in fact, convergent.  Fixing this doctest so something mathematically correct happens will be done in #7745, since Maxima 5.20.1 simply returns that integral now, as opposed to giving 0.
