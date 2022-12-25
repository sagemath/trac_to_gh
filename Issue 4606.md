# Issue 4606: elliptic curves -- implement gross-Zagier L-functions

archive/issues_004606.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @williamstein @craigcitro @categorie\n\nMake it so one can do:\n\n```\nsage: e = EllipticCurve('37a')\nsage: K.<a> = QuadraticField(-40)\nsage: A = K.class_group().gen(0); A\nFractional ideal class (2, -1/2*a)\nsage: L = e.lseries_gross_zagier(A)  \nsage: L(2)\n0\nsage: L.taylor_series(2,5)\nnobody has seen this!\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/4606\n\n",
    "created_at": "2008-11-24T22:59:03Z",
    "labels": [
        "component: number theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.8",
    "title": "elliptic curves -- implement gross-Zagier L-functions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4606",
    "user": "https://github.com/robertwb"
}
```
Assignee: @williamstein

CC:  @williamstein @craigcitro @categorie

Make it so one can do:

```
sage: e = EllipticCurve('37a')
sage: K.<a> = QuadraticField(-40)
sage: A = K.class_group().gen(0); A
Fractional ideal class (2, -1/2*a)
sage: L = e.lseries_gross_zagier(A)  
sage: L(2)
0
sage: L.taylor_series(2,5)
nobody has seen this!
```

Issue created by migration from https://trac.sagemath.org/ticket/4606





---

archive/issue_comments_034463.json:
```json
{
    "body": "Attachment [4606-gz-lseries.patch](tarball://root/attachments/some-uuid/ticket4606/4606-gz-lseries.patch) by @robertwb created at 2008-11-25 06:44:02",
    "created_at": "2008-11-25T06:44:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4606#issuecomment-34463",
    "user": "https://github.com/robertwb"
}
```

