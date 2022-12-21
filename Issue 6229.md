# Issue 6229: efficiency in Lagrange polynomial interpolation (easy fix...)

Issue created by migration from Trac.

Original creator: ylchapuy

Original creation time: 2009-06-05 22:15:54

Assignee: tbd

CC:  mvngu

This is a follow-up to #6043.

This nested loop is useless:
{{
        P = 0 
        for i in xrange(n): 
            prod = 1 
            for j in xrange(i): 
                prod *= (x - points[j][0]) 
            P += (F[i] * prod) 
        return P

}}

and should be replaced with (something like)

{{
        P = F[n-1]
        for i in xrange(n-2,-1,-1): 
            P *= (x - points[i][0])
            P += F[i]
        return P
}}


---

Comment by ylchapuy created at 2009-06-05 22:18:05

I have no clean install yet to produce the patch myself...


---

Comment by mvngu created at 2009-06-05 23:42:16

You mean like evaluating it in nested form, similar to Horner's method? Do'h, I missed that.


---

Comment by mvngu created at 2009-06-06 00:31:14

The patch contains the suggested fix by ylchapuy. It's ylchapuy's code, not mine, so authorship credit goes to ylchapuy. I'm just reviewing the code. Here are some timing statistics on sage.math:

```
# BEFORE

sage: R = PolynomialRing(QQ, 'x')
sage: %timeit R.lagrange_polynomial([(0,1),(2,2),(3,-2),(-4,9)])
1000 loops, best of 3: 830 µs per loop
sage: R.lagrange_polynomial([(0,1),(2,2),(3,-2),(-4,9)])
-23/84*x^3 - 11/84*x^2 + 13/7*x + 1
sage: R = PolynomialRing(GF(2**3,'a'), 'x')
sage: a = R.base_ring().gen()
sage: timeit("R.lagrange_polynomial([(a^2+a,a),(a,1),(a^2,a^2+a+1)])")
625 loops, best of 3: 112 µs per loop
sage: R.lagrange_polynomial([(a^2+a,a),(a,1),(a^2,a^2+a+1)])
a^2*x^2 + a^2*x + a^2


# AFTER

sage: R = PolynomialRing(QQ, 'x')
sage: %timeit R.lagrange_polynomial([(0,1),(2,2),(3,-2),(-4,9)])
1000 loops, best of 3: 416 µs per loop
sage: R.lagrange_polynomial([(0,1),(2,2),(3,-2),(-4,9)])
-23/84*x^3 - 11/84*x^2 + 13/7*x + 1
sage: R = PolynomialRing(GF(2**3,'a'), 'x')
sage: a = R.base_ring().gen()
sage: timeit("R.lagrange_polynomial([(a^2+a,a),(a,1),(a^2,a^2+a+1)])")
625 loops, best of 3: 86.2 µs per loop
sage: R.lagrange_polynomial([(a^2+a,a),(a,1),(a^2,a^2+a+1)])
a^2*x^2 + a^2*x + a^2
```

So efficiency gain of up to 50%. Positive review.


---

Attachment

based on Sage 4.0.1.rc2


---

Comment by ncalexan created at 2009-06-13 21:18:38

Resolution: fixed
