# Issue 9019: Full doctest coverage for sage.categories.map

archive/issues_009019.json:
```json
{
    "body": "Assignee: @nthiery\n\nKeywords: doctest map composition\n\nApart from full doctest coverage for sage.categories.map, the patch provides the following:\n\n1. Test for injectivity and surjectivity of `MatrixMorphism`:\n\n```\nsage: V1 = QQ^2\nsage: V2 = QQ^3\nsage: phi = V1.hom(Matrix([[1,2],[3,4],[5,6]]),V2)\nsage: phi.is_injective()\nTrue\nsage: phi.is_surjective()\nFalse\nsage: psi = V2.hom(Matrix([[1,2,3],[4,5,6]]),V1)\nsage: psi.is_injective()\nFalse\nsage: psi.is_surjective()\nTrue\n```\n\n2. Composition of a `RingHomomorphism_im_gens` with another ring homomorphism (this used to return a `FormalCompositeMap`, which is not very efficient):\n\n```\nsage: R.<x,y> = QQ[]\nsage: S.<a,b> = QQ[]\nsage: f = R.hom([a+b,a-b])\nsage: g = S.hom(Frac(S))\nsage: g*f\nRing morphism:\n  From: Multivariate Polynomial Ring in x, y over Rational Field\n  To:   Fraction Field of Multivariate Polynomial Ring in a, b over Rational Field\n  Defn: x |--> a + b\n        y |--> a - b\nsage: h = S.hom([x+y,x-y])\nsage: h*f\nRing endomorphism of Multivariate Polynomial Ring in x, y over Rational Field\n  Defn: x |--> 2*x\n        y |--> 2*y\n```\n\n3. Comparison of `FormalCompositeMap`s:\n\n```\nsage: R.<x,y> = QQ[]\nsage: S.<a,b> = QQ[]\nsage: f = R.hom([a+b,a-b])\nsage: g = S.hom([x+y,x-y])\nsage: from sage.categories.map import FormalCompositeMap\nsage: H = Hom(R,R,Rings())\nsage: m = FormalCompositeMap(H,f,g)\nsage: m == loads(dumps(m))  # this used to be False!\nTrue\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9019\n\n",
    "closed_at": "2010-06-05T21:59:26Z",
    "created_at": "2010-05-22T17:34:21Z",
    "labels": [
        "component: categories",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.4",
    "title": "Full doctest coverage for sage.categories.map",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9019",
    "user": "https://github.com/simon-king-jena"
}
```
Assignee: @nthiery

Keywords: doctest map composition

Apart from full doctest coverage for sage.categories.map, the patch provides the following:

1. Test for injectivity and surjectivity of `MatrixMorphism`:

```
sage: V1 = QQ^2
sage: V2 = QQ^3
sage: phi = V1.hom(Matrix([[1,2],[3,4],[5,6]]),V2)
sage: phi.is_injective()
True
sage: phi.is_surjective()
False
sage: psi = V2.hom(Matrix([[1,2,3],[4,5,6]]),V1)
sage: psi.is_injective()
False
sage: psi.is_surjective()
True
```

2. Composition of a `RingHomomorphism_im_gens` with another ring homomorphism (this used to return a `FormalCompositeMap`, which is not very efficient):

```
sage: R.<x,y> = QQ[]
sage: S.<a,b> = QQ[]
sage: f = R.hom([a+b,a-b])
sage: g = S.hom(Frac(S))
sage: g*f
Ring morphism:
  From: Multivariate Polynomial Ring in x, y over Rational Field
  To:   Fraction Field of Multivariate Polynomial Ring in a, b over Rational Field
  Defn: x |--> a + b
        y |--> a - b
sage: h = S.hom([x+y,x-y])
sage: h*f
Ring endomorphism of Multivariate Polynomial Ring in x, y over Rational Field
  Defn: x |--> 2*x
        y |--> 2*y
```

3. Comparison of `FormalCompositeMap`s:

```
sage: R.<x,y> = QQ[]
sage: S.<a,b> = QQ[]
sage: f = R.hom([a+b,a-b])
sage: g = S.hom([x+y,x-y])
sage: from sage.categories.map import FormalCompositeMap
sage: H = Hom(R,R,Rings())
sage: m = FormalCompositeMap(H,f,g)
sage: m == loads(dumps(m))  # this used to be False!
True
```


Issue created by migration from https://trac.sagemath.org/ticket/9019





---

archive/issue_comments_083320.json:
```json
{
    "body": "Attachment [9019_map_doctests.patch](tarball://root/attachments/some-uuid/ticket9019/9019_map_doctests.patch) by @simon-king-jena created at 2010-05-22 17:37:07\n\nis_injective/is_surjective for MatrixMorphism, cmp for FormalCompositeMap, more efficient composition of ring homomorphisms, full doctest coverage for sage.categories.map",
    "created_at": "2010-05-22T17:37:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9019",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9019#issuecomment-83320",
    "user": "https://github.com/simon-king-jena"
}
```

Attachment [9019_map_doctests.patch](tarball://root/attachments/some-uuid/ticket9019/9019_map_doctests.patch) by @simon-king-jena created at 2010-05-22 17:37:07

is_injective/is_surjective for MatrixMorphism, cmp for FormalCompositeMap, more efficient composition of ring homomorphisms, full doctest coverage for sage.categories.map



---

archive/issue_comments_083321.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-22T17:37:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9019",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9019#issuecomment-83321",
    "user": "https://github.com/simon-king-jena"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_083322.json:
```json
{
    "body": "Attachment [9019-map-doctest-referee.patch](tarball://root/attachments/some-uuid/ticket9019/9019-map-doctest-referee.patch) by @robertwb created at 2010-05-25 01:15:10\n\nLooks good, positive review, modulo approval of my tiny referee patch that adds an actual example for Map.section()",
    "created_at": "2010-05-25T01:15:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9019",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9019#issuecomment-83322",
    "user": "https://github.com/robertwb"
}
```

Attachment [9019-map-doctest-referee.patch](tarball://root/attachments/some-uuid/ticket9019/9019-map-doctest-referee.patch) by @robertwb created at 2010-05-25 01:15:10

Looks good, positive review, modulo approval of my tiny referee patch that adds an actual example for Map.section()



---

archive/issue_comments_083323.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-25T07:27:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9019",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9019#issuecomment-83323",
    "user": "https://github.com/simon-king-jena"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_083324.json:
```json
{
    "body": "Replying to [comment:2 robertwb]:\n> Looks good, positive review, modulo approval of my tiny referee patch that adds an actual example for Map.section()\n\n\nDear Robert,\n\nThank you for the review and the example!\n\nI don't know if I am in the position to approve your example, but it works for me, so that I take this as a positive review.\n\nIf nobody opposes, I'll insert your name as a reviewer and mark the ticket accordingly.\n\nCheers,\n\nSimon",
    "created_at": "2010-05-25T07:27:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9019",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9019#issuecomment-83324",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:2 robertwb]:
> Looks good, positive review, modulo approval of my tiny referee patch that adds an actual example for Map.section()


Dear Robert,

Thank you for the review and the example!

I don't know if I am in the position to approve your example, but it works for me, so that I take this as a positive review.

If nobody opposes, I'll insert your name as a reviewer and mark the ticket accordingly.

Cheers,

Simon



---

archive/issue_events_022071.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-06-05T21:59:26Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9019",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9019#event-22071"
}
```



---

archive/issue_comments_083325.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-05T21:59:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9019",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9019#issuecomment-83325",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
