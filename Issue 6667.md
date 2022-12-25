# Issue 6667: bug in newton_polygon() for p-adic polynomials

archive/issues_006667.json:
```json
{
    "body": "Assignee: @roed314\n\nKeywords: newton polygon\n\nThis is as simple as I can make it at the moment:\n\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n**********************************************************************\n*                                                                    *\n* Warning: this is a prerelease version, and it may be unstable.     *\n*                                                                    *\n**********************************************************************\nsage: K = Qp(2, prec=5)\nsage: P.<x> = K[]\nsage: f = P(x^4 + 2^3*x^3 + 2^13*x^2 + 2^21*x + 2^37)\nsage: f.newton_polygon()\n[(0, 37), (1, 21), (2, 13), (3, 3), (4, 0)]\n```\n\n| Sage Version 4.1.1.rc0, Release Date: 2009-07-29                   |\n| Type notebook() for the GUI, and license() for information.        |\nThis is wrong, as it's not convex (the point (2,13) should not be there).  Indeed, note that the sequence of Newton slopes is not non-increasing:\n\n\n```\nsage: f.newton_slopes()\n[16, 8, 10, 3]\n```\n\n\nThis should be [16, 9, 9, 3].\n\nIssue created by migration from https://trac.sagemath.org/ticket/6667\n\n",
    "created_at": "2009-08-03T08:00:58Z",
    "labels": [
        "component: padics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.12",
    "title": "bug in newton_polygon() for p-adic polynomials",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6667",
    "user": "https://github.com/aghitza"
}
```
Assignee: @roed314

Keywords: newton polygon

This is as simple as I can make it at the moment:


```
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
sage: K = Qp(2, prec=5)
sage: P.<x> = K[]
sage: f = P(x^4 + 2^3*x^3 + 2^13*x^2 + 2^21*x + 2^37)
sage: f.newton_polygon()
[(0, 37), (1, 21), (2, 13), (3, 3), (4, 0)]
```

| Sage Version 4.1.1.rc0, Release Date: 2009-07-29                   |
| Type notebook() for the GUI, and license() for information.        |
This is wrong, as it's not convex (the point (2,13) should not be there).  Indeed, note that the sequence of Newton slopes is not non-increasing:


```
sage: f.newton_slopes()
[16, 8, 10, 3]
```


This should be [16, 9, 9, 3].

Issue created by migration from https://trac.sagemath.org/ticket/6667





---

archive/issue_comments_054631.json:
```json
{
    "body": "I'm probably not going to be able to take a look at this until August 20 or so.  If someone else wants to fix it, feel free.  :-)",
    "created_at": "2009-08-04T01:56:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6667#issuecomment-54631",
    "user": "https://github.com/roed314"
}
```

I'm probably not going to be able to take a look at this until August 20 or so.  If someone else wants to fix it, feel free.  :-)



---

archive/issue_comments_054632.json:
```json
{
    "body": "This is fixed in the new p-adic polynomial code, which is in progress.",
    "created_at": "2009-11-27T04:36:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6667#issuecomment-54632",
    "user": "https://github.com/roed314"
}
```

This is fixed in the new p-adic polynomial code, which is in progress.



---

archive/issue_comments_054633.json:
```json
{
    "body": "Still there in 5.12.beta2",
    "created_at": "2013-08-23T09:24:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6667#issuecomment-54633",
    "user": "https://github.com/fchapoton"
}
```

Still there in 5.12.beta2



---

archive/issue_comments_054634.json:
```json
{
    "body": "Attachment [trac_6667.patch](tarball://root/attachments/some-uuid/ticket6667/trac_6667.patch) by @fchapoton created at 2013-08-23 10:16:54\n\nhere is a quick patch that should fix the problem\n\nI have not been careful concerning the precision of the coefficients\n\nNeeds review !",
    "created_at": "2013-08-23T10:16:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6667#issuecomment-54634",
    "user": "https://github.com/fchapoton"
}
```

Attachment [trac_6667.patch](tarball://root/attachments/some-uuid/ticket6667/trac_6667.patch) by @fchapoton created at 2013-08-23 10:16:54

here is a quick patch that should fix the problem

I have not been careful concerning the precision of the coefficients

Needs review !



---

archive/issue_comments_054635.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-08-23T10:16:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6667#issuecomment-54635",
    "user": "https://github.com/fchapoton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_054636.json:
```json
{
    "body": "bot is happy, is there somebody out there for a review ?",
    "created_at": "2013-08-25T07:20:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6667#issuecomment-54636",
    "user": "https://github.com/fchapoton"
}
```

bot is happy, is there somebody out there for a review ?



---

archive/issue_comments_054637.json:
```json
{
    "body": "Here is a patch taking in account precision issues (see discussion in ticket #14828).\n\n-----\n\nFor the bot: apply only [attachment:trac_6667_caruso.patch]",
    "created_at": "2013-08-27T08:13:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6667#issuecomment-54637",
    "user": "https://github.com/xcaruso"
}
```

Here is a patch taking in account precision issues (see discussion in ticket #14828).

-----

For the bot: apply only [attachment:trac_6667_caruso.patch]



---

archive/issue_comments_054638.json:
```json
{
    "body": "your patch does not apply on a clean 5.12.beta3",
    "created_at": "2013-08-27T08:22:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6667#issuecomment-54638",
    "user": "https://github.com/fchapoton"
}
```

your patch does not apply on a clean 5.12.beta3



---

archive/issue_comments_054639.json:
```json
{
    "body": "Attachment [trac_6667_caruso.patch](tarball://root/attachments/some-uuid/ticket6667/trac_6667_caruso.patch) by @xcaruso created at 2013-08-27 16:44:18\n\nSorry. I was working with an older version of Sage. It should be fixed now.",
    "created_at": "2013-08-27T16:44:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6667#issuecomment-54639",
    "user": "https://github.com/xcaruso"
}
```

Attachment [trac_6667_caruso.patch](tarball://root/attachments/some-uuid/ticket6667/trac_6667_caruso.patch) by @xcaruso created at 2013-08-27 16:44:18

Sorry. I was working with an older version of Sage. It should be fixed now.



---

archive/issue_comments_054640.json:
```json
{
    "body": "Attachment [trac_6667_review_patch_1.patch](tarball://root/attachments/some-uuid/ticket6667/trac_6667_review_patch_1.patch) by @fchapoton created at 2013-08-27 18:56:15\n\nhere is a review patch, with only minor changes to your code\n\nin my opinion, it would be good to add examples for the two other raise statements.",
    "created_at": "2013-08-27T18:56:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6667#issuecomment-54640",
    "user": "https://github.com/fchapoton"
}
```

Attachment [trac_6667_review_patch_1.patch](tarball://root/attachments/some-uuid/ticket6667/trac_6667_review_patch_1.patch) by @fchapoton created at 2013-08-27 18:56:15

here is a review patch, with only minor changes to your code

in my opinion, it would be good to add examples for the two other raise statements.



---

archive/issue_comments_054641.json:
```json
{
    "body": "Replying to [comment:10 chapoton]:\n> here is a review patch, with only minor changes to your code\n\nThanks!\n\n> in my opinion, it would be good to add examples for the two other raise statements.\n\nActually, I believe that they can't occur but it seemed to be really safer to check them anyway. (I added a comment in the code to mention that.)\n\nI also corrected another bug: the valuation of the coefficients are not the values in the list `self._valadded` but these values augmented by `self._valbase` (as far as I understand David's code). As a consequence, the computation was wrong when the gcd of all coefficients was not 1. I added a doctest to check this issue.\n\nApply only [attachment:trac_6667_caruso_revised.patch] (it includes your review).",
    "created_at": "2013-08-27T20:26:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6667#issuecomment-54641",
    "user": "https://github.com/xcaruso"
}
```

Replying to [comment:10 chapoton]:
> here is a review patch, with only minor changes to your code

Thanks!

> in my opinion, it would be good to add examples for the two other raise statements.

Actually, I believe that they can't occur but it seemed to be really safer to check them anyway. (I added a comment in the code to mention that.)

I also corrected another bug: the valuation of the coefficients are not the values in the list `self._valadded` but these values augmented by `self._valbase` (as far as I understand David's code). As a consequence, the computation was wrong when the gcd of all coefficients was not 1. I added a doctest to check this issue.

Apply only [attachment:trac_6667_caruso_revised.patch] (it includes your review).



---

archive/issue_comments_054642.json:
```json
{
    "body": "Attachment [trac_6667_caruso_revised.patch](tarball://root/attachments/some-uuid/ticket6667/trac_6667_caruso_revised.patch) by @fchapoton created at 2013-08-28 09:48:14",
    "created_at": "2013-08-28T09:48:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6667#issuecomment-54642",
    "user": "https://github.com/fchapoton"
}
```

Attachment [trac_6667_caruso_revised.patch](tarball://root/attachments/some-uuid/ticket6667/trac_6667_caruso_revised.patch) by @fchapoton created at 2013-08-28 09:48:14



---

archive/issue_comments_054643.json:
```json
{
    "body": "apply only trac_6667_caruso_revised.patch",
    "created_at": "2013-08-29T07:43:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6667#issuecomment-54643",
    "user": "https://github.com/fchapoton"
}
```

apply only trac_6667_caruso_revised.patch



---

archive/issue_comments_054644.json:
```json
{
    "body": "apply only trac_6667_caruso_revised.patch",
    "created_at": "2013-08-29T07:45:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6667#issuecomment-54644",
    "user": "https://github.com/fchapoton"
}
```

apply only trac_6667_caruso_revised.patch



---

archive/issue_comments_054645.json:
```json
{
    "body": "ok, good to me. Positive review",
    "created_at": "2013-09-15T11:22:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6667#issuecomment-54645",
    "user": "https://github.com/fchapoton"
}
```

ok, good to me. Positive review



---

archive/issue_events_015735.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2013-09-15T11:22:59Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6667",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6667#event-15735"
}
```



---

archive/issue_comments_054646.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-09-15T11:22:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6667#issuecomment-54646",
    "user": "https://github.com/fchapoton"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_015736.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-10-01T07:17:35Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6667",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6667#event-15736"
}
```



---

archive/issue_comments_054647.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2013-10-01T07:17:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6667#issuecomment-54647",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
