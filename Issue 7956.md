# Issue 7956: constructing a scheme morphism to an affine curve

Issue created by migration from https://trac.sagemath.org/ticket/7956

Original creator: wjp

Original creation time: 2010-01-16 18:27:44

Assignee: AlexGhitza

CC:  mjo

From http://groups.google.com/group/sage-devel/browse_thread/thread/1f3d4eca8bbff6c2/d3108ab8f2060050

Ronald van Luijk encountered the following problem:

sage: S.<p,q> = QQ[]
sage: A1.<r> = AffineSpace(QQ,1)
sage: A1_emb = Curve(p-2)
sage: type(A1_emb)
<class 'sage.schemes.plane_curves.affine_curve.AffineCurve_generic'>
sage: g = A1.hom([2,r],A1_emb)
TypeError: _point_morphism_class() takes exactly 1 non-keyword argument (3 
given)

We browsed through the schemes module a bit, and the functionality for a morphism to an affine curve does seem to exist through functions such as AlgebraicScheme_subscheme_affine._point_morphism_class(), but
is not accessible since AlgebraicScheme_subscheme_affine is not a superclass of AffineCurve_generic. Comparing it to the projective case, AlgebraicScheme_subscheme_projective _is_ a superclass of ProjectiveCurve_generic.

Is this a simple oversight in the class hierarchy for AffineCurve_generic, or is there a more fundamental reason why this does not yet work?


I made a patch (for sage 4.2) that makes the class hierarchy for affine curves similar to that of projective curves, but would appreciate if someone familiar with the schemes module could take a look since it is a rather invasive change:

http://www.math.leidenuniv.nl/~wpalenst/sage/affine_morphism.patch

The patch also changes the constructor of SchemeMorphism_on_points_affine_space to expect a number of polynomials equal to the dimension of the ambient space instead of the dimension of the curve/subscheme, analogous to a change to
SchemeMorphism_on_points_projective_space by David Kohel from 2007.


---

Comment by wjp created at 2010-01-16 18:29:07

A cleaner version of the code to reproduce it:


```
sage: S.<p,q> = QQ[]
sage: A1.<r> = AffineSpace(QQ,1)
sage: A1_emb = Curve(p-2)
sage: type(A1_emb)
<class 'sage.schemes.plane_curves.affine_curve.AffineCurve_generic'>
sage: g = A1.hom([2,r],A1_emb)
TypeError: _point_morphism_class() takes exactly 1 non-keyword argument (3 given)
```



---

Attachment


---

Attachment

Add a doctest constructing such a morphism.


---

Comment by mjo created at 2012-01-13 19:24:47

It looks like this is working, here's a doctest for it.


---

Comment by mjo created at 2012-01-13 19:24:47

Changing status from new to needs_review.


---

Comment by mstreng created at 2012-01-16 16:16:49

Replying to [comment:3 mjo]:
> It looks like this is working, here's a doctest for it.

You mean that the bug is fixed in current Sage already, not that wjp's patch is working.

Apply sage-trac_7956.patch only.


---

Comment by mstreng created at 2012-01-16 18:59:58

Why not just have the ticket closed, instead of adding a doctest?


---

Comment by mjo created at 2012-01-16 19:24:19

Replying to [comment:5 mstreng]:
> Why not just have the ticket closed, instead of adding a doctest?

Primarily to prevent someone from breaking it again in the future (by accident, anyway).


---

Comment by mstreng created at 2012-08-03 11:12:49

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-08-14 07:02:13

Resolution: fixed
