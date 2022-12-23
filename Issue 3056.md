# Issue 3056: bug with polynomials over power series

Issue created by migration from https://trac.sagemath.org/ticket/3056

Original creator: kedlaya

Original creation time: 2008-04-29 21:04:34

Assignee: mabshoff

CC:  burcin

The first computation of z^2 is incorrect, whereas the second is correct:

```
sage: C.<t> = PowerSeriesRing(ZZ)
sage: D.<s> = PolynomialRing(C)
sage: z = (1 + O(t)) + t*s^2
sage: z^2
 t^2*s^4 + 1 + O(t)
sage: z._mul_generic(z)
 t^2*s^4 + (2*t + O(t^2))*s^2 + 1 + O(t)
```



---

Comment by kedlaya created at 2008-04-29 21:07:10

Changing assignee from mabshoff to dmharvey.


---

Comment by kedlaya created at 2008-04-29 21:07:10

Changing keywords from "" to "polynomials, power series, Karatsuba".


---

Comment by kedlaya created at 2008-04-29 21:07:10

Changing component from Cygwin to basic arithmetic.


---

Comment by kedlaya created at 2008-04-29 21:07:10

Changing priority from major to blocker.


---

Comment by kedlaya created at 2008-04-29 21:07:10

A bit of experimentation by David Harvey suggests that _mul_karatsuba is at fault.


---

Comment by kedlaya created at 2008-04-29 21:14:25

Changing assignee from dmharvey to roed.


---

Comment by kedlaya created at 2008-04-29 21:14:25

In my previous example:

```
sage: (z^2).list()
 [1 + O(t), O(t^1), O(t^1), 0, t^2]
```

so the output is not actually incorrect, just less precise than it should be. So maybe we should not use Karatsuba for polynomials over an inexact ring? (We already don't for polynomials over a p-adic ring.)


---

Comment by dmharvey created at 2008-04-30 13:28:40

Changing priority from blocker to major.


---

Comment by dmharvey created at 2008-04-30 13:28:40

Given that this is a printing problem rather than an incorrect output problem, I'm removing the blocker tag.


---

Attachment


---

Attachment

Changes doctests to reflect classical multiplication used instead of karatsuba.  Note that in every case (with possible exception of the test in padics/pow_computer_ext.pyx), the result is better (higher precision when inexact; simpler form when exact).  In the case of padics/pow_computer_ext.pyx, it is unclear that the original was correct to any reasonable precision.  David Roe seemed to think that this was ok.

Also, I added the test that presented this problem to the doctests of polynomial_element.__mul__


---

Comment by craigcitro created at 2009-01-24 12:49:30

Looks good.


---

Comment by mabshoff created at 2009-01-24 18:42:01

Resolution: fixed


---

Comment by mabshoff created at 2009-01-24 18:42:01

Merged in Sage 3.3.alpha2
