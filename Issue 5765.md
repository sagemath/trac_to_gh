# Issue 5765: improve doctest coverage for schemes/generic/algebraic_scheme.py

Issue created by migration from https://trac.sagemath.org/ticket/5765

Original creator: AlexGhitza

Original creation time: 2009-04-11 22:32:56

Assignee: AlexGhitza

Keywords: doctest algebraic scheme




---

Comment by AlexGhitza created at 2009-04-11 22:33:06

Changing status from new to assigned.


---

Comment by mabshoff created at 2009-04-15 06:44:50

Alex, is there a patch coming here? :)

Cheers,

Michael


---

Comment by AlexGhitza created at 2009-04-15 06:53:58

Good question.  I have done almost all I wanted to do with it, but unfortunately it's all mixed up with another patch that already got merged.  It will take me a bit of time to disentangle it, though.  Don't wait on it, although I'll do my best to get it done soon.


---

Attachment

The attached patch brings up the doctest coverage from 24% to 87% (29 of 33).

There is also some fairly straightforward refactoring of code, e.g. moving `_validate` to the ambient spaces where it belongs logically.  I also realised that `self.complement(other)` is counterintuitive and changed it to match normal speech patterns: it should be "the complement of self in other", which is other-self, not self-other.  An added bonus is that now one can write `X.complement()` to get the complement of X in its ambient space, which is highly intuitive.  Normally such a change in behaviour would be tricky but since the functions were just broken until 3.4.1.rc3, this shouldn't lead to any confusion (since nobody has used them yet).

Note that the patch relies on changes that only went in at 3.4.1.rc3, so it should only be applied on top of 3.4.1.rc3.


---

Comment by cremona created at 2009-04-18 15:52:17

Patch applies fine and looks good.  All doctests in schemes/generic pass.  Reference manual docs build ok and look good.  Pass!


---

Comment by mabshoff created at 2009-04-23 06:41:51

There are some doctest failures against 3.4.1:

```
        sage -t  devel/sage/sage/schemes/elliptic_curves/ell_point.py # 2 doctests failed
        sage -t  devel/sage/sage/schemes/elliptic_curves/sha_tate.py # 0 doctests failed
        sage -t  devel/sage/sage/schemes/elliptic_curves/ell_generic.py # 3 doctests failed
        sage -t  devel/sage/sage/schemes/plane_curves/constructor.py # 1 doctests failed
        sage -t  devel/sage/sage/schemes/elliptic_curves/ell_field.py # 1 doctests failed
```


Cheers,

Michael


---

Comment by cremona created at 2009-04-23 08:36:56

Replying to [comment:6 mabshoff]:
> There are some doctest failures against 3.4.1:
> {{{
>         sage -t  devel/sage/sage/schemes/elliptic_curves/ell_point.py # 2 doctests failed
>         sage -t  devel/sage/sage/schemes/elliptic_curves/sha_tate.py # 0 doctests failed
>         sage -t  devel/sage/sage/schemes/elliptic_curves/ell_generic.py # 3 doctests failed
>         sage -t  devel/sage/sage/schemes/plane_curves/constructor.py # 1 doctests failed
>         sage -t  devel/sage/sage/schemes/elliptic_curves/ell_field.py # 1 doctests failed
> }}}
> 
> Cheers,
> 
> Michael

Those failures are in files where I changed the docstrings recently, so I'll take a look.  John


---

Attachment

Replaces earlier patch


---

Comment by cremona created at 2009-04-23 09:42:59

