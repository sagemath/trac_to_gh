# Issue 8555: Unexpected behaviour of symbolic zero.

Issue created by migration from https://trac.sagemath.org/ticket/8555

Original creator: lfousse

Original creation time: 2010-03-17 20:17:19

Assignee: AlexGhitza

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


---

Comment by lfousse created at 2010-03-17 20:19:32

Changing component from algebra to symbolics.


---

Comment by lfousse created at 2010-03-17 20:19:32

Changing assignee from AlexGhitza to burcin.


---

Comment by aapitzsch created at 2014-07-26 13:21:52

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

Comment by aapitzsch created at 2014-07-26 13:21:52

Changing status from new to needs_review.


---

Comment by nbruin created at 2014-07-26 19:37:30

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

Comment by vdelecroix created at 2015-02-01 11:15:17

Hello,

Peter: On the other hand, fast comparisons with `0` should be done within `__nonzero__` and called via `bool(P)` or possibly `P.is_zero()` that indirectly calls the former.

André: Could you check that `__nonzero__` is implemented and modify the appropriate part of the code which uses `P == 0` or `P != 0`?

Vincent


---

Comment by vdelecroix created at 2015-02-01 11:15:17

Changing status from needs_review to needs_work.
