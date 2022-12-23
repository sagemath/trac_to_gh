# Issue 9646: Incorrect calculation of elliptic curve formal group law

Issue created by migration from https://trac.sagemath.org/ticket/9646

Original creator: hlaw

Original creation time: 2010-07-30 15:06:26

Assignee: cremona

CC:  wuthrich

Keywords: elliptic curve formal group law

If `F(t1, t2)` is a formal group law, then `F(t1, t2) = t1 + t2 (mod t1*t2)`.  So in particular, the coefficients of `t1^i` and `t2^i` are zero for all `i > 1`.  However the formal group law of an elliptic curve as returned by Sage includes (at least) the terms `-a1<sup>2*t1</sup>3` and `-a1<sup>2*t2</sup>2`, as the following example shows:

```
sage: P.<a1, a2, a3, a4, a6> = PolynomialRing(ZZ, 5)
sage: E = EllipticCurve(list(P.gens()))
sage: F = E.formal().group_law(prec = 4)
sage: t2 = F.parent().gen()
sage: t1 = F.parent().base_ring().gen()
sage: F(t1, 0)
t1 - a1^2*t1^3   # should be t1
sage: F(0, t2)
t2 - a1^2*t2^3
```

Note also that the coefficient of `t1^2*t2 + t1*t2^2` returned by sage is `-a1^2 - a2`, whereas, according to Silverman AEC IV.1, it should be simply `-a2`.


---

Comment by hlaw created at 2010-07-30 15:10:24

Added my Sage version and system info.


---

Comment by hlaw created at 2010-07-30 16:33:36

The bug appears to be related to the precision in a regular way:

```
sage: for prec in srange(4, 7):
....: E = EllipticCurve(list(P.gens()))
....: F = E.formal_group()
....: fg = F.group_law(prec)
....: print prec, fg(0, fg.parent().gen())
....: 
4 t2 - a1^2*t2^3
5 t2 + (-a1^3 - a1*a2)*t2^4
6 t2 + (-a1^4 - 2*a1^2*a2 - a1*a3)*t2^5
```

Note that the error is always of degree one less than the precision.  This might be related to the following issue, whereby the calculation dies when the precision is set to 2 or 3:

```
sage: E = EllipticCurve(list(P.gens()))
sage: F = E.formal_group()
sage: fg = F.group_law(2)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/Users/hlaw/Dropbox/phd/thesis/<ipython console> in <module>()

/Users/hlaw/src/sage-src/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/formal_group.pyc in group_law(self, prec)
    524         t3 = -t1 - t2 - \
    525              (a1*lam + a3*lam2 + a2*nu + 2*a4*lam*nu + 3*a6*lam2*nu)/  \
--> 526              (1 + a2*lam + a4*lam2 + a6*lam3)
    527         inv = self.inverse(prec)
    528 

/Users/hlaw/src/sage-src/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.RingElement.__sub__ (sage/structure/element.c:11073)()

/Users/hlaw/src/sage-src/local/lib/python2.6/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6966)()

TypeError: unsupported operand parent(s) for '-': 'Power Series Ring in t2 over Power Series Ring in t1 over Multivariate Polynomial Ring in a1, a2, a3, a4, a6 over Integer Ring' and 'Power Series Ring in t1 over Fraction Field of Multivariate Polynomial Ring in a1, a2, a3, a4, a6 over Integer Ring'
sage: fg = F.group_law(3)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/Users/hlaw/Dropbox/phd/thesis/<ipython console> in <module>()

/Users/hlaw/src/sage-src/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/formal_group.pyc in group_law(self, prec)
    524         t3 = -t1 - t2 - \
    525              (a1*lam + a3*lam2 + a2*nu + 2*a4*lam*nu + 3*a6*lam2*nu)/  \
--> 526              (1 + a2*lam + a4*lam2 + a6*lam3)
    527         inv = self.inverse(prec)
    528 

/Users/hlaw/src/sage-src/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.RingElement.__sub__ (sage/structure/element.c:11073)()

/Users/hlaw/src/sage-src/local/lib/python2.6/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6966)()

TypeError: unsupported operand parent(s) for '-': 'Power Series Ring in t2 over Power Series Ring in t1 over Multivariate Polynomial Ring in a1, a2, a3, a4, a6 over Integer Ring' and 'Power Series Ring in t1 over Fraction Field of Multivariate Polynomial Ring in a1, a2, a3, a4, a6 over Integer Ring'
```