Attachment [4606-gz-lseries.patch](tarball://root/attachments/some-uuid/ticket4606/4606-gz-lseries.patch) by @robertwb created at 2008-11-25 06:44:02



---

archive/issue_comments_034464.json:
```json
{
    "body": "Still going to add some doctests right now, but here's the code. Note, however, the check \\sum_A L_A(E,s) = L(E/K,s) fails. :(",
    "created_at": "2008-11-25T06:46:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4606#issuecomment-34464",
    "user": "https://github.com/robertwb"
}
```

Still going to add some doctests right now, but here's the code. Note, however, the check \sum_A L_A(E,s) = L(E/K,s) fails. :(



---

archive/issue_comments_034465.json:
```json
{
    "body": "Attachment [4606-gz-doctests.patch](tarball://root/attachments/some-uuid/ticket4606/4606-gz-doctests.patch) by @robertwb created at 2008-11-25 08:17:14",
    "created_at": "2008-11-25T08:17:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4606#issuecomment-34465",
    "user": "https://github.com/robertwb"
}
```

Attachment [4606-gz-doctests.patch](tarball://root/attachments/some-uuid/ticket4606/4606-gz-doctests.patch) by @robertwb created at 2008-11-25 08:17:14



---

archive/issue_comments_034466.json:
```json
{
    "body": "Attachment [trac-4606-pt3.patch](tarball://root/attachments/some-uuid/ticket4606/trac-4606-pt3.patch) by @craigcitro created at 2008-11-28 11:10:18",
    "created_at": "2008-11-28T11:10:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4606#issuecomment-34466",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac-4606-pt3.patch](tarball://root/attachments/some-uuid/ticket4606/trac-4606-pt3.patch) by @craigcitro created at 2008-11-28 11:10:18



---

archive/issue_comments_034467.json:
```json
{
    "body": "So I've attached a patch, which at least fixes a few issues. This patch fixes two definite bugs:\n\n* In `E.lseries_gross_zagier(A)`, you were caching the value -- no matter what value of `A` was getting passed in! That was an easy fix. :) Unfortunately, after fixing that, there were still issues. \n\n* There was a subtle issue in `I.quadratic_form()`, for `I` an ideal in a quadratic number field. For instance, with just the first two patches above, taking `K = QuadraticField(-40)` and `I` the trivial element in the class group, the code returned `x^2 + 40*y^2` for `I.quadratic_form()`. The underlying issue was one of choice of generators: you were using `K.gen()` where you really needed `K.ring_of_integers().gen()`, because you needed to know that something generated all of `I` over `ZZ`, not just `QQ`. I'm **fairly** certain that the current code is correct, but it's after 2AM, so someone should double check me. \n\nSo, now that those are fixed, we go back to the example Robert points out in the code: \n\n```\nsage: E = EllipticCurve('37a')\nsage: K.<a> = QuadraticField(-40)\nsage: A = K.class_group().gen(0)\nsage: L = E.lseries_gross_zagier(A)\nsage: LL = E.lseries_gross_zagier(A**2)\nsage: L(2) + LL(2)\n0.506799279512368\n\nsage: E.lseries()(2) * E.quadratic_twist(-40).lseries()(2)\n0.502803417587467\n```\n\nSo we're now quite close. In particular, I wonder if there isn't rounding going on:\n\n```\nsage: E.lseries().taylor_series(2,5) * E.quadratic_twist(-40).lseries().taylor_series(2,5)\n0.50 + 0.38*z - 0.16*z^2 + 0.0078*z^3 + 0.070*z^4 - 0.039*z^5 + O(z^6)\n```\n\nThat definitely seems to suggest small precision to me. In any event, we're getting close:\n\n```\nsage: L.taylor_series(2,5) + LL.taylor_series(2,5)\n0.506799279512368 + 0.360199571567893*z - 0.122141848388581*z^2 - 0.00635398874570253*z^3 + 0.0383995215484257*z^4 + O(z^5)\n\nsage: L.taylor_series(2,5) + LL.taylor_series(2,5) - (E.lseries().taylor_series(2,5) * E.quadratic_twist(-40).lseries().taylor_series(2,5))\n-0.016*z + 0.035*z^2 - 0.014*z^3 - 0.031*z^4 + O(z^5)\n```\n\nI'll cook up a few more examples and post what I find.",
    "created_at": "2008-11-28T11:38:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4606#issuecomment-34467",
    "user": "https://github.com/craigcitro"
}
```

So I've attached a patch, which at least fixes a few issues. This patch fixes two definite bugs:

* In `E.lseries_gross_zagier(A)`, you were caching the value -- no matter what value of `A` was getting passed in! That was an easy fix. :) Unfortunately, after fixing that, there were still issues. 

* There was a subtle issue in `I.quadratic_form()`, for `I` an ideal in a quadratic number field. For instance, with just the first two patches above, taking `K = QuadraticField(-40)` and `I` the trivial element in the class group, the code returned `x^2 + 40*y^2` for `I.quadratic_form()`. The underlying issue was one of choice of generators: you were using `K.gen()` where you really needed `K.ring_of_integers().gen()`, because you needed to know that something generated all of `I` over `ZZ`, not just `QQ`. I'm **fairly** certain that the current code is correct, but it's after 2AM, so someone should double check me. 

So, now that those are fixed, we go back to the example Robert points out in the code: 

```
sage: E = EllipticCurve('37a')
sage: K.<a> = QuadraticField(-40)
sage: A = K.class_group().gen(0)
sage: L = E.lseries_gross_zagier(A)
sage: LL = E.lseries_gross_zagier(A**2)
sage: L(2) + LL(2)
0.506799279512368

sage: E.lseries()(2) * E.quadratic_twist(-40).lseries()(2)
0.502803417587467
```

So we're now quite close. In particular, I wonder if there isn't rounding going on:

```
sage: E.lseries().taylor_series(2,5) * E.quadratic_twist(-40).lseries().taylor_series(2,5)
0.50 + 0.38*z - 0.16*z^2 + 0.0078*z^3 + 0.070*z^4 - 0.039*z^5 + O(z^6)
```

That definitely seems to suggest small precision to me. In any event, we're getting close:

```
sage: L.taylor_series(2,5) + LL.taylor_series(2,5)
0.506799279512368 + 0.360199571567893*z - 0.122141848388581*z^2 - 0.00635398874570253*z^3 + 0.0383995215484257*z^4 + O(z^5)

sage: L.taylor_series(2,5) + LL.taylor_series(2,5) - (E.lseries().taylor_series(2,5) * E.quadratic_twist(-40).lseries().taylor_series(2,5))
-0.016*z + 0.035*z^2 - 0.014*z^3 - 0.031*z^4 + O(z^5)
```

I'll cook up a few more examples and post what I find.



---

archive/issue_comments_034468.json:
```json
{
    "body": "Excellent. That's looking very good. I was very tired the day I was finishing that up, so I'm glad you caught these errors.",
    "created_at": "2008-11-28T18:12:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4606#issuecomment-34468",
    "user": "https://github.com/robertwb"
}
```

Excellent. That's looking very good. I was very tired the day I was finishing that up, so I'm glad you caught these errors.



---

archive/issue_comments_034469.json:
```json
{
    "body": "Replying to [comment:3 robertwb]:\n> Excellent. That's looking very good. I was very tired the day I was finishing that up, so I'm glad you caught these errors. \n\n\nShould this ticker be \"[with patch, needs review]\" ? \n\nCheers,\n\nMichael",
    "created_at": "2008-11-28T18:25:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4606#issuecomment-34469",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:3 robertwb]:
> Excellent. That's looking very good. I was very tired the day I was finishing that up, so I'm glad you caught these errors. 


Should this ticker be "[with patch, needs review]" ? 

Cheers,

Michael



---

archive/issue_comments_034470.json:
```json
{
    "body": "No, I don't think so yet (but if Craig is happy with it, then sure).",
    "created_at": "2008-11-28T18:28:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4606#issuecomment-34470",
    "user": "https://github.com/robertwb"
}
```

No, I don't think so yet (but if Craig is happy with it, then sure).



---

archive/issue_comments_034471.json:
```json
{
    "body": "Changing assignee from @williamstein to @loefflerd.",
    "created_at": "2009-07-20T19:50:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4606#issuecomment-34471",
    "user": "https://github.com/loefflerd"
}
```

Changing assignee from @williamstein to @loefflerd.



---

archive/issue_comments_034472.json:
```json
{
    "body": "Changing component from number theory to elliptic curves.",
    "created_at": "2009-07-20T19:50:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4606#issuecomment-34472",
    "user": "https://github.com/loefflerd"
}
```

Changing component from number theory to elliptic curves.



---

archive/issue_comments_034473.json:
```json
{
    "body": "Remove assignee @loefflerd.",
    "created_at": "2009-10-09T09:12:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4606#issuecomment-34473",
    "user": "https://github.com/loefflerd"
}
```

Remove assignee @loefflerd.



---

archive/issue_events_010462.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4606",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4606#event-10462"
}
```



---

archive/issue_comments_034474.json:
```json
{
    "body": "for the **patchbots**:\n\napply only trac_4606_gross_zagier_lseries_rebased.patch",
    "created_at": "2013-09-19T19:54:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4606#issuecomment-34474",
    "user": "https://github.com/fchapoton"
}
```

for the **patchbots**:

apply only trac_4606_gross_zagier_lseries_rebased.patch



---

archive/issue_comments_034475.json:
```json
{
    "body": "Attachment [trac_4606_gross_zagier_lseries_rebased.patch](tarball://root/attachments/some-uuid/ticket4606/trac_4606_gross_zagier_lseries_rebased.patch) by @fchapoton created at 2013-09-20 16:09:19\n\nfolded all three patches and rebased on 5.12.beta5",
    "created_at": "2013-09-20T16:09:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4606#issuecomment-34475",
    "user": "https://github.com/fchapoton"
}
```

Attachment [trac_4606_gross_zagier_lseries_rebased.patch](tarball://root/attachments/some-uuid/ticket4606/trac_4606_gross_zagier_lseries_rebased.patch) by @fchapoton created at 2013-09-20 16:09:19

folded all three patches and rebased on 5.12.beta5



---

archive/issue_comments_034476.json:
```json
{
    "body": "apply trac_4606_gross_zagier_lseries_rebased.patch",
    "created_at": "2013-10-15T19:25:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4606#issuecomment-34476",
    "user": "https://github.com/fchapoton"
}
```

apply trac_4606_gross_zagier_lseries_rebased.patch



---

archive/issue_comments_034477.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2014-01-09T19:34:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4606#issuecomment-34477",
    "user": "https://github.com/fchapoton"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_034478.json:
```json
{
    "body": "New commits:",
    "created_at": "2014-01-09T19:34:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4606#issuecomment-34478",
    "user": "https://github.com/fchapoton"
}
```

New commits:



---

archive/issue_comments_034479.json:
```json
{
    "body": "Changing status from needs_info to needs_work.",
    "created_at": "2014-01-09T19:35:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4606#issuecomment-34479",
    "user": "https://github.com/fchapoton"
}
```

Changing status from needs_info to needs_work.



---

archive/issue_events_010463.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4606",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4606#event-10463"
}
```



---

archive/issue_events_010464.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4606",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4606#event-10464"
}
```



---

archive/issue_events_010465.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4606",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4606#event-10465"
}
```



