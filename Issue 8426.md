# Issue 8426: polynomial * constant does not work if constant is a numpy type

archive/issues_008426.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @williamstein @robertwb\n\nThis should work:\n\n\n```\nimport numpy\nR.<x>=RR[]\nx*numpy.float32('23.0')\n```\n\n\nInstead, I get:\n\n```\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/jason/tmp/<ipython console> in <module>()\n\n/home/jason/sage/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.RingElement.__mul__ (sage/structure/element.c:11337)()\n\n/home/jason/sage/local/lib/python2.6/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6994)()\n\nTypeError: unsupported operand parent(s) for '*': 'Univariate Polynomial Ring in x over Real Field with 53 bits of precision' and '<type 'numpy.float32'>'\n```\n\n\nNote that this does work:\n\n\n```\nsage: numpy.float32('23.0')*x\n23.0000000000000*x\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8426\n\n",
    "created_at": "2010-03-03T05:17:18Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "polynomial * constant does not work if constant is a numpy type",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8426",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @aghitza

CC:  @williamstein @robertwb

This should work:


```
import numpy
R.<x>=RR[]
x*numpy.float32('23.0')
```


Instead, I get:

```
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/jason/tmp/<ipython console> in <module>()

/home/jason/sage/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.RingElement.__mul__ (sage/structure/element.c:11337)()

/home/jason/sage/local/lib/python2.6/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6994)()

TypeError: unsupported operand parent(s) for '*': 'Univariate Polynomial Ring in x over Real Field with 53 bits of precision' and '<type 'numpy.float32'>'
```


Note that this does work:


```
sage: numpy.float32('23.0')*x
23.0000000000000*x
```



Issue created by migration from https://trac.sagemath.org/ticket/8426





---

archive/issue_comments_075418.json:
```json
{
    "body": "Now works, but see #15695.",
    "created_at": "2014-03-15T18:55:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8426",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8426#issuecomment-75418",
    "user": "https://github.com/mezzarobba"
}
```

Now works, but see #15695.



---

archive/issue_comments_075419.json:
```json
{
    "body": "Hello,\n\nI propose to close this as duplicates because of #18076 that fixes it. With the branch applied I got\n\n```\nsage: import numpy\nsage: R.<x> = RR[]\nsage: x * numpy.float32('23.0')\n23.0000000000000*x\n```\n\nand even the pushout works\n\n```\nsage: R.<x> = ZZ[]\nsage: x * numpy.float32('23.0')\n23.0*x\nsage: parent(_)\nUnivariate Polynomial Ring in x over Real Double Field\n```\n\n\nVincent",
    "created_at": "2015-03-28T11:57:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8426",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8426#issuecomment-75419",
    "user": "https://github.com/videlec"
}
```

Hello,

I propose to close this as duplicates because of #18076 that fixes it. With the branch applied I got

```
sage: import numpy
sage: R.<x> = RR[]
sage: x * numpy.float32('23.0')
23.0000000000000*x
```

and even the pushout works

```
sage: R.<x> = ZZ[]
sage: x * numpy.float32('23.0')
23.0*x
sage: parent(_)
Univariate Polynomial Ring in x over Real Double Field
```


Vincent



---

archive/issue_comments_075420.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2015-03-28T11:57:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8426",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8426#issuecomment-75420",
    "user": "https://github.com/videlec"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_075421.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2015-04-23T09:40:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8426",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8426#issuecomment-75421",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_075422.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2015-04-23T14:52:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8426",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8426#issuecomment-75422",
    "user": "https://github.com/vbraun"
}
```

Resolution: duplicate



---

archive/issue_events_008611.json:
```json
{
    "actor": "@vbraun",
    "created_at": "2015-04-23T14:52:09Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8426",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8426#event-8611"
}
```
