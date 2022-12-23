# Issue 7907: Bug in characteristic 2 isogenies of degree >3

Issue created by migration from https://trac.sagemath.org/ticket/7907

Original creator: cremona

Original creation time: 2010-01-12 12:36:44

Assignee: cremona

CC:  wuthrich shumow

Keywords: isogeny

The method  __compute_omega_general() in ell_curve_isogeny.py contains

```
        for j  in xrange(0,n-1):
            psi_prpr = psi_prpr + \
                binomial(j+2,2)*psi_coeffs[(j+2)]*cur_x_pow
            cur_x_pow = x*cur_x_pow
```

where the degree of the isogeny is 2*n+1.   In degree 3 (the only case doctested) n=1 and the loop is empty.  Otherwise there is a run-time error since the name "binomial" has not been imported.

This will be simple to patch, but of course as this indicated that higher degree isogenies in char.2 have not been tested, other issues might arise.

Patch up soon.


---

Comment by cremona created at 2010-01-12 12:45:25

Here's an example of the failure which will be put into a doctest in the patch.

Before:


```
sage: F = GF(128,'a')                                     
sage: a = F.gen()                                         
sage: E = EllipticCurve([1,0,0,0,(a**6+a**4+a**2+a)])     
sage: x = polygen(F)
sage: ker =  (x^6 + (a^6 + a^5 + a^4 + a^3 + a^2 + a)*x^5 + (a^6 + a^5 + a^2 + 1)*x^4 + (a^6 + a^5 + a^4 + a^3 + a^2 + 1)*x^3 + (a^6 + a^3 + a)*x^2 + (a^4 + a^3 + 1)*x + a^5 + a^4 + a) 
sage: E.isogeny(ker)        
Traceback (most recent call last):
...
NameError: global name 'binomial' is not defined
```


After:

```
sage: F = GF(128,'a')                                     
sage: a = F.gen()                                         
sage: E = EllipticCurve([1,0,0,0,(a**6+a**4+a**2+a)])     
sage: x = polygen(F)
sage: ker =  (x^6 + (a^6 + a^5 + a^4 + a^3 + a^2 + a)*x^5 + (a^6 + a^5 + a^2 + 1)*x^4 + (a^6 + a^5 + a^4 + a^3 + a^2 + 1)*x^3 + (a^6 + a^3 + a)*x^2 + (a^4 + a^3 + 1)*x + a^5 + a^4 + a)
sage: E.isogeny(ker)                                      
Isogeny of degree 13 from Elliptic Curve defined by y^2 + x*y = x^3 + (a^6+a^4+a^2+a) over Finite Field in a of size 2^7 to Elliptic Curve defined by y^2 + x*y = x^3 + (a^6+a^5+a^4+a^3+a^2+a)*x + (a^5+a^3) over Finite Field in a of size 2^7
```



---

Comment by cremona created at 2010-01-12 12:49:40

Applies to 4.3.1.alpha1


---

Attachment

Applies to 4.3.1.alpha1; replaced previous (wrongly named!)


---

Attachment


---

Comment by cremona created at 2010-01-12 12:51:43

Changing status from new to needs_review.


---

Comment by wuthrich created at 2010-01-12 14:46:21

fine. it passes all tests.


---

Comment by wuthrich created at 2010-01-12 14:46:21

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-01-13 08:02:18

Resolution: fixed
