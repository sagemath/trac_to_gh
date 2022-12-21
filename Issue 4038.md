# Issue 4038: Problem in factor() and roots() for p-adic polynomials

Issue created by migration from Trac.

Original creator: cremona

Original creation time: 2008-09-02 13:37:32

Assignee: malb

CC:  wuthrich

Keywords: polynomial p-adic

This was reported by Chris Wuthrich while reviewing #3377:


```
sage: E = EllipticCurve('37a1')
sage: K =Qp(7,10)                 
sage: EK = E.base_extend(K)
sage: E = EllipticCurve('37a1')
sage: K = Qp(7,10)             
sage: EK = E.base_extend(K)    
sage: g = EK.division_polynomial_0(3)
sage: type(g)
<class 'sage.rings.polynomial.padics.polynomial_padic_capped_relative_dense.Polynomial_padic_capped_relative_dense'>
sage: g.factor()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/home/john/sage-3.1.2.alpha3/<ipython console> in <module>()

/home/john/sage-3.1.2.alpha3/local/lib/python2.5/site-packages/sage/rings/polynomial/padics/polynomial_padic_capped_relative_dense.py in factor(self)
   1009         R = ZpCA(base.prime(), prec = m)
   1010         S = PolynomialRing(R, self.parent().variable_name())
-> 1011         F = S(self).factor()
   1012         return Factorization([(self.parent()(a), b) for (a, b) in F], base(F.unit()))
   1013 

/home/john/sage-3.1.2.alpha3/local/lib/python2.5/site-packages/sage/rings/polynomial/padics/polynomial_padic_flat.py in factor(self, absprec)
    133             lval = F[i][0].leading_coefficient().valuation()
    134             if upart != 1:
--> 135                 F[i] = (F[i][0] // upart, F[i][1])
    136                 u *= upart ** F[i][1]
    137             c -= lval * F[i][1]

/home/john/sage-3.1.2.alpha3/polynomial_element.pyx in sage.rings.polynomial.polynomial_element.Polynomial_generic_dense.__floordiv__ (sage/rings/polynomial/polynomial_element.c:28101)()

AttributeError: 'Polynomial_padic_flat' object has no attribute '__coeffs'
```


Somewhere in the polynomial hierarchy, this particular type of polynomial is not having its `__coeffs` field set.


---

Attachment

In 3.2.2 the error message changes to:

```
sage: g.factor()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/home/jec/.sage/temp/host_57_89/5017/_home_jec__sage_init_sage_0.py in <module>()
----> 1
      2
      3
      4
      5

/home/jec/sage-3.2.2/local/lib/python2.5/site-packages/sage/rings/polynomial/padics/polynomial_padic_capped_relative_dense.pyc in factor(self)
   1009         R = ZpCA(base.prime(), prec = m)
   1010         S = PolynomialRing(R, self.parent().variable_name())
-> 1011         F = S(self).factor()
   1012         return Factorization([(self.parent()(a), b) for (a, b) in F], base(F.unit()))
   1013

/home/jec/sage-3.2.2/local/lib/python2.5/site-packages/sage/rings/polynomial/padics/polynomial_padic_flat.pyc in factor(self, absprec)
    133             lval = F[i][0].leading_coefficient().valuation()
    134             if upart != 1:
--> 135                 F[i] = (F[i][0] // upart, F[i][1])
    136                 u *= upart ** F[i][1]
    137             c -= lval * F[i][1]

/home/jec/sage-3.2.2/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_element.so in sage.rings.polynomial.polynomial_element.Polynomial_generic_dense.__floordiv__ (sage/rings/polynomial/polynomial_element.c:30443)()
   4436
   4437
-> 4438
   4439
   4440

AttributeError: 'Polynomial_padic_flat' object has no attribute '_parent'
```

And the problem goes away if I change "//" to "/" on line 135 of sage/rings/polynomial/padics/polynomial_padic_flat.py.

Attached patch applies to 3.2.2.


---

Comment by AlexGhitza created at 2008-12-23 12:58:44

Looks good.


---

Comment by mabshoff created at 2008-12-23 21:14:17

Merged in Sage 3.2.3.alpha0


---

Comment by mabshoff created at 2008-12-23 21:14:17

Resolution: fixed