---

Comment by wuthrich created at 2010-11-14 16:36:48

There was indeed a precision error in the code and the patch that I attach should fix that. This is quite a bad bug as ALL the computations with formal groups happen to be wrong...


---

Attachment

exported against 4.6


---

Comment by wuthrich created at 2010-11-14 16:38:05

Changing status from new to needs_review.


---

Comment by wuthrich created at 2010-11-14 16:53:59

... and now to the other thing. As I played around with this, I found that I get different results than the [Errata](http://www.math.brown.edu/~jhs/AEC/AECErrata.pdf) of [Silverman](http://books.google.co.uk/books?id=Z90CA_EUCCkC&lpg=PR1&ots=3K8lmtWd1a&dq=silverman%20arithmetic%20of%20elliptic%20curves&pg=PA120#v=onepage&q&f=false). So I had to dig a little deeper and I found that the formula in Silverman are not correct.

Here is an example. Let E be the elliptic curve `y^2 + y = x^3+1` Because `a1=a2=0`, the formula in the middle of page 120 of Silverman tells us that

`F(t,t) = [2](t) = 2*t + t^4 + ... `

But I claim that it should be `2*t -7*t^4`. Here is an example. 


```
sage: K = Qp(43,5)
sage: E = EllipticCurve(K,[0,0,1,0,1])
sage: Q = E(-779/43^2,-125945/43^3)
sage: tQ =-Q[0]/Q[1]
sage: tQ
24*43 + 4*43^2 + 32*43^3 + 41*43^4 + 34*43^5 + O(43^6)
```


so the point lies in the formal group. We use the multiplication law on the curve and find

```
sage: ttwoQ = -(2*Q)[0]/(2*Q)[1]
sage: ttwoQ
5*43 + 9*43^2 + 21*43^3 + 38*43^4 + 37*43^5 + O(43^6)
```



```
sage: sage: 2*tQ +tQ^4
5*43 + 9*43^2 + 21*43^3 + 28*43^4 + 37*43^5 + O(43^6)
sage: sage: 2*tQ -7*tQ^4
5*43 + 9*43^2 + 21*43^3 + 38*43^4 + 37*43^5 + O(43^6)
```


shows that -7 is correct. I have added a docstring in `mult_by_n` to illustrate that our formula is correct, because this function is computed without using `group_law` if the base ring is a field of char 0 (instead it uses the multiplication on the curve). 

In fact, the error appears as a sign error in the formula for `z_3`. The corrected formula should read

`F(z_1,z_2) = z_1+z_2 -a_1 z_1z_2 -a_2(z_1^2 z_2+z_1 z_2^2) - 2a_3 z_1^3 z_2 +(a_1 a_2-3 a_3) z_1^2 z_2^2 - 2a_3 z_1 z_2^3 + ...`


---

Comment by cremona created at 2010-11-14 17:03:08

I suggest that you write to Silverman, since he likes to keep his errata up to date!  And add something in the docstring here to explain why you use a formula different from that in Silverman.


---

Comment by wuthrich created at 2010-11-14 17:13:34

Yes, I was typing my email as you wrote that :-). and yes, it is a good idea to add a comment in the code.


---

Comment by wuthrich created at 2010-11-14 17:14:03

to be applied after the first patch


---

Attachment


---

Comment by davidloeffler created at 2010-12-16 12:07:21

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-01-23 20:32:58

Is there a reason the milestone is sage-5.0?


---

Comment by wuthrich created at 2011-01-23 21:22:52

No, this can go in asap.


---

Comment by jdemeyer created at 2011-01-26 22:26:41

Resolution: fixed
