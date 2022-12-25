# Issue 7788: followup patch to #5396

archive/issues_007788.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @craigcitro @JohnCremona ylchapuy @robertwb\n\nI am attaching  patchs which adds to the documentation that the derivatives loose about half the precision. There is additional documentation to guide how many dirichlet coefficients are needed, at least for computing near the real axis.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7788\n\n",
    "created_at": "2009-12-29T16:45:25Z",
    "labels": [
        "component: number theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "followup patch to #5396",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7788",
    "user": "https://github.com/rishikesha"
}
```
Assignee: @williamstein

CC:  @craigcitro @JohnCremona ylchapuy @robertwb

I am attaching  patchs which adds to the documentation that the derivatives loose about half the precision. There is additional documentation to guide how many dirichlet coefficients are needed, at least for computing near the real axis.

Issue created by migration from https://trac.sagemath.org/ticket/7788





---

archive/issue_comments_067096.json:
```json
{
    "body": "Attachment [minor_change_lcalc-1.patch](tarball://root/attachments/some-uuid/ticket7788/minor_change_lcalc-1.patch) by @rishikesha created at 2009-12-29 16:45:42",
    "created_at": "2009-12-29T16:45:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7788",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7788#issuecomment-67096",
    "user": "https://github.com/rishikesha"
}
```

Attachment [minor_change_lcalc-1.patch](tarball://root/attachments/some-uuid/ticket7788/minor_change_lcalc-1.patch) by @rishikesha created at 2009-12-29 16:45:42



---

archive/issue_comments_067097.json:
```json
{
    "body": "Attachment [minor_change_lcalc-combined.patch](tarball://root/attachments/some-uuid/ticket7788/minor_change_lcalc-combined.patch) by @rishikesha created at 2009-12-29 18:24:14",
    "created_at": "2009-12-29T18:24:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7788",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7788#issuecomment-67097",
    "user": "https://github.com/rishikesha"
}
```

Attachment [minor_change_lcalc-combined.patch](tarball://root/attachments/some-uuid/ticket7788/minor_change_lcalc-combined.patch) by @rishikesha created at 2009-12-29 18:24:14



---

archive/issue_comments_067098.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-29T18:32:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7788",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7788#issuecomment-67098",
    "user": "https://github.com/rishikesha"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_067099.json:
```json
{
    "body": "I finally figured out how to combine several commits",
    "created_at": "2009-12-29T18:32:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7788",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7788#issuecomment-67099",
    "user": "https://github.com/rishikesha"
}
```

I finally figured out how to combine several commits



---

archive/issue_comments_067100.json:
```json
{
    "body": "I'm giving this a positive review, though the formatting of the docstrings in  lcalc_Lfunction.pyx is not correct so that sphinx would choke on these.  But at the moment this file is not included in the reference manual.  So rather than delay the merging of the lcalc wrapping, it seems reasonable to pass this as is and create a new TODO ticket for that.",
    "created_at": "2009-12-30T16:17:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7788",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7788#issuecomment-67100",
    "user": "https://github.com/JohnCremona"
}
```

I'm giving this a positive review, though the formatting of the docstrings in  lcalc_Lfunction.pyx is not correct so that sphinx would choke on these.  But at the moment this file is not included in the reference manual.  So rather than delay the merging of the lcalc wrapping, it seems reasonable to pass this as is and create a new TODO ticket for that.



---

archive/issue_comments_067101.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-30T16:17:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7788",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7788#issuecomment-67101",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_067102.json:
```json
{
    "body": "I don't think it's helpful to have this tagged as \"positive review\" when it depends on #5396 which is still being worked on.  So I am switching it back to \"needs work\" and it can go to \"needs review\" after #5396 is positively reviewed.",
    "created_at": "2010-01-17T18:16:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7788",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7788#issuecomment-67102",
    "user": "https://github.com/JohnCremona"
}
```

I don't think it's helpful to have this tagged as "positive review" when it depends on #5396 which is still being worked on.  So I am switching it back to "needs work" and it can go to "needs review" after #5396 is positively reviewed.



---

archive/issue_comments_067103.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-01-17T18:16:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7788",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7788#issuecomment-67103",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_067104.json:
```json
{
    "body": "John,\n\nI put a new spkg in [#5396](http://trac.sagemath.org/sage_trac/ticket/5396)\n\nI tested it on my computer and on sage.math. I believe this should work.\n\nRishi",
    "created_at": "2010-01-17T19:03:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7788",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7788#issuecomment-67104",
    "user": "https://github.com/rishikesha"
}
```

John,

I put a new spkg in [#5396](http://trac.sagemath.org/sage_trac/ticket/5396)

I tested it on my computer and on sage.math. I believe this should work.

Rishi



---

archive/issue_comments_067105.json:
```json
{
    "body": "This patch is superseded by #8623. This ticket can be discarded.",
    "created_at": "2010-07-11T02:49:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7788",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7788#issuecomment-67105",
    "user": "https://github.com/rishikesha"
}
```

This patch is superseded by #8623. This ticket can be discarded.



---

archive/issue_comments_067106.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-11T02:49:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7788",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7788#issuecomment-67106",
    "user": "https://github.com/rishikesha"
}
```

Resolution: fixed



---

archive/issue_events_018629.json:
```json
{
    "actor": "https://github.com/rishikesha",
    "created_at": "2010-07-11T02:49:35Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7788",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7788#event-18629"
}
```



---

archive/issue_comments_067107.json:
```json
{
    "body": "Resolution changed from fixed to duplicate",
    "created_at": "2010-07-11T03:34:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7788",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7788#issuecomment-67107",
    "user": "https://github.com/mwhansen"
}
```

Resolution changed from fixed to duplicate



---

archive/issue_events_018630.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-07-11T03:34:33Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7788",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7788#event-18630"
}
```
