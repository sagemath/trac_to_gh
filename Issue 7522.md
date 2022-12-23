# Issue 7522: Implement orthogonal complement in vector spaces

Issue created by migration from https://trac.sagemath.org/ticket/7522

Original creator: kcrisman

Original creation time: 2009-11-24 01:27:57

Assignee: was

CC:  jason rbeezer

It should be easy to get the orthogonal complement of a subspace W of a vector space V.   From Jason Grout: 

```
sage: def orthogonal_complement(space):
....:     if space.dimension()==0:
....:         return space.ambient_vector_space()
....:     else:
....:         return space.basis_matrix().right_kernel()
```

One would also want to add an option to specify the larger space in which you were dealing, with it defaulting to the ambient vector space.  Probably 'perp()' should be an alias.


---

Attachment


---

Comment by jason created at 2010-09-22 03:03:14

This adds the basic orthogonal complement command.  Specifying a larger space can go on another ticket, if someone wants it.


---

Comment by jason created at 2010-09-22 03:03:14

Changing status from new to needs_review.


---

Comment by kcrisman created at 2010-09-23 00:33:24

Replying to [comment:1 jason]:
> This adds the basic orthogonal complement command.  Specifying a larger space can go on another ticket, if someone wants it.
Thanks for doing this - I never got to it, since I haven't used this lately.   Agreed on the enhancement.

The documentation should make it clear what the ambient space is by default, perhaps by adding an example where things fail?  Or at least commenting that the first example just shows itself as the ambient space.  What would happen if one took a double subspace - what would it consider to be the ambient subspace?


---

Comment by jason created at 2010-09-23 23:27:56

apply on top of previous patches


---

Attachment

Replying to [comment:2 kcrisman]:


> The documentation should make it clear what the ambient space is by default, perhaps by adding an example where things fail?  Or at least commenting that the first example just shows itself as the ambient space.  What would happen if one took a double subspace - what would it consider to be the ambient subspace?  

Review patch attached.  Better now?


---

Comment by kcrisman created at 2010-09-27 12:54:06

Changing status from needs_review to needs_work.


---

Comment by kcrisman created at 2010-09-27 12:54:06

I got a chance to look at this over the weekend.  Unsurprisingly, in general it's great.  But...

Since this is in the free module module (!), there should be a better error for 

```
sage: c = FreeModule(Integers(8), 2)
sage: c.perp()
---------------------------------------------------------------------------
<snip>
NotImplementedError: Don't know how to compute kernels over Ring of integers modulo 8
```

I also noticed the following behavior, which is probably desirable, but which should then definitely be explicitly mentioned in the documentation for this function, since it does return a different type of object for the perp object:

```
sage: c = FreeModule(ZZ, 2)
sage: c
Ambient free module of rank 2 over the principal ideal domain Integer Ring
sage: c.perp()
Vector space of degree 2 and dimension 0 over Rational Field
Basis matrix:
[]
```



---

Comment by kcrisman created at 2010-09-27 20:41:49

By the way, why didn't `TestSuite` catch this?

```
    sage: M = ZZ^3
    sage: TestSuite(M).run()
    sage: W = M.span_of_basis([[1,2,3],[4,5,19]])
    sage: TestSuite(W).run()
```



---

Comment by tscrim created at 2013-04-04 22:58:40

I've uploaded a new version of the patch which moves the `perp()` method to the free module with the PID as a base ring (so you shouldn't get the `NotImplementedError`) and made sure the submodules have the correct base rings.


---

Comment by tscrim created at 2013-04-04 22:58:40

Changing status from needs_work to needs_review.


---

Comment by tscrim created at 2013-04-04 22:59:25

For patchbot:

Apply: trac_7522-perp-ts.patch


---

Comment by kcrisman created at 2013-04-05 00:41:01

`perp()` isn't documented in this patch.  Also,

```
sage: c = FreeModule(Integers(8), 2)
sage: c.perp()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
AttributeError: 'FreeModule_ambient_with_category' object has no attribute 'perp'
<and later>
AttributeError: 'IntegerModRing_generic_with_category' object has no attribute 'parent'
```

Apparently `Integers(8)` isn't a PID, according to Sage?  This isn't bad, but perhaps we should have a different error message... or maybe this is okay.


---

Comment by kcrisman created at 2013-04-05 00:41:01

Changing status from needs_review to needs_work.


---

Comment by kcrisman created at 2013-04-05 00:57:32

Also, would it be better to do the kernel first and then change the ring?  Just wondering if there might be any difference.


---

Comment by nbruin created at 2013-04-05 01:33:17

- You only have an orthogonal complement on an inner product space.
 - Whenever you have a canonical isomorphism between a vector space and its dual, you can do the "kernel trick" that you're doing (note you have to take a transpose somewhere). A basis choice induces such a canonical isomorphism, as does an inner product. For every subspace `W subset V` it gives you a complementary subspace `W'` such that V is a direct product of `W` and `W'`.
 - For (free) modules over rings this doesn't really work, because not every submodule is a direct summand.
 - Of course, if your ring is a domain, you can tensor with the field of fractions, take the complement, and intersect with the module inside to get another submodule. Doing that twice should get you the "saturation" of your original module.

I suggest you don't call it orthogonal complement. For instance, on vector spaces over finite fields, it's not (but a basis choice still induces an isomorphism to the dual).


