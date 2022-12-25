# Issue 2418: pari polroots gives division by zero sometimes

archive/issues_002418.json:
```json
{
    "body": "Assignee: @williamstein\n\nI think the problem may be in how Sage calls polroots; in particular, I'm suspicious of the coercion from CC to pari.\n\n```\nsage: x = polygen(QQ)\nsage: p = (x^50/2^100 + x^10 + x + 1).change_ring(ComplexField(106))\nsage: len(p.roots())\n50\nsage: (p/2^100).roots()\n---------------------------------------------------------------------------\n<class 'sage.libs.pari.gen.PariError'>    Traceback (most recent call last)\n\n/home/cwitty/my-sage/<ipython console> in <module>()\n\n/home/cwitty/my-sage/polynomial_element.pyx in sage.rings.polynomial.polynomial_element.Polynomial.roots()\n\n/home/cwitty/my-sage/gen.pyx in sage.libs.pari.gen._pari_trap()\n\n<class 'sage.libs.pari.gen.PariError'>: division by zero (46)\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/2418\n\n",
    "created_at": "2008-03-07T05:01:20Z",
    "labels": [
        "component: interfaces",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "pari polroots gives division by zero sometimes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2418",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: @williamstein

I think the problem may be in how Sage calls polroots; in particular, I'm suspicious of the coercion from CC to pari.

```
sage: x = polygen(QQ)
sage: p = (x^50/2^100 + x^10 + x + 1).change_ring(ComplexField(106))
sage: len(p.roots())
50
sage: (p/2^100).roots()
---------------------------------------------------------------------------
<class 'sage.libs.pari.gen.PariError'>    Traceback (most recent call last)

/home/cwitty/my-sage/<ipython console> in <module>()

/home/cwitty/my-sage/polynomial_element.pyx in sage.rings.polynomial.polynomial_element.Polynomial.roots()

/home/cwitty/my-sage/gen.pyx in sage.libs.pari.gen._pari_trap()

<class 'sage.libs.pari.gen.PariError'>: division by zero (46)
```

Issue created by migration from https://trac.sagemath.org/ticket/2418





---

archive/issue_comments_016269.json:
```json
{
    "body": "Actually, this is really just pari giving us an error: \n\n```\n? fp\n%4 = (6.223015277861140000000000000 E-61 + 0.E-38*I)*x^50 + (0.E-38 + 0.E-38*I)*x^49 + (0.E-38 + 0.E-38*I)*x^48 + (0.E-38 + 0.E-38*I)*x^47 + (0.E-38 + 0.E-38*I)*x^46 + (0.E-38 + 0.E-38*I)*x^45 + (0.E-38 + 0.E-38*I)*x^44 + (0.E-38 + 0.E-38*I)*x^43 + (0.E-38 + 0.E-38*I)*x^42 + (0.E-38 + 0.E-38*I)*x^41 + (0.E-38 + 0.E-38*I)*x^40 + (0.E-38 + 0.E-38*I)*x^39 + (0.E-38 + 0.E-38*I)*x^38 + (0.E-38 + 0.E-38*I)*x^37 + (0.E-38 + 0.E-38*I)*x^36 + (0.E-38 + 0.E-38*I)*x^35 + (0.E-38 + 0.E-38*I)*x^34 + (0.E-38 + 0.E-38*I)*x^33 + (0.E-38 + 0.E-38*I)*x^32 + (0.E-38 + 0.E-38*I)*x^31 + (0.E-38 + 0.E-38*I)*x^30 + (0.E-38 + 0.E-38*I)*x^29 + (0.E-38 + 0.E-38*I)*x^28 + (0.E-38 + 0.E-38*I)*x^27 + (0.E-38 + 0.E-38*I)*x^26 + (0.E-38 + 0.E-38*I)*x^25 + (0.E-38 + 0.E-38*I)*x^24 + (0.E-38 + 0.E-38*I)*x^23 + (0.E-38 + 0.E-38*I)*x^22 + (0.E-38 + 0.E-38*I)*x^21 + (0.E-38 + 0.E-38*I)*x^20 + (0.E-38 + 0.E-38*I)*x^19 + (0.E-38 + 0.E-38*I)*x^18 + (0.E-38 + 0.E-38*I)*x^17 + (0.E-38 + 0.E-38*I)*x^16 + (0.E-38 + 0.E-38*I)*x^15 + (0.E-38 + 0.E-38*I)*x^14 + (0.E-38 + 0.E-38*I)*x^13 + (0.E-38 + 0.E-38*I)*x^12 + (0.E-38 + 0.E-38*I)*x^11 + (7.888609052210120000000000000 E-31 + 0.E-38*I)*x^10 + (0.E-38 + 0.E-38*I)*x^9 + (0.E-38 + 0.E-38*I)*x^8 + (0.E-38 + 0.E-38*I)*x^7 + (0.E-38 + 0.E-38*I)*x^6 + (0.E-38 + 0.E-38*I)*x^5 + (0.E-38 + 0.E-38*I)*x^4 + (0.E-38 + 0.E-38*I)*x^3 + (0.E-38 + 0.E-38*I)*x^2 + (7.888609052210120000000000000 E-31 + 0.E-38*I)*x + (7.888609052210120000000000000 E-31 + 0.E-38*I)\n? polroots(fp)\n  *** polroots: division by zero\n```\n\nI think that makes this ticket invalid ... Carl, does that seem reasonable to you? In particular, do you have any code you've written that we might fall back on if Pari fails like this?",
    "created_at": "2009-01-23T13:09:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2418#issuecomment-16269",
    "user": "https://github.com/craigcitro"
}
```

Actually, this is really just pari giving us an error: 

```
? fp
%4 = (6.223015277861140000000000000 E-61 + 0.E-38*I)*x^50 + (0.E-38 + 0.E-38*I)*x^49 + (0.E-38 + 0.E-38*I)*x^48 + (0.E-38 + 0.E-38*I)*x^47 + (0.E-38 + 0.E-38*I)*x^46 + (0.E-38 + 0.E-38*I)*x^45 + (0.E-38 + 0.E-38*I)*x^44 + (0.E-38 + 0.E-38*I)*x^43 + (0.E-38 + 0.E-38*I)*x^42 + (0.E-38 + 0.E-38*I)*x^41 + (0.E-38 + 0.E-38*I)*x^40 + (0.E-38 + 0.E-38*I)*x^39 + (0.E-38 + 0.E-38*I)*x^38 + (0.E-38 + 0.E-38*I)*x^37 + (0.E-38 + 0.E-38*I)*x^36 + (0.E-38 + 0.E-38*I)*x^35 + (0.E-38 + 0.E-38*I)*x^34 + (0.E-38 + 0.E-38*I)*x^33 + (0.E-38 + 0.E-38*I)*x^32 + (0.E-38 + 0.E-38*I)*x^31 + (0.E-38 + 0.E-38*I)*x^30 + (0.E-38 + 0.E-38*I)*x^29 + (0.E-38 + 0.E-38*I)*x^28 + (0.E-38 + 0.E-38*I)*x^27 + (0.E-38 + 0.E-38*I)*x^26 + (0.E-38 + 0.E-38*I)*x^25 + (0.E-38 + 0.E-38*I)*x^24 + (0.E-38 + 0.E-38*I)*x^23 + (0.E-38 + 0.E-38*I)*x^22 + (0.E-38 + 0.E-38*I)*x^21 + (0.E-38 + 0.E-38*I)*x^20 + (0.E-38 + 0.E-38*I)*x^19 + (0.E-38 + 0.E-38*I)*x^18 + (0.E-38 + 0.E-38*I)*x^17 + (0.E-38 + 0.E-38*I)*x^16 + (0.E-38 + 0.E-38*I)*x^15 + (0.E-38 + 0.E-38*I)*x^14 + (0.E-38 + 0.E-38*I)*x^13 + (0.E-38 + 0.E-38*I)*x^12 + (0.E-38 + 0.E-38*I)*x^11 + (7.888609052210120000000000000 E-31 + 0.E-38*I)*x^10 + (0.E-38 + 0.E-38*I)*x^9 + (0.E-38 + 0.E-38*I)*x^8 + (0.E-38 + 0.E-38*I)*x^7 + (0.E-38 + 0.E-38*I)*x^6 + (0.E-38 + 0.E-38*I)*x^5 + (0.E-38 + 0.E-38*I)*x^4 + (0.E-38 + 0.E-38*I)*x^3 + (0.E-38 + 0.E-38*I)*x^2 + (7.888609052210120000000000000 E-31 + 0.E-38*I)*x + (7.888609052210120000000000000 E-31 + 0.E-38*I)
? polroots(fp)
  *** polroots: division by zero
```

I think that makes this ticket invalid ... Carl, does that seem reasonable to you? In particular, do you have any code you've written that we might fall back on if Pari fails like this?



---

archive/issue_comments_016270.json:
```json
{
    "body": "I certainly don't think the ticket is invalid; it's definitely a bug in Sage (via Pari), even if it's not a bug in the Sage library code.\n\nFor this example, it presumably works to divide through by the leading coefficient (to get a monic polynomial) before handing off to Pari.  Maybe that's a reasonable strategy in general?\n\nOr, we could just report it as a bug to Pari upstream, and hope they fix it.",
    "created_at": "2009-01-23T20:59:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2418#issuecomment-16270",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

I certainly don't think the ticket is invalid; it's definitely a bug in Sage (via Pari), even if it's not a bug in the Sage library code.

For this example, it presumably works to divide through by the leading coefficient (to get a monic polynomial) before handing off to Pari.  Maybe that's a reasonable strategy in general?

Or, we could just report it as a bug to Pari upstream, and hope they fix it.



---

archive/issue_comments_016271.json:
```json
{
    "body": "I've followed Carl's suggestion -- see the attached patch.",
    "created_at": "2010-01-03T06:47:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2418#issuecomment-16271",
    "user": "https://github.com/aghitza"
}
```

I've followed Carl's suggestion -- see the attached patch.



---

archive/issue_comments_016272.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-03T06:47:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2418#issuecomment-16272",
    "user": "https://github.com/aghitza"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_016273.json:
```json
{
    "body": "Attachment [trac_2418.patch](tarball://root/attachments/some-uuid/ticket2418/trac_2418.patch) by @aghitza created at 2010-01-03 06:48:10",
    "created_at": "2010-01-03T06:48:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2418#issuecomment-16273",
    "user": "https://github.com/aghitza"
}
```

Attachment [trac_2418.patch](tarball://root/attachments/some-uuid/ticket2418/trac_2418.patch) by @aghitza created at 2010-01-03 06:48:10



---

archive/issue_comments_016274.json:
```json
{
    "body": "Positive review.  The patch applies to 4.3 and all tests in rings/polynomial pass.",
    "created_at": "2010-01-06T16:37:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2418#issuecomment-16274",
    "user": "https://github.com/JohnCremona"
}
```

Positive review.  The patch applies to 4.3 and all tests in rings/polynomial pass.



---

archive/issue_comments_016275.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-06T16:37:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2418#issuecomment-16275",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_016276.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-01-13T10:50:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2418#issuecomment-16276",
    "user": "https://github.com/rlmill"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_016277.json:
```json
{
    "body": "```\npatching file sage/rings/polynomial/polynomial_element.pyx\nHunk #1 FAILED at 4281\n1 out of 2 hunks FAILED -- saving rejects to file sage/rings/polynomial/polynomial_element.pyx.rej\npatch failed, unable to continue (try -v)\npatch failed, rejects left in working dir\nerrors during apply, please fix and refresh trac_2418.patch\n```",
    "created_at": "2010-01-13T10:50:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2418#issuecomment-16277",
    "user": "https://github.com/rlmill"
}
```

```
patching file sage/rings/polynomial/polynomial_element.pyx
Hunk #1 FAILED at 4281
1 out of 2 hunks FAILED -- saving rejects to file sage/rings/polynomial/polynomial_element.pyx.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh trac_2418.patch
```



---

archive/issue_comments_016278.json:
```json
{
    "body": "Robert,\n\nThe merging failure is due to the fact that this patch touches the same code as #6237, which just got merged (thank you!).  It is a trivial rebase job, and I am attaching the rebased version.  I kept the old version around so you can see that no other changes were made.\n\nI'm not sure what the protocol is here.  I'd normally go from needs_work to needs_review, but this doesn't really need review...",
    "created_at": "2010-01-13T11:23:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2418#issuecomment-16278",
    "user": "https://github.com/aghitza"
}
```

Robert,

The merging failure is due to the fact that this patch touches the same code as #6237, which just got merged (thank you!).  It is a trivial rebase job, and I am attaching the rebased version.  I kept the old version around so you can see that no other changes were made.

I'm not sure what the protocol is here.  I'd normally go from needs_work to needs_review, but this doesn't really need review...



---

archive/issue_comments_016279.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-13T11:23:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2418#issuecomment-16279",
    "user": "https://github.com/aghitza"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_016280.json:
```json
{
    "body": "rebased on 4.3.1.alpha1 and #6237, apply instead of the previous patch",
    "created_at": "2010-01-13T11:23:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2418#issuecomment-16280",
    "user": "https://github.com/aghitza"
}
```

rebased on 4.3.1.alpha1 and #6237, apply instead of the previous patch



---

archive/issue_comments_016281.json:
```json
{
    "body": "Attachment [trac_2418-rebased.patch](tarball://root/attachments/some-uuid/ticket2418/trac_2418-rebased.patch) by @JohnCremona created at 2010-01-13 11:47:31\n\nI checked that this applies fine on top of 4.3.1.alpha1 + #6237, and tests pass, so positive review.",
    "created_at": "2010-01-13T11:47:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2418#issuecomment-16281",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [trac_2418-rebased.patch](tarball://root/attachments/some-uuid/ticket2418/trac_2418-rebased.patch) by @JohnCremona created at 2010-01-13 11:47:31

I checked that this applies fine on top of 4.3.1.alpha1 + #6237, and tests pass, so positive review.



---

archive/issue_comments_016282.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-13T11:47:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2418#issuecomment-16282",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_016283.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-14T08:00:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2418#issuecomment-16283",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed



---

archive/issue_events_005702.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2010-01-14T08:00:30Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2418",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2418#event-5702"
}
```
