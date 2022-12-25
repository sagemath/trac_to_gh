# Issue 9495: Incomplete plot of EllipticCurve

archive/issues_009495.json:
```json
{
    "body": "Assignee: jason, was\n\nPlotting \n\n```\nE2 = EllipticCurve([0,0,0,-7,0])\nplot(E2)\n```\n\nshows the entire EC, but\n\n```\nE = EllipticCurve([-6,6])\nplot(E)\n```\n\ndoes not, although there are points with positive x:\n\n```\nE = EllipticCurve([-6,6])\nprint '\\n'.join([ '%s'%E.lift_x(xp)for xp in srange(-2,5,0.5)])\n```\n\n\nThis is possibly related to [#5124](http://trac.sagemath.org/sage_trac/ticket/5124) because e.g. plot(E, (-3,3)) is ignored and hence impossible to plot the entire picture of E.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9495\n\n",
    "created_at": "2010-07-14T09:57:39Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "Incomplete plot of EllipticCurve",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9495",
    "user": "https://github.com/haraldschilly"
}
```
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

Issue created by migration from https://trac.sagemath.org/ticket/9495


