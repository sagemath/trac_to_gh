# Issue 8111: gcd of rationals is trouble

archive/issues_008111.json:
```json
{
    "body": "Assignee: @aghitza\n\nThe GCD of rationals is still unclear (see trac 3214), and leads to definite problems with reduce(). \n\n\n```\nK.<k>= QQ[];\nprint gcd(64,256)\nprint gcd(K(64),K(256))\nprint gcd(64*k^2+128,64*k^3+256)\nfrac = (64*k^2+128)/(64*k^3+256)\nfrac.reduce()\nprint frac\n```\n\ngives\n\n```\n64\n1\n1\n(64*k^2 + 128)/(64*k^3 + 256)\n```\n\nThe last line in particular is false, according to me.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8111\n\n",
    "created_at": "2010-01-28T15:04:16Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-9.2",
    "title": "gcd of rationals is trouble",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8111",
    "user": "https://trac.sagemath.org/admin/accounts/users/pdehaye"
}
```
Assignee: @aghitza

The GCD of rationals is still unclear (see trac 3214), and leads to definite problems with reduce(). 


```
K.<k>= QQ[];
print gcd(64,256)
print gcd(K(64),K(256))
print gcd(64*k^2+128,64*k^3+256)
frac = (64*k^2+128)/(64*k^3+256)
frac.reduce()
print frac
```

gives

```
64
1
1
(64*k^2 + 128)/(64*k^3 + 256)
```

The last line in particular is false, according to me.

Issue created by migration from https://trac.sagemath.org/ticket/8111





---

archive/issue_comments_071078.json:
```json
{
    "body": "I think the trouble here is our generic fraction field code, not how we define the gcd of rational numbers.\n\nFor efficiency, we should represent QQ(x) as Frac(ZZ[x]), and do the necessary normalisation of the denominator (it should be monic) when the user accesses it with `.denominator()`.",
    "created_at": "2010-01-29T15:07:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8111#issuecomment-71078",
    "user": "https://github.com/burcin"
}
```

I think the trouble here is our generic fraction field code, not how we define the gcd of rational numbers.

For efficiency, we should represent QQ(x) as Frac(ZZ[x]), and do the necessary normalisation of the denominator (it should be monic) when the user accesses it with `.denominator()`.



---

archive/issue_comments_071079.json:
```json
{
    "body": "#10771 is probably related/same thing.",
    "created_at": "2011-02-16T21:21:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8111#issuecomment-71079",
    "user": "https://github.com/kcrisman"
}
```

#10771 is probably related/same thing.



---

archive/issue_comments_071080.json:
```json
{
    "body": "Replying to [comment:2 kcrisman]:\n> #10771 is probably related/same thing.\n\nIt may be related, but my patch from #10771 does not touch the gcd for `QQ['x']` (perhaps it should?). So far, the two tickets are about different issues.",
    "created_at": "2011-02-17T07:35:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8111#issuecomment-71080",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:2 kcrisman]:
> #10771 is probably related/same thing.

It may be related, but my patch from #10771 does not touch the gcd for `QQ['x']` (perhaps it should?). So far, the two tickets are about different issues.



---

archive/issue_comments_071081.json:
```json
{
    "body": "Replying to [comment:3 SimonKing]:\n> Replying to [comment:2 kcrisman]:\n> > #10771 is probably related/same thing.\n> \n> It may be related, but my patch from #10771 does not touch the gcd for `QQ['x']` (perhaps it should?). So far, the two tickets are about different issues.\n\nPS: It seems to me that for changing gcd for univariate polynomials over the rationals, one has to dive into flint. I'll not do that, it'd be too far off topic for me. BTW, the doc string explicitly states that gcd in `QQ['x']` returns the *monic* gcd.",
    "created_at": "2011-02-17T07:43:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8111#issuecomment-71081",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:3 SimonKing]:
> Replying to [comment:2 kcrisman]:
> > #10771 is probably related/same thing.
> 
> It may be related, but my patch from #10771 does not touch the gcd for `QQ['x']` (perhaps it should?). So far, the two tickets are about different issues.

PS: It seems to me that for changing gcd for univariate polynomials over the rationals, one has to dive into flint. I'll not do that, it'd be too far off topic for me. BTW, the doc string explicitly states that gcd in `QQ['x']` returns the *monic* gcd.



---

archive/issue_comments_071082.json:
```json
{
    "body": "Possibly related: [this discussion](https://groups.google.com/forum/#!searchin/sage-devel/xgcd/sage-devel/JV8fCPUqTzo/FTGonGmYyCgJ).",
    "created_at": "2015-02-12T15:06:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8111#issuecomment-71082",
    "user": "https://github.com/kcrisman"
}
```

Possibly related: [this discussion](https://groups.google.com/forum/#!searchin/sage-devel/xgcd/sage-devel/JV8fCPUqTzo/FTGonGmYyCgJ).



---

archive/issue_comments_071083.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-05-27T19:04:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8111#issuecomment-71083",
    "user": "https://github.com/kliem"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_071084.json:
```json
{
    "body": "Changing keywords from \"\" to \"sd109\".",
    "created_at": "2020-05-27T19:04:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8111#issuecomment-71084",
    "user": "https://github.com/kliem"
}
```

Changing keywords from "" to "sd109".



---

archive/issue_comments_071085.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2020-05-27T19:15:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8111#issuecomment-71085",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_071086.json:
```json
{
    "body": "If this is fixed, we should probably have a doctest then.  Unless it wasn't an error to begin with?  Or it's possible it was fixed elsewhere and doctested, which is fine too.",
    "created_at": "2020-05-27T19:15:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8111#issuecomment-71086",
    "user": "https://github.com/kcrisman"
}
```

If this is fixed, we should probably have a doctest then.  Unless it wasn't an error to begin with?  Or it's possible it was fixed elsewhere and doctested, which is fine too.



---

archive/issue_comments_071087.json:
```json
{
    "body": "Changing type from defect to task.",
    "created_at": "2020-05-27T19:15:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8111#issuecomment-71087",
    "user": "https://github.com/kcrisman"
}
```

Changing type from defect to task.



---

archive/issue_comments_071088.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2020-05-27T19:15:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8111#issuecomment-71088",
    "user": "https://github.com/kcrisman"
}
```

Changing priority from major to minor.



---

archive/issue_comments_071089.json:
```json
{
    "body": "New commits:",
    "created_at": "2020-05-27T19:22:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8111#issuecomment-71089",
    "user": "https://github.com/kliem"
}
```

New commits:



---

archive/issue_comments_071090.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2020-05-27T19:22:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8111#issuecomment-71090",
    "user": "https://github.com/kliem"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_071091.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2020-06-14T14:15:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8111#issuecomment-71091",
    "user": "https://github.com/mkoeppe"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_071092.json:
```json
{
    "body": "Thank you.",
    "created_at": "2020-06-14T18:26:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8111#issuecomment-71092",
    "user": "https://github.com/kliem"
}
```

Thank you.



---

archive/issue_events_008317.json:
```json
{
    "actor": "@vbraun",
    "created_at": "2020-07-08T19:32:46Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8111",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8111#event-8317"
}
```



---

archive/issue_comments_071093.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2020-07-08T19:32:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8111#issuecomment-71093",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed
