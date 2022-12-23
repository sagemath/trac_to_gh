# Issue 9402: Extend dokchitser L-function package in Elliptic Curves to Number Fields

archive/issues_009402.json:
```json
{
    "body": "Assignee: cremona\n\nCC:  alexjbest\n\nKeywords: Elliptic Curves, L-series,\n\nThis patch adds the attribute .dokchitser() to an elliptic_curve.lseries() over a number field (this capability is present over QQ). It also adds an attribute to .dokchitser(), namely get_coeffs(bound), which returns the first bound coefficients in the Dirichlet expansion of the associated L-series.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9402\n\n",
    "created_at": "2010-07-01T16:24:25Z",
    "labels": [
        "elliptic curves",
        "major",
        "enhancement"
    ],
    "title": "Extend dokchitser L-function package in Elliptic Curves to Number Fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9402",
    "user": "adam"
}
```
Assignee: cremona

CC:  alexjbest

Keywords: Elliptic Curves, L-series,

This patch adds the attribute .dokchitser() to an elliptic_curve.lseries() over a number field (this capability is present over QQ). It also adds an attribute to .dokchitser(), namely get_coeffs(bound), which returns the first bound coefficients in the Dirichlet expansion of the associated L-series.

Issue created by migration from https://trac.sagemath.org/ticket/9402





---

archive/issue_comments_089585.json:
```json
{
    "body": "Use lseries_num_fields2.patch, the second one. This adds documentation and fixes a bug in the first one. \n\nThe bug fixed is that the elliptic curve E was calling E.reduction(prime_ideal).count_points() where prime_ideal is a prime of good reduction but E is not minimal with respect to that ideal; i.e., that ideal's norm divides the conductor of E.\n\nThe fix first checks that E is minimal with respect to said ideal. If not, E.local_minimal_model(prime_ideal).reduction(prime_ideal).count_points() \nis calles.",
    "created_at": "2010-07-02T20:37:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9402#issuecomment-89585",
    "user": "adam"
}
```

Use lseries_num_fields2.patch, the second one. This adds documentation and fixes a bug in the first one. 

The bug fixed is that the elliptic curve E was calling E.reduction(prime_ideal).count_points() where prime_ideal is a prime of good reduction but E is not minimal with respect to that ideal; i.e., that ideal's norm divides the conductor of E.

The fix first checks that E is minimal with respect to said ideal. If not, E.local_minimal_model(prime_ideal).reduction(prime_ideal).count_points() 
is calles.



---

archive/issue_comments_089586.json:
```json
{
    "body": "Hi,\n\n1. If you want to get this code refereed you have to set it to \"needs review\" (under action below). \n\n2. You function to get the coefficients computes for all primes with residue characteristic up to a given bound.  Instead, it would make vastly more sense to compute for all primes with *norm* up to a given bound.    This is much easier, and in many cases means counting points in easier cases (e.g. over the prime subfield).",
    "created_at": "2011-02-03T10:37:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9402#issuecomment-89586",
    "user": "was"
}
```

Hi,

1. If you want to get this code refereed you have to set it to "needs review" (under action below). 

2. You function to get the coefficients computes for all primes with residue characteristic up to a given bound.  Instead, it would make vastly more sense to compute for all primes with *norm* up to a given bound.    This is much easier, and in many cases means counting points in easier cases (e.g. over the prime subfield).



---

archive/issue_comments_089587.json:
```json
{
    "body": "I also implemented something like this in psage, but it's really just a little reference implementation of computing the Fourier coefficients a_I.     See \n\n   http://code.google.com/p/purplesage/source/detail?r=7c1e21eb34dbeada1ed0cd5d2011da1226ef5518\n\nIt's nice to separate computing the Fourier coefficients from the actual Dokchitser code, I think, since that makes using them much more flexible.",
    "created_at": "2011-02-03T10:40:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9402#issuecomment-89587",
    "user": "was"
}
```

I also implemented something like this in psage, but it's really just a little reference implementation of computing the Fourier coefficients a_I.     See 

   http://code.google.com/p/purplesage/source/detail?r=7c1e21eb34dbeada1ed0cd5d2011da1226ef5518

It's nice to separate computing the Fourier coefficients from the actual Dokchitser code, I think, since that makes using them much more flexible.



---

archive/issue_comments_089588.json:
```json
{
    "body": "I think my comment (2) above is wrong.  I just misunderstood your code.",
    "created_at": "2011-02-03T12:28:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9402#issuecomment-89588",
    "user": "was"
}
```

I think my comment (2) above is wrong.  I just misunderstood your code.



---

archive/issue_comments_089589.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-02-03T15:11:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9402#issuecomment-89589",
    "user": "adam"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_089590.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-05-11T16:16:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9402#issuecomment-89590",
    "user": "aly.deines"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_089591.json:
