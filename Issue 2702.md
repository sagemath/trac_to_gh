# Issue 2702: [with patch, needs review] multi_polynomial_libsingular coverage almost 100%

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2008-03-28 17:24:12

Assignee: failure


```
----------------------------------------------------------------------
sage/rings/polynomial/multi_polynomial_libsingular.pyx
SCORE sage/rings/polynomial/multi_polynomial_libsingular.pyx: 98% (80 of 81)

Missing doctests:
         * _macaulay2_set_ring(self, macaulay2)

----------------------------------------------------------------------
```


I cannot write a doctest for `_macaulay2_set_ring` yet because the optional M2 spkg is not installable.


---

Attachment

This is a positive review about the patch, but it's a big patch and could use another set of eyes, I expect.  I think it looks like it cleans up a lot of evolved changes to make the whole thing more cohesive.  I did not apply and doc-test (because I don't have a recent 2.11.alphaX build).

Two specific comments:
 * 1) I think the documentation of is_monomial should be very clear that 2*x is not monomial (with a sentence in the initial header).  This is not my intuitive definition of monomial, but it's a sane definition.  I would prefer that 2*x be a monomial, but it's not a big deal.
 * 2)  I see a number of lines like

```
sage: Q.<x,y,z>=MPolynomialRing(QQ,3)
```

I think they should be one of the following:

```
sage: Q.<x,y,z>=PolynomialRing(QQ)
sage: Q.<x,y,z>=QQ[]
```

William has made the comment that doc-tests should represent good sage usage and I think both of those are better than the first (certainly the "3" is unnecessary and obnoxious -- I suspect it's only recently that the 3 wasn't required.).  I think there is some room for personal opinion here -- perhaps some mixture is also good to let people see alternate styles as well.


---

Comment by malb created at 2008-03-28 19:23:28

Replying to [comment:1 jbmohler]:
> Two specific comments:
>  * 1) I think the documentation of is_monomial should be very clear that 2*x is not monomial (with a sentence in the initial header).  This is not my intuitive definition of monomial, but it's a sane definition.  I would prefer that 2*x be a monomial, but it's not a big deal.

I'll add that to the docstring.

>  * 2)  I see a number of lines like
> {{{
> sage: Q.<x,y,z>=MPolynomialRing(QQ,3)
> }}}
> I think they should be one of the following:
> {{{
> sage: Q.<x,y,z>=PolynomialRing(QQ)
> sage: Q.<x,y,z>=QQ[]
> }}}

It is still not clear what will happen to `MPolynomialRing` and `PolynomialRing`, but I'll remove the unnecessary "3".


---

Comment by jbmohler created at 2008-03-28 22:37:04

Replying to [comment:2 malb]:
> Replying to [comment:1 jbmohler]:
> > Two specific comments:
> >  * 1) I think the documentation of is_monomial should be very clear that 2*x is not monomial (with a sentence in the initial header).  This is not my intuitive definition of monomial, but it's a sane definition.  I would prefer that 2*x be a monomial, but it's not a big deal.
> 
> I'll add that to the docstring.

Upon more checking, I noticed that MPolynomial_polydict takes the differing convention.  They certainly should be consistent -- I don't care which way.


---

Comment by mhansen created at 2008-03-29 08:12:07

malb, I'm reviewing the patch too and taking care of these issues.


---

Comment by mhansen created at 2008-03-29 08:44:56

I changed many of the doctests to use a more "modern" style for constructing the polynomial rings.  I also changed is_monomial to treat 2*x as a monomial since it agrees with _polydict and matches the standard mathematical definition for a monomial.

Apply the last two patches.  They apply to 2.11 alpha1 and pass -testall


---

Comment by malb created at 2008-03-29 11:39:48

Replying to [comment:5 mhansen]:
> I changed many of the doctests to use a more "modern" style for constructing the polynomial rings.  

mhansen, thanks for taking car of this!

> I also changed is_monomial to treat 2*x as a monomial since it agrees with 
> _polydict and matches the standard mathematical definition for a monomial.

Please don't!
 * there is no standard mathematical definition for a monomial. If *t = 2xy* Cox, Little, O'Shea call *xy* a monomial and *2xy* a term in "Ideals, Varieties, and Algorithms". Becker and Weispfennig call *xy* the term and *2xy* the monomial in "Gröbner Bases".
 * Singular is inconsistent: `lead` returns the leading term and means *2yx*, `leadmonom` returns *yx* but they define a monomial as

```
[coefficient] ring_variable [ exponent] [ring_variable [exponent] ...]
```

 * Magma has *yx* == monomial too: "A monomial (or power product) of P is a product of powers of the variables (or indeterminates) of P, that is, an expression of the form x1> ... xn> with ei ≥0 for 1 ≤i ≤n. Multivariate polynomials in Magma are stored efficiently in distributive form, using arrays of coefficient-monomial pairs, where the coefficient is in the base ring R. The word `term' will always refer to a coefficient multiplied by a monomial."
 * Sage is (or should be) strict so far: `lm()` returns *xy* and not *2yx*


> Apply the last two patches.  They apply to 2.11 alpha1 and pass -testall


---

Comment by mhansen created at 2008-03-29 19:50:19

I've updated 2702-referee.patch to use the old definition of monomial, added an extra docstest, and a sentence in the docstring describing what it's using for the definition of monomial.


This should probably be taken to sage-devel.


I'm fine with the last two patches being applied.


---

Attachment


---

Comment by mabshoff created at 2008-03-29 20:30:46

Resolution: fixed


---

Attachment

Merged 2702.patch and 2702-referee.patch in Sage 2.11.rc0
