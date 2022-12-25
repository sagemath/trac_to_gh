# Issue 6881: Conics

archive/issues_006881.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @mstreng\n\nKeywords: conic, curve\n\nWe should have a class (or classes) for conic curves, and, more specially diagonal conics.  In particular, one of the methods should be John Cremona's algorithms for finding points on solvable conics, both over Q and over fraction fields of polynomial rings.  Other methods might include getting discriminants, primes of bad reduction, producing parametrized solutions, etc.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6881\n\n",
    "created_at": "2009-09-03T22:47:34Z",
    "labels": [
        "component: algebra",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.10",
    "title": "Conics",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6881",
    "user": "https://trac.sagemath.org/admin/accounts/users/victor"
}
```
Assignee: tbd

CC:  @mstreng

Keywords: conic, curve

We should have a class (or classes) for conic curves, and, more specially diagonal conics.  In particular, one of the methods should be John Cremona's algorithms for finding points on solvable conics, both over Q and over fraction fields of polynomial rings.  Other methods might include getting discriminants, primes of bad reduction, producing parametrized solutions, etc.

Issue created by migration from https://trac.sagemath.org/ticket/6881





---

archive/issue_comments_056688.json:
```json
{
    "body": "Changing component from algebra to algebraic geometry.",
    "created_at": "2009-11-15T13:13:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56688",
    "user": "https://github.com/aghitza"
}
```

Changing component from algebra to algebraic geometry.



---

archive/issue_comments_056689.json:
```json
{
    "body": "See #727\nA patch defining a conic class and using Simon's algorithms for finding points over Q is in progress.",
    "created_at": "2010-07-06T11:09:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56689",
    "user": "https://github.com/mstreng"
}
```

See #727
A patch defining a conic class and using Simon's algorithms for finding points over Q is in progress.



---

archive/issue_comments_056690.json:
```json
{
    "body": "I changed the description to better fit what is already in #727. Besides things that are already in #727, all that I removed from the original description were the following two requests.\n\n1. Use John Cremona's algorithms for finding points on conics over QQ.\n\nIt seems that Simon's algorithms (in #727) are better, but that doesn't have to stop us from giving Cremona's code as an option. It is inside mwrank, which is part of Sage. If someone wants to do it, then it can be made into a separate ticket.\n\n2. Getting primes of bad reduction of conics.\n\nThis is as good as in #727: make a Conic C. Then do C.determinant().factor()",
    "created_at": "2010-07-20T21:13:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56690",
    "user": "https://github.com/mstreng"
}
```

I changed the description to better fit what is already in #727. Besides things that are already in #727, all that I removed from the original description were the following two requests.

1. Use John Cremona's algorithms for finding points on conics over QQ.

It seems that Simon's algorithms (in #727) are better, but that doesn't have to stop us from giving Cremona's code as an option. It is inside mwrank, which is part of Sage. If someone wants to do it, then it can be made into a separate ticket.

2. Getting primes of bad reduction of conics.

This is as good as in #727: make a Conic C. Then do C.determinant().factor()



---

archive/issue_comments_056691.json:
```json
{
    "body": "Changing assignee from tbd to @lennartack.",
    "created_at": "2015-08-07T21:15:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56691",
    "user": "https://github.com/lennartack"
}
```

Changing assignee from tbd to @lennartack.



---

archive/issue_comments_056692.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-10-03T01:19:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56692",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_056693.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-10-28T13:04:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56693",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_056694.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-12-11T16:19:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56694",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_056695.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2015-12-11T16:31:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56695",
    "user": "https://github.com/lennartack"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_056696.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-12-11T16:56:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56696",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_056697.json:
```json
{
    "body": "Changing keywords from \"conic, curve\" to \"conic, curve, function field\".",
    "created_at": "2015-12-14T15:24:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56697",
    "user": "https://github.com/mstreng"
}
```

Changing keywords from "conic, curve" to "conic, curve, function field".



---

archive/issue_comments_056698.json:
```json
{
    "body": "Not 100% doctest coverage, and there is a doctest that fails.",
    "created_at": "2015-12-15T15:22:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56698",
    "user": "https://github.com/mstreng"
}
```

Not 100% doctest coverage, and there is a doctest that fails.



---

archive/issue_comments_056699.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2015-12-15T15:22:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56699",
    "user": "https://github.com/mstreng"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_056700.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-12-16T23:46:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56700",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_056701.json:
```json
{
    "body": "Replying to [comment:16 mstreng]:\n> Not 100% doctest coverage, and there is a doctest that fails.\nShould be okay now.",
    "created_at": "2015-12-16T23:51:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56701",
    "user": "https://github.com/lennartack"
}
```

Replying to [comment:16 mstreng]:
> Not 100% doctest coverage, and there is a doctest that fails.
Should be okay now.



---

archive/issue_comments_056702.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2015-12-16T23:51:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56702",
    "user": "https://github.com/lennartack"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_056703.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-12-27T16:18:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56703",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_056704.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2016-01-28T09:06:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56704",
    "user": "https://github.com/mstreng"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_056705.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-02-03T11:12:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56705",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_056706.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2016-02-03T11:14:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56706",
    "user": "https://github.com/lennartack"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_056707.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-02-04T15:10:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56707",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_056708.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2016-02-05T12:53:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56708",
    "user": "https://github.com/mstreng"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_056709.json:
```json
{
    "body": "All tests pass. Documentation looks good.\n\nThe functions do not work perfectly in all cases due to #20003, but after bypassing `squarefree_decomposition`, I get:\n\n\n\n\n```\nsage: K.<t> = PolynomialRing(GF(7))\nsage: C = Conic([5*t^2+4, t^2+3*t+3, 6*t^2+3*t+2, 5*t^2+5, 4*t+3, 4*t^2+t+5])\nsage: C.has_rational_point()\nTrue\n```\n\n\nand\n\n\n```\nsage: F = FiniteField(7)\nsage: P.<t> = F[]                                                               \nsage: K = P.fraction_field()\nsage: for i in range(50):                                                       \n    c = [K.random_element() for j in range(6)]\n    C = Conic(c)\n    C.has_rational_point(point=True)\n....:     \n(False, None)\n(False, None)\n(False, None)\n(False, None)\n(True,\n ((2*t^8 + 5*t^7 + 6*t^6 + 5*t^5 + 4*t^4 + 5*t^2 + 3*t + 2)/(t^8 + 5*t^7 + 5*t^6\n + 4*t^5 + 3*t^4 + 2*t^3 + t^2 + 5*t + 6) : (t^8 + 2*t^7 + t^5 + t^4 + 2*t^3 + 2\n*t^2 + 4*t + 4)/(t^8 + 6*t^7 + t^6 + 4*t^5 + t^4 + 2*t^2 + 5*t + 3) : 1))\n(False, None)\n(False, None)\n(False, None)\n(True,\n ((2*t^8 + t^7 + 6*t^6 + 4*t^5 + 6*t^4 + 5*t^2 + 1)/(t^8 + 2*t^7 + 6*t^6 + 3*t^5\n + 3*t^4 + 6*t^3 + 6*t^2 + 6*t) : (2*t^8 + 4*t^7 + 5*t^6 + 3*t^5 + t^4 + 5*t + 1\n)/(t^8 + 2*t^7 + 6*t^6 + 3*t^5 + 3*t^4 + 6*t^3 + 6*t^2 + 6*t) : 1))\n(False, None)\n(False, None)\n(False, None)\n(False, None)\n(False, None)\n(False, None)\n(False, None)\n(False, None)\n(False, None)\n(False, None)\n(False, None)\n(False, None)\n(False, None)\n(False, None)\n(False, None)\n(False, None)\n(False, None)\n(False, None)\n(False, None)\n(True,\n ((2*t^4 + 2*t^3 + 3*t^2)/(t^7 + t^6 + 5*t^4 + t^2 + t + 4) : (5*t^7 + 3*t^6 + t\n^5 + 5*t^4 + 6*t^3 + 2*t^2 + 4*t)/(t^7 + t^6 + 5*t^4 + t^2 + t + 4) : 1))\n(False, None)\n(False, None)\n(False, None)\n(False, None)\n(False, None)\n(True,\n ((t^8 + 5*t^7 + 2*t^6 + 2*t^5 + 3*t^3 + t^2 + 3)/(t^7 + t^6 + 6*t^4 + 5*t^3 + 6\n*t^2 + 2*t + 2) : (4*t^5 + 2*t^4 + 5*t^3 + 4*t^2 + 5*t + 2)/(t^4 + 2*t^3 + 5*t^2\n + 4*t + 5) : 1))\n(False, None)\n(False, None)\n(False, None)\n(False, None)\n(False, None)\n(False, None)\n(False, None)\n(False, None)\n(False, None)\n(False, None)\n(True,\n ((2*t^11 + 3*t^10 + 6*t^9 + t^8 + 6*t^7 + 4*t^6 + t^5 + 4*t^4 + 2*t^3 + 3*t + 5\n)/(t^11 + 5*t^10 + 5*t^9 + t^8 + t^7 + 6*t^6 + 6*t^5 + 4*t^4 + 6*t^3 + 4*t) : (2\n*t^9 + 4*t^8 + 4*t^7 + 6*t^6 + 5*t^5 + 5*t^4 + 4*t^3 + t^2 + 6*t + 1)/(t^10 + 5*\nt^8 + 4*t^7 + 2*t^6 + 3*t^5 + 5*t^4 + 6*t^2 + 5*t) : 1))\n(False, None)\n(False, None)\n(False, None)\n(False, None)\n```\n",
    "created_at": "2016-02-05T12:53:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56709",
    "user": "https://github.com/mstreng"
}
```

All tests pass. Documentation looks good.

The functions do not work perfectly in all cases due to #20003, but after bypassing `squarefree_decomposition`, I get:




```
sage: K.<t> = PolynomialRing(GF(7))
sage: C = Conic([5*t^2+4, t^2+3*t+3, 6*t^2+3*t+2, 5*t^2+5, 4*t+3, 4*t^2+t+5])
sage: C.has_rational_point()
True
```


and


```
sage: F = FiniteField(7)
sage: P.<t> = F[]                                                               
sage: K = P.fraction_field()
sage: for i in range(50):                                                       
    c = [K.random_element() for j in range(6)]
    C = Conic(c)
    C.has_rational_point(point=True)
