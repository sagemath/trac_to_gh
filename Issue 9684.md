# Issue 9684: Make use of _tidy_model() optional

archive/issues_009684.json:
```json
{
    "body": "Assignee: @JohnCremona\n\nCC:  cturner beankao\n\nKeywords: local_data\n\nCurrently, local_data() after running Tate's algorithm always also calls _tidy_model().  The attached patch makes this behaviour optional by introducing a parameter tidy.  This functionality is needed for the implementation of ticket #9320.\n\n\n```\nsage: E = EllipticCurve([2, 1, 0, -2, -1])\nsage: E.local_data(ZZ.ideal(2), algorithm=\"generic\").minimal_model()\nElliptic Curve defined by y^2 = x^3 - x^2 - 3*x + 2 over Rational Field\nsage: E.local_data(ZZ.ideal(2), algorithm=\"generic\").minimal_model(tidy=False)\nElliptic Curve defined by y^2 + 2*x*y + 2*y = x^3 + x^2 - 4*x - 2 over Rational Field\n```\n\n\nSince Pari also does this \"tidying\", the patch needs to add the parameter algorithm to various functions.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9684\n\n",
    "created_at": "2010-08-04T05:14:25Z",
    "labels": [
        "component: elliptic curves",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "Make use of _tidy_model() optional",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9684",
    "user": "https://github.com/arminstraub"
}
```
Assignee: @JohnCremona

CC:  cturner beankao

Keywords: local_data

Currently, local_data() after running Tate's algorithm always also calls _tidy_model().  The attached patch makes this behaviour optional by introducing a parameter tidy.  This functionality is needed for the implementation of ticket #9320.


```
sage: E = EllipticCurve([2, 1, 0, -2, -1])
sage: E.local_data(ZZ.ideal(2), algorithm="generic").minimal_model()
Elliptic Curve defined by y^2 = x^3 - x^2 - 3*x + 2 over Rational Field
sage: E.local_data(ZZ.ideal(2), algorithm="generic").minimal_model(tidy=False)
Elliptic Curve defined by y^2 + 2*x*y + 2*y = x^3 + x^2 - 4*x - 2 over Rational Field
```


Since Pari also does this "tidying", the patch needs to add the parameter algorithm to various functions.

Issue created by migration from https://trac.sagemath.org/ticket/9684





---

archive/issue_comments_093981.json:
```json
{
    "body": "Attachment [9684_dirty_model.patch](tarball://root/attachments/some-uuid/ticket9684/9684_dirty_model.patch) by @arminstraub created at 2010-08-04 05:16:15",
    "created_at": "2010-08-04T05:16:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9684",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9684#issuecomment-93981",
    "user": "https://github.com/arminstraub"
}
```

Attachment [9684_dirty_model.patch](tarball://root/attachments/some-uuid/ticket9684/9684_dirty_model.patch) by @arminstraub created at 2010-08-04 05:16:15



---

archive/issue_comments_093982.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-04T05:19:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9684",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9684#issuecomment-93982",
    "user": "https://github.com/arminstraub"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_093983.json:
```json
{
    "body": "I will review this.  I'm afraid that I coined the phrase \"tidy model\", which I now regret.  It would be better, and consistent with other usage, to call this operation *reducing* the model.  Minimization and reduction are different things and so should be implemented independently.",
    "created_at": "2010-08-11T19:49:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9684",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9684#issuecomment-93983",
    "user": "https://github.com/JohnCremona"
}
```

I will review this.  I'm afraid that I coined the phrase "tidy model", which I now regret.  It would be better, and consistent with other usage, to call this operation *reducing* the model.  Minimization and reduction are different things and so should be implemented independently.



---

archive/issue_comments_093984.json:
```json
{
    "body": "Attachment [trac_9684-reviewer.patch](tarball://root/attachments/some-uuid/ticket9684/trac_9684-reviewer.patch) by @JohnCremona created at 2010-08-12 20:05:18\n\nApply after previous",
    "created_at": "2010-08-12T20:05:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9684",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9684#issuecomment-93984",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [trac_9684-reviewer.patch](tarball://root/attachments/some-uuid/ticket9684/trac_9684-reviewer.patch) by @JohnCremona created at 2010-08-12 20:05:18

Apply after previous



---

archive/issue_comments_093985.json:
```json
{
    "body": "The first patch is fine, applies to 4.5.3.alpha0 and tests pass.\n\nI added a second patch which **only** changes \"tidy\" to \"reduce\" as appropriate, which I think is better terminology.  If the original poster is happy with that, please mark the ticket \"positive review\".  If not, I'll still give the first patch a positive review.\n\nFor the future, there is an addition reduction step not yet implemented but useful (only non-trivial over number fields):  scale by [u,0,0,0] where u is a unit chosen so that the discriminant is in a sense minimal (minimal height modulo 12th powers of units).  But that is for another day.",
    "created_at": "2010-08-12T20:09:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9684",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9684#issuecomment-93985",
    "user": "https://github.com/JohnCremona"
}
```

The first patch is fine, applies to 4.5.3.alpha0 and tests pass.

I added a second patch which **only** changes "tidy" to "reduce" as appropriate, which I think is better terminology.  If the original poster is happy with that, please mark the ticket "positive review".  If not, I'll still give the first patch a positive review.

For the future, there is an addition reduction step not yet implemented but useful (only non-trivial over number fields):  scale by [u,0,0,0] where u is a unit chosen so that the discriminant is in a sense minimal (minimal height modulo 12th powers of units).  But that is for another day.



---

archive/issue_comments_093986.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-08-13T00:29:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9684",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9684#issuecomment-93986",
    "user": "https://github.com/arminstraub"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_093987.json:
```json
{
    "body": "Thank you for the review!\n\nYes, I'm happy with this renaming.  Even though we did enjoy your earlier terminology at the Sage Days ;)",
    "created_at": "2010-08-13T00:29:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9684",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9684#issuecomment-93987",
    "user": "https://github.com/arminstraub"
}
```

Thank you for the review!

Yes, I'm happy with this renaming.  Even though we did enjoy your earlier terminology at the Sage Days ;)



---

archive/issue_comments_093988.json:
```json
{
    "body": "Thanks.\n\nRelease manager:  please apply both patches.",
    "created_at": "2010-08-13T08:38:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9684",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9684#issuecomment-93988",
    "user": "https://github.com/JohnCremona"
}
```

Thanks.

Release manager:  please apply both patches.



---

archive/issue_events_009816.json:
```json
{
    "actor": "@qed777",
    "created_at": "2010-09-15T11:38:05Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9684",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9684#event-9816"
}
```



---

archive/issue_comments_093989.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-15T11:38:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9684",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9684#issuecomment-93989",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed
