# Issue 2276: M.divides(N) gives an error if M and N are monomials in R.<x,y> = PolynomialRing(QQ); ok for R.<x>

Issue created by migration from https://trac.sagemath.org/ticket/2276

Original creator: jxxcarlson

Original creation time: 2008-02-23 08:41:02

Assignee: was

sage: R.<x,y> = PolynomialRing(QQ)
sage: M = x*y
sage: N = x<sup>2*y</sup>3
sage: M.divides(N)
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/Users/carlson/docs`@`chiquito/_Research/CIMAT_Lectures/Computation/sageprogs/<ipython console> in <module>()

/Users/carlson/docs`@`chiquito/_Research/CIMAT_Lectures/Computation/sageprogs/element.pyx in sage.structure.element.CommutativeRingElement.divides()

<type 'exceptions.TypeError'>: unsupported operand type(s) for %: 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular' and 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'


---

Comment by mabshoff created at 2008-02-23 14:58:51

Changing component from algebraic geometry to commutative algebra.


---

Comment by mabshoff created at 2008-02-23 14:58:51

Changing assignee from was to malb.


---

Comment by mabshoff created at 2008-03-18 21:06:16

Changing priority from major to blocker.


---

Comment by mabshoff created at 2008-03-18 21:06:16

This is still an issue with 2.10.4. 

Cheers,

Michael


---

Attachment

The attached patch implements `__mod__` which fixes the issue. Note, that type checking is performed in `quo_rem` and thus is not needed in `__mod__`.


---

Comment by mabshoff created at 2008-03-28 12:42:57

Patch looks good to me, is sufficiently doctested. Nice. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-28 13:27:07

Merged in Sage 2.11.alpha2


---

Comment by mabshoff created at 2008-03-28 13:27:07

Resolution: fixed
