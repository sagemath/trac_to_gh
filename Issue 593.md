# Issue 593: MPolynomialIdeal.reduced_basis() doesn't behave as expected

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2007-09-05 16:25:38

Assignee: was

It is an important result in commutative algebra that reduced Gröbner bases are unique representations of ideals. Thus, one would believe that if two systems compute a Gröbner basis for the same initial basis which is reduced afterwards these reduced Gröbner bases are equal, however:


```
k.<a> = GF(2^4)
```



```
P.<k100,k101,k102,k103,x100,x101,x102,x103,w100,w101,w102,w103,s000,s001,s002,s003,k000,k001,k002,k003> = PolynomialRing(k,20)
```



```
F = [ w100 + k000 + (a^3 + 1), \
w101 + k001 + (a^3 + a^2 + 1), \
w102 + k002 + (a^3 + a^2 + a), \
w103 + k003 + (a^3 + a + 1), \
k000^2 + k001, \
k001^2 + k002, \
k002^2 + k003, \
k000 + k003^2, \
k100 + (a^2 + 1)*x100 + x101 + (a^3 + a^2)*x102 + (a^2 + 1)*x103 + (a^3 + a), \
k101 + (a)*x100 + (a)*x101 + x102 + (a^3 + a^2 + a + 1)*x103 + (a^3), \
k102 + (a^3 + a)*x100 + (a^2)*x101 + (a^2)*x102 + x103 + (a^3 + a^2), \
k103 + x100 + (a^3)*x101 + (a + 1)*x102 + (a + 1)*x103 + (a^3 + a^2 + a + 1), \
x100*w100 + 1, \
x101*w101 + 1, \
x102*w102 + 1, \
x103*w103 + 1, \
x100^2 + x101, \
x101^2 + x102, \
x102^2 + x103, \
x100 + x103^2, \
w100^2 + w101, \
w101^2 + w102, \
w102^2 + w103, \
w100 + w103^2, \
k100 + (a^2 + 1)*s000 + s001 + (a^3 + a^2)*s002 + (a^2 + 1)*s003 + (a^2 + a + 1), \
k101 + (a)*s000 + (a)*s001 + s002 + (a^3 + a^2 + a + 1)*s003 + (a^2 + a), \
k102 + (a^3 + a)*s000 + (a^2)*s001 + (a^2)*s002 + s003 + (a^2 + a + 1), \
k103 + s000 + (a^3)*s001 + (a + 1)*s002 + (a + 1)*s003 + (a^2 + a), \
k100^2 + k101, \
k101^2 + k102, \
k102^2 + k103, \
k100 + k103^2, \
s000^2 + s001, \
s001^2 + s002, \
s002^2 + s003, \
s000 + s003^2, \
s000*k000 + 1, \
s001*k001 + 1, \
s002*k002 + 1, \
s003*k003 + 1 ]
```



```
gb1 = sorted(Ideal(Ideal(F).groebner_basis('magma:GroebnerBasis')).reduced_basis())
print Ideal(gb1).basis_is_groebner()
///
True
```



```
gb2 = sorted(Ideal(Ideal(F).groebner_basis('singular:std')).reduced_basis())
print Ideal(gb1).basis_is_groebner()
///
True
```



```
set(gb1) == set(gb2)
///
False
```




---

Attachment

The attached patch fixes this issue.


---

Comment by malb created at 2007-10-04 03:02:11

Changing assignee from was to malb.


---

Comment by malb created at 2007-10-04 03:02:11

Changing component from algebraic geometry to commutative algebra.


---

Comment by malb created at 2007-10-04 03:02:11

Changing status from new to assigned.


---

Comment by was created at 2007-10-04 17:07:02

Resolution: fixed
