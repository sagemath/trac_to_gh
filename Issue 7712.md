# Issue 7712: error in polynomial substitution with interval coefficients

Issue created by migration from https://trac.sagemath.org/ticket/7712

Original creator: zimmerma

Original creation time: 2009-12-16 13:01:54

Assignee: AlexGhitza

CC:  kohel

Consider the following example:

```
sage: P.<y,z> = PolynomialRing(RealIntervalField(2))
sage: Q.<x> = PolynomialRing(P)
sage: C = (y-x)^3
sage: C(y/2)
0
```

I do not understand why the result is 0. In fact there are two
errors:
(i) the result is a polynomial of degree 3 in y, thus y**3 should appear
(ii) the result should "contain" the exact result which is 0.125*y**3, thus it should be c*y**3 where c is an interval containing
0.125. Compare the following with a precision of 10 bits:

```
sage: P.<y,z> = PolynomialRing(RealIntervalField(10))
sage: Q.<x> = PolynomialRing(P)
sage: C = (y-x)^3
sage: C(y/2)
0.12500?*y^3
```



---

Comment by ylchapuy created at 2009-12-16 14:09:01

It seems it just a printing issue:

```
sage: r = C(y/2)
sage: r
0
sage: r.monomials()
[y^3]
sage: r.monomial_coefficient(y^3).str(style='brackets')
'[-0.00 .. 0.25]'
```



---

Comment by zimmerma created at 2009-12-16 14:18:36

Indeed:

```
sage: R=RealIntervalField(2)
sage: r=R(-0.00,0.25)
sage: r.str(style='brackets')
'[-0.00 .. 0.25]'
sage: r
1.?
sage: r*x
0
```

I thus changed the summary.


---

Comment by zimmerma created at 2009-12-17 09:22:10

Here is a more complex example, which shows this is not only a printing issue:

```
def method2(prec):
   n=[0,9,7,8,11,6,3,7,6,6,4,3,4,1,2,2,1,1,1,2,0,0,0,3,0,0,0,0,1]
   R = RealIntervalField(prec)
   P.<xk1,sk1,sk2> = PolynomialRing(R)
   Q.<xk> = PolynomialRing(P)
   C = (sk1-xk)^n[1]*xk^n[2]
   C=C.integral()
   C=C(sk1/2)-C(xk1)
   C=R(10^6)*C.subs(sk1=sk2-xk1)
   C=C.subs(xk1=xk,sk2=sk1)
   for k in range(3,29):
      C=C*xk^n[k]
      C=C.integral()
      C=C(sk1/k)-C(xk1)
      C=R(10^6)*C.subs(sk1=sk2-xk1)
      C=C.subs(xk1=xk,sk2=sk1)
   C=C.subs(xk=R(0),sk1=R(1))
   return C(0,0,0)

sage: method2(391)
0
sage: _.parent() 
Integer Ring

sage: method2(392)
1.?e-8
sage: _.parent()
Real Interval Field with 392 bits of precision
```

Normally, both calls should return an object of type "Real Interval Field", isn't it?
(If necessary, I can open a different trac ticket for both issues.)


---

Comment by was created at 2009-12-24 07:08:08

I'm declaring a total feature freeze on sage-4.3.


---

Comment by zimmerma created at 2010-02-05 20:22:08

Still there in 4.3.1.


---

Comment by ylchapuy created at 2010-03-12 08:33:04

Replying to [comment:3 zimmerma]:
>    C=C.subs(xk=R(0),sk1=R(1))

The two polynomials obtained here are constants.
The strange behaviour about the type comes from line 153 of

`sage/rings/polynomial/multi_polynomial_element.py`

where we find:


```
        try:
            K = x[0].parent()     <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        except AttributeError:
            K = self.parent().base_ring()
        y = K(0) 
        for (m,c) in self.element().dict().iteritems():  
            y += c*misc.mul([ x[i]**m[i] for i in range(n) if m[i] != 0])
```


I don't know exactly why, but It first try to take the type of the first input (here Integer 0) and this type is then changed only by coercion when doing the computation.

With precision 391 the polynomial is null and no operations are performed, so the results stays Integer.