---

archive/issue_events_010466.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4606",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4606#event-10466"
}
```



---

archive/issue_events_010467.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4606",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4606#event-10467"
}
```



---

archive/issue_events_010468.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4606",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4606#event-10468"
}
```



---

archive/issue_comments_034480.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-04-25T16:21:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4606#issuecomment-34480",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_events_010469.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2015-04-26T07:18:38Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4606",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4606#event-10469"
}
```



---

archive/issue_events_010470.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2015-04-26T07:18:38Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4606",
    "milestone": "sage-6.7",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4606#event-10470"
}
```



---

archive/issue_comments_034481.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-04-26T07:54:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4606#issuecomment-34481",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_034482.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-05-01T19:54:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4606#issuecomment-34482",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_034483.json:
```json
{
    "body": "It seems that the Dirichlet coefficients of\n\n- the product of Dirichlet series for E and its twists\n- the sum of Dirichlet series for (E,A) over all classes A\n\ndo not quite exactly match. I have not been able to locate the error so far. It could be either in the quadratic form code implemented here or elsewhere. Quadratic forms theta series should be checked against the generic implementation of theta series.",
    "created_at": "2015-05-02T07:32:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4606#issuecomment-34483",
    "user": "https://github.com/fchapoton"
}
```

It seems that the Dirichlet coefficients of

- the product of Dirichlet series for E and its twists
- the sum of Dirichlet series for (E,A) over all classes A

do not quite exactly match. I have not been able to locate the error so far. It could be either in the quadratic form code implemented here or elsewhere. Quadratic forms theta series should be checked against the generic implementation of theta series.



---

archive/issue_comments_034484.json:
```json
{
    "body": "Apparently, the theta series is good (but slower than the generic implementation).\n\nSo the problem must be in the Dirichlet convolution code",
    "created_at": "2015-05-02T07:40:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4606#issuecomment-34484",
    "user": "https://github.com/fchapoton"
}
```

Apparently, the theta series is good (but slower than the generic implementation).

So the problem must be in the Dirichlet convolution code



---

archive/issue_comments_034485.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-05-02T14:00:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4606#issuecomment-34485",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_034486.json:
```json
{
    "body": "Hum, here is the current state of affairs:\n\n```\nsage: E = EllipticCurve('37a')\nsage: K.<a> = QuadraticField(-40)\nsage: A = K.class_group().gen(0)\nsage: L = E.lseries_gross_zagier(A)\nsage: LL = E.lseries_gross_zagier(A**2)\nsage: L(2) + LL(2)\n0.506799279512368\nsage: E.lseries()(2) * E.quadratic_twist(-40).lseries()(2)\n0.502803417587467\n```\nNot so good, in fact. Now let us compare Taylor expansions:\n\n```\nsage: L.taylor_series(2, 5)+LL.taylor_series(2, 5)\n0.506799279512368 + 0.360199571567893*z - 0.122141848388581*z^2 - 0.00635398874570253*z^3 + 0.0383995215484257*z^4 + O(z^5)\nsage: E.lseries().taylor_series(2,series_prec=5) * E.quadratic_twist(-40).lseries().taylor_series(2,series_prec=5)\n0.502803417587467 + 0.374948906665456*z - 0.144641137632262*z^2 + 0.00702138852027905*z^3 + 0.0487513598755609*z^4 + O(z^5)\n```\nNot far, but definitely not good. Note that the syntax of taylor expansion differs.",
    "created_at": "2015-05-02T14:22:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4606#issuecomment-34486",
    "user": "https://github.com/fchapoton"
}
```

Hum, here is the current state of affairs:

```
sage: E = EllipticCurve('37a')
sage: K.<a> = QuadraticField(-40)
sage: A = K.class_group().gen(0)
sage: L = E.lseries_gross_zagier(A)
sage: LL = E.lseries_gross_zagier(A**2)
sage: L(2) + LL(2)
0.506799279512368
sage: E.lseries()(2) * E.quadratic_twist(-40).lseries()(2)
0.502803417587467
```
Not so good, in fact. Now let us compare Taylor expansions:

```
sage: L.taylor_series(2, 5)+LL.taylor_series(2, 5)
0.506799279512368 + 0.360199571567893*z - 0.122141848388581*z^2 - 0.00635398874570253*z^3 + 0.0383995215484257*z^4 + O(z^5)
sage: E.lseries().taylor_series(2,series_prec=5) * E.quadratic_twist(-40).lseries().taylor_series(2,series_prec=5)
0.502803417587467 + 0.374948906665456*z - 0.144641137632262*z^2 + 0.00702138852027905*z^3 + 0.0487513598755609*z^4 + O(z^5)
```
Not far, but definitely not good. Note that the syntax of taylor expansion differs.



---

archive/issue_comments_034487.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-05-02T16:01:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4606#issuecomment-34487",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_034488.json:
```json
{
    "body": "I think that I have checked fully the computation of the Dirichet coefficients.\n\nSo well... maybe something is wrong in the parameters given to Dokchitser program ?\n\n```\nsage: e = EllipticCurve('37a')\nsage: K.<a> = QuadraticField(-40)\nsage: A = K.class_group().gen(0)\nsage: from sage.modular.modform.l_series import GrossZagierLseries\nsage: G = GrossZagierLseries(e, A)\nsage: G._dokchister.check_functional_equation()\n-80.1679727952639\nsage: G = GrossZagierLseries(e, A**2)\nsage: G._dokchister.check_functional_equation()\n47.5616711441054\n```",
    "created_at": "2015-05-02T16:23:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4606#issuecomment-34488",
    "user": "https://github.com/fchapoton"
}
```

I think that I have checked fully the computation of the Dirichet coefficients.

So well... maybe something is wrong in the parameters given to Dokchitser program ?

```
sage: e = EllipticCurve('37a')
sage: K.<a> = QuadraticField(-40)
sage: A = K.class_group().gen(0)
sage: from sage.modular.modform.l_series import GrossZagierLseries
sage: G = GrossZagierLseries(e, A)
sage: G._dokchister.check_functional_equation()
-80.1679727952639
sage: G = GrossZagierLseries(e, A**2)
sage: G._dokchister.check_functional_equation()
47.5616711441054
```



---

archive/issue_comments_034489.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-05-02T18:23:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4606#issuecomment-34489",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_034490.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-05-02T18:29:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4606#issuecomment-34490",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_034491.json:
```json
{
    "body": "This is now working\n\n```\nsage: sage: e = EllipticCurve('37a')\nsage: sage: K.<a> = QuadraticField(-40)\nsage: sage: A = K.class_group().gen(0)\nsage: sage: from sage.modular.modform.l_series import GrossZagierLseries\nsage: sage: G = GrossZagierLseries(e, A)\nsage: sage: G._dokchister.check_functional_equation()\n2.77555756156289e-17\nsage: sage: G = GrossZagierLseries(e, A**2)\nsage: sage: G._dokchister.check_functional_equation()\n-3.64291929955129e-17\n```\nAfter six years !",
    "created_at": "2015-05-02T18:53:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4606#issuecomment-34491",
    "user": "https://github.com/fchapoton"
}
```

This is now working

```
sage: sage: e = EllipticCurve('37a')
sage: sage: K.<a> = QuadraticField(-40)
sage: sage: A = K.class_group().gen(0)
sage: sage: from sage.modular.modform.l_series import GrossZagierLseries
sage: sage: G = GrossZagierLseries(e, A)
sage: sage: G._dokchister.check_functional_equation()
2.77555756156289e-17
sage: sage: G = GrossZagierLseries(e, A**2)
sage: sage: G._dokchister.check_functional_equation()
-3.64291929955129e-17
```
After six years !



---

archive/issue_comments_034492.json:
```json
{
    "body": "Congratulations! I will look at it, but at the moment I am rebuilding with #18340 (new Pari version), and this should surely be tested on top of that?",
    "created_at": "2015-05-02T19:03:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4606#issuecomment-34492",
    "user": "https://github.com/JohnCremona"
}
```

Congratulations! I will look at it, but at the moment I am rebuilding with #18340 (new Pari version), and this should surely be tested on top of that?



---

archive/issue_comments_034493.json:
```json
{
    "body": "I just wrote a report which trac swallowed and deleted as I was not logged in.  I am not going to rewrite it!  More after I have done some more testing.",
    "created_at": "2015-05-04T12:04:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4606#issuecomment-34493",
    "user": "https://github.com/JohnCremona"
}
```

I just wrote a report which trac swallowed and deleted as I was not logged in.  I am not going to rewrite it!  More after I have done some more testing.



---

archive/issue_comments_034494.json:
```json
{
    "body": "Why is this not \"needs review\"?",
    "created_at": "2015-05-04T12:05:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4606#issuecomment-34494",
    "user": "https://github.com/JohnCremona"
}
```

Why is this not "needs review"?



---

archive/issue_comments_034495.json:
```json
{
    "body": "I see some remaining things that should be done:\n\n- maybe use the generic theta function code if it is faster than the one provided here for binary quadratic forms (as it seems to be)\n\n- make sure that the syntax is similar to the other L-functions we have\n\n- test with many curves and many quadratic number fields\n\n- have an expert say something about the conductor. I changed it using my very small understanding of Dokchister parameters and it worked. But I am not very sure if it is the right answer for all curves and all fields.",
    "created_at": "2015-05-04T12:14:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4606#issuecomment-34495",
    "user": "https://github.com/fchapoton"
}
```

I see some remaining things that should be done:

- maybe use the generic theta function code if it is faster than the one provided here for binary quadratic forms (as it seems to be)

- make sure that the syntax is similar to the other L-functions we have

- test with many curves and many quadratic number fields

- have an expert say something about the conductor. I changed it using my very small understanding of Dokchister parameters and it worked. But I am not very sure if it is the right answer for all curves and all fields.



---

archive/issue_comments_034496.json:
```json
{
    "body": "Replying to [comment:33 chapoton]:\n> I see some remaining things that should be done:\n> \n> - maybe use the generic theta function code if it is faster than the one provided here for binary quadratic forms (as it seems to be)\n\n\nSurely such a possible improvement can be noted for later work, and not delay this?\n\n> \n> - make sure that the syntax is similar to the other L-functions we have\n\n\nGood point.  \n\n> \n> - test with many curves and many quadratic number fields\n \n>\n\nI tested with one curve and many fields.  This led to the one suggestion I have:\n\n- somewhere, perhaps in the constructor for GrossZagierLseries, test that the ideal class is associated to an imaginary quadratic field.  If you construct it from an ideal in a real quadratic field there is a resulting error in the quadratic forms code, and this should be more graceful.\n\nJohn\n \n> - have an expert say something about the conductor. I changed it using my very small understanding of Dokchister parameters and it worked. But I am not very sure if it is the right answer for all curves and all fields.",
    "created_at": "2015-05-04T13:33:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4606#issuecomment-34496",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:33 chapoton]:
> I see some remaining things that should be done:
> 
> - maybe use the generic theta function code if it is faster than the one provided here for binary quadratic forms (as it seems to be)


Surely such a possible improvement can be noted for later work, and not delay this?

> 
> - make sure that the syntax is similar to the other L-functions we have


Good point.  

> 
> - test with many curves and many quadratic number fields
 
>

I tested with one curve and many fields.  This led to the one suggestion I have:

- somewhere, perhaps in the constructor for GrossZagierLseries, test that the ideal class is associated to an imaginary quadratic field.  If you construct it from an ideal in a real quadratic field there is a resulting error in the quadratic forms code, and this should be more graceful.

John
 
> - have an expert say something about the conductor. I changed it using my very small understanding of Dokchister parameters and it worked. But I am not very sure if it is the right answer for all curves and all fields.



---

archive/issue_comments_034497.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-05-04T15:10:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4606#issuecomment-34497",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_034498.json:
```json
{
    "body": "Thanks for the IQF patch.\nWe should have someone look at the conductor though.  I won't have time (and would have to look things up for sure). Who?",
    "created_at": "2015-05-04T16:46:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4606#issuecomment-34498",
    "user": "https://github.com/JohnCremona"
}
```

Thanks for the IQF patch.
We should have someone look at the conductor though.  I won't have time (and would have to look things up for sure). Who?



