# Issue 5074: singular factorization over GF(p) need not be a complete factorization

Issue created by migration from https://trac.sagemath.org/ticket/5074

Original creator: was

Original creation time: 2009-01-23 14:30:09

Assignee: malb


```
sage: k.<a> = GF(9)
sage: R.<x,y> = PolynomialRing(k)
sage: h = - (-x^2 - x*y + y^2 - 1)^2 * (x^2*y^2 + y^4 + x^2*y + x*y^2 + y^3 - x^2 + x*y + y^2 - 1) * (-x^4 - x^3*y - x*y^3 + y^4 - x^3 + x^2*y + x*y^2 - x^2 - x*y - y^2 + x + 1)

sage: h.factor()
(-1) * (-x^2 - x*y + y^2 - 1) * (x^2*y^2 + y^4 + x^2*y + x*y^2 + y^3 - x^2 + x*y + y^2 - 1) * (x^6 - x^5*y + x*y^5 + y^6 + x^5 + x*y^4 - x^4 + x^2*y^2 + x*y^3 + y^4 + x^2*y - y^2 - x - 1)
sage: h.factor()
(-1) * (-x^2 - x*y + y^2 - 1)^2 * (-x^6*y^2 - x^5*y^3 - x^4*y^4 + x^3*y^5 + x^2*y^6 - x*y^7 + y^8 - x^6*y - x^4*y^3 + x^3*y^4 + x^2*y^5 + x*y^6 + y^7 + x^6 - x^5*y + x^2*y^4 + x^5 + x^3*y^2 - x^2*y^3 - y^5 - x^4 - x^3*y + x^2*y^2 - y^4 + x^2*y + x*y^2 + y^3 - x*y - y^2 - x - 1)
```


Note that the factors need not even be coprime!




---

Comment by was created at 2009-01-23 14:45:34

Code I use to find countexamples:


```
k.<a> = GF(19^2); R.<x,y> = PolynomialRing(k)
for i in range(5000):
    v = [R.random_element() for _ in range(3)]; print i; assert prod(v).factor().prod() == prod(v)
```



---

Attachment


---

Comment by malb created at 2010-07-12 15:13:41

The original problem seems to be fixed by now. I ran the above snipped and everything was fine. However, for GF(9) I do get an error:

```
sage: k.<a> = GF(9)
sage: R.<x,y> = PolynomialRing(k)
sage: h = - (-x^2 - x*y + y^2 - 1)^2 * (x^2*y^2 + y^4 + x^2*y + x*y^2 + y^3 - x^2 + x*y + y^2 - 1) * (-x^4 - x^3*y - x*y^3 + y^4 - x^3 + x^2*y + x*y^2 - x^2 - x*y - y^2 + x + 1)
sage: factor(h)
---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)

sage.rings.polynomial.multi_polynomial.MPolynomial._factor_over_nonprime_finite_field()
AssertionError: bug in Singular factoring an auxiliary polynomial over GF(p): bad multiplicity (1, 2)
```



---

Comment by malb created at 2010-07-12 15:13:41

Changing status from new to needs_work.


---

Comment by was created at 2010-07-14 22:07:24

It's definitely still broken.  Note that it isn't broken every single time :-):

```

sage: sage: k.<a> = GF(9)sage: sage: R.<x,y> = PolynomialRing(k)
sage: sage: h = - (-x^2 - x*y + y^2 - 1)^2 * (x^2*y^2 + y^4 + x^2*y + x*y^2 + y^3 - x^2 + x*y + y^2 - 1) * (-x^4 - x^3*y - x*y^3 + y^4 - x^3 + x^2*y + x*y^2 - x^2 - x*y - y^2 + x + 1)
sage: h.factor()
(-1) * (-x^2 - x*y + y^2 - 1) * (x^2*y^2 + y^4 + x^2*y + x*y^2 + y^3 - x^2 + x*y + y^2 - 1) * (x^6 - x^5*y + x*y^5 + y^6 + x^5 + x*y^4 - x^4 + x^2*y^2 + x*y^3 + y^4 + x^2*y - y^2 - x - 1)
sage: h.factor()
(-1) * (-x^2 - x*y + y^2 - 1)^2 * (-x^6*y^2 - x^5*y^3 - x^4*y^4 + x^3*y^5 + x^2*y^6 - x*y^7 + y^8 - x^6*y - x^4*y^3 + x^3*y^4 + x^2*y^5 + x*y^6 + y^7 + x^6 - x^5*y + x^2*y^4 + x^5 + x^3*y^2 - x^2*y^3 - y^5 - x^4 - x^3*y + x^2*y^2 - y^4 + x^2*y + x*y^2 + y^3 - x*y - y^2 - x - 1)
sage: h.factor()
(-1) * (-x^2 - x*y + y^2 - 1) * (x^8*y^2 - x^7*y^3 + x^6*y^4 - x^5*y^5 + x^3*y^7 + x^2*y^8 + x*y^9 + y^10 + x^8*y + x^7*y^2 - x^3*y^6 - x^2*y^7 + y^9 - x^8 + x^3*y^5 + x*y^7 - y^8 - x^7 + x^4*y^3 + x^3*y^4 - x^2*y^5 + y^7 - x^4*y^2 + x^3*y^3 + x^2*y^4 + x*y^5 - y^6 - x^5 - x^4*y - y^5 + x^4 - x^3*y + x^2*y^2 + x^3 + x*y^2 - y^3 + x^2 - x*y + x + 1)
sage: h.factor()
(-1) * (-x^2 - x*y + y^2 - 1)^2 * (x^2*y^2 + y^4 + x^2*y + x*y^2 + y^3 - x^2 + x*y + y^2 - 1) * (-x^4 - x^3*y - x*y^3 + y^4 - x^3 + x^2*y + x*y^2 - x^2 - x*y - y^2 + x + 1)
```