I would say this is a bug but maybe there is a purpose behind this.


---

Comment by zimmerma created at 2010-03-12 08:53:19

Yann, are you sure this method __call__ is called? I've added a print statement before
`y=K(0)` and nothing is printed (in 4.3.3). I add David in cc, maybe he can help us.


---

Comment by ylchapuy created at 2010-03-12 09:15:52

Sorry, my last comment was not clear. The method call is called when you do `return C(0,0,0)`.


---

Comment by zimmerma created at 2010-03-12 09:22:26

> Sorry, my last comment was not clear. The method call is called when you do return C(0,0,0). 

with `C(0,0,0)` I see no problem:

```
sage: P.<y,z> = PolynomialRing(RealIntervalField(2))
sage: Q.<x> = PolynomialRing(P)
sage: C = (y-x)^3
sage: a=C(0,0,0)
sage: type(a)
<type 'sage.rings.real_mpfi.RealIntervalFieldElement'>
sage: a.lower()
0.00
sage: a.upper()
0.00
```



---

Comment by ylchapuy created at 2010-03-12 09:34:11

Here is my point:

```
sage: def method2(prec):
....:        n=[0,9,7,8,11,6,3,7,6,6,4,3,4,1,2,2,1,1,1,2,0,0,0,3,0,0,0,0,1]
....:    R = RealIntervalField(prec)
....:    P.<xk1,sk1,sk2> = PolynomialRing(R)
....:    Q.<xk> = PolynomialRing(P)
....:    C = (sk1-xk)^n[1]*xk^n[2]
....:    C=C.integral()
....:    C=C(sk1/2)-C(xk1)
....:    C=R(10^6)*C.subs(sk1=sk2-xk1)
....:    C=C.subs(xk1=xk,sk2=sk1)
....:    for k in range(3,29):
....:           C=C*xk^n[k]
....:       C=C.integral()
....:       C=C(sk1/k)-C(xk1)
....:       C=R(10^6)*C.subs(sk1=sk2-xk1)
....:       C=C.subs(xk1=xk,sk2=sk1)
....:    C=C.subs(xk=R(0),sk1=R(1))
....:    return C
....: 
sage: C391 = method2(391)
sage: C391
0
sage: type(C391)
<class 'sage.rings.polynomial.multi_polynomial_element.MPolynomial_polydict'>
sage: type(C391(0,0,0))
<type 'sage.rings.integer.Integer'>
sage: type(C391(GF(17)['z'](0),0,0))
<type 'sage.rings.polynomial.polynomial_zmod_flint.Polynomial_zmod_flint'>
```



---

Comment by zimmerma created at 2010-03-12 15:15:02

> Here is my point: [...]

ok, I thought you were speaking about the first (smaller) examples. I can reduce this second
problem to the following:

```
sage: R.<x,y> = PolynomialRing(RR)
sage: f=R(1); type(f(0,0))
<type 'sage.rings.real_mpfr.RealNumber'>
sage: f=R(0); type(f(0,0))
<type 'sage.rings.integer.Integer'>
```

David, please can you explain why it is so?


---

Comment by gmoroz created at 2012-12-06 10:35:35

I didn't see this ticket when submitting the new ticket #13760. There I provide a patch that corrects this bug. The two tickets should be merged (and probably closed after review of the patch).


---

Attachment

Tests should work after applying trac 13760 patch


---

Comment by gmoroz created at 2012-12-14 09:50:44

Changing status from new to needs_review.


---

Comment by zimmerma created at 2012-12-14 17:16:27

I propose to mark this as "duplicate", since #13760 solves that issue.

Paul


---

Comment by tscrim created at 2012-12-15 16:37:32

Hey Paul and Guillaume,

For future reference, just mark the patch as duplicate in the milestone dropdown and set it to _needs_review_.

#13760 does seem to fix the problem:

```
sage: method2(391)
0.?e-8
sage: _.parent()
Real Interval Field with 391 bits of precision
```


Best,

Travis


---

Comment by tscrim created at 2012-12-15 16:37:32

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-12-21 22:49:33

Resolution: duplicate