---

archive/issue_comments_034499.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-05-04T19:52:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4606#issuecomment-34499",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_034500.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-05-13T09:59:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4606#issuecomment-34500",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_034501.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-05-13T12:16:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4606#issuecomment-34501",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_034502.json:
```json
{
    "body": "Now working better, but not perfectly (some problems with trivial ideal classes)\n\n```\nsage: K=QuadraticField(-79)\nsage: K.class_group()\nClass group of order 5 with structure C5 of Number Field in a with defining polynomial x^2 + 79\nsage: A=K.class_group().gen()\nsage: E=EllipticCurve('433a1')\nsage: sum(E.lseries_gross_zagier(A**i)(2) for i in range(5))\n0.173957331997956\nsage: E.lseries()(2)*E.quadratic_twist(-79).lseries()(2)\n0.327922081982688\nsage: lgz=E.lseries_gross_zagier(A)\nsage: lgz._dokchister.check_functional_equation()\n8.32667268468867e-17\nsage: lgz=E.lseries_gross_zagier(A**2)\nsage: lgz._dokchister.check_functional_equation()\n-2.20309881449055e-16\nsage: lgz=E.lseries_gross_zagier(A**3)\nsage: lgz._dokchister.check_functional_equation()\n-2.20309881449055e-16\nsage: lgz=E.lseries_gross_zagier(A**4)\nsage: lgz._dokchister.check_functional_equation()\n8.32667268468867e-17\nsage: lgz=E.lseries_gross_zagier(A**5)\nsage: lgz._dokchister.check_functional_equation()\n-1383.90668128107\n```",
    "created_at": "2015-05-13T12:18:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4606#issuecomment-34502",
    "user": "https://github.com/fchapoton"
}
```

Now working better, but not perfectly (some problems with trivial ideal classes)

```
sage: K=QuadraticField(-79)
sage: K.class_group()
Class group of order 5 with structure C5 of Number Field in a with defining polynomial x^2 + 79
sage: A=K.class_group().gen()
sage: E=EllipticCurve('433a1')
sage: sum(E.lseries_gross_zagier(A**i)(2) for i in range(5))
0.173957331997956
sage: E.lseries()(2)*E.quadratic_twist(-79).lseries()(2)
0.327922081982688
sage: lgz=E.lseries_gross_zagier(A)
sage: lgz._dokchister.check_functional_equation()
8.32667268468867e-17
sage: lgz=E.lseries_gross_zagier(A**2)
sage: lgz._dokchister.check_functional_equation()
-2.20309881449055e-16
sage: lgz=E.lseries_gross_zagier(A**3)
sage: lgz._dokchister.check_functional_equation()
-2.20309881449055e-16
sage: lgz=E.lseries_gross_zagier(A**4)
sage: lgz._dokchister.check_functional_equation()
8.32667268468867e-17
sage: lgz=E.lseries_gross_zagier(A**5)
sage: lgz._dokchister.check_functional_equation()
-1383.90668128107
```



---

archive/issue_comments_034503.json:
```json
{
    "body": "Is the following thing normal ?\n\n```\nsage: K=QuadraticField(-79)\nsage: A=K.class_group().gen()\nsage: [(A**i).ideal().quadratic_form().discriminant() for i in range(5)]\n[-316, -79, -79, -79, -79]\n```",
    "created_at": "2015-05-13T12:30:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4606#issuecomment-34503",
    "user": "https://github.com/fchapoton"
}
```

Is the following thing normal ?

```
sage: K=QuadraticField(-79)
sage: A=K.class_group().gen()
sage: [(A**i).ideal().quadratic_form().discriminant() for i in range(5)]
[-316, -79, -79, -79, -79]
```



---

archive/issue_comments_034504.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-05-13T13:39:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4606#issuecomment-34504",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_034505.json:
```json
{
    "body": "Ok. Now everything seems to work fine. As far as I can tell.\n\nThere remains to add a little more doc.",
    "created_at": "2015-05-13T13:48:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4606#issuecomment-34505",
    "user": "https://github.com/fchapoton"
}
```

Ok. Now everything seems to work fine. As far as I can tell.

There remains to add a little more doc.



---

archive/issue_comments_034506.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-05-17T19:45:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4606#issuecomment-34506",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_034507.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-05-17T19:47:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4606#issuecomment-34507",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_034508.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2015-05-17T19:58:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4606#issuecomment-34508",
    "user": "https://github.com/fchapoton"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_034509.json:
```json
{
    "body": "Anybody interested, please give me feed back. It seems to work.",
    "created_at": "2015-05-17T19:58:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4606#issuecomment-34509",
    "user": "https://github.com/fchapoton"
}
```

Anybody interested, please give me feed back. It seems to work.



---

