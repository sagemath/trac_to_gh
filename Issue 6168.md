# Issue 6168: FLINT wrapper not reducing coefficients properly

Issue created by migration from https://trac.sagemath.org/ticket/6168

Original creator: dmharvey

Original creation time: 2009-05-31 05:40:26

Assignee: tbd

It is possible to create FLINT `zmod_poly` objects whose coefficients are not reduced mod n (where n is the modulus). This is difficult to show directly in Sage, but here is an example symptom:


```
sage: R.<x> = PolynomialRing(Integers(15))
sage: S.<y> = PolynomialRing(Integers(5))
sage: f = S(5*x)
sage: f
0
sage: f == 0
False
sage: f.degree()
1
```


Internally the coefficient 5 is not reduced, but it prints as reduced.

This bug is probably the main cause of #5817.



---

Comment by dmharvey created at 2009-05-31 05:42:36

See also

http://groups.google.com/group/sage-devel/browse_thread/thread/3d1e310b021c1620


---

Comment by was created at 2009-05-31 20:51:33

Changing component from algebra to basic arithmetic.


---

Attachment


---

Comment by was created at 2009-05-31 20:51:33

Changing assignee from tbd to somebody.


---

Comment by was created at 2009-05-31 20:51:33

Changing priority from major to critical.


---

Comment by kedlaya created at 2009-06-02 01:28:09

The patch applies against 4.0, and fixes the bug:

```
sage: R.<x> = PolynomialRing(Integers(15))
sage: S.<y> = PolynomialRing(Integers(5))
sage: f = S(5*x)
sage: f
0
sage: f == 0
True
sage: f.degree()
-1
```

Moreover, with this patch in, the spkg at #5817 passes all doctests. Positive review.


---

Comment by mhansen created at 2009-06-03 18:26:22

Merged in 4.0.1.rc0.


---

Comment by mhansen created at 2009-06-03 18:26:22

Resolution: fixed
