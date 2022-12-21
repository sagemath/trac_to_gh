# Issue 9695: AdditiveAbelianGroup, __call__ is misleading and complicated

Issue created by migration from Trac.

Original creator: rbeezer

Original creation time: 2010-08-06 03:16:32

Assignee: AlexGhitza

CC:  davidloeffler cremona was

The `__call__` functions for `AdditiveAbelianGroup` and `AdditiveAbelianGroupWrapper` don't behave as I would expect, nor as the doctests would lead one to believe.

Documentation for the wrapper class says:

```
...or an iterable (in which case the result is the corresponding
product of the generators of self).
```


It seems that the iterable instead gives a linear combination of the generators used in the "optimized" version of the quotient modules.  Most (all?) of the doctests use examples where the number of invariants is equal to the number of original generators, so the optimization is trivial and the situations below are not exposed.

See #9694 for an example of working around this.

Here, I'd expect `M([1,1,1])` to be `M.0+M.1+M.2`, and not an error

```
sage: E = EllipticCurve('30a2')
sage: pts = [E(4,-7,1), E(7/4, -11/8, 1), E(3, -2, 1)]
sage: M = AdditiveAbelianGroupWrapper(pts[0].parent(), pts, [3, 2, 2])
sage: M.gens()
((4 : -7 : 1), (7/4 : -11/8 : 1), (3 : -2 : 1))
sage: M([1,1,1])
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/sage/sage-4.5.2.rc1/devel/sage-main/<ipython console> in <module>()

/sage/sage-4.5.2.rc1/local/lib/python2.6/site-packages/sage/groups/additive_abelian/additive_abelian_wrapper.pyc in __call__(self, x, check)
    234             elif x.parent() is self.universe():
    235                 return AdditiveAbelianGroupWrapperElement(self, self._discrete_log(x), element = x)
--> 236         return addgp.AdditiveAbelianGroup_fixed_gens.__call__(self, x, check)
    237
    238 class AdditiveAbelianGroupWrapperElement(addgp.AdditiveAbelianGroupElement):

/sage/sage-4.5.2.rc1/local/lib/python2.6/site-packages/sage/modules/fg_pid/fgp_module.pyc in __call__(self, x, check)
    481                 x = self.optimized()[0].V().linear_combination_of_basis(x)
    482             except ValueError, msg:
--> 483                 raise TypeError, msg
    484         elif isinstance(x, FGP_Element):
    485             x = x.lift()

TypeError: length of v must be at most the number of rows of self
```



No problem when the number of invariants equal the number of generators:

```
sage: G=AdditiveAbelianGroup([17])
sage: a=G([12])
sage: a
(12)
```


The problem case again, up in the base class

```
sage: H=AdditiveAbelianGroup([3,7])
sage: b=H([12])
sage: b
(0, 4)

sage: c=H([2,3])
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/sage/sage-4.5.2.rc1/devel/sage-main/<ipython console> in <module>()

/sage/sage-4.5.2.rc1/local/lib/python2.6/site-packages/sage/modules/fg_pid/fgp_module.pyc in __call__(self, x, check)
    481                 x = self.optimized()[0].V().linear_combination_of_basis(x)
    482             except ValueError, msg:
--> 483                 raise TypeError, msg
    484         elif isinstance(x, FGP_Element):
    485             x = x.lift()

TypeError: length of v must be at most the number of rows of self
```



---

Comment by rbeezer created at 2010-08-23 06:46:33

Mystery solved.  The `FGP_Module` class will accept an iterable in `__call__`, which it uses for a linear combination of a minimal set of generators.  It will also accept a vector (which is a module element) and use its entries as the scalars in a linear combination of the "original", "obvious", or "non-minimal" generators.  This distinction was hard to discern in the doctests.

As part of working on other documentation items, I have addressed this at #9783.  So this ticket could be closed once #9783 is merged, if not sooner.


---

Comment by mpatel created at 2010-08-23 09:42:24

Resolution: invalid


---

Comment by mpatel created at 2010-08-23 09:49:17

Actually, now that I'm a bit more awake:  I'll close this ticket as a "duplicate" when #9783 is merged.  I'm changing this to `positive_review` so that it appears in reports {11} and {32}.


---

Comment by mpatel created at 2010-08-23 09:49:17

Changing status from closed to new.


---

Comment by mpatel created at 2010-08-23 09:49:17

Resolution changed from invalid to 


---

Comment by mpatel created at 2010-08-23 09:49:25

Changing status from new to needs_review.


---

Comment by mpatel created at 2010-08-23 09:49:30

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-08-23 09:52:21

# To the release manager

Please close this ticket when you merge #9783.


---

Comment by cremona created at 2010-08-23 09:57:56

Replying to [comment:3 mpatel]:
> Actually, now that I'm a bit more awake:  I'll close this ticket as a "duplicate" when #9783 is merged.  I'm changing this to `positive_review` so that it appears in reports {11} and {32}.

That looks good to me.


---

Comment by mpatel created at 2010-09-05 03:22:32

Resolution: duplicate
