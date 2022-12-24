# Issue 8555: Unexpected behaviour of symbolic zero.

archive/issues_008555.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  jakobkroeker\n\nConsider the following commands:\n\n```\nsage: x = PolynomialRing(RealField(42), 'x', 2).gens() \nsage: x[0]^2 - x[1]^2 == SR(1)\nx0^2 - x1^2 == 1\nsage: x[0]^2 - x[1]^2 == SR(0)\nFalse\n```\n\n\nIt seems the symbolic zero is behaving in an unexpected way.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8555\n\n",
    "created_at": "2010-03-17T20:17:19Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "title": "Unexpected behaviour of symbolic zero.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8555",
    "user": "lfousse"
}
```
Assignee: @aghitza

CC:  jakobkroeker

Consider the following commands:

```
sage: x = PolynomialRing(RealField(42), 'x', 2).gens() 
sage: x[0]^2 - x[1]^2 == SR(1)
x0^2 - x1^2 == 1
sage: x[0]^2 - x[1]^2 == SR(0)
False
```


It seems the symbolic zero is behaving in an unexpected way.

Issue created by migration from https://trac.sagemath.org/ticket/8555





---

archive/issue_comments_077401.json:
```json
{
    "body": "Changing component from algebra to symbolics.",
    "created_at": "2010-03-17T20:19:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8555#issuecomment-77401",
    "user": "lfousse"
}
```

Changing component from algebra to symbolics.



---

archive/issue_comments_077402.json:
```json
{
    "body": "Changing assignee from @aghitza to @burcin.",
    "created_at": "2010-03-17T20:19:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8555#issuecomment-77402",
    "user": "lfousse"
}
```

Changing assignee from @aghitza to @burcin.



---

archive/issue_comments_077403.json:
```json
{
    "body": "Since we have\n\n```\nsage: SR(0) == x[0]^2 - x[1]^2\n0  == x[0]^2 - x[1]^2\n```\n\nthe patch changes\n\n```\nsage: x[0]^2 - x[1]^2 == SR(0)\nFalse\n```\n\nto\n\n```\nsage: x[0]^2 - x[1]^2 == SR(0)\n x[0]^2 - x[1]^2 == 0\n```\n\nThe same applies to `!=`.\n----\nNew commits:",
    "created_at": "2014-07-26T13:21:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8555#issuecomment-77403",
    "user": "@a-andre"
}
```

Since we have

```
sage: SR(0) == x[0]^2 - x[1]^2
0  == x[0]^2 - x[1]^2
```

the patch changes

```
sage: x[0]^2 - x[1]^2 == SR(0)
False
```

to

```
sage: x[0]^2 - x[1]^2 == SR(0)
 x[0]^2 - x[1]^2 == 0
```

The same applies to `!=`.
----
New commits:



---

archive/issue_comments_077404.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-07-26T13:21:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8555#issuecomment-77404",
    "user": "@a-andre"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_077405.json:
```json
{
    "body": "Perhaps it's better to be a bit more selective than just avoiding the zero shortcut completely. It's only `SR(0)` that has this funny behaviour. All other zeros should be fine. So the test should probably be something like\n\n```\n    if not isinstance(right, sage.symbolic.expression.Expression) and right == 0:\n        return bool(self._MPolynomial_element__element)\n```\n\nNote the chance to the if body.\nThis return value evaluates slightly faster when `self` is in fact 0 and a lot faster if `self` is nonzero (I suspect it kicks down to checking if `self._MPolynomial_element__element.__len__()` is 0, but does so on CPython slot level, so saves quite a bit of lookup).\n\nIt's of course nice to try and make symbolic entities work consistently with MPolynomial, but interacting with SR is not the main purpose of MPolynomial, so you should make sure that measures undertaken for it do not affect other use cases.\n\nI don't have an immediate answer on what the best way is to make available the symbol `sage.symbolic.expression.Expression` (or what the best test is determine reliably and cheaply whether `right` is an element of SR). One way is of course to just `import sage.symbolic.expression`, but it's a little unfortunate to create an apparent dependence (even if that's a circular import, it should be fine, though). Doing the import in the method is not an option.",
    "created_at": "2014-07-26T19:37:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8555#issuecomment-77405",
    "user": "@nbruin"
}
```

Perhaps it's better to be a bit more selective than just avoiding the zero shortcut completely. It's only `SR(0)` that has this funny behaviour. All other zeros should be fine. So the test should probably be something like

```
    if not isinstance(right, sage.symbolic.expression.Expression) and right == 0:
        return bool(self._MPolynomial_element__element)
```

Note the chance to the if body.
This return value evaluates slightly faster when `self` is in fact 0 and a lot faster if `self` is nonzero (I suspect it kicks down to checking if `self._MPolynomial_element__element.__len__()` is 0, but does so on CPython slot level, so saves quite a bit of lookup).

It's of course nice to try and make symbolic entities work consistently with MPolynomial, but interacting with SR is not the main purpose of MPolynomial, so you should make sure that measures undertaken for it do not affect other use cases.

I don't have an immediate answer on what the best way is to make available the symbol `sage.symbolic.expression.Expression` (or what the best test is determine reliably and cheaply whether `right` is an element of SR). One way is of course to just `import sage.symbolic.expression`, but it's a little unfortunate to create an apparent dependence (even if that's a circular import, it should be fine, though). Doing the import in the method is not an option.



---

archive/issue_comments_077406.json:
```json
{
    "body": "Hello,\n\nPeter: On the other hand, fast comparisons with `0` should be done within `__nonzero__` and called via `bool(P)` or possibly `P.is_zero()` that indirectly calls the former.\n\nAndr\u00e9: Could you check that `__nonzero__` is implemented and modify the appropriate part of the code which uses `P == 0` or `P != 0`?\n\nVincent",
    "created_at": "2015-02-01T11:15:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8555#issuecomment-77406",
    "user": "@videlec"
}
```

Hello,

Peter: On the other hand, fast comparisons with `0` should be done within `__nonzero__` and called via `bool(P)` or possibly `P.is_zero()` that indirectly calls the former.

André: Could you check that `__nonzero__` is implemented and modify the appropriate part of the code which uses `P == 0` or `P != 0`?

Vincent



---

archive/issue_comments_077407.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2015-02-01T11:15:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8555#issuecomment-77407",
    "user": "@videlec"
}
```

Changing status from needs_review to needs_work.