The new patch replaces the first one and deals with this.  (Sorry, I forgot to do "sage -hg qnew" so it is not a separate patch,

The problem was:  in ell_field.py the function  _check_satisfies_equations called _error_bad_coords which Alex had renamed.  But all it did was riase an error with an appropriate message, so I just raised the error in place.

One remaining question: why is the error raised a TypeError?  In my view the type is fine but the values are wrong if the coordinates do not satisfy the equation.  I would have made it a ValueError.  but for consistence with the general scheme functions I left it as a TypeError.

I put this back to "needs review" but if Michael is happy with test passing there's no more needed.

John


---

Comment by AlexGhitza created at 2009-04-23 13:10:19

John's changes look good and fix most of the broken doctests.

There was one left, in `schemes/plane_curves/constructor.py`.  The fix is trivial and in the new patch `trac_5765-2.patch`, which should be applied after `trac_5765-1.patch`.


---

Attachment

apply after trac_5765-1.patch


---

Comment by cremona created at 2009-04-23 15:22:39

Replying to [comment:9 AlexGhitza]:
> John's changes look good and fix most of the broken doctests.
> 
> There was one left, in `schemes/plane_curves/constructor.py`.  The fix is trivial and in the new patch `trac_5765-2.patch`, which should be applied after `trac_5765-1.patch`.

Sorry I missed that one!


---

Comment by mabshoff created at 2009-04-24 02:35:23

Ahh, this now collides with #5851 it seems:

```
sage-3.4.2.alpha0/devel/sage$ patch -p1 --dry-run < trac_5765-1.patch 
patching file sage/schemes/elliptic_curves/ell_field.py
Hunk #1 FAILED at 27.
1 out of 1 hunk FAILED -- saving rejects to file sage/schemes/elliptic_curves/ell_field.py.rej
patching file sage/schemes/elliptic_curves/ell_generic.py
patching file sage/schemes/elliptic_curves/ell_point.py
patching file sage/schemes/generic/affine_space.py
patching file sage/schemes/generic/algebraic_scheme.py
patching file sage/schemes/generic/projective_space.py
patching file sage/schemes/generic/scheme.py
```

I will see if I can resolve the problem myself.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-24 02:38:39

Ok, looking at the changes I think either John or Alex will rebase this - I am on to other merges for now. So "needs rebase".

Cheers,

Michael


---

Comment by AlexGhitza created at 2009-04-24 04:44:52

I'll do this in a few hours.


---

Comment by AlexGhitza created at 2009-04-24 13:02:12

I was working on rebasing the patch against 3.4.2.alpha0, when I realised that `ell_field.py` has no reason to implement `_check_satisfies_equations`, since I have fixed the corresponding function "upstream" in `algebraic_scheme.py`.  In other words, the inherited method now works as it should so there's no need to reimplement it for elliptic curves.

Of course, once you remove `_check_satisfies_equations` from `ell_field.py`, there's nothing left.  I think we just just get rid of this file and make classes that currently inherit from `EllipticCurve_field` inherit directly from `EllipticCurve_generic` instead.

The newly attached patch `trac_5765-rebased.patch` implements all this, and is based on 3.4.2.alpha0.  Doctests pass for me, but this is a significant change so I'd like John to review this so he can object if need be.


---

Comment by cremona created at 2009-04-24 13:28:55

While I am waiting for 3.4.2.alpha0 to build (before which I cannot test the new patch!) I want to raise an issue.

I agree that the one and only function in ell_field was redundant, since the general machinery for checking that a point lies on a scheme can do what it does.  So I am happy with that.

But do we really want to eliminate the *class* EllipticCurve_field?    The design seems to be as follows.  In principle one can define elliptic curves over general base schemes.  The most important special case is elliptic curves over a field.  At the moment Sage has essentially no support for an elliptic curve over a non-field, but that might change.  So at present,  all the generic stuff in ell_generic is quite likely to only work for curves over fields anyway, and that is where anything relevant to general fields is put.  Might it not be a better plan to look carefully through ell_generic, see if there is anything there which should really only be for curves over fields, and move that to ell_field (keeping the EllipticCurve_field class)?

Just a thought -- at least a move such as the one this patch does deserves a little more public debate ;)


---

Comment by AlexGhitza created at 2009-04-24 13:40:22

Replying to [comment:15 cremona]:
> While I am waiting for 3.4.2.alpha0 to build (before which I cannot test the new patch!) I want to raise an issue.
> 
> I agree that the one and only function in ell_field was redundant, since the general machinery for checking that a point lies on a scheme can do what it does.  So I am happy with that.
> 
> But do we really want to eliminate the *class* EllipticCurve_field?    The design seems to be as follows.  In principle one can define elliptic curves over general base schemes.  The most important special case is elliptic curves over a field.  At the moment Sage has essentially no support for an elliptic curve over a non-field, but that might change.  So at present,  all the generic stuff in ell_generic is quite likely to only work for curves over fields anyway, and that is where anything relevant to general fields is put.  Might it not be a better plan to look carefully through ell_generic, see if there is anything there which should really only be for curves over fields, and move that to ell_field (keeping the EllipticCurve_field class)?
> 
> Just a thought -- at least a move such as the one this patch does deserves a little more public debate ;)

