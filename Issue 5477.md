# Issue 5477: Make R.quotient_ring(I) normalize generator in the univariate case (easy to fix!)

archive/issues_005477.json:
```json
{
    "body": "Assignee: @malb\n\nFrom a Sage Days 14 user (see below).\n\nIn short, in the univariate over-a-field case, `R.quotient_ring(I)` should normalize the generator of the ideal before forming the quotient. \n\n\n```\nIn each case below \"I\" and \"J\" are defined by different choices of\ngenerators and are recognized as the same ideal.  In case 1 the\nquotients are considered equal and in case 2 they are considered\nunequal.\n\n(I checked this with the latest version)\n\nCase 1:\n----------\n\nsage: R.<x> = PolynomialRing(QQ)\nsage: I = R.ideal([x + x^2, x])\nsage: J = R.ideal([2*x + 2*x^2, x])\nsage: S = R.quotient_ring(I)\nsage: U = R.quotient_ring(J)\nsage: I==J\nTrue\nsage: S==U\nTrue\n\nCase 2:\n----------\n\nsage: R.<x> = PolynomialRing(QQ)\nsage: I = R.ideal([x + x^2])\nsage: J = R.ideal([2*x + 2*x^2])\nsage: S = R.quotient_ring(I)\nsage: U = R.quotient_ring(J)\nsage: I==J\nTrue\nsage: S==U\nFalse\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5477\n\n",
    "created_at": "2009-03-11T03:19:20Z",
    "labels": [
        "commutative algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "Make R.quotient_ring(I) normalize generator in the univariate case (easy to fix!)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5477",
    "user": "@williamstein"
}
```
Assignee: @malb

From a Sage Days 14 user (see below).

In short, in the univariate over-a-field case, `R.quotient_ring(I)` should normalize the generator of the ideal before forming the quotient. 


```
In each case below "I" and "J" are defined by different choices of
generators and are recognized as the same ideal.  In case 1 the
quotients are considered equal and in case 2 they are considered
unequal.

(I checked this with the latest version)

Case 1:
----------

sage: R.<x> = PolynomialRing(QQ)
sage: I = R.ideal([x + x^2, x])
sage: J = R.ideal([2*x + 2*x^2, x])
sage: S = R.quotient_ring(I)
sage: U = R.quotient_ring(J)
sage: I==J
True
sage: S==U
True

Case 2:
----------

sage: R.<x> = PolynomialRing(QQ)
sage: I = R.ideal([x + x^2])
sage: J = R.ideal([2*x + 2*x^2])
sage: S = R.quotient_ring(I)
sage: U = R.quotient_ring(J)
sage: I==J
True
sage: S==U
False
```


Issue created by migration from https://trac.sagemath.org/ticket/5477





---

archive/issue_comments_042481.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-02T10:53:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5477#issuecomment-42481",
    "user": "@aghitza"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_042482.json:
```json
{
    "body": "See attached patch for a fix.",
    "created_at": "2010-01-02T10:53:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5477#issuecomment-42482",
    "user": "@aghitza"
}
```

See attached patch for a fix.



---

archive/issue_comments_042483.json:
```json
{
    "body": "Attachment [trac_5477.patch](tarball://root/attachments/some-uuid/ticket5477/trac_5477.patch) by @rishikesha created at 2010-01-21 15:22:33\n\nFixes by taking gcd with itself when only one generator is given, thus assuring a normalized generator.",
    "created_at": "2010-01-21T15:22:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5477#issuecomment-42483",
    "user": "@rishikesha"
}
```

Attachment [trac_5477.patch](tarball://root/attachments/some-uuid/ticket5477/trac_5477.patch) by @rishikesha created at 2010-01-21 15:22:33

Fixes by taking gcd with itself when only one generator is given, thus assuring a normalized generator.



---

archive/issue_comments_042484.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-21T15:22:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5477#issuecomment-42484",
    "user": "@rishikesha"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_042485.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-23T08:39:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5477#issuecomment-42485",
    "user": "mvngu"
}
```

Resolution: fixed
