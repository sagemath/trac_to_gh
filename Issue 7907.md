# Issue 7907: Bug in characteristic 2 isogenies of degree >3

archive/issues_007907.json:
```json
{
    "body": "Assignee: @JohnCremona\n\nCC:  @categorie shumow\n\nKeywords: isogeny\n\nThe method  __compute_omega_general() in ell_curve_isogeny.py contains\n\n```\n        for j  in xrange(0,n-1):\n            psi_prpr = psi_prpr + \\\n                binomial(j+2,2)*psi_coeffs[(j+2)]*cur_x_pow\n            cur_x_pow = x*cur_x_pow\n```\n\nwhere the degree of the isogeny is 2*n+1.   In degree 3 (the only case doctested) n=1 and the loop is empty.  Otherwise there is a run-time error since the name \"binomial\" has not been imported.\n\nThis will be simple to patch, but of course as this indicated that higher degree isogenies in char.2 have not been tested, other issues might arise.\n\nPatch up soon.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7907\n\n",
    "created_at": "2010-01-12T12:36:44Z",
    "labels": [
        "component: elliptic curves",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "Bug in characteristic 2 isogenies of degree >3",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7907",
    "user": "https://github.com/JohnCremona"
}
```
Assignee: @JohnCremona

CC:  @categorie shumow

Keywords: isogeny

The method  __compute_omega_general() in ell_curve_isogeny.py contains

```
        for j  in xrange(0,n-1):
            psi_prpr = psi_prpr + \
                binomial(j+2,2)*psi_coeffs[(j+2)]*cur_x_pow
            cur_x_pow = x*cur_x_pow
```

where the degree of the isogeny is 2*n+1.   In degree 3 (the only case doctested) n=1 and the loop is empty.  Otherwise there is a run-time error since the name "binomial" has not been imported.

This will be simple to patch, but of course as this indicated that higher degree isogenies in char.2 have not been tested, other issues might arise.

Patch up soon.

Issue created by migration from https://trac.sagemath.org/ticket/7907





---

archive/issue_comments_068627.json:
```json
{
    "body": "Here's an example of the failure which will be put into a doctest in the patch.\n\nBefore:\n\n\n```\nsage: F = GF(128,'a')                                     \nsage: a = F.gen()                                         \nsage: E = EllipticCurve([1,0,0,0,(a**6+a**4+a**2+a)])     \nsage: x = polygen(F)\nsage: ker =  (x^6 + (a^6 + a^5 + a^4 + a^3 + a^2 + a)*x^5 + (a^6 + a^5 + a^2 + 1)*x^4 + (a^6 + a^5 + a^4 + a^3 + a^2 + 1)*x^3 + (a^6 + a^3 + a)*x^2 + (a^4 + a^3 + 1)*x + a^5 + a^4 + a) \nsage: E.isogeny(ker)        \nTraceback (most recent call last):\n...\nNameError: global name 'binomial' is not defined\n```\n\n\nAfter:\n\n```\nsage: F = GF(128,'a')                                     \nsage: a = F.gen()                                         \nsage: E = EllipticCurve([1,0,0,0,(a**6+a**4+a**2+a)])     \nsage: x = polygen(F)\nsage: ker =  (x^6 + (a^6 + a^5 + a^4 + a^3 + a^2 + a)*x^5 + (a^6 + a^5 + a^2 + 1)*x^4 + (a^6 + a^5 + a^4 + a^3 + a^2 + 1)*x^3 + (a^6 + a^3 + a)*x^2 + (a^4 + a^3 + 1)*x + a^5 + a^4 + a)\nsage: E.isogeny(ker)                                      \nIsogeny of degree 13 from Elliptic Curve defined by y^2 + x*y = x^3 + (a^6+a^4+a^2+a) over Finite Field in a of size 2^7 to Elliptic Curve defined by y^2 + x*y = x^3 + (a^6+a^5+a^4+a^3+a^2+a)*x + (a^5+a^3) over Finite Field in a of size 2^7\n```\n",
    "created_at": "2010-01-12T12:45:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7907",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7907#issuecomment-68627",
    "user": "https://github.com/JohnCremona"
}
```

