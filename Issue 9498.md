# Issue 9498: The function _factor_over_nonprime_finite_field is wrong in Sage, so remove it

Issue created by migration from https://trac.sagemath.org/ticket/9498

Original creator: was

Original creation time: 2010-07-14 14:18:10

Assignee: malb

I wrote the function _factor_over_nonprime_finite_field in multi_polynomial.pyx in hopes that Singular's multivariate poly factorization worked over GF(p).  But it doesn't, so that function is pointless.  Moreover, as John Cremona pointed out in email on the sagedays23 list recently, the algorithm there is wrong!:

```
If f is irreducible over R but not over S then your
gcd will be f again which does not help you factor over S.

Basically what one needs is that the conjugates of f (whose product is
the norm) are coprime.

?
```


Here's an example to illustrate that it is wrong:

```
flat:polynomial wstein$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: R.<x> = GF(3)[]
sage: x^2+1
x^2 + 1
sage: (x^2+1).factor()
x^2 + 1
sage: f = x^2+1
sage: f
x^2 + 1
sage: g = f.change_ring(GF(9,'a'))
sage: g
x^2 + 1
sage: g.factor()
(x + a + 1) * (x + 2*a + 2)
sage: type(g)
<type 'sage.rings.polynomial.polynomial_zz_pex.Polynomial_ZZ_pEX'>
sage: R.<x,y> = GF(3)[]
sage: f = x^2+1
sage: g = f.change_ring(GF(9,'a'))
sage: g
x^2 + 1
sage: g.factor()
---------------------------------------------------------------------------
NotImplementedError                       Traceback (most recent call last)
| Sage Version 4.4.4, Release Date: 2010-06-23                       |
| Type notebook() for the GUI, and license() for information.        |
/Users/wstein/sage/build/sage-4.4.4/devel/sage-main/sage/rings/polynomial/<ipython console> in <module>()

/Users/wstein/sage/build/sage-4.4.4/local/lib/python2.6/site-packages/sage/rings/polynomial/multi_polynomial_libsingular.so in sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular.factor (sage/rings/polynomial/multi_polynomial_libsingular.cpp:22745)()
   3586                 raise NotImplementedError, "Factorization of multivariate polynomials over prime fields with characteristic > 2^29 is not implemented."
   3587             if proof:
-> 3588                 raise NotImplementedError, "proof = True factorization not implemented.  Call factor with proof=False."
   3589             if not self._parent._base.is_prime_field():
   3590                 return self._factor_over_nonprime_finite_field()

NotImplementedError: proof = True factorization not implemented.  Call factor with proof=False.
sage: g._factor_over_nonprime_finite_field()
x^2 + 1
sage: g.factor(proof=False)
x^2 + 1
```


The point is that g should factor as a product of two linear factors. 

So, let's just delete this function, and anything that calls it, and use Singular's builtin factorization code in the non-prime case. 


---

Comment by was created at 2010-07-14 15:10:58

Look into whether the comment malb posted on #5074 is really just an indication of a bug in this code, and not in Singular.


---

Attachment


---

Attachment


---

Comment by was created at 2010-07-14 22:15:38

Changing status from new to needs_review.


---

Comment by davidloeffler created at 2010-12-16 11:28:48

Looks good to me. Since there seems to be no movement on #5074 -- I guess we're waiting for the Singular performance bug to be resolved -- let's at least deal with this ticket. 

I tested `sage/rings` with `trac_9498.patch` applied and everything passed. Strictly speaking we should perhaps have a doctest, but since the patch adds no new code -- it just removes bad old code -- I don't think there's any need to insist on that.


---

Comment by davidloeffler created at 2010-12-16 11:28:48

Changing status from needs_review to positive_review.


---

Attachment

Same patch, fixed commit message


---

Comment by jdemeyer created at 2011-01-19 22:21:28

Resolution: fixed
