# Issue 1888: 3d graphics -- cool plots of space curves (examples for docstrings)

archive/issues_001888.json:
```json
{
    "body": "Assignee: @williamstein\n\nThese need to be nicely test, sped up, etc., then\nmade into docstrings:\n\n\n```\nHere are a few cool space curves.\nI'd like to make more from\nhttp://www.math.umd.edu/research/bianchi/Gifspacecurves/spcu.html\nand\nhttp://virtualmathmuseum.org/SpaceCurves/\nIf anyone knows of some parametric equations for them, I'd appreciate it.\n\n#trefoil knot\n#http://en.wikipedia.org/wiki/Trefoil_knot\nsage: fx = 0.01*(41*cos(t) - 18*sin(t) - 83*cos(2*t)-83*sin(2*t) -\n11*cos(3*t) + 27*sin(3*t))\nsage: fy = 0.01*(36*cos(t) + 27*sin(t) - 113*cos(2*t)+30*sin(2*t) +\n11*cos(3*t) - 27*sin(3*t))\nsage: fz = 0.01*(45*sin(t) - 30*cos(2*t) + 113*sin(2*t)-11*cos(3*t) +\n27*sin(3*t))\nsage: parametric_plot3d( (fx, fy, fz), (t, 0, 6*pi), plot_points =\n500, frame=False)\n\n\n#figure-eight knot\n#http://en.wikipedia.org/wiki/Figure-eight_knot_%28mathematics%29\nsage: fx = (2 + cos(2*t))*cos(3*t)\nsage: fy = (2 + cos(2*t))*sin(3*t)\nsage: fz = sin(4*t)\nsage: parametric_plot3d( (fx, fy, fz), (t, 0, 6*pi), plot_points =\n500, frame=False)\n\n\n#Cinquefoil Knot (a=2 is this one):\n#http://en.wikipedia.org/wiki/Skein_relation\n#http://virtualmathmuseum.org/SpaceCurves/index.html#Classic\nfx = cos(t)*(2 - cos(2a*t/(2*a + 1)))\nfy = sin(t)*(2 - cos(2*t/(2*a + 1)))\nfz = - sin(2*t/(2*a + 1))\nsage: parametric_plot3d( (fx, fy, fz), (t, 0, 20*pi), plot_points =\n500, frame=False)\n\n\n#3-leafed space curve\nsage: a = 1; b = 1; c = 1; d = 3; e = 2\nsage: fx = (a + b*cos(d*t))*cos(e*t)\nsage: fy = (a + b*cos(d*t))*sin(e*t)\nsage: fz = c*sin(d*t)\nsage: parametric_plot3d( (fx, fy, fz), (t, 0, 4*pi), plot_points =\n100, frame=False)\n\n\n#    The Viviani Curve\n#http://en.wikipedia.org/wiki/Viviani's_curve\nsage: a = 1\nsage: fx = a*2*sin(t/2)\nsage: fy = a*sin(t)\nsage: fz = a*(1 + cos(t))\nsage: parametric_plot3d( (fx, fy, fz), (t, 0, 4*pi), plot_points =\n100, frame=False)\n\n#loxodrome\n#http://en.wikipedia.org/wiki/Loxodrome\nsage: fx = sin(t)/sqrt(1+t^2)\nsage: fy = cos(t)/sqrt(1+t^2)\nsage: fz = t/sqrt(1+t^2)\nsage: parametric_plot3d( (fx, fy, fz), (t, -4*pi, 4*pi), plot_points =\n100, frame=False)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1888\n\n",
    "created_at": "2008-01-23T01:49:19Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "3d graphics -- cool plots of space curves (examples for docstrings)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1888",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

These need to be nicely test, sped up, etc., then
made into docstrings:


```
Here are a few cool space curves.
I'd like to make more from
http://www.math.umd.edu/research/bianchi/Gifspacecurves/spcu.html
and
http://virtualmathmuseum.org/SpaceCurves/
If anyone knows of some parametric equations for them, I'd appreciate it.

#trefoil knot
#http://en.wikipedia.org/wiki/Trefoil_knot
sage: fx = 0.01*(41*cos(t) - 18*sin(t) - 83*cos(2*t)-83*sin(2*t) -
11*cos(3*t) + 27*sin(3*t))
sage: fy = 0.01*(36*cos(t) + 27*sin(t) - 113*cos(2*t)+30*sin(2*t) +
11*cos(3*t) - 27*sin(3*t))
sage: fz = 0.01*(45*sin(t) - 30*cos(2*t) + 113*sin(2*t)-11*cos(3*t) +
27*sin(3*t))
sage: parametric_plot3d( (fx, fy, fz), (t, 0, 6*pi), plot_points =
500, frame=False)


#figure-eight knot
#http://en.wikipedia.org/wiki/Figure-eight_knot_%28mathematics%29
sage: fx = (2 + cos(2*t))*cos(3*t)
sage: fy = (2 + cos(2*t))*sin(3*t)
sage: fz = sin(4*t)
sage: parametric_plot3d( (fx, fy, fz), (t, 0, 6*pi), plot_points =
500, frame=False)


#Cinquefoil Knot (a=2 is this one):
#http://en.wikipedia.org/wiki/Skein_relation
#http://virtualmathmuseum.org/SpaceCurves/index.html#Classic
fx = cos(t)*(2 - cos(2a*t/(2*a + 1)))
fy = sin(t)*(2 - cos(2*t/(2*a + 1)))
fz = - sin(2*t/(2*a + 1))
sage: parametric_plot3d( (fx, fy, fz), (t, 0, 20*pi), plot_points =
500, frame=False)


#3-leafed space curve
sage: a = 1; b = 1; c = 1; d = 3; e = 2
sage: fx = (a + b*cos(d*t))*cos(e*t)
sage: fy = (a + b*cos(d*t))*sin(e*t)
sage: fz = c*sin(d*t)
sage: parametric_plot3d( (fx, fy, fz), (t, 0, 4*pi), plot_points =
100, frame=False)


#    The Viviani Curve
#http://en.wikipedia.org/wiki/Viviani's_curve
sage: a = 1
sage: fx = a*2*sin(t/2)
sage: fy = a*sin(t)
sage: fz = a*(1 + cos(t))
sage: parametric_plot3d( (fx, fy, fz), (t, 0, 4*pi), plot_points =
100, frame=False)

#loxodrome
#http://en.wikipedia.org/wiki/Loxodrome
sage: fx = sin(t)/sqrt(1+t^2)
sage: fy = cos(t)/sqrt(1+t^2)
sage: fz = t/sqrt(1+t^2)
sage: parametric_plot3d( (fx, fy, fz), (t, -4*pi, 4*pi), plot_points =
100, frame=False)
```


Issue created by migration from https://trac.sagemath.org/ticket/1888





---

archive/issue_comments_011928.json:
```json
{
    "body": "Remark: using the thickness=10 parameter makes some of these look much nicer.",
    "created_at": "2008-01-23T01:53:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1888",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1888#issuecomment-11928",
    "user": "https://github.com/williamstein"
}
```

Remark: using the thickness=10 parameter makes some of these look much nicer.



---

archive/issue_comments_011929.json:
```json
{
    "body": "Mmh, maybe this has been merged already.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-16T08:42:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1888",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1888#issuecomment-11929",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Mmh, maybe this has been merged already.

Cheers,

Michael



---

archive/issue_comments_011930.json:
```json
{
    "body": "I not so sure about that. The surfaces are at\nhttp://www.sagemath.org/doc/html/ref/module-sage.plot.plot3d.parametric-plot3d.html\nbut if you go to the bottom of that page, you see \n\n\n```\n\nparametric_plot3d_curve(  \tf, urange, plot_points)\n\n    This function is used internally by the parametric_plot3d command. \n```\n\nwith no examples.",
    "created_at": "2008-03-16T10:56:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1888",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1888#issuecomment-11930",
    "user": "https://github.com/wdjoyner"
}
```

I not so sure about that. The surfaces are at
http://www.sagemath.org/doc/html/ref/module-sage.plot.plot3d.parametric-plot3d.html
but if you go to the bottom of that page, you see 


```

parametric_plot3d_curve(  	f, urange, plot_points)

    This function is used internally by the parametric_plot3d command. 
```

with no examples.



---

archive/issue_comments_011931.json:
```json
{
    "body": "Hi,\n\nType\n\n\n```\nsage: parametric_plot3d?\n```\n\n\nIf you don't see the examples above (I don't), then this isn't in Sage yet.",
    "created_at": "2008-03-16T11:07:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1888",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1888#issuecomment-11931",
    "user": "https://github.com/williamstein"
}
```

Hi,

Type


```
sage: parametric_plot3d?
```


If you don't see the examples above (I don't), then this isn't in Sage yet.



---

archive/issue_comments_011932.json:
```json
{
    "body": "Is this code still not in Sage? It should be trivial to add those curves to the plot3d.py docstring somewhere.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-10T19:03:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1888",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1888#issuecomment-11932",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Is this code still not in Sage? It should be trivial to add those curves to the plot3d.py docstring somewhere.

Cheers,

Michael



---

archive/issue_comments_011933.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-22T18:27:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1888",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1888#issuecomment-11933",
    "user": "https://github.com/aghitza"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_011934.json:
```json
{
    "body": "There are already a ton of examples (almost annoyingly many) in the docstring for parametric_plot3d.  I don't think that adding the few listed here is helpful at this point.\n\nIf someone really wants to add them, then they can repoen this ticket.",
    "created_at": "2009-10-19T18:25:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1888",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1888#issuecomment-11934",
    "user": "https://github.com/mwhansen"
}
```

There are already a ton of examples (almost annoyingly many) in the docstring for parametric_plot3d.  I don't think that adding the few listed here is helpful at this point.

If someone really wants to add them, then they can repoen this ticket.



---

archive/issue_comments_011935.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2009-10-19T18:25:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1888",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1888#issuecomment-11935",
    "user": "https://github.com/mwhansen"
}
```

Resolution: invalid