Very good, that's why I wanted to hear others say something about it.

I don't feel strongly either way.  From what I can see, `EllipticCurve_generic` has stuff that makes sense for elliptic curves over rings.  I agree that it would be good to sift through that and see if there are methods that really only work over fields, and move these to `ell_field.py`.

In the meantime, I'll modify the patch so that it just removes `_check_satisfies_equations` and leaves only `pass` in the definition of the class `EllipticCurve_field`.

I really need sleep now, but I'll have a corrected patch up in the morning.


---

Comment by was created at 2009-04-24 15:55:09

I think it would be nice to be able to implement the elliptic curve factorization method (ECM) without having to use this hack:


```
R = Zmod(N)
R.is_field = lambda: True
E = EllipticCurve(R, [-1,0])
```



---

Attachment


---

Comment by AlexGhitza created at 2009-04-24 23:13:44

OK, I replaced the controversial version of the patch with the tame one.  It is just a rebase of the original positive-reviewed patch, together with the removal of the redundant method `_check_satisfies_equations`, but leaving a blank `ell_field.py` for further refactoring as discussed above.

I'm not sure whether this needs a review any more, but if John's around and can have a quick peak, that wouldn't hurt.  (Note that the changes to the elliptic curves code are all at the top of the patch.)


---

Comment by AlexGhitza created at 2009-04-24 23:44:08

There's a followup ticket at #5890.


---

Comment by cremona created at 2009-04-27 11:16:52

The patch applies but tests in ell_point.py fila revealing this horror:

```
sage: Fx.<b>=GF(2^(4*5))
sage: Ex=EllipticCurve(Fx,[0,0,1,1,1])
sage: Ex.defining_polynomial()
x^3 + y^2*z + 0*x*z^2 + 0*y*z^2 + 0*z^3
```

-- note the zero coefficients!

Adding a whole lot of print statements I get to this:

```
sage: Ex=EllipticCurve(Fx,[0,0,1,1,1])
K =  Finite Field in b of size 2^20
PP =  Projective Space of dimension 2 over Finite Field in b of size 2^20
PP.coordinate_ring() =  Multivariate Polynomial Ring in x, y, z over Finite Field in b of size 2^20
PP.coordinate_ring().base_ring() =  Finite Field in b of size 2^20
PP.coordinate_ring()(1) =  1
ainvs =  [0, 0, 1, 1, 1]
a1, a2, a3, a4, a6 =  0 0 1 1 1
a4*x*z**2 =  0*x*z^2
a4's parent =  Finite Field in b of size 2^20
 f =  x^3 + y^2*z + 0*x*z^2 + 0*y*z^2 + 0*z^3
```

At which point I am stuck.  We have the constant 1 in the multivariate poly ring in x,y,z over the field GF(2^20), but when I multiply a monomial by it it displays with coefficient zero.

This has surely been caused by something not in this patch!  I tried constructing an example outside this bit of code but failed (to make it fail in this way).  In fact this happens in unpatched 3.4.2.alpha0:

```
sage: Fx.<b>=GF(2^(4*5))
sage: Ex=EllipticCurve(Fx,[0,0,1,1,1])
sage: Ex.defining_polynomial()
x^3 + y^2*z + 0*x*z^2 + 0*y*z^2 + 0*z^3
```



---

Comment by cremona created at 2009-04-28 15:52:21

After applying also the patch at #5919, all tests in sage/schemes pass, so I am changing this to "positive review" but note that it does depend on that patch for the tests in ell_point.py to pass.  

The patches (here and at #5919) can be merged in either order.


---

Comment by mabshoff created at 2009-04-29 23:17:43

Merged trac_5765-rebased.patch in Sage 3.4.2.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-29 23:17:43

Resolution: fixed
