# Issue 9391: kolyvagin_cohomology_class() method differs from doc

Issue created by migration from https://trac.sagemath.org/ticket/9391

Original creator: justin

Original creation time: 2010-06-30 05:27:57

Assignee: cremona

Keywords: kolyvagin classes

If P is a 'kolyvagin_point' created from an elliptic curve, the doc string says

```
Definition:	P.kolyvagin_cohomology_class(self, n=None)
Docstring:
       INPUT:
    
          * n -- positive integer that divides the gcd of a_p and p+1 for
            all p dividing the conductor.  If n is None, choose the
            largest valid n.
```

In fact, if "n" is None, a ValueError is thrown.


---

Comment by chapoton created at 2014-03-06 16:00:45

The problem happens when the conductor is 1.

```
sage: y = EllipticCurve('389a').heegner_point(-7,1)
sage: y.conductor()
1
sage: P=y.kolyvagin_cohomology_class()
BOOM
```

This is because the gcd of the empty list is 0. I do not know what to do to solve the issue.
