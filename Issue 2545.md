# Issue 2545: [with patch, needs review] FractionFieldElement lacks derivative method

Issue created by migration from https://trac.sagemath.org/ticket/2545

Original creator: burcin

Original creation time: 2008-03-16 12:35:22

Assignee: burcin

Attached patch adds a `derivative` method to `FractionFieldElement`s, and fixes a bug in the `_derivative` method of `Polynomial_rational_dense`.

So these now work:


```
sage: R = ZZ['x']
sage: S = R.fraction_field(); x = S.gen()
sage: R(1).derivative(R(x))
0

sage: F = FractionField(PolynomialRing(RationalField(),'x,y'))
sage: x,y = F.gens()
sage: (1/(x+y)).derivative(x,y)
2/(x^3 + 3*x^2*y + 3*x*y^2 + y^3)
```






---

Comment by burcin created at 2008-03-16 12:35:51

derivative method for FractionFieldElement


---

Attachment

This appears to work as advertised.  I have one request: the docstrings for derivative() and _derivative() refer to "the derivative of this polynomial", which is bad since these elements are (most of the time) not polynomials.  This should be replaced with "rational function" or something similar.


---

Comment by burcin created at 2008-03-16 14:48:47

new patch with requested doc changes


---

Attachment

You're right, I copied the text from the docstring for polynomials, and forgot to change it. :)

attachment:2545-sage_fraction_field_derivative-1.patch replaces "polynomial" with "rational function" as suggested.


---

Comment by AlexGhitza created at 2008-03-16 15:14:42

Cool.  I'm satisfied.


---

Comment by mabshoff created at 2008-03-18 00:06:36

Resolution: fixed


---

Comment by mabshoff created at 2008-03-18 00:06:36

Merged in Sage 2.11.alpha0