---

Comment by kcrisman created at 2013-04-05 01:54:12

>  - You only have an orthogonal complement on an inner product space.
>  - Whenever you have a canonical isomorphism between a vector space and its dual, you can do the "kernel trick" that you're doing (note you have to take a transpose somewhere). A basis choice induces such a canonical isomorphism, as does an inner product. For every subspace `W subset V` it gives you a complementary subspace `W'` such that V is a direct product of `W` and `W'`.
>  - For (free) modules over rings this doesn't really work, because not every submodule is a direct summand.
Aargh!  You had to go remind us of the whole mathematical correctness thing.  You're right, of course.  Not every submodule is projective.
>  - Of course, if your ring is a domain, you can tensor with the field of fractions, take the complement, and intersect with the module inside to get another submodule. Doing that twice should get you the "saturation" of your original module.
> I suggest you don't call it orthogonal complement. For instance, on vector spaces over finite fields, it's not (but a basis choice still induces an isomorphism to the dual).
Then what do you suggest?  Since this is primarily useful for pedagogical purposes, perhaps we can just raise an error outside of QQ, RR, and friends.  In particular, I think it's definitely appropriate to not allow this for anything but vector spaces.

One interesting thing is that Sage is already doing something analogous to your suggestion about tensoring in getting the "basis matrix", which led to the workaround Travis made.  Then again,

```
Vector space of degree 3 and dimension 2 over Integer Ring
```

shouldn't even be legal to appear in Sage, in some sense...


---

Comment by nbruin created at 2013-04-05 03:09:21

Replying to [comment:12 kcrisman]:
> Then what do you suggest?  Since this is primarily useful for pedagogical purposes, perhaps we can just raise an error outside of QQ, RR, and friends.

Even there it's only wrt the standard inner product (i.e., if your basis is orthogonal) that this complement is _orthogonal_.

Wouldn't just `complement` work? I think that's a reasonably established term for direct cofactor.

And indeed, you should probably only offer this for vector spaces, i.e., when the base ring is a field.


---

Comment by tscrim created at 2013-04-05 16:09:28

First, if the ring is not a PID, there are many attributes that are not there anymore (ex. `span()`), so getting the attribute error is consistent with the rest of free modules.

As for them being inner product spaces, we have this in sage:

```
sage: F = FreeModule(Integers(8), 3)
sage: v = F([1, 2, 3])
sage: v*v
6
sage: F.inner_product_matrix()
[1 0 0]
[0 1 0]
[0 0 1]
```

so I think sage always assumes it has an inner product (although not necessarily a nice inner product).

For the

```
Vector space of degree 3 and dimension 2 over Integer Ring
```

that was a doctest error coming from me thinking I know what the output should be >_<.

Anyways, new version of the patch with the method now called `complement()`, removed `perp()`, and only works for vector spaces.

For patchbot:

Apply: trac_7522-perp-ts.patch


---

Comment by tscrim created at 2013-04-05 16:09:28

Changing status from needs_work to needs_review.


---

Comment by kcrisman created at 2013-04-05 17:26:46

Question for Jason and Rob: for teaching linear algebra, would it be useful to have `complement` but not `perp` or `orthogonal_complement`?  I think that the standard basis is always kind of implicit in such situations; we aren't asking for complements with respect to other (orthogonal or not) bases with this function, or at least originally weren't.


---

Comment by nbruin created at 2013-04-05 17:56:53

Rather than testing if the base ring is a field, shouldn't you place the method on `sage.modules.free_module.FreeModule_generic_field` or something like that? The usual idea is to let inheritance take care of which methods are available rather than explicit argument checking wherever possible.


---

Attachment

Here I was looking for something called `VectorSpace`... Done. Now just waiting on a response from Rob or Jason.


---

Comment by kcrisman created at 2013-06-18 23:06:07

I've just discussed this with Rob and Jason at Sage Days 48.  The consensus is that the solution here is acceptable.

Patchbot, apply: trac_7522-perp-ts.patch


---

Comment by kcrisman created at 2013-06-18 23:06:07

Changing keywords from "" to "sd48".


---

Comment by kcrisman created at 2013-06-18 23:23:32

I'm going to add an example pointing out that over a finite field this gives a complement which intersects the original subspace, which 3 people here say is fine (in the sense that it's not wrong, but we should just point out it's not what one might expect from the "usual" case).  Nils, is it okay as long as we don't call it orthogonal?


---

Comment by kcrisman created at 2013-06-18 23:29:25

Okay, Travis and/or Nils and/or anyone else, is this okay?  The terminology is really the issue here, but hopefully this will satisfy everyone.

Patchbot, apply trac_7522-perp-ts.patch and trac_7522-finite.patch


---

Comment by tscrim created at 2013-06-18 23:43:31

There's a small typo:

```
a a vector
```

once that is fixed, I'm fine with this being set to positive reivew (but I'm probably one of the less opinionated people on this). Feel free to do this on my behalf because I'm going to sleep now to be ready for more Sage Days 49. Hope the 48 is going well.

Travis


---

Attachment

Thanks, fixed.

Patchbot, apply trac_7522-perp-ts.patch and trac_7522-finite.patch


---

Comment by kcrisman created at 2013-06-20 00:18:51

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-06-20 21:33:49

Resolution: fixed
