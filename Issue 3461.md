# Issue 3461: write a construction for permutation groups so that the coercion system can find a common parent

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2008-06-18 09:05:16

Assignee: joyner

This happens in the coercion branch:


```
sage: P1 = PermutationGroup([This is the Trac macro ** that was inherited from the migration called with arguments (1,2))](https://trac.sagemath.org/wiki/WikiMacros#-macro)); P1
Permutation Group with generators [(1,2)]
sage: P2 = PermutationGroup([This is the Trac macro ** that was inherited from the migration called with arguments (1,3))](https://trac.sagemath.org/wiki/WikiMacros#-macro)); P2
Permutation Group with generators [(1,3)]
sage: p1 = P1.gen(); p2 = P2.gen()
sage: p1*p2
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/opt/sage-3.0.3.rc0/devel/sage-main/sage/combinat/matrices/<ipython console> in <module>()

/opt/sage-3.0.3.rc0/devel/sage-main/sage/combinat/matrices/element.pyx in sage.structure.element.MonoidElement.__mul__ (sage/structure/element.c:7517)()

TypeError: unsupported operand parent(s) for '*': 'Permutation Group with generators [(1,2)]' and 'Permutation Group with generators [(1,3)]'
```



---

Attachment


---

Comment by mhansen created at 2010-01-17 03:25:00

Changing status from new to needs_review.


---

Attachment

replaces previous patch


---

Comment by davidloeffler created at 2010-05-17 10:10:59

The original patch suffered from a particularly evil piece of bitrotting: since the patch was written, some change somewhere has meant that the trivial permutation now has truth value True, not False, which meant that the pushout code would never terminate -- it would keep on returning bigger and bigger towers of (empty) construction functors! 

The new patch I've just uploaded gets around this by using the `is_one` method, instead of a plain truth value test. It passes doctests under 4.4.1. Anyone willing to sign off on my tiny changes, and maybe we can get this into Sage 5.0?


---

Comment by mhansen created at 2010-05-17 17:11:15

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-05-17 17:11:15

Looks good to me.  Thanks David!


---

Comment by mhansen created at 2010-06-06 01:31:40

Resolution: fixed
