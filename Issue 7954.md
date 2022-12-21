# Issue 7954: Defining affine curves in 3D space

Issue created by migration from Trac.

Original creator: wjp

Original creation time: 2010-01-16 18:15:19

Assignee: AlexGhitza

CC:  klee

Reported by Ronald van Luijk:

because the Curve constructor automatically interprets a homogeneous polynomial in 3 variables as a projective curve, the following doesn't work:


```
A.<x,y,z>=AffineSpace(QQ,3)
C=Curve([x-y,x-z])
```



---

Attachment


---

Comment by wjp created at 2010-01-17 03:53:24

The attached patch adds an optional `space='affine'/'projective'` keyword argument to the Curve constructor.


---

Comment by wjp created at 2010-01-17 03:53:24

Changing status from new to needs_review.


---

Attachment

the previous patch was part 1.  apply this after that one.


---

Comment by was created at 2010-01-17 09:41:20

Hi,

I made some important improvements to the patch while refereeing it.  However, it is clear after looking at this code for a bit that there is a *MAJOR* design flaw (which Willem pointed out to me in person).  The flaw is this in plane_curve/affine_curve.py:

```
class AffineSpaceCurve_generic(Curve_generic, AlgebraicScheme_subscheme_affine):
    def _repr_type(self):
        return "Affine Space"
```

However, Curve_generic is very much a *plane* curve:

```
class Curve_generic(AlgebraicScheme_subscheme):
...
    def defining_polynomial(self):
        return self.defining_polynomials()[0]
```


Thus the *isa* relationship that *must* be satisfied by derivation of objects is broken.

The space curve code must be completely moved out of this directory to the appropriate place.


---

Comment by was created at 2010-01-17 09:41:20

Changing status from needs_review to needs_work.


---

Comment by was created at 2010-01-17 09:42:43

I'm going to wait to talk to willem about this instead of just trying to do it myself.


---

Comment by klee created at 2020-07-06 09:54:53

The issue seems to have been solved now by adding `A`mbient space argument to the `Curve` constructor.


```
sage: A.<x,y,z>=AffineSpace(QQ,3)
sage: C = Curve([x-y,y-z],A)
sage: C
Affine Curve over Rational Field defined by x - y, y - z
```



---

Comment by klee created at 2020-07-06 09:57:06

Changing status from needs_work to needs_review.


---

Comment by mkoeppe created at 2020-07-06 12:11:29

Changing status from needs_review to positive_review.


---

Comment by slelievre created at 2020-08-22 07:20:12

Resolution: fixed
