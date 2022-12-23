# Issue 7946: Spec(...) does not specify its category

Issue created by migration from https://trac.sagemath.org/ticket/7946

Original creator: nthiery

Original creation time: 2010-01-16 12:37:52

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


---

Comment by novoselt created at 2012-02-20 00:36:39

#11599 claims to fix this, but I am not entirely sure what would it take to fix this ticket - the reported category is now schemes and only 3 of the `TestSuite` tests fail.


---

Comment by pbruin created at 2014-04-12 14:23:30

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
(Mathematically speaking, Spec [as a functor from commutative rings to schemes, or even locally ringed spaces] can be defined as the adjoint functor of the global sections functor _X_ -> _O<sub>X</sub>_(_X_) from schemes to commutative rings, and this gives an anti-equivalence of categories from commutative rings to affine schemes; I wonder if this could somehow be formalised in Sage's category framework, but that's another story...)

[Edit: the above idea is now essentially #16158, although there is no category of affine schemes yet.]


---

Comment by pbruin created at 2014-05-03 15:34:38

To show that the first part of the original ticket is fixed:

```
sage: S = Spec(ZZ)
sage: S.category()
Category of Schemes
sage: isinstance(S, S.category().parent_class) 
True
```



---

Comment by pbruin created at 2014-05-03 21:30:09

Changing status from new to needs_review.


---

Comment by pbruin created at 2014-05-03 21:30:09

The attached branch makes affine schemes, and points on them, cooperate better with the category and coercion code.  The `TestSuite` now runs without failures.


---

Comment by tscrim created at 2014-11-03 07:56:42

Replying to [comment:8 pbruin]:
> The attached branch makes affine schemes, and points on them, cooperate better with the category and coercion code.  The `TestSuite` now runs without failures.

Is there some way you can get rid of that custom `__call__` method in `AffineScheme`, or at least passes things up through the `Parent.__call__` when trying to construct an element? If not, then I think we're okay setting this to positive review as it fixes the issues as stated in the ticket description (you can do this on my behalf).

Also, I think that comment:6 (from the _very_ limited understanding I have of the math) is the correct way to do things. However that would be a major overhaul to be done on a separate ticket, and perhaps the above change to `__call__` would fit into that.


---

Comment by pbruin created at 2014-11-03 14:34:53

Replying to [comment:11 tscrim]:
> Replying to [comment:8 pbruin]:
> > The attached branch makes affine schemes, and points on them, cooperate better with the category and coercion code.  The `TestSuite` now runs without failures.
> 
> Is there some way you can get rid of that custom `__call__` method in `AffineScheme`, or at least passes things up through the `Parent.__call__` when trying to construct an element? If not, then I think we're okay setting this to positive review as it fixes the issues as stated in the ticket description (you can do this on my behalf).
The reason this is done via the `__call__()` method is that an affine scheme _S_ accepts two kinds of input; only one of them (input is a prime ideal) constructs an element with _S_ as its parent.  In the other case (input is a list of coordinates) the `__call__()` syntax constructs an element of a suitable scheme homset.  I don't see an easy way to avoid a custom `__call__()` method; it may be possible (and would be nice) to get rid of it, but it is better to do this on separate ticket.  (Note also that the `__call__()` method was already present, I just improved it as necessary.)
> Also, I think that comment:6 (from the _very_ limited understanding I have of the math) is the correct way to do things. However that would be a major overhaul to be done on a separate ticket, and perhaps the above change to `__call__` would fit into that.
What I was talking about in that comment was mostly done on #16158 (closed a couple of months ago).  I think the remaining issue of making a category `AffineSchemes` would probably be disjoint from getting rid of the `__call__()` method.

I'm setting this to positive review since you gave the green light.


---

Comment by pbruin created at 2014-11-03 14:34:53

Changing status from needs_review to positive_review.


---

Comment by tscrim created at 2014-11-03 15:44:43

> The reason this is done via the `__call__()` method is that an affine scheme _S_ accepts two kinds of input; only one of them (input is a prime ideal) constructs an element with _S_ as its parent.  In the other case (input is a list of coordinates) the `__call__()` syntax constructs an element of a suitable scheme homset.  I don't see an easy way to avoid a custom `__call__()` method; it may be possible (and would be nice) to get rid of it, but it is better to do this on separate ticket.  (Note also that the `__call__()` method was already present, I just improved it as necessary.)

That's what I was thinking from a quick look through. Anyways, for later.

> What I was talking about in that comment was mostly done on #16158 (closed a couple of months ago).  I think the remaining issue of making a category `AffineSchemes` would probably be disjoint from getting rid of the `__call__()` method.

I knew the last one was done, but forgot that it moved the functionality. Unfortunately I think you're right, but we can at least do a followup to create the category of `AffineSchemes`.

> I'm setting this to positive review since you gave the green light.

Thanks.


---

Comment by vbraun created at 2014-11-14 21:01:45

Resolution: fixed
