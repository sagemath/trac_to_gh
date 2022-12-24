# Issue 3856: Multiply between QQ and GF(7) gives exception

archive/issues_003856.json:
```json
{
    "body": "Assignee: robertwb\n\n\n```\nsage: 1/4*GF(7)['t'](1)\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/gfurnish/coercion-test/sage-3.1.alpha2-sage.math-only-x86_64-Linux/<ipython console> in <module>()\n\n/home/gfurnish/coercion-test/sage-3.1.alpha2-sage.math-only-x86_64-Linux/element.pyx in sage.structure.element.RingElement.__mul__ (sage/structure/element.c:9190)()\n\n/home/gfurnish/coercion-test/sage-3.1.alpha2-sage.math-only-x86_64-Linux/coerce.pyx in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6288)()\n\nTypeError: unsupported operand parent(s) for '*': 'Rational Field' and 'Univariate Polynomial Ring in t over Finite Field of size 7'\n```\n\nThis is implied to work by the following doctest in coercion_maps.pyx\n\n```\n            sage: mor = NamedConvertMap(SR, GF(7)[['t']], '_polynomial_')\n            sage: mor(x^2/4+1)\n            1 + 2*t^2\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3856\n\n",
    "created_at": "2008-08-14T20:53:11Z",
    "labels": [
        "coercion",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Multiply between QQ and GF(7) gives exception",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3856",
    "user": "gfurnish"
}
```
Assignee: robertwb


```
sage: 1/4*GF(7)['t'](1)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/gfurnish/coercion-test/sage-3.1.alpha2-sage.math-only-x86_64-Linux/<ipython console> in <module>()

/home/gfurnish/coercion-test/sage-3.1.alpha2-sage.math-only-x86_64-Linux/element.pyx in sage.structure.element.RingElement.__mul__ (sage/structure/element.c:9190)()

/home/gfurnish/coercion-test/sage-3.1.alpha2-sage.math-only-x86_64-Linux/coerce.pyx in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6288)()

TypeError: unsupported operand parent(s) for '*': 'Rational Field' and 'Univariate Polynomial Ring in t over Finite Field of size 7'
```

This is implied to work by the following doctest in coercion_maps.pyx

```
            sage: mor = NamedConvertMap(SR, GF(7)[['t']], '_polynomial_')
            sage: mor(x^2/4+1)
            1 + 2*t^2
```


Issue created by migration from https://trac.sagemath.org/ticket/3856





---

archive/issue_comments_027465.json:
```json
{
    "body": "I don't think this is a bug, this should *not* work. Conversion != Coercion.",
    "created_at": "2008-08-14T21:31:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3856#issuecomment-27465",
    "user": "robertwb"
}
```

I don't think this is a bug, this should *not* work. Conversion != Coercion.



---

archive/issue_comments_027466.json:
```json
{
    "body": "So _polynomial_ should also create any underlying conversions needed?",
    "created_at": "2008-08-15T19:31:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3856#issuecomment-27466",
    "user": "gfurnish"
}
```

So _polynomial_ should also create any underlying conversions needed?



---

archive/issue_comments_027467.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2008-08-26T09:58:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3856#issuecomment-27467",
    "user": "mabshoff"
}
```

Resolution: invalid



---

archive/issue_comments_027468.json:
```json
{
    "body": "Replying to [comment:1 robertwb]:\n> I don't think this is a bug, this should *not* work. Conversion != Coercion. \n\nHence this is invalid.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-26T09:58:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3856#issuecomment-27468",
    "user": "mabshoff"
}
```

Replying to [comment:1 robertwb]:
> I don't think this is a bug, this should *not* work. Conversion != Coercion. 

Hence this is invalid.

Cheers,

Michael
