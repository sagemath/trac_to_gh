# Issue 5065: elliptic curve torsion subgroup doesn't know it's identity

Issue created by migration from https://trac.sagemath.org/ticket/5065

Original creator: boothby

Original creation time: 2009-01-23 08:29:47

Assignee: was

The torsion subgroup of an elliptic curve appears to be quite broken -- it barfs when trying to coerce in 0,


```
sage: E = EllipticCurve(1)
sage: T = E.torsion_subgroup()
sage: T(0)
...
...
TypeError: Argument x (= 0) is of wrong type.
```


further, it returns a mysterious 1 when coercing in a 1


```
sage: a = T(1); a
1
sage: b = T.gens()[0]-T.gens()[0]; b
(0 : 1 : 0)
sage: a+b
TypeError: unsupported operand parent(s) for '+': 'Abelian group of points on Elliptic Curve defined by y^2 + x*y + y = x^3 - 19*x + 26 over Rational Field' and 'Torsion Subgroup isomorphic to Multiplicative Abelian Group isomorphic to C6 x C2 associated to the Elliptic Curve defined by y^2 + x*y + y = x^3 - 19*x + 26 over Rational Field'
```


Yet, it's all cool with the original curve.

```
sage: E(0)
(0 : 1 : 0)
sage: E(1)
...
...
TypeError: v (=(1,)) must have 3 components
sage: 
```





---

Comment by cremona created at 2009-05-07 16:21:15

Here is the reason.  the torsion subgroup class is derived from the Abelian group class, which in Sage is always a multiplicative group!  So it can coerce in 1 to give the identity 1, but not 0.

I produced a lovely patch adding proper additive support to the AbelianGroup class months ago, motivated mainly by situations such as this, but nobody else was interested and it never got in.  (To be fair, the patch is on trac labelled "not for review" for some reason).

Of course, for this specific group we could easily write a call() function to handle this, but the whole point of my Abeliangroup patch was that if you say that a group is additive on creation then that was all automatic.  Sigh.

I see that this was reported 3 months ago.  Sorry, I never saw it until now!


---

Comment by davidloeffler created at 2009-07-20 20:23:37

Changing assignee from was to davidloeffler.


---

Comment by davidloeffler created at 2009-07-20 20:23:37

Changing component from number theory to elliptic curves.


---

Comment by davidloeffler created at 2009-10-09 09:12:37

Remove assignee davidloeffler.


---

Comment by cremona created at 2010-08-14 16:47:11

In 4.5.3.alpha3 this works fine:

```
sage: E = EllipticCurve(j=1)
sage: T = E.torsion_subgroup()
sage: T(0)
(0 : 1 : 0)
```

thanks to the new Abelian Groups support.  So this ticket can be closed as fixed.


---

Comment by cremona created at 2010-08-14 16:47:11

Resolution: fixed


---

Comment by mpatel created at 2010-08-14 21:01:56

I'm setting the resolution to "duplicate" and changing the milestone accordingly.


---

Comment by mpatel created at 2010-08-14 21:01:56

Resolution changed from fixed to duplicate
