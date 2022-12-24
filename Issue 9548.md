# Issue 9548: Sage does not support infinities with complex direction

archive/issues_009548.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nThis should do something reasonable:\n\n\n```\nsage: Infinity * I\n---------------------------------------------------------------------------\nArithmeticError                           Traceback (most recent call last)\n\n/home/fredrik/sage/<ipython console> in <module>()\n\n/home/fredrik/sage/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.RingElement.__mul__ (sage/structure/element.c:11428)()\n\n/home/fredrik/sage/local/lib/python2.6/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6123)()\n\n/home/fredrik/sage/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.RingElement.__mul__ (sage/structure/element.c:11356)()\n\n/home/fredrik/sage/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression._mul_ (sage/symbolic/expression.cpp:11042)()\n\nArithmeticError: x*Infinity with non real x encountered.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9548\n\n",
    "created_at": "2010-07-19T08:27:56Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-wishlist",
    "title": "Sage does not support infinities with complex direction",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9548",
    "user": "fredrik.johansson"
}
```
Assignee: AlexGhitza

This should do something reasonable:


```
sage: Infinity * I
---------------------------------------------------------------------------
ArithmeticError                           Traceback (most recent call last)

/home/fredrik/sage/<ipython console> in <module>()

/home/fredrik/sage/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.RingElement.__mul__ (sage/structure/element.c:11428)()

/home/fredrik/sage/local/lib/python2.6/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6123)()

/home/fredrik/sage/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.RingElement.__mul__ (sage/structure/element.c:11356)()

/home/fredrik/sage/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression._mul_ (sage/symbolic/expression.cpp:11042)()

ArithmeticError: x*Infinity with non real x encountered.
```


Issue created by migration from https://trac.sagemath.org/ticket/9548





---

archive/issue_comments_092042.json:
```json
{
    "body": "`I*Infinity` now returns an element of the symbolic ring. I'm leaving the ticket open (as a wishlist item), though, since it would probably make sense to make infinities with complex direction more similar to\u00a0\u00b1\u221e.",
    "created_at": "2014-02-02T11:40:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9548",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9548#issuecomment-92042",
    "user": "mmezzarobba"
}
```

`I*Infinity` now returns an element of the symbolic ring. I'm leaving the ticket open (as a wishlist item), though, since it would probably make sense to make infinities with complex direction more similar to ±∞.



---

archive/issue_comments_092043.json:
```json
{
    "body": "This may be a stupid question but now that we have complex (unsigned) infinity, shouldn't that be the result of `I*Infinity`?",
    "created_at": "2015-04-21T14:42:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9548",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9548#issuecomment-92043",
    "user": "rws"
}
```

This may be a stupid question but now that we have complex (unsigned) infinity, shouldn't that be the result of `I*Infinity`?



---

archive/issue_comments_092044.json:
```json
{
    "body": "I don't know. It would definitely be useful to be able to write things like integrals from 0 to i\u221e, (1+i)\u221e, or exp(i\u03b8)\u221e. Whether `I*infinity` should return on of these \u201cdirectional\u201d infinities or unsigned infinity is another question. Without thinking, I'd say `I*PlusInfinity()` should return the former and `I*UnsignedInfinity()` the latter.",
    "created_at": "2015-04-22T09:51:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9548",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9548#issuecomment-92044",
    "user": "mmezzarobba"
}
```

I don't know. It would definitely be useful to be able to write things like integrals from 0 to i∞, (1+i)∞, or exp(iθ)∞. Whether `I*infinity` should return on of these “directional” infinities or unsigned infinity is another question. Without thinking, I'd say `I*PlusInfinity()` should return the former and `I*UnsignedInfinity()` the latter.
