# Issue 250: strange display of nested rings

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-02-08 03:39:35

Assignee: was

{{{ 
sage: R, u = PolynomialRing(GF(p), 'u').objgen()
 
sage: S, v = PolynomialRing(R, 'v').objgen()
 
sage: T = S.fraction_field()
 
sage: F = EllipticCurve(T, [a, b])
 
sage: F
 Elliptic Curve defined by y^2 + (0)*x*y + (0)*y = x^3 + (0)*x^2 + x
+1 over Fraction Field of Univariate Polynomial Ring in v over
Univariate Polynomial Ring in u over Finite Field of size 29
 
I'm sure there's a better example of this strange printing, but this
is how I found it.
 
Nick
 
 }}}


---

Attachment


---

Comment by was created at 2007-10-21 02:54:20

Resolution: fixed
