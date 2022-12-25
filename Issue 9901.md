# Issue 9901: base_extend() not implemented in MPolynomialRing

archive/issues_009901.json:
```json
{
    "body": "Assignee: @malb\n\nCC:  @novoselt @nilesjohnson\n\nThe base `class Ring` defines `base_extend()`, but the implementation needs to be overridden in the derived class `MPolynomialRing`:\n\n```\nsage: sage: P.<x,y,z> = PolynomialRing(QQ,'x, y, z'); P\nMultivariate Polynomial Ring in x, y, z over Rational Field\nsage: P.base_extend(CC)\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/vbraun/opt/sage-4.5.3/devel/sage-main/<ipython console> in <module>()\n\n/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/sage/rings/ring.so in sage.rings.ring.Ring.base_extend (sage/rings/ring.c:3190)()\n\nTypeError: no base extension defined\n```\n\nThe patch implements the override and adds documentation.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9902\n\n",
    "created_at": "2010-09-12T11:15:06Z",
    "labels": [
        "component: commutative algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "base_extend() not implemented in MPolynomialRing",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9901",
    "user": "https://github.com/vbraun"
}
```
Assignee: @malb

CC:  @novoselt @nilesjohnson

The base `class Ring` defines `base_extend()`, but the implementation needs to be overridden in the derived class `MPolynomialRing`:

```
sage: sage: P.<x,y,z> = PolynomialRing(QQ,'x, y, z'); P
Multivariate Polynomial Ring in x, y, z over Rational Field
sage: P.base_extend(CC)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/vbraun/opt/sage-4.5.3/devel/sage-main/<ipython console> in <module>()

/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/sage/rings/ring.so in sage.rings.ring.Ring.base_extend (sage/rings/ring.c:3190)()

TypeError: no base extension defined
```

The patch implements the override and adds documentation.

Issue created by migration from https://trac.sagemath.org/ticket/9902





---

archive/issue_comments_098273.json:
```json
{
    "body": "Attachment [trax_9902_fix_base_extension.patch](tarball://root/attachments/some-uuid/ticket9902/trax_9902_fix_base_extension.patch) by @vbraun created at 2010-09-12 11:17:44\n\nInitial patch",
    "created_at": "2010-09-12T11:17:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9901",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9901#issuecomment-98273",
    "user": "https://github.com/vbraun"
}
```

Attachment [trax_9902_fix_base_extension.patch](tarball://root/attachments/some-uuid/ticket9902/trax_9902_fix_base_extension.patch) by @vbraun created at 2010-09-12 11:17:44

Initial patch



---

archive/issue_comments_098274.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-09-17T14:05:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9901",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9901#issuecomment-98274",
    "user": "https://github.com/vbraun"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_098275.json:
```json
{
    "body": "Andrey, I wrote this patch a while a go to be able to extend the base field of the toric coordinate ring. It might be useful...",
    "created_at": "2010-12-20T19:16:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9901",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9901#issuecomment-98275",
    "user": "https://github.com/vbraun"
}
```

Andrey, I wrote this patch a while a go to be able to extend the base field of the toric coordinate ring. It might be useful...



---

archive/issue_comments_098276.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2010-12-20T19:53:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9901",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9901#issuecomment-98276",
    "user": "https://github.com/novoselt"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_098277.json:
```json
{
    "body": "I am not quite sure it is the right approach. It seems to me that we have two methods: `change_ring` that constructs \"the same object but over different ring\" and `base_extend` which does the same, but only if there is a natural coercion. Given this description, it seems to me that there should be only one implementation of `base_extend` in the base class:\n\n```\ndef base_extend(self, R):\n    if R.has_coerce_map(self.base_ring()):\n        return self.change_ring(R)\n    else:\n        raise TypeError(\"%s cannot be extened to %s!\" % (self.base_ring(), R))\n```\n\nand then each derived class should implement `change_ring` only. (If the detailed error message breaks a lot of doctests I am fine with keeping the current one.) Thoughts?\n\nThere is also discrepancy between actual argument names and their description in documentation (`base_ring` vs. `R`).",
    "created_at": "2010-12-20T19:53:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9901",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9901#issuecomment-98277",
    "user": "https://github.com/novoselt"
}
```

I am not quite sure it is the right approach. It seems to me that we have two methods: `change_ring` that constructs "the same object but over different ring" and `base_extend` which does the same, but only if there is a natural coercion. Given this description, it seems to me that there should be only one implementation of `base_extend` in the base class:

```
def base_extend(self, R):
    if R.has_coerce_map(self.base_ring()):
        return self.change_ring(R)
    else:
        raise TypeError("%s cannot be extened to %s!" % (self.base_ring(), R))
```

and then each derived class should implement `change_ring` only. (If the detailed error message breaks a lot of doctests I am fine with keeping the current one.) Thoughts?

There is also discrepancy between actual argument names and their description in documentation (`base_ring` vs. `R`).