....:     
(False, None)
(False, None)
(False, None)
(False, None)
(True,
 ((2*t^8 + 5*t^7 + 6*t^6 + 5*t^5 + 4*t^4 + 5*t^2 + 3*t + 2)/(t^8 + 5*t^7 + 5*t^6
 + 4*t^5 + 3*t^4 + 2*t^3 + t^2 + 5*t + 6) : (t^8 + 2*t^7 + t^5 + t^4 + 2*t^3 + 2
*t^2 + 4*t + 4)/(t^8 + 6*t^7 + t^6 + 4*t^5 + t^4 + 2*t^2 + 5*t + 3) : 1))
(False, None)
(False, None)
(False, None)
(True,
 ((2*t^8 + t^7 + 6*t^6 + 4*t^5 + 6*t^4 + 5*t^2 + 1)/(t^8 + 2*t^7 + 6*t^6 + 3*t^5
 + 3*t^4 + 6*t^3 + 6*t^2 + 6*t) : (2*t^8 + 4*t^7 + 5*t^6 + 3*t^5 + t^4 + 5*t + 1
)/(t^8 + 2*t^7 + 6*t^6 + 3*t^5 + 3*t^4 + 6*t^3 + 6*t^2 + 6*t) : 1))
(False, None)
(False, None)
(False, None)
(False, None)
(False, None)
(False, None)
(False, None)
(False, None)
(False, None)
(False, None)
(False, None)
(False, None)
(False, None)
(False, None)
(False, None)
(False, None)
(False, None)
(False, None)
(False, None)
(True,
 ((2*t^4 + 2*t^3 + 3*t^2)/(t^7 + t^6 + 5*t^4 + t^2 + t + 4) : (5*t^7 + 3*t^6 + t
^5 + 5*t^4 + 6*t^3 + 2*t^2 + 4*t)/(t^7 + t^6 + 5*t^4 + t^2 + t + 4) : 1))
(False, None)
(False, None)
(False, None)
(False, None)
(False, None)
(True,
 ((t^8 + 5*t^7 + 2*t^6 + 2*t^5 + 3*t^3 + t^2 + 3)/(t^7 + t^6 + 6*t^4 + 5*t^3 + 6
*t^2 + 2*t + 2) : (4*t^5 + 2*t^4 + 5*t^3 + 4*t^2 + 5*t + 2)/(t^4 + 2*t^3 + 5*t^2
 + 4*t + 5) : 1))