Here's an example of the failure which will be put into a doctest in the patch.

Before:


```
sage: F = GF(128,'a')                                     
sage: a = F.gen()                                         
sage: E = EllipticCurve([1,0,0,0,(a**6+a**4+a**2+a)])     
sage: x = polygen(F)
sage: ker =  (x^6 + (a^6 + a^5 + a^4 + a^3 + a^2 + a)*x^5 + (a^6 + a^5 + a^2 + 1)*x^4 + (a^6 + a^5 + a^4 + a^3 + a^2 + 1)*x^3 + (a^6 + a^3 + a)*x^2 + (a^4 + a^3 + 1)*x + a^5 + a^4 + a) 
sage: E.isogeny(ker)        
Traceback (most recent call last):
...
NameError: global name 'binomial' is not defined
```


After:

```
sage: F = GF(128,'a')                                     
sage: a = F.gen()                                         
sage: E = EllipticCurve([1,0,0,0,(a**6+a**4+a**2+a)])     
sage: x = polygen(F)
sage: ker =  (x^6 + (a^6 + a^5 + a^4 + a^3 + a^2 + a)*x^5 + (a^6 + a^5 + a^2 + 1)*x^4 + (a^6 + a^5 + a^4 + a^3 + a^2 + 1)*x^3 + (a^6 + a^3 + a)*x^2 + (a^4 + a^3 + 1)*x + a^5 + a^4 + a)
sage: E.isogeny(ker)                                      
Isogeny of degree 13 from Elliptic Curve defined by y^2 + x*y = x^3 + (a^6+a^4+a^2+a) over Finite Field in a of size 2^7 to Elliptic Curve defined by y^2 + x*y = x^3 + (a^6+a^5+a^4+a^3+a^2+a)*x + (a^5+a^3) over Finite Field in a of size 2^7
```




---

archive/issue_comments_068628.json:
```json
{
    "body": "Applies to 4.3.1.alpha1",
    "created_at": "2010-01-12T12:49:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7907",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7907#issuecomment-68628",
    "user": "https://github.com/JohnCremona"
}
```

Applies to 4.3.1.alpha1



---

archive/issue_comments_068629.json:
```json
{
    "body": "Attachment [trac_7906-isogeny.patch](tarball://root/attachments/some-uuid/ticket7907/trac_7906-isogeny.patch) by @JohnCremona created at 2010-01-12 12:51:13\n\nApplies to 4.3.1.alpha1; replaced previous (wrongly named!)",
    "created_at": "2010-01-12T12:51:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7907",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7907#issuecomment-68629",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [trac_7906-isogeny.patch](tarball://root/attachments/some-uuid/ticket7907/trac_7906-isogeny.patch) by @JohnCremona created at 2010-01-12 12:51:13

Applies to 4.3.1.alpha1; replaced previous (wrongly named!)



---

archive/issue_comments_068630.json:
```json
{
    "body": "Attachment [trac_7907-isogeny.patch](tarball://root/attachments/some-uuid/ticket7907/trac_7907-isogeny.patch) by @JohnCremona created at 2010-01-12 12:51:43",
    "created_at": "2010-01-12T12:51:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7907",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7907#issuecomment-68630",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [trac_7907-isogeny.patch](tarball://root/attachments/some-uuid/ticket7907/trac_7907-isogeny.patch) by @JohnCremona created at 2010-01-12 12:51:43



---

archive/issue_comments_068631.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-12T12:51:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7907",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7907#issuecomment-68631",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_068632.json:
```json
{
    "body": "fine. it passes all tests.",
    "created_at": "2010-01-12T14:46:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7907",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7907#issuecomment-68632",
    "user": "https://github.com/categorie"
}
```

fine. it passes all tests.



---

archive/issue_comments_068633.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-12T14:46:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7907",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7907#issuecomment-68633",
    "user": "https://github.com/categorie"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_018912.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2010-01-13T08:02:18Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7907",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7907#event-18912"
}
```



---

archive/issue_comments_068634.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-13T08:02:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7907",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7907#issuecomment-68634",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed
