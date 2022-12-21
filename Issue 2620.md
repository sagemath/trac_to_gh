# Issue 2620: [with patch, needs review] generator generator support for ideal

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2008-03-20 22:15:35

Assignee: malb

Python has a generator type which is cool and now this works:


```
P.<a,b,c,d,e> = PolynomialRing(GF(2), 5, order='lex')
I1 = ideal([a*b + c*d + 1, a*c*e + d*e, a*b*e + c*e, b*c + c*d*e + 1])
Q = P.quotient( sage.rings.ideal.FieldIdeal(P) )
I2 = ideal( Q(f) for f in I1.gens() ) # note we don't construct a list
```



---

Attachment

Patch looks good to me. Doctests pass. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-01 14:30:59

Merged in Sage 3.0.alpha0


---

Comment by mabshoff created at 2008-04-01 14:30:59

Resolution: fixed
