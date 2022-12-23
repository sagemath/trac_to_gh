# Issue 9809: Heisenbug in RationalPolyhedralCone.facets

archive/issues_009809.json:
```json
{
    "body": "Assignee: mhampton\n\nCC:  novoselt\n\nThe `faces` method of a cone in a fan manages to screw up subsequent `facet` output:\n\n```\nsage: cone = toric_varieties.dP8().fan().generating_cone(0)\nsage: cone\n2-d cone of Rational polyhedral fan in 2-d lattice N\nsage: cone.facets()\n(1-d cone of Rational polyhedral fan in 2-d lattice N, 1-d cone of Rational polyhedral fan in 2-d lattice N)\nsage: cone.faces()\n((0-d cone of Rational polyhedral fan in 2-d lattice N,), (1-d cone of Rational polyhedral fan in 2-d lattice N, 1-d cone of Rational polyhedral fan in 2-d lattice N), (2-d cone of Rational polyhedral fan in 2-d lattice N,))\nsage: cone.facets()\n(2-d cone of Rational polyhedral fan in 2-d lattice N,)\n```\n\nThis is on vanilla Sage 4.5.2 without any patches applied. Andrey, I think its somewhere in your code so you'll probably find it faster than I can.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9810\n\n",
    "created_at": "2010-08-26T21:12:05Z",
    "labels": [
        "geometry",
        "major",
        "bug"
    ],
    "title": "Heisenbug in RationalPolyhedralCone.facets",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9809",
    "user": "vbraun"
}
```
Assignee: mhampton

CC:  novoselt

The `faces` method of a cone in a fan manages to screw up subsequent `facet` output:

```
sage: cone = toric_varieties.dP8().fan().generating_cone(0)
sage: cone
2-d cone of Rational polyhedral fan in 2-d lattice N
sage: cone.facets()
(1-d cone of Rational polyhedral fan in 2-d lattice N, 1-d cone of Rational polyhedral fan in 2-d lattice N)
sage: cone.faces()
((0-d cone of Rational polyhedral fan in 2-d lattice N,), (1-d cone of Rational polyhedral fan in 2-d lattice N, 1-d cone of Rational polyhedral fan in 2-d lattice N), (2-d cone of Rational polyhedral fan in 2-d lattice N,))
sage: cone.facets()
(2-d cone of Rational polyhedral fan in 2-d lattice N,)
```

This is on vanilla Sage 4.5.2 without any patches applied. Andrey, I think its somewhere in your code so you'll probably find it faster than I can.

Issue created by migration from https://trac.sagemath.org/ticket/9810





---

archive/issue_comments_096736.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-08-26T21:31:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9809",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9809#issuecomment-96736",
    "user": "novoselt"
}
```

Attachment



---

archive/issue_comments_096737.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-26T21:33:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9809",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9809#issuecomment-96737",
    "user": "novoselt"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_096738.json:
```json
{
    "body": "Should be 2 instead of 1... Thanks for catching!",
    "created_at": "2010-08-26T21:33:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9809",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9809#issuecomment-96738",
    "user": "novoselt"
}
```

Should be 2 instead of 1... Thanks for catching!



---

archive/issue_comments_096739.json:
```json
{
    "body": "Fixes it!",
    "created_at": "2010-08-26T21:52:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9809",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9809#issuecomment-96739",
    "user": "vbraun"
}
```

Fixes it!



---

archive/issue_comments_096740.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-08-26T21:52:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9809",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9809#issuecomment-96740",
    "user": "vbraun"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_096741.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-15T09:57:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9809",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9809#issuecomment-96741",
    "user": "mpatel"
}
```

Resolution: fixed
