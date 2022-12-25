# Issue 8873: Inconsistency with CombinatorialFreeModule: Vector Space vs. Module

archive/issues_008873.json:
```json
{
    "body": "Assignee: @nthiery\n\nCC:  sage-combinat @nthiery\n\nConsider the following code:\n\n```\nsage: G = Zmod(5)\nsage: A = CombinatorialFreeModule(QQ, G)\nsage: B = CombinatorialFreeMoudle(ZZ, G)\nsage: A(G(1))\nB[1]\nsage: B(G(1))\nTypeError\n```\n\n\nThis should probably work the same for both.  My guess is that this will involve moving some VectorSpace code up to ModuleWithBasis, but I haven't investigated yet.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8873\n\n",
    "created_at": "2010-05-04T19:16:11Z",
    "labels": [
        "component: categories",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "Inconsistency with CombinatorialFreeModule: Vector Space vs. Module",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8873",
    "user": "https://github.com/jbandlow"
}
```
Assignee: @nthiery

CC:  sage-combinat @nthiery

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

Issue created by migration from https://trac.sagemath.org/ticket/8873





---

archive/issue_comments_081419.json:
```json
{
    "body": "This ticket is 4 years old any so far nobody has bothered to act on it. I suppose this is a \"wontfix\" ticket, for two reasons:\n\n* there is a workaround: the following both work \n  {{{\n  sage: A.monomial(G(1))\n  sage: B.monomial(G(1))\n  }}}\n\n* according to the following comment in `CombinatorialFreeModule._element_constructor_` the syntax `B(G(1))` is discouraged because it is ambiguous in certain situations:\n\n  {{{\n  Do not rely on the following feature which may be removed in the future::\n\n           sage: QS3 = SymmetricGroupAlgebra(QQ,3)\n           sage: QS3([2,3,1])     # indirect doctest\n           [2, 3, 1]\n\n       instead, use::\n\n           sage: P = QS3.basis().keys()\n           sage: QS3.monomial(P([2,3,1]))   # indirect doctest\n           [2, 3, 1]\n  }}}\n\nI'll set this ticket to \"wontfix\" to see if someone complains.",
    "created_at": "2014-08-17T19:12:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8873#issuecomment-81419",
    "user": "https://github.com/cnassau"
}
```

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

archive/issue_comments_081420.json:
```json
{
    "body": "Changing assignee from @nthiery to @robertwb.",
    "created_at": "2014-11-06T01:45:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8873#issuecomment-81420",
    "user": "https://github.com/tscrim"
}
```

Changing assignee from @nthiery to @robertwb.



---

archive/issue_comments_081421.json:
```json
{
    "body": "Changing component from categories to coercion.",
    "created_at": "2014-11-06T01:45:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8873#issuecomment-81421",
    "user": "https://github.com/tscrim"
}
```

Changing component from categories to coercion.



---

archive/issue_comments_081422.json:
```json
{
    "body": "The problem actually stems from this:\n\n```\nsage: G(1) in ZZ\nTrue\nsage: G(1) in QQ\nFalse\n```\n\nFirst off, I think this behavior is very inconsistent. Pertaining to this ticket, I think this should be fixed as it was made explicit that we wanted an element of the indexing set. The natural thing to do would be to check the parent matches the indexing set provided the indices do not coerce into the base ring (to avoid the ambiguity). Yet this has a subtly with say you take `4 / 2`, this is now in `QQ`, and pass that to a CFM with indices QQ and base ring ZZ and you might unexpectedly get `B[2]` as opposed to `2*B[0]` (or whatever the one basis element is).\n\nAlthough I guess for modules, there is no ambiguity; it's only for unital algebras that such a conversion is (naturally) defined, right? So perhaps we want to refactor things around and have separate behavior for non-unital algebras.\n\nThoughts?\n\nEdit - I have no idea why the owner changed...",
    "created_at": "2014-11-06T01:45:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8873#issuecomment-81422",
    "user": "https://github.com/tscrim"
}
```

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
