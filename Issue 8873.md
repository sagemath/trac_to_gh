# Issue 8873: Inconsistency with CombinatorialFreeModule: Vector Space vs. Module

Issue created by migration from https://trac.sagemath.org/ticket/8873

Original creator: jbandlow

Original creation time: 2010-05-04 19:16:11

Assignee: nthiery

CC:  sage-combinat nthiery

Consider the following code:

```
sage: G = Zmod(5)
sage: A = CombinatorialFreeModule(QQ, G)
sage: B = CombinatorialFreeMoudle(ZZ, G)
sage: A(G(1))
B[1]
sage: B(G(1))
TypeError
```


This should probably work the same for both.  My guess is that this will involve moving some VectorSpace code up to ModuleWithBasis, but I haven't investigated yet.


---

Comment by cnassau created at 2014-08-17 19:12:49

This ticket is 4 years old any so far nobody has bothered to act on it. I suppose this is a "wontfix" ticket, for two reasons:

 * there is a workaround: the following both work 
   {{{
   sage: A.monomial(G(1))
   sage: B.monomial(G(1))
   }}}

 * according to the following comment in `CombinatorialFreeModule._element_constructor_` the syntax `B(G(1))` is discouraged because it is ambiguous in certain situations:

   {{{
   Do not rely on the following feature which may be removed in the future::

            sage: QS3 = SymmetricGroupAlgebra(QQ,3)
            sage: QS3([2,3,1])     # indirect doctest
            [2, 3, 1]

        instead, use::

            sage: P = QS3.basis().keys()
            sage: QS3.monomial(P([2,3,1]))   # indirect doctest
            [2, 3, 1]
   }}}

I'll set this ticket to "wontfix" to see if someone complains.


---

Comment by tscrim created at 2014-11-06 01:45:06

Changing assignee from nthiery to robertwb.


---

Comment by tscrim created at 2014-11-06 01:45:06

Changing component from categories to coercion.


---

Comment by tscrim created at 2014-11-06 01:45:06

The problem actually stems from this:

```
sage: G(1) in ZZ
True
sage: G(1) in QQ
False
```

First off, I think this behavior is very inconsistent. Pertaining to this ticket, I think this should be fixed as it was made explicit that we wanted an element of the indexing set. The natural thing to do would be to check the parent matches the indexing set provided the indices do not coerce into the base ring (to avoid the ambiguity). Yet this has a subtly with say you take `4 / 2`, this is now in `QQ`, and pass that to a CFM with indices QQ and base ring ZZ and you might unexpectedly get `B[2]` as opposed to `2*B[0]` (or whatever the one basis element is).

Although I guess for modules, there is no ambiguity; it's only for unital algebras that such a conversion is (naturally) defined, right? So perhaps we want to refactor things around and have separate behavior for non-unital algebras.

Thoughts?

Edit - I have no idea why the owner changed...
