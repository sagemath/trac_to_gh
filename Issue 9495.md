# Issue 9495: Incomplete plot of EllipticCurve

Issue created by migration from https://trac.sagemath.org/ticket/9495

Original creator: schilly

Original creation time: 2010-07-14 09:57:39

Assignee: jason, was

Plotting 

```
E2 = EllipticCurve([0,0,0,-7,0])
plot(E2)
```

shows the entire EC, but

```
E = EllipticCurve([-6,6])
plot(E)
```

does not, although there are points with positive x:

```
E = EllipticCurve([-6,6])
print '\n'.join([ '%s'%E.lift_x(xp)for xp in srange(-2,5,0.5)])
```


This is possibly related to [#5124](http://trac.sagemath.org/sage_trac/ticket/5124) because e.g. plot(E, (-3,3)) is ignored and hence impossible to plot the entire picture of E.
