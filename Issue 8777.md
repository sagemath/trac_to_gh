# Issue 8777: unify the definitions and semantics for elliptic curve and abelian variety torsion subgroups

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-04-27 04:42:42

Assignee: was


```
Hi,

Maybe this is a frivolous comment, but I'd like to express my surprise at the use of "torsion_subgroup" to mean two very different things for an abelian variety and for an elliptic curve:

sage: E=EllipticCurve('11a')
sage: E.torsion_subgroup()
Torsion Subgroup isomorphic to Multiplicative Abelian Group isomorphic to C5 associated to the Elliptic Curve defined by y^2 + y = x^3 - x^2 - 10*x - 20 over Rational Field
sage: A=J0(11)
sage: A.torsion_subgroup()
Traceback (most recent call last):
...
TypeError: torsion_subgroup() takes exactly 2 arguments (1 given)
sage: A.torsion_subgroup(5)
Finite subgroup with invariants [5, 5] over QQ of Abelian variety J0(11) of dimension 1
sage: A.rational_torsion_subgroup()
Torsion subgroup of Abelian variety J0(11) of dimension 1
sage: A.rational_torsion_subgroup().order()
5
sage: A.rational_torsion_subgroup().abelian_group()
Traceback (most recent call last):
...
AttributeError: 'RationalTorsionSubgroup' object has no attribute 'abelian_group'

I'm surprised that "torsion_subgroup" for an elliptic curve over Q refers to *rational* torsion while for an abelian variety over Q it refers to *all* torsion.  Further, it's frustrating to me that the rational torsion subgroup of an abelian variety over Q has an order but not the structure of an abelian group.  I'm sure that there are good reasons for this, but this end user is kind of amazed.  Before the sage session above, I used to think that elliptic curves and abelian varieties of dimension 1 were the same thing!  Live and learn....

Best,
Ken Ribet
```



---

Comment by was created at 2010-04-27 04:47:43

Instead of trying to decide based on any sort of logic, I think the at this point the best thing to do is to
change the behavior/semantics of modular abelian varieties to match elliptic curves, since there are probably 100 times as many users (and client code) for elliptic curves as for abelian varieties.  

By the way, to get the invariants of the J0(11)'s rational torsion subgroup, do this:

```
sage: T = J0(11).rational_torsion_subgroup()
sage: T.invariants()
[5]
```

One reason that there is no T.abelian_group(), is that abelian groups didn't exist in Sage when I first implemented finite subgroups of abelian varieties.
