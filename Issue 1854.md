# Issue 1854: add more 3d plots to the reference manual

archive/issues_001854.json:
```json
{
    "body": "Assignee: @williamstein\n\nTest every one of these carefully; fix any problems with rendering them, then put them in the appropriate place in the plot3d/ docstrings:\n\n```\nHi:\nHere are a few more surfaces, most from a source file\nParisoMathObject.cpp sent by Jurgis Pralgauskis but some from\nwikipedia. More later ...\n- David Joyner\n\n#\"Sinus\" (water ripple-like surface)\nsage: x = var(\"x\")\nsage: y = var(\"y\")\nsage: plot3d(sin(pi*((x)^2+(y)^2))/2,(x,-1,1),(y,-1,1))\n\n\n#hill and valley (flat surface with a bump and a dent)\nsage: x = var(\"x\")\nsage: y = var(\"y\")\nsage: plot3d( 4*x*exp(-x^2-y^2), (x,-2,2), (y,-2,2))\n\n\n#cylindrical Star of David\nsage: u = var(\"u\")\nsage: v = var(\"v\")\nsage: f_x = cos(u)*cos(v)*(abs(cos(3*v/4))^500 +\nabs(sin(3*v/4))^500)^(-1/260)*(abs(cos(4*u/4))^200 +\nabs(sin(4*u/4))^200)^(-1/200)\nsage: f_y = cos(u)*sin(v)*(abs(cos(3*v/4))^500 +\nabs(sin(3*v/4))^500)^(-1/260)*(abs(cos(4*u/4))^200 +\nabs(sin(4*u/4))^200)^(-1/200)\nsage: f_z = sin(u)*(abs(cos(4*u/4))^200 + abs(sin(4*u/4))^200)^(-1/200)\nsage: parametric_plot3d([f_x, f_y, f_z], (u, -pi, pi), (v, 0, 2*pi),\nplot_points = [50,50])\n\n#double heart\nsage: f_x = ( abs(v) - abs(u) - abs(tanh((1/sqrt(2))*u)/(1/sqrt(2))) +\nabs(tanh((1/sqrt(2))*v)/(1/sqrt(2))) )*sin(v)\nsage: f_y = ( abs(v) - abs(u) - abs(tanh((1/sqrt(2))*u)/(1/sqrt(2))) -\nabs(tanh((1/sqrt(2))*v)/(1/sqrt(2))) )*cos(v)\nsage: f_z = sin(u)*(abs(cos(4*u/4))^1 + abs(sin(4*u/4))^1)^(-1/1)\nsage: parametric_plot3d([f_x, f_y, f_z], (u, 0, pi), (v, -pi, pi),\nplot_points = [50,50])\n\n#heart\nsage: f_x = cos(u)*(4*sqrt(1-v^2)*sin(abs(u))^abs(u))\nsage: f_y = sin(u) *(4*sqrt(1-v^2)*sin(abs(u))^abs(u))\nsage: f_z = v\nsage: parametric_plot3d([f_x, f_y, f_z], (u, -pi, pi), (v, -1, 1),\nplot_points = [50,50], frame=False, color=\"red\")\n\n#green bowtie\nsage: f_x = sin(u) / (sqrt(2) + sin(v))\nsage: f_y = sin(u) / (sqrt(2) + cos(v))\nsage: f_z = cos(u) / (1 + sqrt(2))\nsage: parametric_plot3d([f_x, f_y, f_z], (u, -pi, pi), (v, -pi, pi),\nplot_points = [50,50], frame=False, color=\"green\")\n\n\n#Boy's surface\n#http://en.wikipedia.org/wiki/Boy's_surface\nsage: fx = 2/3* (cos(u)* cos(2*v) + sqrt(2)* sin(u)* cos(v))* cos(u) /\n(sqrt(2) - sin(2*u)* sin(3*v))\nsage: fy = 2/3* (cos(u)* sin(2*v) - sqrt(2)* sin(u)* sin(v))* cos(u) /\n(sqrt(2) - sin(2*u)* sin(3*v))\nsage: fz = sqrt(2)* cos(u)* cos(u) / (sqrt(2) - sin(2*u)* sin(3*v))\nsage: parametric_plot3d([fx, fy, fz], (u, -2*pi, 2*pi), (v, 0, pi),\nplot_points = [90,90], frame=False, color=\"orange\")\n\n\n#Maeder's_Owl (pretty but can't find an internet reference)\nsage: fx = v *cos(u) - 0.5* v^2 * cos(2* u)\nsage: fy = -v *sin(u) - 0.5* v^2 * sin(2* u)\nsage: fz = 4 *v^1.5 * cos(3 *u / 2) / 3\nsage: parametric_plot3d([fx, fy, fz], (u, -2*pi, 2*pi), (v, 0, 1),\nplot_points = [90,90], frame=False, color=\"purple\")\n\n#bracelet\nsage: fx = (2 + 0.2*sin(2*pi*u))*sin(pi*v)\nsage: fy = 0.2*cos(2*pi*u) *3*cos(2*pi*v)\nsage: fz = (2 + 0.2*sin(2*pi*u))*cos(pi*v)\nsage: parametric_plot3d([fx, fy, fz], (u, 0, pi/2), (v, 0, 3*pi/4),\nplot_points = [50,50], frame=False, color=\"gray\")\n\n#green goblet\nsage: fx = cos(u)*cos(2*v)\nsage: fy = sin(u)*cos(2*v)\nsage: fz = sin(v)\nsage: parametric_plot3d([fx, fy, fz], (u, 0, 2*pi), (v, 0, pi),\nplot_points = [50,50], frame=False, color=\"green\")\n\n#funny folded surface - with square projection\nsage: fx = cos(u)*sin(2*v)\nsage: fy = sin(u)*cos(2*v)\nsage: fz = sin(v)\nsage: parametric_plot3d([fx, fy, fz], (u, 0, 2*pi), (v, 0, 2*pi),\nplot_points = [50,50], frame=False, color=\"green\")\n\n#surface of revolution of figure 8\nsage: fx = cos(u)*sin(2*v)\nsage: fy = sin(u)*sin(2*v)\nsage: fz = sin(v)\nsage: parametric_plot3d([fx, fy, fz], (u, 0, 2*pi), (v, 0, 2*pi),\nplot_points = [50,50], frame=False, color=\"green\")\n\n#yellow Whitney's umbrella\n#http://en.wikipedia.org/wiki/Whitney_umbrella\nsage: fx = u*v\nsage: fy = u\nsage: fz = v^2\nsage: parametric_plot3d([fx, fy, fz], (u, -1, 1), (v, -1, 1),\nplot_points = [50,50], frame=False, color=\"yellow\")\n\n#cross cap\n#http://en.wikipedia.org/wiki/Cross-cap\nsage: fx = (1+cos(v))*cos(u)\nsage: fy = (1+cos(v))*sin(u)\nsage: fz = -tanh((2/3)*(u-pi))*sin(v)\nsage: parametric_plot3d([fx, fy, fz], (u, 0, 2*pi), (v, 0, 2*pi),\nplot_points = [50,50], frame=False, color=\"red\")\n\n#twisted torus\nsage: fx = (3+sin(v)+cos(u))*cos(2*v)\nsage: fy = (3+sin(v)+cos(u))*sin(2*v)\nsage: fz = sin(u)+2*cos(v)\nsage: parametric_plot3d([fx, fy, fz], (u, 0, 2*pi), (v, 0, 2*pi),\nplot_points = [50,50], frame=False, color=\"red\")\n\n#four intersecting discs\nsage: sage: fx = v *cos(u) -0.5*v^2*cos(2*u)\nsage: sage: fy = -v*sin(u) -0.5*v^2*sin(2*u)\nsage: sage: fz = 4* v^1.5 *cos(3* u / 2) / 3\nsage: sage: parametric_plot3d([fx, fy, fz], (u, 0, 4*pi), (v, 0,\n2*pi), plot_points = [50,50], frame=False, color=\"red\")\n\n#Steiner surface/Roman's surface\nhttp://en.wikipedia.org/wiki/Roman_surface\nhttp://en.wikipedia.org/wiki/Steiner_surface\nsage: fx = (sin(2 * u) * cos(v) * cos(v))\nsage: fy = (sin(u) * sin(2 * v))\nsage: fz = (cos(u) * sin(2 * v))\nsage: parametric_plot3d([fx, fy, fz], (u, -pi/2, pi/2), (v, -pi/2,\npi/2), plot_points = [50,50], frame=False, color=\"red\")\n\n#Klein bottle?\n#http://en.wikipedia.org/wiki/Klein_bottle\nsage: fx = (3*(1+sin(v)) + 2*(1-cos(v)/2)*cos(u))*cos(v)\nsage: fy = (4+2*(1-cos(v)/2)*cos(u))*sin(v)\nsage: fz = -2*(1-cos(v)/2) * sin(u)\nsage: parametric_plot3d([fx, fy, fz], (u, 0, 2*pi), (v, 0, 2*pi),\nplot_points = [50,50], frame=False, color=\"red\")\n\n#\"figure 8 embedding\" of Klein bottle\n#http://en.wikipedia.org/wiki/Klein_bottle\nsage: fx = (2 + cos(v/2)* sin(u) - sin(v/2)* sin(2 *u))* cos(v)\nsage: fy = (2 + cos(v/2)* sin(u) - sin(v/2)* sin(2 *u))* sin(v)\nsage: fz = sin(v/2)* sin(u) + cos(v/2) *sin(2* u)\nsage: parametric_plot3d([fx, fy, fz], (u, 0, 2*pi), (v, 0, 2*pi),\nplot_points = [50,50], frame=False, color=\"red\")\n\n#Enneper's surface\n#http://en.wikipedia.org/wiki/Enneper_surface\nsage: fx = u -u^3/3  + u*v^2\nsage: fy = v -v^3/3  + v*u^2\nsage: fz = u^2 - v^2\nsage: parametric_plot3d([fx, fy, fz], (u, -2, 2), (v, -2, 2),\nplot_points = [50,50], frame=False, color=\"red\")\n\n#Henneberg's surface\n#http://xahlee.org/surface/gallery_m.html\nsage: fx = 2*sinh(u)*cos(v) -(2/3)*sinh(3*u)*cos(3*v)\nsage: fy = 2*sinh(u)*sin(v) +(2/3)*sinh(3*u)*sin(3*v)\nsage: fz = 2*cosh(2*u)*cos(2*v)\nsage: parametric_plot3d([fx, fy, fz], (u, -1, 1), (v, -pi/2, pi/2),\nplot_points = [50,50], frame=False, color=\"red\")\n\n#Dini's spiral\nsage: fx = cos(u)*sin(v)\nsage: fy = sin(u)*sin(v)\nsage: fz = (cos(v)+log(tan(v/2))) + 0.2*u\nsage: parametric_plot3d([fx, fy, fz], (u, 0, 12.4), (v, 0.1, 2),\nplot_points = [50,50], frame=False, color=\"red\")\n\n#Catalan's surface\n#http://xahlee.org/surface/catalan/catalan.html\nsage: fx = u-sin(u)*cosh(v)\nsage: fy = 1-cos(u)*cosh(v)\nsage: fz = 4*sin(1/2*u)*sinh(v/2)\nsage: parametric_plot3d([fx, fy, fz], (u, -pi, 3*pi), (v, -2, 2),\nplot_points = [50,50], frame=False, color=\"red\")\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1854\n\n",
    "created_at": "2008-01-19T22:13:53Z",
    "labels": [
        "component: algebraic geometry",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "add more 3d plots to the reference manual",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1854",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

Test every one of these carefully; fix any problems with rendering them, then put them in the appropriate place in the plot3d/ docstrings:

```
Hi:
Here are a few more surfaces, most from a source file
ParisoMathObject.cpp sent by Jurgis Pralgauskis but some from
wikipedia. More later ...
- David Joyner

#"Sinus" (water ripple-like surface)
sage: x = var("x")
sage: y = var("y")
sage: plot3d(sin(pi*((x)^2+(y)^2))/2,(x,-1,1),(y,-1,1))


#hill and valley (flat surface with a bump and a dent)
sage: x = var("x")
sage: y = var("y")
sage: plot3d( 4*x*exp(-x^2-y^2), (x,-2,2), (y,-2,2))


#cylindrical Star of David
sage: u = var("u")
sage: v = var("v")
sage: f_x = cos(u)*cos(v)*(abs(cos(3*v/4))^500 +
abs(sin(3*v/4))^500)^(-1/260)*(abs(cos(4*u/4))^200 +
abs(sin(4*u/4))^200)^(-1/200)
sage: f_y = cos(u)*sin(v)*(abs(cos(3*v/4))^500 +
abs(sin(3*v/4))^500)^(-1/260)*(abs(cos(4*u/4))^200 +
abs(sin(4*u/4))^200)^(-1/200)
sage: f_z = sin(u)*(abs(cos(4*u/4))^200 + abs(sin(4*u/4))^200)^(-1/200)
sage: parametric_plot3d([f_x, f_y, f_z], (u, -pi, pi), (v, 0, 2*pi),
plot_points = [50,50])

#double heart
sage: f_x = ( abs(v) - abs(u) - abs(tanh((1/sqrt(2))*u)/(1/sqrt(2))) +
abs(tanh((1/sqrt(2))*v)/(1/sqrt(2))) )*sin(v)
sage: f_y = ( abs(v) - abs(u) - abs(tanh((1/sqrt(2))*u)/(1/sqrt(2))) -
abs(tanh((1/sqrt(2))*v)/(1/sqrt(2))) )*cos(v)
sage: f_z = sin(u)*(abs(cos(4*u/4))^1 + abs(sin(4*u/4))^1)^(-1/1)
sage: parametric_plot3d([f_x, f_y, f_z], (u, 0, pi), (v, -pi, pi),
plot_points = [50,50])

#heart
sage: f_x = cos(u)*(4*sqrt(1-v^2)*sin(abs(u))^abs(u))
sage: f_y = sin(u) *(4*sqrt(1-v^2)*sin(abs(u))^abs(u))
sage: f_z = v
sage: parametric_plot3d([f_x, f_y, f_z], (u, -pi, pi), (v, -1, 1),
plot_points = [50,50], frame=False, color="red")

#green bowtie
sage: f_x = sin(u) / (sqrt(2) + sin(v))
sage: f_y = sin(u) / (sqrt(2) + cos(v))
sage: f_z = cos(u) / (1 + sqrt(2))
sage: parametric_plot3d([f_x, f_y, f_z], (u, -pi, pi), (v, -pi, pi),
plot_points = [50,50], frame=False, color="green")


#Boy's surface
#http://en.wikipedia.org/wiki/Boy's_surface
sage: fx = 2/3* (cos(u)* cos(2*v) + sqrt(2)* sin(u)* cos(v))* cos(u) /
(sqrt(2) - sin(2*u)* sin(3*v))
sage: fy = 2/3* (cos(u)* sin(2*v) - sqrt(2)* sin(u)* sin(v))* cos(u) /
(sqrt(2) - sin(2*u)* sin(3*v))
sage: fz = sqrt(2)* cos(u)* cos(u) / (sqrt(2) - sin(2*u)* sin(3*v))
sage: parametric_plot3d([fx, fy, fz], (u, -2*pi, 2*pi), (v, 0, pi),
plot_points = [90,90], frame=False, color="orange")


#Maeder's_Owl (pretty but can't find an internet reference)
sage: fx = v *cos(u) - 0.5* v^2 * cos(2* u)
sage: fy = -v *sin(u) - 0.5* v^2 * sin(2* u)
sage: fz = 4 *v^1.5 * cos(3 *u / 2) / 3
sage: parametric_plot3d([fx, fy, fz], (u, -2*pi, 2*pi), (v, 0, 1),
plot_points = [90,90], frame=False, color="purple")

#bracelet
sage: fx = (2 + 0.2*sin(2*pi*u))*sin(pi*v)
sage: fy = 0.2*cos(2*pi*u) *3*cos(2*pi*v)
sage: fz = (2 + 0.2*sin(2*pi*u))*cos(pi*v)
sage: parametric_plot3d([fx, fy, fz], (u, 0, pi/2), (v, 0, 3*pi/4),
plot_points = [50,50], frame=False, color="gray")

#green goblet
sage: fx = cos(u)*cos(2*v)
sage: fy = sin(u)*cos(2*v)
sage: fz = sin(v)
sage: parametric_plot3d([fx, fy, fz], (u, 0, 2*pi), (v, 0, pi),
plot_points = [50,50], frame=False, color="green")

#funny folded surface - with square projection
sage: fx = cos(u)*sin(2*v)
sage: fy = sin(u)*cos(2*v)
sage: fz = sin(v)
sage: parametric_plot3d([fx, fy, fz], (u, 0, 2*pi), (v, 0, 2*pi),
plot_points = [50,50], frame=False, color="green")

#surface of revolution of figure 8
sage: fx = cos(u)*sin(2*v)
sage: fy = sin(u)*sin(2*v)
sage: fz = sin(v)
sage: parametric_plot3d([fx, fy, fz], (u, 0, 2*pi), (v, 0, 2*pi),
plot_points = [50,50], frame=False, color="green")

#yellow Whitney's umbrella
#http://en.wikipedia.org/wiki/Whitney_umbrella
sage: fx = u*v
sage: fy = u
sage: fz = v^2
sage: parametric_plot3d([fx, fy, fz], (u, -1, 1), (v, -1, 1),
plot_points = [50,50], frame=False, color="yellow")

#cross cap
#http://en.wikipedia.org/wiki/Cross-cap
sage: fx = (1+cos(v))*cos(u)
sage: fy = (1+cos(v))*sin(u)
sage: fz = -tanh((2/3)*(u-pi))*sin(v)
sage: parametric_plot3d([fx, fy, fz], (u, 0, 2*pi), (v, 0, 2*pi),
plot_points = [50,50], frame=False, color="red")

#twisted torus
sage: fx = (3+sin(v)+cos(u))*cos(2*v)
sage: fy = (3+sin(v)+cos(u))*sin(2*v)
sage: fz = sin(u)+2*cos(v)
sage: parametric_plot3d([fx, fy, fz], (u, 0, 2*pi), (v, 0, 2*pi),
plot_points = [50,50], frame=False, color="red")

#four intersecting discs
sage: sage: fx = v *cos(u) -0.5*v^2*cos(2*u)
sage: sage: fy = -v*sin(u) -0.5*v^2*sin(2*u)
sage: sage: fz = 4* v^1.5 *cos(3* u / 2) / 3
sage: sage: parametric_plot3d([fx, fy, fz], (u, 0, 4*pi), (v, 0,
2*pi), plot_points = [50,50], frame=False, color="red")

#Steiner surface/Roman's surface
http://en.wikipedia.org/wiki/Roman_surface
http://en.wikipedia.org/wiki/Steiner_surface
sage: fx = (sin(2 * u) * cos(v) * cos(v))
sage: fy = (sin(u) * sin(2 * v))
sage: fz = (cos(u) * sin(2 * v))
sage: parametric_plot3d([fx, fy, fz], (u, -pi/2, pi/2), (v, -pi/2,
pi/2), plot_points = [50,50], frame=False, color="red")

#Klein bottle?
#http://en.wikipedia.org/wiki/Klein_bottle
sage: fx = (3*(1+sin(v)) + 2*(1-cos(v)/2)*cos(u))*cos(v)
sage: fy = (4+2*(1-cos(v)/2)*cos(u))*sin(v)
sage: fz = -2*(1-cos(v)/2) * sin(u)
sage: parametric_plot3d([fx, fy, fz], (u, 0, 2*pi), (v, 0, 2*pi),
plot_points = [50,50], frame=False, color="red")

#"figure 8 embedding" of Klein bottle
#http://en.wikipedia.org/wiki/Klein_bottle
sage: fx = (2 + cos(v/2)* sin(u) - sin(v/2)* sin(2 *u))* cos(v)
sage: fy = (2 + cos(v/2)* sin(u) - sin(v/2)* sin(2 *u))* sin(v)
sage: fz = sin(v/2)* sin(u) + cos(v/2) *sin(2* u)
sage: parametric_plot3d([fx, fy, fz], (u, 0, 2*pi), (v, 0, 2*pi),
plot_points = [50,50], frame=False, color="red")

#Enneper's surface
#http://en.wikipedia.org/wiki/Enneper_surface
sage: fx = u -u^3/3  + u*v^2
sage: fy = v -v^3/3  + v*u^2
sage: fz = u^2 - v^2
sage: parametric_plot3d([fx, fy, fz], (u, -2, 2), (v, -2, 2),
plot_points = [50,50], frame=False, color="red")

#Henneberg's surface
#http://xahlee.org/surface/gallery_m.html
sage: fx = 2*sinh(u)*cos(v) -(2/3)*sinh(3*u)*cos(3*v)
sage: fy = 2*sinh(u)*sin(v) +(2/3)*sinh(3*u)*sin(3*v)
sage: fz = 2*cosh(2*u)*cos(2*v)
sage: parametric_plot3d([fx, fy, fz], (u, -1, 1), (v, -pi/2, pi/2),
plot_points = [50,50], frame=False, color="red")

#Dini's spiral
sage: fx = cos(u)*sin(v)
sage: fy = sin(u)*sin(v)
sage: fz = (cos(v)+log(tan(v/2))) + 0.2*u
sage: parametric_plot3d([fx, fy, fz], (u, 0, 12.4), (v, 0.1, 2),
plot_points = [50,50], frame=False, color="red")

#Catalan's surface
#http://xahlee.org/surface/catalan/catalan.html
sage: fx = u-sin(u)*cosh(v)
sage: fy = 1-cos(u)*cosh(v)
sage: fz = 4*sin(1/2*u)*sinh(v/2)
sage: parametric_plot3d([fx, fy, fz], (u, -pi, 3*pi), (v, -2, 2),
plot_points = [50,50], frame=False, color="red")
```


Issue created by migration from https://trac.sagemath.org/ticket/1854





---

archive/issue_comments_011702.json:
```json
{
    "body": "Changing component from algebraic geometry to graphics.",
    "created_at": "2008-01-19T22:14:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1854#issuecomment-11702",
    "user": "https://github.com/williamstein"
}
```

Changing component from algebraic geometry to graphics.



---

archive/issue_comments_011703.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-19T22:24:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1854#issuecomment-11703",
    "user": "https://github.com/williamstein"
}
```

Changing status from new to assigned.



---

archive/issue_comments_011704.json:
```json
{
    "body": "Attachment [trac-1854.patch](tarball://root/attachments/some-uuid/ticket1854/trac-1854.patch) by @williamstein created at 2008-01-19 23:10:52\n\nThe only functional change is that the default plot_points is now [40,40] instead of [15,15].  It's clear when doing a lot of plots that [15,15] is not enough -- it was just copied from Mathematica and was probably a good convention back in the stone age (1990s).",
    "created_at": "2008-01-19T23:10:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1854#issuecomment-11704",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac-1854.patch](tarball://root/attachments/some-uuid/ticket1854/trac-1854.patch) by @williamstein created at 2008-01-19 23:10:52

The only functional change is that the default plot_points is now [40,40] instead of [15,15].  It's clear when doing a lot of plots that [15,15] is not enough -- it was just copied from Mathematica and was probably a good convention back in the stone age (1990s).



---

archive/issue_comments_011705.json:
```json
{
    "body": "Attachment [1854.patch](tarball://root/attachments/some-uuid/ticket1854/1854.patch) by @mwhansen created at 2008-01-21 03:41:37",
    "created_at": "2008-01-21T03:41:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1854#issuecomment-11705",
    "user": "https://github.com/mwhansen"
}
```

Attachment [1854.patch](tarball://root/attachments/some-uuid/ticket1854/1854.patch) by @mwhansen created at 2008-01-21 03:41:37



---

archive/issue_comments_011706.json:
```json
{
    "body": "The original patch didn't apply for me due to previous patches, so I put up 1854.patch which applies and passes tests.",
    "created_at": "2008-01-21T03:43:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1854#issuecomment-11706",
    "user": "https://github.com/mwhansen"
}
```

The original patch didn't apply for me due to previous patches, so I put up 1854.patch which applies and passes tests.



---

archive/issue_comments_011707.json:
```json
{
    "body": "1831 and 1833 should be applied before this.",
    "created_at": "2008-01-21T03:44:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1854#issuecomment-11707",
    "user": "https://github.com/mwhansen"
}
```

1831 and 1833 should be applied before this.



---

archive/issue_events_002012.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-01-21T04:16:22Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1854",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1854#event-2012"
}
```



---

archive/issue_comments_011708.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-21T04:16:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1854#issuecomment-11708",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_011709.json:
```json
{
    "body": "Merged in Sage 2.10.1.alpha1",
    "created_at": "2008-01-21T04:16:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1854#issuecomment-11709",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.1.alpha1
