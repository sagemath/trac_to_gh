# Issue 816: [with patch] Commutative Algebra assorted functionality

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2007-10-04 00:38:17

Assignee: was

ideal quotients:


```
sage: R.<x,y,z> = PolynomialRing(GF(181),3)
sage: I = Ideal([x^2+x*y*z,y^2-z^3*y,z^3+y^5*x*z])
sage: J = Ideal([x])
sage: Q = I.quotient(J)
sage: y*z + x in I
False
sage: x in J
True
sage: x * (y*z + x) in I
True
```


changing rings for ideals:


```
sage: P.<x,y,z> = PolynomialRing(QQ,3,order='lex')
sage: I = sage.rings.ideal.Cyclic(P)
sage: I
Ideal (x + y + z, x*y + x*z + y*z, x*y*z - 1) of Polynomial Ring in x, y, z over Rational Field
sage: I.groebner_basis()
[z^3 - 1, y^2 + y*z + z^2, x + y + z]
sage: Q.<x,y,z> = P.new_ring(order='degrevlex'); Q
Polynomial Ring in x, y, z over Rational Field
sage: Q.term_order()
Degree reverse lexicographic term order

sage: J = I.change_ring(Q)
Ideal (x + y + z, x*y + x*z + y*z, x*y*z - 1) of Polynomial Ring in x, y, z over Rational Field
sage: J.groebner_basis()
[x + y + z, y^2 + y*z + z^2, z^3 - 1]
```


constructing new rings


```
sage: P.<x,y,z> = PolynomialRing(GF(127),3,order='lex')
sage: x > y^2
True
sage: Q.<x,y,z> = P.new_ring(order='degrevlex')
sage: x > y^2
False
```




---

Attachment


---

Comment by malb created at 2007-10-04 00:44:05

Changing assignee from was to malb.


---

Comment by malb created at 2007-10-04 00:44:05

Changing component from algebraic geometry to commutative algebra.


---

Comment by malb created at 2007-10-04 00:44:05

Changing status from new to assigned.


---

Comment by was created at 2007-10-04 17:14:07

Resolution: fixed
