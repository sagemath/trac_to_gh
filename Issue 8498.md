# Issue 8498: bug in has_good_reduction for a point on an elliptic curve over a number field

archive/issues_008498.json:
```json
{
    "body": "Assignee: cremona\n\nJean Gillibert reported me the following bug. Define\n\n\n```\nE = EllipticCurve('11a1')\nK.<t> = NumberField(x^2+47)\nEK = E.base_extend(K)\nT = EK(5,5)\nP = EK(-2, -1/2*t - 1/2)\np = K.ideal(11)\n```\n\n\nThen the following works fine\n\n\n```\nsage: T.has_good_reduction(p)\nFalse\n```\n\n\nbut not this one :\n\n\n```\nP.has_good_reduction(p)\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8498\n\n",
    "created_at": "2010-03-11T10:39:16Z",
    "labels": [
        "elliptic curves",
        "major",
        "bug"
    ],
    "title": "bug in has_good_reduction for a point on an elliptic curve over a number field",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8498",
    "user": "wuthrich"
}
```
Assignee: cremona

Jean Gillibert reported me the following bug. Define


```
E = EllipticCurve('11a1')
K.<t> = NumberField(x^2+47)
EK = E.base_extend(K)
T = EK(5,5)
P = EK(-2, -1/2*t - 1/2)
p = K.ideal(11)
```


Then the following works fine


```
sage: T.has_good_reduction(p)
False
```


but not this one :


```
P.has_good_reduction(p)
```



Issue created by migration from https://trac.sagemath.org/ticket/8498





---

archive/issue_comments_076712.json:
```json
{
    "body": "More precisely, I get the error\n\n\n```\n/home/pmzcw/prog/sage/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/ell_point.pyc in has_good_reduction(self, P)\n   1554         F = Emin.defining_polynomial()\n   1555         for v in F.variables():\n-> 1556             if F.derivative(v)(xyz).valuation(P) == 0:\n   1557                 return True\n   1558         return False\n\n/home/pmzcw/prog/sage/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.Element.__getattr__ (sage/structure/element.c:2743)()\n\n/home/pmzcw/prog/sage/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.getattr_from_other_class (sage/structure/parent.c:2844)()\n\n/home/pmzcw/prog/sage/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.raise_attribute_error (sage/structure/parent.c:2611)()\n\nAttributeError: 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular' object has no attribute 'valuation'\n```\n",
    "created_at": "2010-03-11T10:39:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8498#issuecomment-76712",
    "user": "wuthrich"
}
```

More precisely, I get the error


```
/home/pmzcw/prog/sage/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/ell_point.pyc in has_good_reduction(self, P)
   1554         F = Emin.defining_polynomial()
   1555         for v in F.variables():
-> 1556             if F.derivative(v)(xyz).valuation(P) == 0:
   1557                 return True
   1558         return False

/home/pmzcw/prog/sage/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.Element.__getattr__ (sage/structure/element.c:2743)()

/home/pmzcw/prog/sage/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.getattr_from_other_class (sage/structure/parent.c:2844)()

/home/pmzcw/prog/sage/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.raise_attribute_error (sage/structure/parent.c:2611)()

AttributeError: 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular' object has no attribute 'valuation'
```




---

archive/issue_comments_076713.json:
```json
{
    "body": "I'll look into this -- my code :(",
    "created_at": "2010-03-11T13:27:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8498#issuecomment-76713",
    "user": "cremona"
}
```

I'll look into this -- my code :(



---

archive/issue_comments_076714.json:
```json
{
    "body": "This is weird:  I evaluate a polynomial f in K[X,Y,Z] at a triple [x,y,z], but the value lands up not in K but in K[X,Y,Z] again (as a constant polynomial, rather than an actual constant in K).  This is not what the `_call__` function for multivariable polynomials says.  I can fix this here, but it is symptomatic of a deeper problem.",
    "created_at": "2010-03-11T14:40:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8498#issuecomment-76714",
    "user": "cremona"
}
```

This is weird:  I evaluate a polynomial f in K[X,Y,Z] at a triple [x,y,z], but the value lands up not in K but in K[X,Y,Z] again (as a constant polynomial, rather than an actual constant in K).  This is not what the `_call__` function for multivariable polynomials says.  I can fix this here, but it is symptomatic of a deeper problem.



---

archive/issue_comments_076715.json:
```json
{
    "body": "Attachment [trac_8498-has_good_reduction.patch](tarball://root/attachments/some-uuid/ticket8498/trac_8498-has_good_reduction.patch) by cremona created at 2010-03-11 15:24:41\n\nApplies to 4.3.4.alpha1",
    "created_at": "2010-03-11T15:24:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8498#issuecomment-76715",
    "user": "cremona"
}
```

Attachment [trac_8498-has_good_reduction.patch](tarball://root/attachments/some-uuid/ticket8498/trac_8498-has_good_reduction.patch) by cremona created at 2010-03-11 15:24:41

Applies to 4.3.4.alpha1



---

archive/issue_comments_076716.json:
```json
{
    "body": "Patch attached, applies to 4.3.4.alpha1.  I tested everything in sage/schemes/elliptic curves, and included a doctest example showing that the example above now works.",
    "created_at": "2010-03-11T15:26:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8498#issuecomment-76716",
    "user": "cremona"
}
```

Patch attached, applies to 4.3.4.alpha1.  I tested everything in sage/schemes/elliptic curves, and included a doctest example showing that the example above now works.



---

archive/issue_comments_076717.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-11T15:26:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8498#issuecomment-76717",
    "user": "cremona"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_076718.json:
```json
{
    "body": "Changing keywords from \"\" to \"good reduction points\".",
    "created_at": "2010-03-11T15:26:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8498#issuecomment-76718",
    "user": "cremona"
}
```

Changing keywords from "" to "good reduction points".



---

archive/issue_comments_076719.json:
```json
{
    "body": "All tests pass. Thanks for the very fast resolution of this.\n\nAs you said, the patch fixes the problem for the `has_good_reduction` function, but the same issue may arise else where. Could you open another ticket for the general problem ?",
    "created_at": "2010-03-11T21:12:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8498#issuecomment-76719",
    "user": "wuthrich"
}
```

All tests pass. Thanks for the very fast resolution of this.

As you said, the patch fixes the problem for the `has_good_reduction` function, but the same issue may arise else where. Could you open another ticket for the general problem ?



---

archive/issue_comments_076720.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-11T21:12:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8498#issuecomment-76720",
    "user": "wuthrich"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_076721.json:
```json
{
    "body": "Replying to [comment:5 wuthrich]:\n> All tests pass. Thanks for the very fast resolution of this.\n> \n> As you said, the patch fixes the problem for the `has_good_reduction` function, but the same issue may arise else where. Could you open another ticket for the general problem ?\n\nSee #8502",
    "created_at": "2010-03-11T22:08:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8498#issuecomment-76721",
    "user": "cremona"
}
```

Replying to [comment:5 wuthrich]:
> All tests pass. Thanks for the very fast resolution of this.
> 
> As you said, the patch fixes the problem for the `has_good_reduction` function, but the same issue may arise else where. Could you open another ticket for the general problem ?

See #8502



---

archive/issue_comments_076722.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-12T04:53:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8498#issuecomment-76722",
    "user": "mvngu"
}
```

Resolution: fixed
