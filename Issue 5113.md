# Issue 5113: [with patch, needs review] elliptic curve construction from weierstrass equation

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2009-01-27 22:21:12

Assignee: was

CC:  rlm

It would be nice to be able to do 

```
        sage: x, y = var('x,y')
        sage: EllipticCurve(y^2 + y ==  x^3 + x - 9)
        Elliptic Curve defined by y^2 + y = x^3 + x - 9 over Rational Field
        
        sage: R.<x,y> = GF(5)[]
        sage: EllipticCurve(x^3 + x^2 + 2 - y^2 - y*x)
        Elliptic Curve defined by y^2 + x*y  = x^3 + x^2 + 2 over Finite Field of size 5
```



---

Attachment

I'm curious why you don't just do

```
a1 = -1*f.coefficient(x*y)
a2 = f.coefficient(x**2)
```

instead of iterating through `f`. I'm sure it doesn't matter.

The patch looks good though, positive review.

I've also fixed printing of elliptic curves, see #5118.


---

Comment by robertwb created at 2009-01-28 23:00:14

I tried that first. The problem is f.coefficient(x) returns everything divisible by one power of x, not the x (alone) term


```
sage: R.<x,y> = QQ[]
sage: f = x^2 + x*y + y^2*x
sage: f.coef
f.coefficient   f.coefficients  
sage: f.coefficient(x)
y^2 + y
sage: f.coefficient(y^2)
x
```


It is also harder to exclude bad terms using that method.


---

Comment by mabshoff created at 2009-01-29 00:27:38

Resolution: fixed


---

Comment by mabshoff created at 2009-01-29 00:27:38

Merged in Sage 3.3.alpha3.

Cheers,

Michael