---

Comment by was created at 2010-07-14 22:10:30

See also #9498.


---

Comment by malb created at 2010-07-15 09:08:11

I just tried it again with 3-1-1-3 which does have some new factorisation code over GF(p)


```
sage: k.<a> = GF(9)sage: sage: R.<x,y> = PolynomialRing(k)
sage: h = - (-x^2 - x*y + y^2 - 1)^2 * (x^2*y^2 + y^4 + x^2*y + x*y^2 + y^3 - x^2 + x*y + y^2 - 1) * (-x^4 - x^3*y - x*y^3 + y^4 - x^3 + x^2*y + x*y^2 - x^2 - x*y - y^2 + x + 1)
sage: for i in range(10): h.factor(proof=False)
....: 
(x^2 + x*y - y^2 + 1)^2 * (x^2*y^2 + y^4 + x^2*y + x*y^2 + y^3 - x^2 + x*y + y^2 - 1) * (x^4 + x^3*y + x*y^3 - y^4 + x^3 - x^2*y - x*y^2 + x^2 + x*y + y^2 - x - 1)
(x^2 + x*y - y^2 + 1)^2 * (x^2*y^2 + y^4 + x^2*y + x*y^2 + y^3 - x^2 + x*y + y^2 - 1) * (x^4 + x^3*y + x*y^3 - y^4 + x^3 - x^2*y - x*y^2 + x^2 + x*y + y^2 - x - 1)
(x^2 + x*y - y^2 + 1)^2 * (x^2*y^2 + y^4 + x^2*y + x*y^2 + y^3 - x^2 + x*y + y^2 - 1) * (x^4 + x^3*y + x*y^3 - y^4 + x^3 - x^2*y - x*y^2 + x^2 + x*y + y^2 - x - 1)
(x^2 + x*y - y^2 + 1)^2 * (x^2*y^2 + y^4 + x^2*y + x*y^2 + y^3 - x^2 + x*y + y^2 - 1) * (x^4 + x^3*y + x*y^3 - y^4 + x^3 - x^2*y - x*y^2 + x^2 + x*y + y^2 - x - 1)
(x^2 + x*y - y^2 + 1)^2 * (x^2*y^2 + y^4 + x^2*y + x*y^2 + y^3 - x^2 + x*y + y^2 - 1) * (x^4 + x^3*y + x*y^3 - y^4 + x^3 - x^2*y - x*y^2 + x^2 + x*y + y^2 - x - 1)
(x^2 + x*y - y^2 + 1)^2 * (x^2*y^2 + y^4 + x^2*y + x*y^2 + y^3 - x^2 + x*y + y^2 - 1) * (x^4 + x^3*y + x*y^3 - y^4 + x^3 - x^2*y - x*y^2 + x^2 + x*y + y^2 - x - 1)
(x^2 + x*y - y^2 + 1)^2 * (x^2*y^2 + y^4 + x^2*y + x*y^2 + y^3 - x^2 + x*y + y^2 - 1) * (x^4 + x^3*y + x*y^3 - y^4 + x^3 - x^2*y - x*y^2 + x^2 + x*y + y^2 - x - 1)
(x^2 + x*y - y^2 + 1)^2 * (x^2*y^2 + y^4 + x^2*y + x*y^2 + y^3 - x^2 + x*y + y^2 - 1) * (x^4 + x^3*y + x*y^3 - y^4 + x^3 - x^2*y - x*y^2 + x^2 + x*y + y^2 - x - 1)
(x^2 + x*y - y^2 + 1)^2 * (x^2*y^2 + y^4 + x^2*y + x*y^2 + y^3 - x^2 + x*y + y^2 - 1) * (x^4 + x^3*y + x*y^3 - y^4 + x^3 - x^2*y - x*y^2 + x^2 + x*y + y^2 - x - 1)
(x^2 + x*y - y^2 + 1)^2 * (x^2*y^2 + y^4 + x^2*y + x*y^2 + y^3 - x^2 + x*y + y^2 - 1) * (x^4 + x^3*y + x*y^3 - y^4 + x^3 - x^2*y - x*y^2 + x^2 + x*y + y^2 - x - 1)


```



---

Attachment

test quality of factorisation for many random examples


---

Comment by malb created at 2010-11-03 13:20:17

I've written a little script to check the quality of factorisation. While I didn't get any wrong answer so far, factorisation sometimes takes ages. This is ticket #291 in the Singular bug tracker: http://www.singular.uni-kl.de:8002/trac/ticket/291

Strictly speaking, this ticket could be closed (modulo review of the patch etc) since there are no known examples where the wrong factorisation is returned. Alternatively, we could wait for the performance issue to be resolved in Singular.


---

Comment by malb created at 2010-11-03 13:20:17

Changing status from needs_work to needs_info.


---

Comment by malb created at 2010-11-03 13:20:17

Changing keywords from "" to "factorisation".


---

Comment by jdemeyer created at 2013-08-13 15:57:01

Changing status from needs_info to positive_review.


---

Comment by jdemeyer created at 2013-08-13 15:57:01

Totally fixed upstream.


---

Comment by jdemeyer created at 2013-08-16 11:10:49

Resolution: worksforme
