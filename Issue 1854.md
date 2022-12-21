# Issue 1854: add more 3d plots to the reference manual

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-01-19 22:13:53

Assignee: was

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



---

Comment by was created at 2008-01-19 22:14:09

Changing component from algebraic geometry to graphics.


---

Comment by was created at 2008-01-19 22:24:10

Changing status from new to assigned.


---

Attachment

The only functional change is that the default plot_points is now [40,40] instead of [15,15].  It's clear when doing a lot of plots that [15,15] is not enough -- it was just copied from Mathematica and was probably a good convention back in the stone age (1990s).


---

Attachment


---

Comment by mhansen created at 2008-01-21 03:43:20

The original patch didn't apply for me due to previous patches, so I put up 1854.patch which applies and passes tests.


---

Comment by mhansen created at 2008-01-21 03:44:54

1831 and 1833 should be applied before this.


---

Comment by mabshoff created at 2008-01-21 04:16:22

Resolution: fixed


---

Comment by mabshoff created at 2008-01-21 04:16:22

Merged in Sage 2.10.1.alpha1