```json
{
    "body": "This patch failed to apply on sage-4.7.rc2 (Mac OS X, 10.6.7) and on sage-4.7.rc0.",
    "created_at": "2011-05-11T16:16:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9402#issuecomment-89591",
    "user": "aly.deines"
}
```

This patch failed to apply on sage-4.7.rc2 (Mac OS X, 10.6.7) and on sage-4.7.rc0.



---

archive/issue_comments_089592.json:
```json
{
    "body": "Nevermind.  I didn't catch that you need to apply the patches in order.  I'm playing with this code now.",
    "created_at": "2011-05-11T17:04:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9402#issuecomment-89592",
    "user": "aly.deines"
}
```

Nevermind.  I didn't catch that you need to apply the patches in order.  I'm playing with this code now.



---

archive/issue_comments_089593.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-05-11T17:04:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9402#issuecomment-89593",
    "user": "aly.deines"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_089594.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-06-28T19:17:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9402#issuecomment-89594",
    "user": "was"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_089595.json:
```json
{
    "body": "Clearly this needs substantial work.  I'm also deleting the two patches and putting one flattened patch.",
    "created_at": "2011-06-28T19:17:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9402#issuecomment-89595",
    "user": "was"
}
```

Clearly this needs substantial work.  I'm also deleting the two patches and putting one flattened patch.



---

archive/issue_comments_089596.json:
```json
{
    "body": "Attachment\n\n**WARNING**   Extensive improvements on this code (which is really a mess right now) are appearing in psage.  See, e.g., the file lseries_nf.py here:\n\nhttp://code.google.com/p/purplesage/source/browse/#hg%2Fpsage%2Fellcurve%2Flseries\n\nHaving just written that code in psage (which involved going through the code on this ticket), I would definitely not recommend including the current code in Sage with a major rewrite.   For example, code like this in the patch:\n\n```\n    s = 'v = %s; a(k)=if(k>%s,0,v[k]);'%( coeffs, upper_limit) \n    L.init_coeffs('a(k)', pari_precode = s)    \n```\n\nis just masking confusion, since it's setting all Dirichlet coefficients above a certain bound to 0, which is nonsense.",
    "created_at": "2011-07-28T19:37:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9402#issuecomment-89596",
    "user": "was"
}
```

Attachment

**WARNING**   Extensive improvements on this code (which is really a mess right now) are appearing in psage.  See, e.g., the file lseries_nf.py here:

http://code.google.com/p/purplesage/source/browse/#hg%2Fpsage%2Fellcurve%2Flseries

Having just written that code in psage (which involved going through the code on this ticket), I would definitely not recommend including the current code in Sage with a major rewrite.   For example, code like this in the patch:

```
    s = 'v = %s; a(k)=if(k>%s,0,v[k]);'%( coeffs, upper_limit) 
    L.init_coeffs('a(k)', pari_precode = s)    
```

is just masking confusion, since it's setting all Dirichlet coefficients above a certain bound to 0, which is nonsense.



---

archive/issue_comments_089597.json:
```json
{
    "body": "Changing keywords from \"Elliptic Curves, L-series,\" to \"Elliptic Curves, L-series, dokchitser\".",
    "created_at": "2013-09-21T12:12:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9402#issuecomment-89597",
    "user": "chapoton"
}
```

Changing keywords from "Elliptic Curves, L-series," to "Elliptic Curves, L-series, dokchitser".



---

archive/issue_comments_089598.json:
```json
{
    "body": "New commits:",
    "created_at": "2018-08-18T13:38:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9402#issuecomment-89598",
    "user": "chapoton"
}
```

New commits:



---

archive/issue_comments_089599.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2018-08-18T15:31:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9402#issuecomment-89599",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_089600.json:
```json
{
    "body": "There are some failing doctests, namely one check of the functional equation does not pass. Maybe the list of coefficients is wrong in this case, or maybe some other bug is lurking around (or some wrong other Dokchitser parameters ?).",
    "created_at": "2018-08-19T09:16:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9402#issuecomment-89600",
    "user": "chapoton"
}
```

There are some failing doctests, namely one check of the functional equation does not pass. Maybe the list of coefficients is wrong in this case, or maybe some other bug is lurking around (or some wrong other Dokchitser parameters ?).



---

archive/issue_comments_089601.json:
```json
{
    "body": "Changing keywords from \"Elliptic Curves, L-series, dokchitser\" to \"Elliptic Curves, lseries, dokchitser\".",
    "created_at": "2019-03-09T07:32:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9402#issuecomment-89601",
    "user": "chapoton"
}
```

Changing keywords from "Elliptic Curves, L-series, dokchitser" to "Elliptic Curves, lseries, dokchitser".
