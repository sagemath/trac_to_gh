# Issue 8319: elliptic curve canonical height bug for non-minimal models

archive/issues_008319.json:
```json
{
    "body": "Assignee: @JohnCremona\n\nKeywords: canonical height\n\nFor canonical heights of points on elliptic curves defined over QQ, we call the pari function ellheight(), BUT that function only gives the correct value for global minimal models!  (At primes where the model is not minimal the local component is wrong).\n\nHere is an example to show this:\n\n```\nsage: E = EllipticCurve([-5580472329446114952805505804593498080000,\n....:           -157339733785368110382973689903536054787700497223306368000000])\nsage: P3=E([204885147732879546487576840131729064308289385547094673627174585676211859152978311600/23625501907057948132262217188983681204856907657753178415430361,92736254270288706000052529616433462503893110244786566575440613880920567197984949809570153263207165494624214991751142500000000/114834283590033957142081201488956527887145361353994063932282392800295014255070987824900081891])\nsage: P3.height()\n157.086024926474\nsage: 4*(P3.height())-(2*P3).height() # should == 0\n-1.38629436111989\n```\n\nwhile on the minimal model:\n\n```\nsage: Emin = E.minimal_model()\nsage: urst = E.isomorphism_to(Emin)\nsage: 4*urst(P3).height()-urst(2*P3).height()\n0.000000000000000\n```\n\n\nThe cure is to compute the minimal model and transfer the point there before computing the height, as illustrated above.  (Of course, pari could do that too, but this behaviour has been tolerated by pari users for many years!)\n\nIssue created by migration from https://trac.sagemath.org/ticket/8319\n\n",
    "created_at": "2010-02-21T17:27:58Z",
    "labels": [
        "component: elliptic curves",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "elliptic curve canonical height bug for non-minimal models",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8319",
    "user": "https://github.com/JohnCremona"
}
```
Assignee: @JohnCremona

Keywords: canonical height

For canonical heights of points on elliptic curves defined over QQ, we call the pari function ellheight(), BUT that function only gives the correct value for global minimal models!  (At primes where the model is not minimal the local component is wrong).

Here is an example to show this:

```
sage: E = EllipticCurve([-5580472329446114952805505804593498080000,
....:           -157339733785368110382973689903536054787700497223306368000000])
sage: P3=E([204885147732879546487576840131729064308289385547094673627174585676211859152978311600/23625501907057948132262217188983681204856907657753178415430361,92736254270288706000052529616433462503893110244786566575440613880920567197984949809570153263207165494624214991751142500000000/114834283590033957142081201488956527887145361353994063932282392800295014255070987824900081891])
sage: P3.height()
157.086024926474
sage: 4*(P3.height())-(2*P3).height() # should == 0
-1.38629436111989
```

while on the minimal model:

```
sage: Emin = E.minimal_model()
sage: urst = E.isomorphism_to(Emin)
sage: 4*urst(P3).height()-urst(2*P3).height()
0.000000000000000
```


The cure is to compute the minimal model and transfer the point there before computing the height, as illustrated above.  (Of course, pari could do that too, but this behaviour has been tolerated by pari users for many years!)

Issue created by migration from https://trac.sagemath.org/ticket/8319





---

archive/issue_comments_073666.json:
```json
{
    "body": "Applies to 4.3.3",
    "created_at": "2010-02-24T21:00:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8319",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8319#issuecomment-73666",
    "user": "https://github.com/JohnCremona"
}
```

Applies to 4.3.3



---

archive/issue_comments_073667.json:
```json
{
    "body": "Attachment [trac_8319-heights.patch](tarball://root/attachments/some-uuid/ticket8319/trac_8319-heights.patch) by @JohnCremona created at 2010-02-24 21:02:54\n\nThe patch implements the cure.  I did not bother putting in a test for minimality of the original model, since all that does is to compute the minimal model anyway and compare!  Also, the minimal model is cached, so that would only be done once.  We do not cache the isomorphism to the minimal model, but that is cheap to compute.",
    "created_at": "2010-02-24T21:02:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8319",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8319#issuecomment-73667",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [trac_8319-heights.patch](tarball://root/attachments/some-uuid/ticket8319/trac_8319-heights.patch) by @JohnCremona created at 2010-02-24 21:02:54

The patch implements the cure.  I did not bother putting in a test for minimality of the original model, since all that does is to compute the minimal model anyway and compare!  Also, the minimal model is cached, so that would only be done once.  We do not cache the isomorphism to the minimal model, but that is cheap to compute.



---

archive/issue_comments_073668.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-24T21:02:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8319",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8319#issuecomment-73668",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_073669.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-25T04:05:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8319",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8319#issuecomment-73669",
    "user": "https://github.com/categorie"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_073670.json:
```json
{
    "body": "Looks fine to me. All tests pass.",
    "created_at": "2010-02-25T04:05:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8319",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8319#issuecomment-73670",
    "user": "https://github.com/categorie"
}
```

Looks fine to me. All tests pass.



---

archive/issue_comments_073671.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-03T14:03:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8319",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8319#issuecomment-73671",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
