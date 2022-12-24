# Issue 1857: examples of parametric surfaces in 3d

archive/issues_001857.json:
```json
{
    "body": "Assignee: @williamstein\n\nHi:\nAll these need:\n\n```\nsage: u = var(\"u\")\nsage: v = var(\"v\")\n```\n\nSome interesting surfaces can be found here:\nhttp://virtualmathmuseum.org/galleryS.html\n- David Joyner\n\n\n```\n#Hyperhelicoidal\nsage: fx = (sinh(v)*cos(3*u))/(1+cosh(u)*cosh(v))\nsage: fy = (sinh(v)*sin(3*u))/(1+cosh(u)*cosh(v))\nsage: fz = (cosh(v)*sinh(u))/(1+cosh(u)*cosh(v))\nsage: parametric_plot3d([fx, fy, fz], (u, -pi, pi), (v, -pi, pi),\nplot_points = [50,50], frame=False, color=\"red\")\n\n\n#Helicoid (lines through a helix)\n#http://en.wikipedia.org/wiki/Helix\nsage: fx = sinh(v)*sin(u)\nsage: fy = -sinh(v)*cos(u)\nsage: fz = 3*u\nsage: parametric_plot3d([fx, fy, fz], (u, -pi, pi), (v, -pi, pi),\nplot_points = [50,50], frame=False, color=\"red\")\n\n\n#Kuen's surface\n#http://www.math.umd.edu/research/bianchi/Gifccsurfs/ccsurfs.html\nsage: fx = (2*(cos(u) + u*sin(u))*sin(v))/(1+ u^2*sin(v)^2)\nsage: fy = (2*(sin(u) - u*cos(u))*sin(v))/(1+ u^2*sin(v)^2)\nsage: fz = log(tan(1/2 *v)) + (2*cos(v))/(1+ u^2*sin(v)^2)\nsage: parametric_plot3d([fx, fy, fz], (u, 0, 2*pi), (v, 0.01,\npi-0.01), plot_points = [50,50], frame=False, color=\"green\")\n\n\n#5-pointed star\nsage: fx = cos(u)*cos(v)*(abs(cos(1*u/4))^0.5 +\nabs(sin(1*u/4))^0.5)^(-1/0.3)*(abs(cos(5*v/4))^1.7 +\nabs(sin(5*v/4))^1.7)^(-1/0.1)\nsage: fy = cos(u)*sin(v)*(abs(cos(1*u/4))^0.5 +\nabs(sin(1*u/4))^0.5)^(-1/0.3)*(abs(cos(5*v/4))^1.7 +\nabs(sin(5*v/4))^1.7)^(-1/0.1)\nsage: fz = sin(u)*(abs(cos(1*u/4))^0.5 + abs(sin(1*u/4))^0.5)^(-1/0.3)\nsage: parametric_plot3d([fx, fy, fz], (u, -pi/2, pi/2), (v, 0, 2*pi),\nplot_points = [50,50], frame=False, color=\"green\")\n\n#a cool self-intersecting surface (Eppener surface?)\nsage: fx = u - u^3/3 + u*v^2\nsage: fy = v - v^3/3 + v*u^2\nsage: fz = u^2 - v^2\nsage: parametric_plot3d([fx, fy, fz], (u, -25, 25), (v, -25, 25),\nplot_points = [50,50], frame=False, color=\"green\")\n\n#breather surface\n#http://en.wikipedia.org/wiki/Breather_surface\nsage: fx = (2*sqrt(0.84)*cosh(0.4*u)*(-(sqrt(0.84)*cos(v)*cos(sqrt(0.84)*v))\n- sin(v)*sin(sqrt(0.84)*v)))/(0.4*((sqrt(0.84)*cosh(0.4*u))^2 +\n(0.4*sin(sqrt(0.84)*v))^2))\nsage: fy = (2*sqrt(0.84)*cosh(0.4*u)*(-(sqrt(0.84)*sin(v)*cos(sqrt(0.84)*v))\n+ cos(v)*sin(sqrt(0.84)*v)))/(0.4*((sqrt(0.84)*cosh(0.4*u))^2 +\n(0.4*sin(sqrt(0.84)*v))^2))\nsage: fz = -u +\n(2*0.84*cosh(0.4*u)*sinh(0.4*u))/(0.4*((sqrt(0.84)*cosh(0.4*u))^2 +\n(0.4*sin(sqrt(0.84)*v))^2))\nsage: parametric_plot3d([fx, fy, fz], (u, -13.2, 13.2), (v, -37.4,\n37.4), plot_points = [90,90], frame=False, color=\"green\")\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1857\n\n",
    "created_at": "2008-01-20T00:15:14Z",
    "labels": [
        "graphics",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "examples of parametric surfaces in 3d",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1857",
    "user": "@wdjoyner"
}
```
Assignee: @williamstein

Hi:
All these need:

```
sage: u = var("u")
sage: v = var("v")
```

Some interesting surfaces can be found here:
http://virtualmathmuseum.org/galleryS.html
- David Joyner


```
#Hyperhelicoidal
sage: fx = (sinh(v)*cos(3*u))/(1+cosh(u)*cosh(v))
sage: fy = (sinh(v)*sin(3*u))/(1+cosh(u)*cosh(v))
sage: fz = (cosh(v)*sinh(u))/(1+cosh(u)*cosh(v))
sage: parametric_plot3d([fx, fy, fz], (u, -pi, pi), (v, -pi, pi),
plot_points = [50,50], frame=False, color="red")


#Helicoid (lines through a helix)
#http://en.wikipedia.org/wiki/Helix
sage: fx = sinh(v)*sin(u)
sage: fy = -sinh(v)*cos(u)
sage: fz = 3*u
sage: parametric_plot3d([fx, fy, fz], (u, -pi, pi), (v, -pi, pi),
plot_points = [50,50], frame=False, color="red")


#Kuen's surface
#http://www.math.umd.edu/research/bianchi/Gifccsurfs/ccsurfs.html
sage: fx = (2*(cos(u) + u*sin(u))*sin(v))/(1+ u^2*sin(v)^2)
sage: fy = (2*(sin(u) - u*cos(u))*sin(v))/(1+ u^2*sin(v)^2)
sage: fz = log(tan(1/2 *v)) + (2*cos(v))/(1+ u^2*sin(v)^2)
sage: parametric_plot3d([fx, fy, fz], (u, 0, 2*pi), (v, 0.01,
pi-0.01), plot_points = [50,50], frame=False, color="green")


#5-pointed star
sage: fx = cos(u)*cos(v)*(abs(cos(1*u/4))^0.5 +
abs(sin(1*u/4))^0.5)^(-1/0.3)*(abs(cos(5*v/4))^1.7 +
abs(sin(5*v/4))^1.7)^(-1/0.1)
sage: fy = cos(u)*sin(v)*(abs(cos(1*u/4))^0.5 +
abs(sin(1*u/4))^0.5)^(-1/0.3)*(abs(cos(5*v/4))^1.7 +
abs(sin(5*v/4))^1.7)^(-1/0.1)
sage: fz = sin(u)*(abs(cos(1*u/4))^0.5 + abs(sin(1*u/4))^0.5)^(-1/0.3)
sage: parametric_plot3d([fx, fy, fz], (u, -pi/2, pi/2), (v, 0, 2*pi),
plot_points = [50,50], frame=False, color="green")

#a cool self-intersecting surface (Eppener surface?)
sage: fx = u - u^3/3 + u*v^2
sage: fy = v - v^3/3 + v*u^2
sage: fz = u^2 - v^2
sage: parametric_plot3d([fx, fy, fz], (u, -25, 25), (v, -25, 25),
plot_points = [50,50], frame=False, color="green")

#breather surface
#http://en.wikipedia.org/wiki/Breather_surface
sage: fx = (2*sqrt(0.84)*cosh(0.4*u)*(-(sqrt(0.84)*cos(v)*cos(sqrt(0.84)*v))
- sin(v)*sin(sqrt(0.84)*v)))/(0.4*((sqrt(0.84)*cosh(0.4*u))^2 +
(0.4*sin(sqrt(0.84)*v))^2))
sage: fy = (2*sqrt(0.84)*cosh(0.4*u)*(-(sqrt(0.84)*sin(v)*cos(sqrt(0.84)*v))
+ cos(v)*sin(sqrt(0.84)*v)))/(0.4*((sqrt(0.84)*cosh(0.4*u))^2 +
(0.4*sin(sqrt(0.84)*v))^2))
sage: fz = -u +
(2*0.84*cosh(0.4*u)*sinh(0.4*u))/(0.4*((sqrt(0.84)*cosh(0.4*u))^2 +
(0.4*sin(sqrt(0.84)*v))^2))
sage: parametric_plot3d([fx, fy, fz], (u, -13.2, 13.2), (v, -37.4,
37.4), plot_points = [90,90], frame=False, color="green")
```


Issue created by migration from https://trac.sagemath.org/ticket/1857





---

archive/issue_comments_011748.json:
```json
{
    "body": "Did anybody turns this into a patch yet? Did it get merged in some of the other patches that added plotting examples?\n\nCheers,\n\nMichael",
    "created_at": "2008-02-18T14:00:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1857",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1857#issuecomment-11748",
    "user": "mabshoff"
}
```

Did anybody turns this into a patch yet? Did it get merged in some of the other patches that added plotting examples?

Cheers,

Michael



---

archive/issue_comments_011749.json:
```json
{
    "body": "Attached is a patch.",
    "created_at": "2008-02-18T19:10:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1857",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1857#issuecomment-11749",
    "user": "@wdjoyner"
}
```

Attached is a patch.



---

archive/issue_comments_011750.json:
```json
{
    "body": "Attachment [param-plot_18-02-2008.hg](tarball://root/attachments/some-uuid/ticket1857/param-plot_18-02-2008.hg) by mabshoff created at 2008-02-18 19:19:48\n\nPatch looks good to me.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-18T19:19:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1857",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1857#issuecomment-11750",
    "user": "mabshoff"
}
```

Attachment [param-plot_18-02-2008.hg](tarball://root/attachments/some-uuid/ticket1857/param-plot_18-02-2008.hg) by mabshoff created at 2008-02-18 19:19:48

Patch looks good to me.

Cheers,

Michael



---

archive/issue_comments_011751.json:
```json
{
    "body": "Merged in Sage 2.10.2.alpha1",
    "created_at": "2008-02-18T19:21:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1857",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1857#issuecomment-11751",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.2.alpha1



---

archive/issue_comments_011752.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-18T19:21:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1857",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1857#issuecomment-11752",
    "user": "mabshoff"
}
```

Resolution: fixed
