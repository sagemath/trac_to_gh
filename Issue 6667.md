# Issue 6667: bug in newton_polygon() for p-adic polynomials

archive/issues_006667.json:
```json
{
    "body": "Assignee: roed\n\nKeywords: newton polygon\n\nThis is as simple as I can make it at the moment:\n\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n**********************************************************************\n*                                                                    *\n* Warning: this is a prerelease version, and it may be unstable.     *\n*                                                                    *\n**********************************************************************\nsage: K = Qp(2, prec=5)\nsage: P.<x> = K[]\nsage: f = P(x^4 + 2^3*x^3 + 2^13*x^2 + 2^21*x + 2^37)\nsage: f.newton_polygon()\n[(0, 37), (1, 21), (2, 13), (3, 3), (4, 0)]\n```\n\n| Sage Version 4.1.1.rc0, Release Date: 2009-07-29                   |\n| Type notebook() for the GUI, and license() for information.        |\nThis is wrong, as it's not convex (the point (2,13) should not be there).  Indeed, note that the sequence of Newton slopes is not non-increasing:\n\n\n```\nsage: f.newton_slopes()\n[16, 8, 10, 3]\n```\n\n\nThis should be [16, 9, 9, 3].\n\nIssue created by migration from https://trac.sagemath.org/ticket/6667\n\n",
    "created_at": "2009-08-03T08:00:58Z",
    "labels": [
        "padics",
        "major",
        "bug"
    ],
    "title": "bug in newton_polygon() for p-adic polynomials",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6667",
    "user": "AlexGhitza"
}
```
Assignee: roed

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

archive/issue_comments_054732.json:
```json
{
    "body": "I'm probably not going to be able to take a look at this until August 20 or so.  If someone else wants to fix it, feel free.  :-)",
    "created_at": "2009-08-04T01:56:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6667#issuecomment-54732",
    "user": "roed"
}
```

I'm probably not going to be able to take a look at this until August 20 or so.  If someone else wants to fix it, feel free.  :-)



---

archive/issue_comments_054733.json:
```json
{
    "body": "This is fixed in the new p-adic polynomial code, which is in progress.",
    "created_at": "2009-11-27T04:36:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6667#issuecomment-54733",
    "user": "roed"
}
```

This is fixed in the new p-adic polynomial code, which is in progress.



---

archive/issue_comments_054734.json:
```json
{
    "body": "Still there in 5.12.beta2",
    "created_at": "2013-08-23T09:24:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6667#issuecomment-54734",
    "user": "chapoton"
}
```

Still there in 5.12.beta2



---

archive/issue_comments_054735.json:
```json
{
    "body": "Attachment\n\nhere is a quick patch that should fix the problem\n\nI have not been careful concerning the precision of the coefficients\n\nNeeds review !",
    "created_at": "2013-08-23T10:16:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6667#issuecomment-54735",
    "user": "chapoton"
}
```

Attachment

here is a quick patch that should fix the problem

I have not been careful concerning the precision of the coefficients

Needs review !



---

archive/issue_comments_054736.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-08-23T10:16:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6667#issuecomment-54736",
    "user": "chapoton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_054737.json:
```json
{
    "body": "bot is happy, is there somebody out there for a review ?",
    "created_at": "2013-08-25T07:20:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6667#issuecomment-54737",
    "user": "chapoton"
}
```

bot is happy, is there somebody out there for a review ?



---

archive/issue_comments_054738.json:
```json
{
    "body": "Here is a patch taking in account precision issues (see discussion in ticket #14828).\n\n-----\n\nFor the bot: apply only [attachment:trac_6667_caruso.patch]",
    "created_at": "2013-08-27T08:13:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6667#issuecomment-54738",
    "user": "caruso"
}
```

Here is a patch taking in account precision issues (see discussion in ticket #14828).

-----

For the bot: apply only [attachment:trac_6667_caruso.patch]



---

archive/issue_comments_054739.json:
```json
{
    "body": "your patch does not apply on a clean 5.12.beta3",
    "created_at": "2013-08-27T08:22:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6667#issuecomment-54739",
    "user": "chapoton"
}
```

your patch does not apply on a clean 5.12.beta3



---

archive/issue_comments_054740.json:
```json
{
    "body": "Attachment\n\nSorry. I was working with an older version of Sage. It should be fixed now.",
    "created_at": "2013-08-27T16:44:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6667#issuecomment-54740",
    "user": "caruso"
}
```

Attachment

Sorry. I was working with an older version of Sage. It should be fixed now.



---

archive/issue_comments_054741.json:
```json
{
    "body": "Attachment\n\nhere is a review patch, with only minor changes to your code\n\nin my opinion, it would be good to add examples for the two other raise statements.",
    "created_at": "2013-08-27T18:56:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6667#issuecomment-54741",
    "user": "chapoton"
}
```

Attachment

here is a review patch, with only minor changes to your code

in my opinion, it would be good to add examples for the two other raise statements.



---

archive/issue_comments_054742.json:
```json
{
    "body": "Replying to [comment:10 chapoton]:\n> here is a review patch, with only minor changes to your code\n\nThanks!\n\n> in my opinion, it would be good to add examples for the two other raise statements.\n\nActually, I believe that they can't occur but it seemed to be really safer to check them anyway. (I added a comment in the code to mention that.)\n\nI also corrected another bug: the valuation of the coefficients are not the values in the list `self._valadded` but these values augmented by `self._valbase` (as far as I understand David's code). As a consequence, the computation was wrong when the gcd of all coefficients was not 1. I added a doctest to check this issue.\n\nApply only [attachment:trac_6667_caruso_revised.patch] (it includes your review).",
    "created_at": "2013-08-27T20:26:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6667#issuecomment-54742",
    "user": "caruso"
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

archive/issue_comments_054743.json:
```json
{
    "body": "Attachment",
    "created_at": "2013-08-28T09:48:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6667#issuecomment-54743",
    "user": "chapoton"
}
```

Attachment



---

archive/issue_comments_054744.json:
```json
{
    "body": "apply only trac_6667_caruso_revised.patch",
    "created_at": "2013-08-29T07:43:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6667#issuecomment-54744",
    "user": "chapoton"
}
```

apply only trac_6667_caruso_revised.patch



---

archive/issue_comments_054745.json:
```json
{
    "body": "apply only trac_6667_caruso_revised.patch",
    "created_at": "2013-08-29T07:45:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6667#issuecomment-54745",
    "user": "chapoton"
}
```

apply only trac_6667_caruso_revised.patch



---

archive/issue_comments_054746.json:
```json
{
    "body": "ok, good to me. Positive review",
    "created_at": "2013-09-15T11:22:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6667#issuecomment-54746",
    "user": "chapoton"
}
```

ok, good to me. Positive review



---

archive/issue_comments_054747.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-09-15T11:22:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6667#issuecomment-54747",
    "user": "chapoton"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_054748.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2013-10-01T07:17:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6667#issuecomment-54748",
    "user": "jdemeyer"
}
```

Resolution: fixed
