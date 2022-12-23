# Issue 2952: LaurentPolynomialRing coercion error

Issue created by migration from https://trac.sagemath.org/ticket/2952

Original creator: mhansen

Original creation time: 2008-04-18 21:04:57

Assignee: roed

Currently

```
sage: R.<q>=QQ[]
sage: L.<x,y,z> = LaurentPolynomialRing(R)
sage: f=(x+y+z^-1)^2
sage: f.substitute(z=1)
```

gives an error because it PolynomialRing isn't imported categories/pushout.py for the Laurent functor.

Once, that it is fixed, the above commands give a coercion error between the fraction field of QQ['q'] and the Laurent polynomial ring over QQ['q']


---

Attachment


---

Comment by mhansen created at 2008-04-26 01:51:10

The patch doesn't work.  We'll wait on this until the new coercion framework goes in.


---

Comment by mabshoff created at 2008-09-14 02:32:46

This is still broken and the new coercion framework has been merged:

```
----------------------------------------------------------------------
| SAGE Version 3.1.2.rc2, Release Date: 2008-09-12                   |
| Type notebook() for the GUI, and license() for information.        |
sage: R.<q>=QQ[]
sage: L.<x,y,z> = LaurentPolynomialRing(R)
sage: 
sage: f=(x+y+z^-1)^2
sage: f.substitute(z=1)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)

/scratch/mabshoff/release-cycle/sage-3.1.2.rc3/<ipython console> in <module>()

/scratch/mabshoff/release-cycle/sage-3.1.2.rc3/element.pyx in sage.structure.element.Element.substitute (sage/structure/element.c:3756)()

/scratch/mabshoff/release-cycle/sage-3.1.2.rc3/laurent_polynomial.pyx in sage.rings.polynomial.laurent_polynomial.LaurentPolynomial_mpair.subs (sage/rings/polynomial/laurent_polynomial.c:6666)()

/scratch/mabshoff/release-cycle/sage-3.1.2.rc3/element.pyx in sage.structure.element.RingElement.__imul__ (sage/structure/element.c:9590)()

/scratch/mabshoff/release-cycle/sage-3.1.2.rc3/coerce.pyx in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6008)()

/scratch/mabshoff/release-cycle/sage-3.1.2.rc3/coerce.pyx in sage.structure.coerce.CoercionModel_cache_maps.get_action (sage/structure/coerce.c:9310)()

/scratch/mabshoff/release-cycle/sage-3.1.2.rc3/coerce.pyx in sage.structure.coerce.CoercionModel_cache_maps.discover_action (sage/structure/coerce.c:10441)()

/scratch/mabshoff/release-cycle/sage-3.1.2.rc3/coerce.pyx in sage.structure.coerce.CoercionModel_cache_maps.discover_action (sage/structure/coerce.c:10088)()

/scratch/mabshoff/release-cycle/sage-3.1.2.rc3/parent.pyx in sage.structure.parent.Parent.get_action (sage/structure/parent.c:8569)()

/scratch/mabshoff/release-cycle/sage-3.1.2.rc3/parent_old.pyx in sage.structure.parent_old.Parent._get_action_ (sage/structure/parent_old.c:5963)()

/scratch/mabshoff/release-cycle/sage-3.1.2.rc3/parent_old.pyx in sage.structure.parent_old.Parent.get_action_c (sage/structure/parent_old.c:2264)()

/scratch/mabshoff/release-cycle/sage-3.1.2.rc3/parent_old.pyx in sage.structure.parent_old.Parent.get_action_impl (sage/structure/parent_old.c:2481)()

/scratch/mabshoff/release-cycle/sage-3.1.2.rc3/parent_old.pyx in sage.structure.parent_old.Parent.get_action_c_impl (sage/structure/parent_old.c:3341)()

/scratch/mabshoff/release-cycle/sage-3.1.2.rc3/coerce_actions.pyx in sage.structure.coerce_actions.ModuleAction.__init__ (sage/structure/coerce_actions.c:3706)()

/scratch/mabshoff/release-cycle/sage-3.1.2.rc3/local/lib/python2.5/site-packages/sage/categories/pushout.py in pushout(R, S)
    437         if len(Sc) == 0:
    438             c = Rc.pop()
--> 439             Z = c(Z)
    440         elif len(Rc) == 0:
    441             c = Sc.pop()

/scratch/mabshoff/release-cycle/sage-3.1.2.rc3/local/lib/python2.5/site-packages/sage/categories/pushout.py in __call__(self, R)
    136             return LaurentPolynomialRing(R.base_ring(), (list(R.variable_names()) + [self.var]))
    137         else:
--> 138             return PolynomialRing(R, self.var)
    139     def __cmp__(self, other):
    140         c = cmp(type(self), type(other))

NameError: global name 'PolynomialRing' is not defined
sage: 
```

It seems that David's patch is not the right solution, so can someone come up with a better patch?

Cheers,

Michael


---

Comment by chapoton created at 2014-03-04 12:31:29

Changing keywords from "" to "laurent polynomials".


---

Comment by pbruin created at 2014-05-04 23:51:19

It seems the underlying problem is that `LaurentPolynomial_mpair.__pow__()` can return Laurent polynomials whose coefficients do not lie in its base ring, but in its fraction field:

```
sage: R.<q>=QQ[]
sage: L.<x,y,z> = LaurentPolynomialRing(R)
sage: g=z^-1
sage: parent(g)
Multivariate Laurent Polynomial Ring in x, y, z over Univariate Polynomial Ring in q over Rational Field
sage: parent(g.coefficients()[0])
Fraction Field of Univariate Polynomial Ring in q over Rational Field
```

The last line should simply be `Univariate ...`

A slightly unrelated note: `z^-1` still lies in `L` (ignoring this bug), but `1/z` and `~z` return elements of the fraction field of `L`.


---

Comment by pbruin created at 2014-05-05 01:23:17

Changing status from needs_work to needs_review.


---

Comment by pbruin created at 2014-05-05 01:23:17

Changing priority from critical to major.


---

Comment by pbruin created at 2014-05-05 01:23:17

Changing component from coercion to algebra.


---

Comment by pbruin created at 2014-05-05 01:23:17

The attached branch implements `LaurentPolynomial_mpair.__invert__()` from scratch and uses this for `__pow__()` with a negative exponent.


---

Comment by chapoton created at 2014-06-04 19:41:04

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2014-06-04 19:41:04

Looks good to me, and the bot is happy. I have made very minor changes, so I allow myself to put this to positive review.
----
New commits:


---

Comment by vbraun created at 2014-06-06 11:00:32

Resolution: fixed
