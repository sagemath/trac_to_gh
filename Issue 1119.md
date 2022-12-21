# Issue 1119: EllipticCurve.random_element for char=2

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2007-11-07 15:46:20

Assignee: was

This should work:

```
sage: k.<a> = GF(2^5)
sage: E = EllipticCurve(k,[k.random_element() for _ in range(5)])
sage: E
Elliptic Curve defined by y^2 + (a^3+1)*x*y + (a^4+a^3+a)*y = x^3 +
(a^4+a^3+a^2+a)*x^2 + (a^4+a^2+a+1)*x + a^2 over Finite Field in a of
size 2^5
sage: E.random_element()
Exception (click to the left for traceback):
...
ZeroDivisionError: division by zero in finite field.
```



---

Comment by malb created at 2007-11-08 16:59:35

Changing assignee from was to malb.


---

Comment by malb created at 2007-11-08 16:59:35

Changing status from new to assigned.


---

Comment by malb created at 2007-11-08 16:59:35

The attached patch fixes this (probably in a too naive way).


---

Attachment


---

Attachment

Given E defined by f(x,y) = 0, the patch assumed that there were always exactly zero or two values of y for every x, which is not true. I've attached a patch fixing this issue. 

Also, in the characteristic > 2 case, it never considered the 'negative' square-root. I changed this too. 

Otherwise, the patch looks good.


---

Comment by was created at 2007-12-15 05:40:46

#1119 looks good.  It is slow but I don't know if that can be helped.


---

Comment by mabshoff created at 2007-12-15 05:50:13

Merged in 2.9.rc0.


---

Comment by mabshoff created at 2007-12-15 05:50:13

Resolution: fixed
