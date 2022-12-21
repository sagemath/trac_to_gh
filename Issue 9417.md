# Issue 9417: Tamagawa number calculated incorrectly

Issue created by migration from Trac.

Original creator: arminstraub

Original creation time: 2010-07-03 03:41:37

Assignee: cremona

CC:  was justin

Keywords: tamagawa_number local_data

In 4.4.4 the following Tamagawa number gets evaluated as 2:


```
sage: K.<a> = NumberField(x^2+18*x+1)
sage: E = EllipticCurve(K, [0, -36, 0, 320, 0])
sage: E.tamagawa_number(K.ideal(2))
2
```


According to Magma this should be 4.


---

Comment by cremona created at 2011-03-26 22:50:02

As the author of both Sage's and Magma's code for Tamagawa numbers, I have been tracking this one down. It turns out to be due to a bug in how elements of the rings of integers are mapped into residue fields:

```
sage: K.<a> = NumberField(x^2+18*x+1)
sage: P = K.ideal(2)
sage: F = K.residue_field(P)
sage: R = PolynomialRing(F, 'x')
sage: R([0, a, a, 1])
x^3 + abar*x^2 + abar*x
sage: F(a)
1
sage: a.minpoly()
x^2 + 18*x + 1
sage: F.gen()
abar
sage: F.gen().minpoly()
x^2 + x + 1
```

The polynomial `x<sup>3+a*x</sup>2+a*x` reduced modulo P=(2) wrongly to `x<sup>3+abar*x</sup>2+abar*x`. Although the generator of the residue field F is suggestively called abar, it it *not* the reduction of a mod P (which is 1 mod P).

I will open a new ticket for that, and try to fix it. This ticket can probably then be closed, so watch this space.


---

Comment by cremona created at 2011-03-26 22:52:30

See #11055


---

Attachment

Applies to 4.7.alpha2


---

Comment by cremona created at 2011-03-27 19:15:35

Changing status from new to needs_review.


---

Comment by cremona created at 2011-03-27 19:15:35

The patch applies the simple workaround described at #11055.  Now we correctly get

```
sage: K.<a> = NumberField(x^2+18*x+1)
sage: E = EllipticCurve(K, [0, -36, 0, 320, 0])
sage: E.tamagawa_number(K.ideal(2))
4
```

and a doctest has been added.


---

Comment by rlm created at 2011-04-17 21:34:31

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2011-04-17 21:34:31

Looks good to me!


---

Comment by jdemeyer created at 2011-04-20 12:51:16

Resolution: fixed
