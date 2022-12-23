# Issue 6881: Conics

archive/issues_006881.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  mstreng\n\nKeywords: conic, curve\n\nWe should have a class (or classes) for conic curves, and, more specially diagonal conics.  In particular, one of the methods should be John Cremona's algorithms for finding points on solvable conics, both over Q and over fraction fields of polynomial rings.  Other methods might include getting discriminants, primes of bad reduction, producing parametrized solutions, etc.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6881\n\n",
    "created_at": "2009-09-03T22:47:34Z",
    "labels": [
        "algebra",
        "minor",
        "enhancement"
    ],
    "title": "Conics",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6881",
    "user": "victor"
}
```
Assignee: tbd

CC:  mstreng

Keywords: conic, curve

We should have a class (or classes) for conic curves, and, more specially diagonal conics.  In particular, one of the methods should be John Cremona's algorithms for finding points on solvable conics, both over Q and over fraction fields of polynomial rings.  Other methods might include getting discriminants, primes of bad reduction, producing parametrized solutions, etc.

Issue created by migration from https://trac.sagemath.org/ticket/6881





---

archive/issue_comments_056794.json:
```json
{
    "body": "Changing component from algebra to algebraic geometry.",
    "created_at": "2009-11-15T13:13:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56794",
    "user": "AlexGhitza"
}
```

Changing component from algebra to algebraic geometry.



---

archive/issue_comments_056795.json:
```json
{
    "body": "See #727\nA patch defining a conic class and using Simon's algorithms for finding points over Q is in progress.",
    "created_at": "2010-07-06T11:09:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56795",
    "user": "mstreng"
}
```

See #727
A patch defining a conic class and using Simon's algorithms for finding points over Q is in progress.



---

archive/issue_comments_056796.json:
```json
{
    "body": "I changed the description to better fit what is already in #727. Besides things that are already in #727, all that I removed from the original description were the following two requests.\n\n1. Use John Cremona's algorithms for finding points on conics over QQ.\n\nIt seems that Simon's algorithms (in #727) are better, but that doesn't have to stop us from giving Cremona's code as an option. It is inside mwrank, which is part of Sage. If someone wants to do it, then it can be made into a separate ticket.\n\n2. Getting primes of bad reduction of conics.\n\nThis is as good as in #727: make a Conic C. Then do C.determinant().factor()",
    "created_at": "2010-07-20T21:13:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56796",
    "user": "mstreng"
}
```

I changed the description to better fit what is already in #727. Besides things that are already in #727, all that I removed from the original description were the following two requests.

1. Use John Cremona's algorithms for finding points on conics over QQ.

It seems that Simon's algorithms (in #727) are better, but that doesn't have to stop us from giving Cremona's code as an option. It is inside mwrank, which is part of Sage. If someone wants to do it, then it can be made into a separate ticket.

2. Getting primes of bad reduction of conics.

This is as good as in #727: make a Conic C. Then do C.determinant().factor()



---

archive/issue_comments_056797.json:
```json
{
    "body": "Changing assignee from tbd to lackermans.",
    "created_at": "2015-08-07T21:15:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56797",
    "user": "lackermans"
}
```

Changing assignee from tbd to lackermans.



---

archive/issue_comments_056798.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-10-03T01:19:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56798",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_056799.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-10-28T13:04:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56799",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_056800.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-12-11T16:19:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56800",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_056801.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2015-12-11T16:31:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56801",
    "user": "lackermans"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_056802.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-12-11T16:56:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56802",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_056803.json:
```json
{
    "body": "Changing keywords from \"conic, curve\" to \"conic, curve, function field\".",
    "created_at": "2015-12-14T15:24:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56803",
    "user": "mstreng"
}
```

Changing keywords from "conic, curve" to "conic, curve, function field".



---

archive/issue_comments_056804.json:
```json
{
    "body": "Changing priority from minor to major.",
    "created_at": "2015-12-14T15:25:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56804",
    "user": "mstreng"
}
```

Changing priority from minor to major.



---

archive/issue_comments_056805.json:
```json
{
    "body": "Not 100% doctest coverage, and there is a doctest that fails.",
    "created_at": "2015-12-15T15:22:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56805",
    "user": "mstreng"
}
```

Not 100% doctest coverage, and there is a doctest that fails.



---

archive/issue_comments_056806.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2015-12-15T15:22:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56806",
    "user": "mstreng"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_056807.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-12-16T23:46:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56807",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_056808.json:
```json
{
    "body": "Replying to [comment:16 mstreng]:\n> Not 100% doctest coverage, and there is a doctest that fails.\nShould be okay now.",
    "created_at": "2015-12-16T23:51:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56808",
    "user": "lackermans"
}
```

Replying to [comment:16 mstreng]:
> Not 100% doctest coverage, and there is a doctest that fails.
Should be okay now.



---

archive/issue_comments_056809.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2015-12-16T23:51:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56809",
    "user": "lackermans"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_056810.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-12-27T16:18:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56810",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_056811.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2016-01-28T09:06:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56811",
    "user": "mstreng"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_056812.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-02-03T11:12:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56812",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_056813.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2016-02-03T11:14:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56813",
    "user": "lackermans"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_056814.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-02-04T15:10:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56814",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_056815.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2016-02-05T12:53:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56815",
    "user": "mstreng"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_056816.json:
```json
{
    "body": "All tests pass. Documentation looks good.\n\nThe functions do not work perfectly in all cases due to #20003, but after bypassing `squarefree_decomposition`, I get:\n\n\n\n\n```\nsage: K.<t> = PolynomialRing(GF(7))\nsage: C = Conic([5*t^2+4, t^2+3*t+3, 6*t^2+3*t+2, 5*t^2+5, 4*t+3, 4*t^2+t+5])\nsage: C.has_rational_point()\nTrue\n```\n\n\nand\n\n\n```\nsage: F = FiniteField(7)\nsage: P.<t> = F[]                                                               \nsage: K = P.fraction_field()\nsage: for i in range(50):                                                       \n    c = [K.random_element() for j in range(6)]\n    C = Conic(c)\n    C.has_rational_point(point=True)\n....:     \n(False, None)\n(False, None)\n(False, None)\n(False, None)\n(True,\n ((2*t^8 + 5*t^7 + 6*t^6 + 5*t^5 + 4*t^4 + 5*t^2 + 3*t + 2)/(t^8 + 5*t^7 + 5*t^6\n + 4*t^5 + 3*t^4 + 2*t^3 + t^2 + 5*t + 6) : (t^8 + 2*t^7 + t^5 + t^4 + 2*t^3 + 2\n*t^2 + 4*t + 4)/(t^8 + 6*t^7 + t^6 + 4*t^5 + t^4 + 2*t^2 + 5*t + 3) : 1))\n(False, None)\n(False, None)\n(False, None)\n(True,\n ((2*t^8 + t^7 + 6*t^6 + 4*t^5 + 6*t^4 + 5*t^2 + 1)/(t^8 + 2*t^7 + 6*t^6 + 3*t^5\n + 3*t^4 + 6*t^3 + 6*t^2 + 6*t) : (2*t^8 + 4*t^7 + 5*t^6 + 3*t^5 + t^4 + 5*t + 1\n)/(t^8 + 2*t^7 + 6*t^6 + 3*t^5 + 3*t^4 + 6*t^3 + 6*t^2 + 6*t) : 1))\n(False, None)\n(False, None)\n(False, None)\n(False, None)\n(False, None)\n(False, None)\n(False, None)\n(False, None)\n(False, None)\n(False, None)\n(False, None)\n(False, None)\n(False, None)\n(False, None)\n(False, None)\n(False, None)\n(False, None)\n(False, None)\n(False, None)\n(True,\n ((2*t^4 + 2*t^3 + 3*t^2)/(t^7 + t^6 + 5*t^4 + t^2 + t + 4) : (5*t^7 + 3*t^6 + t\n^5 + 5*t^4 + 6*t^3 + 2*t^2 + 4*t)/(t^7 + t^6 + 5*t^4 + t^2 + t + 4) : 1))\n(False, None)\n(False, None)\n(False, None)\n(False, None)\n(False, None)\n(True,\n ((t^8 + 5*t^7 + 2*t^6 + 2*t^5 + 3*t^3 + t^2 + 3)/(t^7 + t^6 + 6*t^4 + 5*t^3 + 6\n*t^2 + 2*t + 2) : (4*t^5 + 2*t^4 + 5*t^3 + 4*t^2 + 5*t + 2)/(t^4 + 2*t^3 + 5*t^2\n + 4*t + 5) : 1))\n(False, None)\n(False, None)\n(False, None)\n(False, None)\n(False, None)\n(False, None)\n(False, None)\n(False, None)\n(False, None)\n(False, None)\n(True,\n ((2*t^11 + 3*t^10 + 6*t^9 + t^8 + 6*t^7 + 4*t^6 + t^5 + 4*t^4 + 2*t^3 + 3*t + 5\n)/(t^11 + 5*t^10 + 5*t^9 + t^8 + t^7 + 6*t^6 + 6*t^5 + 4*t^4 + 6*t^3 + 4*t) : (2\n*t^9 + 4*t^8 + 4*t^7 + 6*t^6 + 5*t^5 + 5*t^4 + 4*t^3 + t^2 + 6*t + 1)/(t^10 + 5*\nt^8 + 4*t^7 + 2*t^6 + 3*t^5 + 5*t^4 + 6*t^2 + 5*t) : 1))\n(False, None)\n(False, None)\n(False, None)\n(False, None)\n```\n",
    "created_at": "2016-02-05T12:53:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56816",
    "user": "mstreng"
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

archive/issue_comments_056817.json:
```json
{
    "body": "Please rebase to sage-7.1.beta2 (in particular, `sage.rings.arith` has moved to `sage.arith.all`) and use the [standard copyright template](http://doc.sagemath.org/html/en/developer/coding_basics.html#headings-of-sage-library-code-files) for the newly added file.\n\nIf you have done this, you can set this ticket back to positive review.",
    "created_at": "2016-02-05T13:18:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56817",
    "user": "jdemeyer"
}
```

Please rebase to sage-7.1.beta2 (in particular, `sage.rings.arith` has moved to `sage.arith.all`) and use the [standard copyright template](http://doc.sagemath.org/html/en/developer/coding_basics.html#headings-of-sage-library-code-files) for the newly added file.

If you have done this, you can set this ticket back to positive review.



---

archive/issue_comments_056818.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2016-02-05T13:18:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56818",
    "user": "jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_056819.json:
```json
{
    "body": "You might also want to fix these `pyflakes` warnings:\n\n```\nsrc/sage/schemes/plane_conics/con_rational_function_field.py:25: 'NumberField' imported but unused\nsrc/sage/schemes/plane_conics/con_rational_function_field.py:26: 'identity_matrix' imported but unused\nsrc/sage/schemes/plane_conics/con_rational_function_field.py:32: redefinition of unused 'vector' from line 30\n```\n",
    "created_at": "2016-02-05T13:23:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56819",
    "user": "jdemeyer"
}
```

You might also want to fix these `pyflakes` warnings:

```
src/sage/schemes/plane_conics/con_rational_function_field.py:25: 'NumberField' imported but unused
src/sage/schemes/plane_conics/con_rational_function_field.py:26: 'identity_matrix' imported but unused
src/sage/schemes/plane_conics/con_rational_function_field.py:32: redefinition of unused 'vector' from line 30
```




---

archive/issue_comments_056820.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. Last 10 new commits:",
    "created_at": "2016-02-07T22:33:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56820",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. Last 10 new commits:



---

archive/issue_comments_056821.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2016-02-07T22:35:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56821",
    "user": "lackermans"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_056822.json:
```json
{
    "body": "Changing status from positive_review to needs_review.",
    "created_at": "2016-02-08T07:28:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56822",
    "user": "jdemeyer"
}
```

Changing status from positive_review to needs_review.



---

archive/issue_comments_056823.json:
```json
{
    "body": "10 new commits? Sorry, but this needs to be reviewed (not by me).",
    "created_at": "2016-02-08T07:28:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56823",
    "user": "jdemeyer"
}
```

10 new commits? Sorry, but this needs to be reviewed (not by me).



---

archive/issue_comments_056824.json:
```json
{
    "body": "This is malformatted:\n\n```\nEXAMPLES:\n    \n    Create a conic::\n\n        sage: K = FractionField(PolynomialRing(QQ, 't'))\n```\n\nIt should be\n\n```\nEXAMPLES:\n    \nCreate a conic::\n\n    sage: K = FractionField(PolynomialRing(QQ, 't'))\n```\n",
    "created_at": "2016-02-08T07:30:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56824",
    "user": "jdemeyer"
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

archive/issue_comments_056825.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2016-02-08T07:30:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56825",
    "user": "jdemeyer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_056826.json:
```json
{
    "body": "Please do this:\n\nReplying to [comment:25 jdemeyer]:\n> use the [standard copyright template](http://doc.sagemath.org/html/en/developer/coding_basics.html#headings-of-sage-library-code-files) for the newly added file.",
    "created_at": "2016-02-08T07:30:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56826",
    "user": "jdemeyer"
}
```

Please do this:

Replying to [comment:25 jdemeyer]:
> use the [standard copyright template](http://doc.sagemath.org/html/en/developer/coding_basics.html#headings-of-sage-library-code-files) for the newly added file.



---

archive/issue_comments_056827.json:
```json
{
    "body": "Replying to [comment:29 jdemeyer]:\n> 10 new commits? Sorry, but this needs to be reviewed (not by me).\nOnly the last 3 are new",
    "created_at": "2016-02-08T11:22:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56827",
    "user": "lackermans"
}
```

Replying to [comment:29 jdemeyer]:
> 10 new commits? Sorry, but this needs to be reviewed (not by me).
Only the last 3 are new



---

archive/issue_comments_056828.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-02-08T11:25:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56828",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_056829.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2016-02-08T11:27:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56829",
    "user": "lackermans"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_056830.json:
```json
{
    "body": "Replying to [comment:31 jdemeyer]:\n> Please do this:\n> \n> Replying to [comment:25 jdemeyer]:\n> > use the [standard copyright template](http://doc.sagemath.org/html/en/developer/coding_basics.html#headings-of-sage-library-code-files) for the newly added file.\n\nSorry, I misunderstood your last comment. All should be okay now.",
    "created_at": "2016-02-08T11:27:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56830",
    "user": "lackermans"
}
```

Replying to [comment:31 jdemeyer]:
> Please do this:
> 
> Replying to [comment:25 jdemeyer]:
> > use the [standard copyright template](http://doc.sagemath.org/html/en/developer/coding_basics.html#headings-of-sage-library-code-files) for the newly added file.

Sorry, I misunderstood your last comment. All should be okay now.



---

archive/issue_comments_056831.json:
```json
{
    "body": "Thanks Jeroen. I checked the changes and documentation html, and I ran the doctests again.",
    "created_at": "2016-02-11T12:07:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56831",
    "user": "mstreng"
}
```

Thanks Jeroen. I checked the changes and documentation html, and I ran the doctests again.



---

archive/issue_comments_056832.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2016-02-11T12:07:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56832",
    "user": "mstreng"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_056833.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2016-02-11T23:26:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6881#issuecomment-56833",
    "user": "vbraun"
}
```

Resolution: fixed
