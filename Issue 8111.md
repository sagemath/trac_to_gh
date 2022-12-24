# Issue 8111: gcd of rationals is trouble

archive/issues_008111.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nThe GCD of rationals is still unclear (see trac 3214), and leads to definite problems with reduce(). \n\n\n```\nK.<k>= QQ[];\nprint gcd(64,256)\nprint gcd(K(64),K(256))\nprint gcd(64*k^2+128,64*k^3+256)\nfrac = (64*k^2+128)/(64*k^3+256)\nfrac.reduce()\nprint frac\n```\n\ngives\n\n```\n64\n1\n1\n(64*k^2 + 128)/(64*k^3 + 256)\n```\n\nThe last line in particular is false, according to me.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8111\n\n",
    "created_at": "2010-01-28T15:04:16Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-9.2",
    "title": "gcd of rationals is trouble",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8111",
    "user": "pdehaye"
}
```
Assignee: AlexGhitza

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

archive/issue_comments_071199.json:
```json
{
    "body": "I think the trouble here is our generic fraction field code, not how we define the gcd of rational numbers.\n\nFor efficiency, we should represent QQ(x) as Frac(ZZ[x]), and do the necessary normalisation of the denominator (it should be monic) when the user accesses it with `.denominator()`.",
    "created_at": "2010-01-29T15:07:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8111#issuecomment-71199",
    "user": "burcin"
}
```

I think the trouble here is our generic fraction field code, not how we define the gcd of rational numbers.

For efficiency, we should represent QQ(x) as Frac(ZZ[x]), and do the necessary normalisation of the denominator (it should be monic) when the user accesses it with `.denominator()`.



---

archive/issue_comments_071200.json:
```json
{
    "body": "#10771 is probably related/same thing.",
    "created_at": "2011-02-16T21:21:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8111#issuecomment-71200",
    "user": "kcrisman"
}
```

#10771 is probably related/same thing.



---

archive/issue_comments_071201.json:
```json
{
    "body": "Replying to [comment:2 kcrisman]:\n> #10771 is probably related/same thing.\n\nIt may be related, but my patch from #10771 does not touch the gcd for `QQ['x']` (perhaps it should?). So far, the two tickets are about different issues.",
    "created_at": "2011-02-17T07:35:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8111#issuecomment-71201",
    "user": "SimonKing"
}
```

Replying to [comment:2 kcrisman]:
> #10771 is probably related/same thing.

It may be related, but my patch from #10771 does not touch the gcd for `QQ['x']` (perhaps it should?). So far, the two tickets are about different issues.



---

archive/issue_comments_071202.json:
```json
{
    "body": "Replying to [comment:3 SimonKing]:\n> Replying to [comment:2 kcrisman]:\n> > #10771 is probably related/same thing.\n> \n> It may be related, but my patch from #10771 does not touch the gcd for `QQ['x']` (perhaps it should?). So far, the two tickets are about different issues.\n\nPS: It seems to me that for changing gcd for univariate polynomials over the rationals, one has to dive into flint. I'll not do that, it'd be too far off topic for me. BTW, the doc string explicitly states that gcd in `QQ['x']` returns the *monic* gcd.",
    "created_at": "2011-02-17T07:43:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8111#issuecomment-71202",
    "user": "SimonKing"
}
```

Replying to [comment:3 SimonKing]:
> Replying to [comment:2 kcrisman]:
> > #10771 is probably related/same thing.
> 
> It may be related, but my patch from #10771 does not touch the gcd for `QQ['x']` (perhaps it should?). So far, the two tickets are about different issues.

PS: It seems to me that for changing gcd for univariate polynomials over the rationals, one has to dive into flint. I'll not do that, it'd be too far off topic for me. BTW, the doc string explicitly states that gcd in `QQ['x']` returns the *monic* gcd.



---

archive/issue_comments_071203.json:
```json
{
    "body": "Possibly related: [this discussion](https://groups.google.com/forum/#!searchin/sage-devel/xgcd/sage-devel/JV8fCPUqTzo/FTGonGmYyCgJ).",
    "created_at": "2015-02-12T15:06:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8111#issuecomment-71203",
    "user": "kcrisman"
}
```

Possibly related: [this discussion](https://groups.google.com/forum/#!searchin/sage-devel/xgcd/sage-devel/JV8fCPUqTzo/FTGonGmYyCgJ).



---

archive/issue_comments_071204.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-05-27T19:04:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8111#issuecomment-71204",
    "user": "@kliem"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_071205.json:
```json
{
    "body": "Changing keywords from \"\" to \"sd109\".",
    "created_at": "2020-05-27T19:04:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8111#issuecomment-71205",
    "user": "@kliem"
}
```

Changing keywords from "" to "sd109".



---

archive/issue_comments_071206.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2020-05-27T19:15:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8111#issuecomment-71206",
    "user": "kcrisman"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_071207.json:
```json
{
    "body": "If this is fixed, we should probably have a doctest then.  Unless it wasn't an error to begin with?  Or it's possible it was fixed elsewhere and doctested, which is fine too.",
    "created_at": "2020-05-27T19:15:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8111#issuecomment-71207",
    "user": "kcrisman"
}
```

If this is fixed, we should probably have a doctest then.  Unless it wasn't an error to begin with?  Or it's possible it was fixed elsewhere and doctested, which is fine too.



---

archive/issue_comments_071208.json:
```json
{
    "body": "Changing type from defect to task.",
    "created_at": "2020-05-27T19:15:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8111#issuecomment-71208",
    "user": "kcrisman"
}
```

Changing type from defect to task.



---

archive/issue_comments_071209.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2020-05-27T19:15:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8111#issuecomment-71209",
    "user": "kcrisman"
}
```

Changing priority from major to minor.



---

archive/issue_comments_071210.json:
```json
{
    "body": "New commits:",
    "created_at": "2020-05-27T19:22:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8111#issuecomment-71210",
    "user": "@kliem"
}
```

New commits:



---

archive/issue_comments_071211.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2020-05-27T19:22:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8111#issuecomment-71211",
    "user": "@kliem"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_071212.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2020-06-14T14:15:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8111#issuecomment-71212",
    "user": "mkoeppe"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_071213.json:
```json
{
    "body": "Thank you.",
    "created_at": "2020-06-14T18:26:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8111#issuecomment-71213",
    "user": "@kliem"
}
```

Thank you.



---

archive/issue_comments_071214.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2020-07-08T19:32:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8111#issuecomment-71214",
    "user": "vbraun"
}
```

Resolution: fixed
