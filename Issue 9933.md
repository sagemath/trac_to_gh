# Issue 9933: Toric divisor class -> divisor lift should be integral

archive/issues_009933.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nCC:  novoselt\n\nAn integral divisor class should lift to an integral divisor. But:\n\n```\nsage: rays = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, 0, 1), (2, -1, -1)]\nsage: cones = [(0, 2, 3), (0, 2, 4), (0, 3, 4), (1, 2, 3), (1, 2, 4), (1, 3, 4)]\nsage: X = ToricVariety(Fan(cones=cones, rays=rays))\nsage: X.rational_class_group().gen(1).lift()\n-1/2*V(z0) + 1/2*V(z1)\n```\n\nThe attached patch fixes this and any doctest fallout.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9934\n\n",
    "created_at": "2010-09-17T14:00:03Z",
    "labels": [
        "algebraic geometry",
        "major",
        "bug"
    ],
    "title": "Toric divisor class -> divisor lift should be integral",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9933",
    "user": "vbraun"
}
```
Assignee: AlexGhitza

CC:  novoselt

An integral divisor class should lift to an integral divisor. But:

```
sage: rays = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, 0, 1), (2, -1, -1)]
sage: cones = [(0, 2, 3), (0, 2, 4), (0, 3, 4), (1, 2, 3), (1, 2, 4), (1, 3, 4)]
sage: X = ToricVariety(Fan(cones=cones, rays=rays))
sage: X.rational_class_group().gen(1).lift()
-1/2*V(z0) + 1/2*V(z1)
```

The attached patch fixes this and any doctest fallout.

Issue created by migration from https://trac.sagemath.org/ticket/9934





---

archive/issue_comments_098906.json:
```json
{
    "body": "Initial patch",
    "created_at": "2010-09-17T14:02:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9933",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9933#issuecomment-98906",
    "user": "vbraun"
}
```

Initial patch



---

archive/issue_comments_098907.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-09-17T14:03:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9933",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9933#issuecomment-98907",
    "user": "vbraun"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_098908.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-09-17T14:03:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9933",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9933#issuecomment-98908",
    "user": "vbraun"
}
```

Attachment



---

archive/issue_comments_098909.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-17T19:08:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9933",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9933#issuecomment-98909",
    "user": "novoselt"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_098910.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2010-09-17T19:08:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9933",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9933#issuecomment-98910",
    "user": "novoselt"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_098911.json:
```json
{
    "body": "Nice improvement! (Not quite defect ;-))\n\nTested on 4.5.3 with all the toric patches that got merged to 4.6.alpha1.",
    "created_at": "2010-09-17T19:08:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9933",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9933#issuecomment-98911",
    "user": "novoselt"
}
```

Nice improvement! (Not quite defect ;-))

Tested on 4.5.3 with all the toric patches that got merged to 4.6.alpha1.



---

archive/issue_comments_098912.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-29T08:39:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9933",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9933#issuecomment-98912",
    "user": "mpatel"
}
```

Resolution: fixed
