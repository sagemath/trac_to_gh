# Issue 3964: projective space homs do not check arguments sufficiently

Issue created by migration from https://trac.sagemath.org/ticket/3964

Original creator: cremona

Original creation time: 2008-08-27 09:06:09

Assignee: was

Keywords: projective space morphism

Alex Ghitsa reported:

```
I am fairly certain the following two things are bugs, but I want to
double-check that I'm not doing something stupid before submitting a ticket:

sage: R.<x,y> = QQ[]
sage: P1 = ProjectiveSpace(R)
sage: H = P1.Hom(P1)
sage: f = H([x-y, x*y])
sage: f

Scheme endomorphism of Projective Space of dimension 1 over Rational Field
 Defn: Defined on coordinates by sending (x : y) to
       (x - y : x*y)


This is nonsense: there is no morphism from P1 to P1 given by those
equations, since the two polynomials x-y and x*y are not homogeneous of
the same degree.  I think Sage should throw a ValueError here.

The second example:

sage: R.<x,y> = QQ[]
sage: P1 = ProjectiveSpace(R)
sage: H = P1.Hom(P1)
sage: f = H([x^2, x*y])
sage: f

Scheme endomorphism of Projective Space of dimension 1 over Rational Field
 Defn: Defined on coordinates by sending (x : y) to
       (x^2 : x*y)


This is also bad: the two polynomials are now homogeneous of degree 2,
but they are not relatively prime (and so this is not a morphism from P1
to P1, but rather a rational map since it is not defined at (0 : y)).  I
think Sage should also throw a ValueError here.

(Or maybe I'm doing things wrong, in which case I'd love to find out how
to make this work.)
```


to which John Cremona added:

```
You are definitely right.  The problem lies (as far as I can see) in
sage.schemes.generic in the __init__ funtion of class
SchemeMorphism_on_points_projective_space.  (I only found this out by
tring to construct a morphism from P^1 to P^1 using 3 polynomials,
which did raise an error in this very function.)

It appears that the only check this function does is that the number
of polys is correct.  It does not check that they are actually polys,
or have the right number of variables, let alone that they are coprime
and homogeneous of the same degree:

sage: S.<u,v,w> = QQ[]
sage: f = H([u,v])
sage: f = H([u*v*w,u+v+w])
sage: f = H([exp(u),exp(v)])
sage: f

Scheme endomorphism of Projective Space of dimension 1 over Rational Field
 Defn: Defined on coordinates by sending (x : y) to
       (e^u : e^v)

with H as in your example.

This definitely deserves a ticket, which I will create. now.
```



---

Comment by AlexGhitza created at 2008-12-21 10:26:15

I finally got around to fixing this.  The attached patch fixes the issues reported above (by John and myself), and adds some doctests.


---

Attachment


---

Comment by cremona created at 2008-12-21 13:25:52

This looks pretty good (I have not actually tested it yet though).  Alex, can we not check that the polys define a map to the correct space by checking that the defining polys of the target (if any) vanish when evaluated at the tuple of polys defining the map?  If that works it would be worthwhile adding it.


---

Comment by AlexGhitza created at 2008-12-21 15:55:22

Good point.  I will implement this and submit a new patch.  I also just realized that I misread a docstring and implemented some things the wrong way around, so I will get that fixed.


---

Comment by AlexGhitza created at 2009-03-29 08:18:53

Changing assignee from was to AlexGhitza.


---

Comment by AlexGhitza created at 2009-03-29 08:18:53

Changing status from new to assigned.


---

Comment by was created at 2010-01-17 08:59:11

apply this (not the previous one).


---

Attachment


---

Comment by was created at 2010-01-17 08:59:26

Changing status from needs_work to needs_review.


---

Comment by was created at 2010-01-17 09:00:07

Hi,

I took Alex's patch, added a bunch of doctests, changed it some, and read it.  I think this should go in if it looks ok to John or Alex.  It's a clear improvement, though arbitrarily much works remains!


---

Comment by cremona created at 2010-01-17 11:16:38

Changing status from needs_review to positive_review.


---

Comment by cremona created at 2010-01-17 11:16:38

Patch applies fine to 4.3.1.rc0 and tests pass.  So I'll give this a positive review despite the fact that (as was said) there's a lot more needing to be done, for example:


```
sage: S.<u,v,w> = QQ[]
sage: C = Curve(u^2+v^2-w^2); C
Projective Curve over Rational Field defined by u^2 + v^2 - w^2
sage: H = C.Hom(C); H
Set of points of Projective Curve over Rational Field defined by u^2 + v^2 - w^2 defined over Quotient of Multivariate Polynomial Ring in u, v, w over Rational Field by the ideal (u^2 + v^2 - w^2)
sage: 
sage: H([u,v,w])
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
...
AttributeError: 'QuotientRingElement' object has no attribute 'degree'
```



---

Comment by rlm created at 2010-01-18 23:44:40

Resolution: fixed


---

Comment by cremona created at 2010-11-21 16:50:40

See #10297 for the next step in this direction.
