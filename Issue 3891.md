# Issue 3891: polynomial sqrt method

Issue created by migration from Trac.

Original creator: jbmohler

Original creation time: 2008-08-18 14:00:37

Assignee: somebody

CC:  cremona

John Cremona requests a sqrt for polynomial rings:


```
I have needed the following.  g(x) is a univariate polynomial which I
know to be a square, and i want its square root.  g.factor() does too
much, as does g.squarefree_decomposition().  I can get the sqrt via
g.gcd(g.derivative()), which works in my case since I know that the
sqrt is itself square-free.
```




---

Comment by jhpalmieri created at 2008-11-19 21:56:57

Changing priority from major to minor.


---

Comment by jhpalmieri created at 2008-11-19 21:56:57

For an integer n, there are two options: n.sqrt() or n.is_square().  n.sqrt() returns a square root by passing to a larger ring (like CC) if it needs to, while n.is_square() returns True (and optionally returns a square root) if n is the square of an integer, false otherwise.  I think that we need an is_square method for polynomials, not a sqrt method.

The attached patch provides an is_square method.  It also fixes a bug in squarefree_decomposition: that method would barf for the wrong reason if you gave it a polynomial over a finite field.  Now it barfs for the right reason.


---

Comment by jhpalmieri created at 2008-11-19 21:56:57

Changing keywords from "" to "polynomial, square root".


---

Comment by jhpalmieri created at 2008-11-19 21:56:57

Changing type from defect to enhancement.


---

Attachment


---

Attachment

Positive review for polynomial_is_square.patch, after my own trac3891-reviewer-fixes.patch is applied (so only my patch needs further review).

I think Cremona may have been hoping for a polynomial sqrt that was more efficient than squarefree_decomposition; maybe that should be opened as a new wishlist ticket after this one is closed.


---

Comment by jhpalmieri created at 2008-11-23 23:37:34

The reviewer's patch looks good to me, and all tests passed.  (I based the docstring for is_square on the one for the is_square method for integers, but your modifications make it better.)


---

Comment by mabshoff created at 2008-11-24 00:47:04

Merged both patches in Sage 3.2.1.alpha1


---

Comment by mabshoff created at 2008-11-24 00:47:04

Resolution: fixed