archive/issue_events_010471.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2015-06-26T11:31:51Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4606",
    "milestone": "sage-6.7",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4606#event-10471"
}
```



---

archive/issue_events_010472.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2015-06-26T11:31:51Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4606",
    "milestone": "sage-6.8",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4606#event-10472"
}
```



---

archive/issue_comments_034510.json:
```json
{
    "body": "ping ?",
    "created_at": "2015-06-26T11:31:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4606#issuecomment-34510",
    "user": "https://github.com/fchapoton"
}
```

ping ?



---

archive/issue_comments_034511.json:
```json
{
    "body": "... pong!\n\nI added a little bit more to the documentation. Just pointing to the article is not enough.\n\nI tested this (merged into 6.8.beta6) and all passed. \n\n---\nNew commits:",
    "created_at": "2015-06-28T20:15:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4606#issuecomment-34511",
    "user": "https://github.com/categorie"
}
```

... pong!

I added a little bit more to the documentation. Just pointing to the article is not enough.

I tested this (merged into 6.8.beta6) and all passed. 

---
New commits:



---

archive/issue_comments_034512.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2015-06-28T20:15:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4606#issuecomment-34512",
    "user": "https://github.com/categorie"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_034513.json:
```json
{
    "body": "oops, sorry, something went wrong. I should be able fix that..",
    "created_at": "2015-06-28T20:17:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4606#issuecomment-34513",
    "user": "https://github.com/categorie"
}
```

oops, sorry, something went wrong. I should be able fix that..



---

archive/issue_comments_034514.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2015-06-28T20:17:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4606#issuecomment-34514",
    "user": "https://github.com/categorie"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_034515.json:
```json
{
    "body": "done and retested.\n\n---\nNew commits:",
    "created_at": "2015-06-29T07:52:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4606#issuecomment-34515",
    "user": "https://github.com/categorie"
}
```

done and retested.

---
New commits:



---

archive/issue_comments_034516.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2015-06-29T07:52:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4606#issuecomment-34516",
    "user": "https://github.com/categorie"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_034517.json:
```json
{
    "body": "There is one thing, I should add here, although I am in favour of putting this into sage: It is unlikely that this code will be used much. I might be wrong.",
    "created_at": "2015-06-29T08:34:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4606#issuecomment-34517",
    "user": "https://github.com/categorie"
}
```

There is one thing, I should add here, although I am in favour of putting this into sage: It is unlikely that this code will be used much. I might be wrong.



---

archive/issue_comments_034518.json:
```json
{
    "body": "You may well be right, and the fact that nothing much happened to this code for 7 years tends to support that.  But surely that does not matter -- far better that the code be here, properly documented and tested for the future, than that it should wither and die!",
    "created_at": "2015-06-29T08:49:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4606#issuecomment-34518",
    "user": "https://github.com/JohnCremona"
}
```

You may well be right, and the fact that nothing much happened to this code for 7 years tends to support that.  But surely that does not matter -- far better that the code be here, properly documented and tested for the future, than that it should wither and die!



---

archive/issue_comments_034519.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2015-06-29T22:31:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4606#issuecomment-34519",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed



---

archive/issue_events_010473.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2015-06-29T22:31:25Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4606",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4606#event-10473"
}
```