(False, None)
(False, None)
(False, None)
(False, None)
(False, None)
(False, None)
(False, None)
(False, None)
(False, None)
(False, None)
(True,
 ((2*t^11 + 3*t^10 + 6*t^9 + t^8 + 6*t^7 + 4*t^6 + t^5 + 4*t^4 + 2*t^3 + 3*t + 5
)/(t^11 + 5*t^10 + 5*t^9 + t^8 + t^7 + 6*t^6 + 6*t^5 + 4*t^4 + 6*t^3 + 4*t) : (2
*t^9 + 4*t^8 + 4*t^7 + 6*t^6 + 5*t^5 + 5*t^4 + 4*t^3 + t^2 + 6*t + 1)/(t^10 + 5*
t^8 + 4*t^7 + 2*t^6 + 3*t^5 + 5*t^4 + 6*t^2 + 5*t) : 1))
(False, None)
(False, None)
(False, None)
(False, None)
```




---

archive/issue_comments_056710.json:
```json
{
    "body": "Please rebase to sage-7.1.beta2 (in particular, `sage.rings.arith` has moved to `sage.arith.all`) and use the [standard copyright template](http://doc.sagemath.org/html/en/developer/coding_basics.html#headings-of-sage-library-code-files) for the newly added file.\n\nIf you have done this, you can set this ticket back to positive review.",
    "created_at": "2016-02-05T13:18:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56710",
    "user": "https://github.com/jdemeyer"
}
```

Please rebase to sage-7.1.beta2 (in particular, `sage.rings.arith` has moved to `sage.arith.all`) and use the [standard copyright template](http://doc.sagemath.org/html/en/developer/coding_basics.html#headings-of-sage-library-code-files) for the newly added file.

If you have done this, you can set this ticket back to positive review.



---

archive/issue_comments_056711.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2016-02-05T13:18:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56711",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_056712.json:
```json
{
    "body": "You might also want to fix these `pyflakes` warnings:\n\n```\nsrc/sage/schemes/plane_conics/con_rational_function_field.py:25: 'NumberField' imported but unused\nsrc/sage/schemes/plane_conics/con_rational_function_field.py:26: 'identity_matrix' imported but unused\nsrc/sage/schemes/plane_conics/con_rational_function_field.py:32: redefinition of unused 'vector' from line 30\n```\n",
    "created_at": "2016-02-05T13:23:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56712",
    "user": "https://github.com/jdemeyer"
}
```

You might also want to fix these `pyflakes` warnings:

```
src/sage/schemes/plane_conics/con_rational_function_field.py:25: 'NumberField' imported but unused
src/sage/schemes/plane_conics/con_rational_function_field.py:26: 'identity_matrix' imported but unused
src/sage/schemes/plane_conics/con_rational_function_field.py:32: redefinition of unused 'vector' from line 30
```




---

archive/issue_comments_056713.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. Last 10 new commits:",
    "created_at": "2016-02-07T22:33:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56713",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. Last 10 new commits:



---

archive/issue_comments_056714.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2016-02-07T22:35:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56714",
    "user": "https://github.com/lennartack"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_056715.json:
```json
{
    "body": "Changing status from positive_review to needs_review.",
    "created_at": "2016-02-08T07:28:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56715",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_review.



---

archive/issue_comments_056716.json:
```json
{
    "body": "10 new commits? Sorry, but this needs to be reviewed (not by me).",
    "created_at": "2016-02-08T07:28:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56716",
    "user": "https://github.com/jdemeyer"
}
```

10 new commits? Sorry, but this needs to be reviewed (not by me).



---

archive/issue_comments_056717.json:
```json
{
    "body": "This is malformatted:\n\n```\nEXAMPLES:\n    \n    Create a conic::\n\n        sage: K = FractionField(PolynomialRing(QQ, 't'))\n```\n\nIt should be\n\n```\nEXAMPLES:\n    \nCreate a conic::\n\n    sage: K = FractionField(PolynomialRing(QQ, 't'))\n```\n",
    "created_at": "2016-02-08T07:30:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56717",
    "user": "https://github.com/jdemeyer"
}
```

This is malformatted:

```
EXAMPLES:
    
    Create a conic::

        sage: K = FractionField(PolynomialRing(QQ, 't'))
```

It should be

```
EXAMPLES:
    
Create a conic::

    sage: K = FractionField(PolynomialRing(QQ, 't'))
```




---

archive/issue_comments_056718.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2016-02-08T07:30:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56718",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_056719.json:
```json
{
    "body": "Please do this:\n\nReplying to [comment:25 jdemeyer]:\n> use the [standard copyright template](http://doc.sagemath.org/html/en/developer/coding_basics.html#headings-of-sage-library-code-files) for the newly added file.",
    "created_at": "2016-02-08T07:30:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56719",
    "user": "https://github.com/jdemeyer"
}
```

Please do this:

Replying to [comment:25 jdemeyer]:
> use the [standard copyright template](http://doc.sagemath.org/html/en/developer/coding_basics.html#headings-of-sage-library-code-files) for the newly added file.



---

archive/issue_comments_056720.json:
```json
{
    "body": "Replying to [comment:29 jdemeyer]:\n> 10 new commits? Sorry, but this needs to be reviewed (not by me).\nOnly the last 3 are new",
    "created_at": "2016-02-08T11:22:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56720",
    "user": "https://github.com/lennartack"
}
```

Replying to [comment:29 jdemeyer]:
> 10 new commits? Sorry, but this needs to be reviewed (not by me).
Only the last 3 are new



---

archive/issue_comments_056721.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-02-08T11:25:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56721",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_056722.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2016-02-08T11:27:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56722",
    "user": "https://github.com/lennartack"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_056723.json:
```json
{
    "body": "Replying to [comment:31 jdemeyer]:\n> Please do this:\n> \n> Replying to [comment:25 jdemeyer]:\n> > use the [standard copyright template](http://doc.sagemath.org/html/en/developer/coding_basics.html#headings-of-sage-library-code-files) for the newly added file.\n\nSorry, I misunderstood your last comment. All should be okay now.",
    "created_at": "2016-02-08T11:27:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56723",
    "user": "https://github.com/lennartack"
}
```

Replying to [comment:31 jdemeyer]:
> Please do this:
> 
> Replying to [comment:25 jdemeyer]:
> > use the [standard copyright template](http://doc.sagemath.org/html/en/developer/coding_basics.html#headings-of-sage-library-code-files) for the newly added file.

Sorry, I misunderstood your last comment. All should be okay now.



---

archive/issue_comments_056724.json:
```json
{
    "body": "Thanks Jeroen. I checked the changes and documentation html, and I ran the doctests again.",
    "created_at": "2016-02-11T12:07:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56724",
    "user": "https://github.com/mstreng"
}
```

Thanks Jeroen. I checked the changes and documentation html, and I ran the doctests again.



---

archive/issue_comments_056725.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2016-02-11T12:07:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56725",
    "user": "https://github.com/mstreng"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_056726.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2016-02-11T23:26:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56726",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed
