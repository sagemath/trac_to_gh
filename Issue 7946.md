# Issue 7946: Spec(...) does not specify its category

archive/issues_007946.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nCC:  vbraun\n\n\n```\nsage: C = Spec(ZZ)\nsage: C.category()\nCategory of sets\nsage: isinstance(C, C.category().element_class)\nFalse\n```\n\n\nCaught with #7921; please write patch on top of it to avoid conflicts.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7946\n\n",
    "created_at": "2010-01-16T12:37:52Z",
    "labels": [
        "algebraic geometry",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "Spec(...) does not specify its category",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7946",
    "user": "nthiery"
}
```
Assignee: AlexGhitza

CC:  vbraun


```
sage: C = Spec(ZZ)
sage: C.category()
Category of sets
sage: isinstance(C, C.category().element_class)
False
```


Caught with #7921; please write patch on top of it to avoid conflicts.

Issue created by migration from https://trac.sagemath.org/ticket/7946





---

archive/issue_comments_069325.json:
```json
{
    "body": "#11599 claims to fix this, but I am not entirely sure what would it take to fix this ticket - the reported category is now schemes and only 3 of the `TestSuite` tests fail.",
    "created_at": "2012-02-20T00:36:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7946",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7946#issuecomment-69325",
    "user": "novoselt"
}
```

#11599 claims to fix this, but I am not entirely sure what would it take to fix this ticket - the reported category is now schemes and only 3 of the `TestSuite` tests fail.



---

archive/issue_comments_069326.json:
```json
{
    "body": "What is `Spec` intended to mean in the first place?  The definition currently starts with\n\n```\nclass Spec(AffineScheme):\n    ....\n```\n\nThis suggests that `Spec` is a special kind of affine scheme.  But aren't \"the spectrum of a ring\" and \"an affine scheme\" exactly the same thing?\n\nThis code probably predates the category framework.  A more modern design would perhaps be something like the following:\n- define the category `AffineSchemes` (or `Schemes().Affine()`) of affine schemes;\n- designate `AffineScheme` as the \"canonical\" type for objects in this category, and move functionality from `Spec` to `AffineScheme` as appropriate;\n- convert `Spec` into a functor from `CommutativeRings` to `AffineSchemes`.\n(Mathematically speaking, Spec [as a functor from commutative rings to schemes, or even locally ringed spaces] can be defined as the adjoint functor of the global sections functor *X* -> *O<sub>X</sub>*(*X*) from schemes to commutative rings, and this gives an anti-equivalence of categories from commutative rings to affine schemes; I wonder if this could somehow be formalised in Sage's category framework, but that's another story...)\n\n[Edit: the above idea is now essentially #16158, although there is no category of affine schemes yet.]",
    "created_at": "2014-04-12T14:23:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7946",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7946#issuecomment-69326",
    "user": "pbruin"
}
```

What is `Spec` intended to mean in the first place?  The definition currently starts with

```
class Spec(AffineScheme):
    ....
```

This suggests that `Spec` is a special kind of affine scheme.  But aren't "the spectrum of a ring" and "an affine scheme" exactly the same thing?

This code probably predates the category framework.  A more modern design would perhaps be something like the following:
- define the category `AffineSchemes` (or `Schemes().Affine()`) of affine schemes;
- designate `AffineScheme` as the "canonical" type for objects in this category, and move functionality from `Spec` to `AffineScheme` as appropriate;
- convert `Spec` into a functor from `CommutativeRings` to `AffineSchemes`.
(Mathematically speaking, Spec [as a functor from commutative rings to schemes, or even locally ringed spaces] can be defined as the adjoint functor of the global sections functor *X* -> *O<sub>X</sub>*(*X*) from schemes to commutative rings, and this gives an anti-equivalence of categories from commutative rings to affine schemes; I wonder if this could somehow be formalised in Sage's category framework, but that's another story...)

[Edit: the above idea is now essentially #16158, although there is no category of affine schemes yet.]



---

archive/issue_comments_069327.json:
```json
{
    "body": "To show that the first part of the original ticket is fixed:\n\n```\nsage: S = Spec(ZZ)\nsage: S.category()\nCategory of Schemes\nsage: isinstance(S, S.category().parent_class) \nTrue\n```\n",
    "created_at": "2014-05-03T15:34:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7946",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7946#issuecomment-69327",
    "user": "pbruin"
}
```

To show that the first part of the original ticket is fixed:

```
sage: S = Spec(ZZ)
sage: S.category()
Category of Schemes
sage: isinstance(S, S.category().parent_class) 
True
```




---

archive/issue_comments_069328.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-05-03T21:30:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7946",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7946#issuecomment-69328",
    "user": "pbruin"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_069329.json:
```json
{
    "body": "The attached branch makes affine schemes, and points on them, cooperate better with the category and coercion code.  The `TestSuite` now runs without failures.",
    "created_at": "2014-05-03T21:30:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7946",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7946#issuecomment-69329",
    "user": "pbruin"
}
```

The attached branch makes affine schemes, and points on them, cooperate better with the category and coercion code.  The `TestSuite` now runs without failures.



---

archive/issue_comments_069330.json:
```json
{
    "body": "Replying to [comment:8 pbruin]:\n> The attached branch makes affine schemes, and points on them, cooperate better with the category and coercion code.  The `TestSuite` now runs without failures.\n\nIs there some way you can get rid of that custom `__call__` method in `AffineScheme`, or at least passes things up through the `Parent.__call__` when trying to construct an element? If not, then I think we're okay setting this to positive review as it fixes the issues as stated in the ticket description (you can do this on my behalf).\n\nAlso, I think that comment:6 (from the *very* limited understanding I have of the math) is the correct way to do things. However that would be a major overhaul to be done on a separate ticket, and perhaps the above change to `__call__` would fit into that.",
    "created_at": "2014-11-03T07:56:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7946",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7946#issuecomment-69330",
    "user": "tscrim"
}
```

Replying to [comment:8 pbruin]:
> The attached branch makes affine schemes, and points on them, cooperate better with the category and coercion code.  The `TestSuite` now runs without failures.

Is there some way you can get rid of that custom `__call__` method in `AffineScheme`, or at least passes things up through the `Parent.__call__` when trying to construct an element? If not, then I think we're okay setting this to positive review as it fixes the issues as stated in the ticket description (you can do this on my behalf).

Also, I think that comment:6 (from the *very* limited understanding I have of the math) is the correct way to do things. However that would be a major overhaul to be done on a separate ticket, and perhaps the above change to `__call__` would fit into that.



---

archive/issue_comments_069331.json:
```json
{
    "body": "Replying to [comment:11 tscrim]:\n> Replying to [comment:8 pbruin]:\n> > The attached branch makes affine schemes, and points on them, cooperate better with the category and coercion code.  The `TestSuite` now runs without failures.\n> \n> Is there some way you can get rid of that custom `__call__` method in `AffineScheme`, or at least passes things up through the `Parent.__call__` when trying to construct an element? If not, then I think we're okay setting this to positive review as it fixes the issues as stated in the ticket description (you can do this on my behalf).\nThe reason this is done via the `__call__()` method is that an affine scheme *S* accepts two kinds of input; only one of them (input is a prime ideal) constructs an element with *S* as its parent.  In the other case (input is a list of coordinates) the `__call__()` syntax constructs an element of a suitable scheme homset.  I don't see an easy way to avoid a custom `__call__()` method; it may be possible (and would be nice) to get rid of it, but it is better to do this on separate ticket.  (Note also that the `__call__()` method was already present, I just improved it as necessary.)\n> Also, I think that comment:6 (from the *very* limited understanding I have of the math) is the correct way to do things. However that would be a major overhaul to be done on a separate ticket, and perhaps the above change to `__call__` would fit into that.\nWhat I was talking about in that comment was mostly done on #16158 (closed a couple of months ago).  I think the remaining issue of making a category `AffineSchemes` would probably be disjoint from getting rid of the `__call__()` method.\n\nI'm setting this to positive review since you gave the green light.",
    "created_at": "2014-11-03T14:34:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7946",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7946#issuecomment-69331",
    "user": "pbruin"
}
```

Replying to [comment:11 tscrim]:
> Replying to [comment:8 pbruin]:
> > The attached branch makes affine schemes, and points on them, cooperate better with the category and coercion code.  The `TestSuite` now runs without failures.
> 
> Is there some way you can get rid of that custom `__call__` method in `AffineScheme`, or at least passes things up through the `Parent.__call__` when trying to construct an element? If not, then I think we're okay setting this to positive review as it fixes the issues as stated in the ticket description (you can do this on my behalf).
The reason this is done via the `__call__()` method is that an affine scheme *S* accepts two kinds of input; only one of them (input is a prime ideal) constructs an element with *S* as its parent.  In the other case (input is a list of coordinates) the `__call__()` syntax constructs an element of a suitable scheme homset.  I don't see an easy way to avoid a custom `__call__()` method; it may be possible (and would be nice) to get rid of it, but it is better to do this on separate ticket.  (Note also that the `__call__()` method was already present, I just improved it as necessary.)
> Also, I think that comment:6 (from the *very* limited understanding I have of the math) is the correct way to do things. However that would be a major overhaul to be done on a separate ticket, and perhaps the above change to `__call__` would fit into that.
What I was talking about in that comment was mostly done on #16158 (closed a couple of months ago).  I think the remaining issue of making a category `AffineSchemes` would probably be disjoint from getting rid of the `__call__()` method.

I'm setting this to positive review since you gave the green light.



---

archive/issue_comments_069332.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-11-03T14:34:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7946",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7946#issuecomment-69332",
    "user": "pbruin"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_069333.json:
```json
{
    "body": "> The reason this is done via the `__call__()` method is that an affine scheme *S* accepts two kinds of input; only one of them (input is a prime ideal) constructs an element with *S* as its parent.  In the other case (input is a list of coordinates) the `__call__()` syntax constructs an element of a suitable scheme homset.  I don't see an easy way to avoid a custom `__call__()` method; it may be possible (and would be nice) to get rid of it, but it is better to do this on separate ticket.  (Note also that the `__call__()` method was already present, I just improved it as necessary.)\n\nThat's what I was thinking from a quick look through. Anyways, for later.\n\n> What I was talking about in that comment was mostly done on #16158 (closed a couple of months ago).  I think the remaining issue of making a category `AffineSchemes` would probably be disjoint from getting rid of the `__call__()` method.\n\nI knew the last one was done, but forgot that it moved the functionality. Unfortunately I think you're right, but we can at least do a followup to create the category of `AffineSchemes`.\n\n> I'm setting this to positive review since you gave the green light.\n\nThanks.",
    "created_at": "2014-11-03T15:44:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7946",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7946#issuecomment-69333",
    "user": "tscrim"
}
```

> The reason this is done via the `__call__()` method is that an affine scheme *S* accepts two kinds of input; only one of them (input is a prime ideal) constructs an element with *S* as its parent.  In the other case (input is a list of coordinates) the `__call__()` syntax constructs an element of a suitable scheme homset.  I don't see an easy way to avoid a custom `__call__()` method; it may be possible (and would be nice) to get rid of it, but it is better to do this on separate ticket.  (Note also that the `__call__()` method was already present, I just improved it as necessary.)

That's what I was thinking from a quick look through. Anyways, for later.

> What I was talking about in that comment was mostly done on #16158 (closed a couple of months ago).  I think the remaining issue of making a category `AffineSchemes` would probably be disjoint from getting rid of the `__call__()` method.

I knew the last one was done, but forgot that it moved the functionality. Unfortunately I think you're right, but we can at least do a followup to create the category of `AffineSchemes`.

> I'm setting this to positive review since you gave the green light.

Thanks.



---

archive/issue_comments_069334.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-11-14T21:01:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7946",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7946#issuecomment-69334",
    "user": "vbraun"
}
```

Resolution: fixed
