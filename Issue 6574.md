# Issue 6574: Type issue in is_quadratic_twist

Issue created by migration from Trac.

Original creator: wuthrich

Original creation time: 2009-07-20 23:03:04

Assignee: davidloeffler

CC:  cremona

Keywords: elliptic curve, quadratic twist


```
E = EllipticCurve('32a1')
D = E.is_quadratic_twist(E)
D, type(D)
```


yields


```
(1, <type 'sage.rings.rational.Rational'>)
```


but


```
D = E.is_quadratic_twist(E.quadratic_twist(5))
D, type(D)
```


gives back


```
(5, <type 'sage.rings.integer.Integer'>)
```


I think in the first case, we should also give back the integer 1. The cause of this is in ell_field.py. In the first case we exit is_quadratic_twist at line 353 with


```
return K.one_element()
```


In the second case we exit at the end after
line 394 has changed the type by 


```
if K is rings.QQ:
    D = D.squarefree_part()
```





---

Comment by cremona created at 2009-07-21 08:01:35

Well spotted.  But note that this is in ell_field and general fields will not have integers, so the consistent return type should be that of the field.  So I would rather change the second behaviour, which will mean that when K is QQ we coerce back to ZZ after taking the square-free part.

On second thoughts we already have special code for QQ (calling squarefree_part()) so we could make a special case here and return a square-free integer (in ZZ) in all cases for K=QQ, and otherwise return a field element.  Is that acceptable?


---

Attachment

I opted for your second suggestion. In case K is QQ it is ZZ(1) that is returned.


---

Comment by cremona created at 2009-07-21 21:45:26

Positive review.  The patch fixes the problem (according to the above discussion) with a doctest + documentation to explain this special case.


---

Comment by mvngu created at 2009-07-23 08:40:09

Resolution: fixed
