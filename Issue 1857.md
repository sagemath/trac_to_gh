# Issue 1857: examples of parametric surfaces in 3d

Issue created by migration from https://trac.sagemath.org/ticket/1857

Original creator: wdj

Original creation time: 2008-01-20 00:15:14

Assignee: was

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



---

Comment by mabshoff created at 2008-02-18 14:00:35

Did anybody turns this into a patch yet? Did it get merged in some of the other patches that added plotting examples?

Cheers,

Michael


---

Comment by wdj created at 2008-02-18 19:10:40

Attached is a patch.


---

Attachment

Patch looks good to me.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-18 19:21:30

Merged in Sage 2.10.2.alpha1


---

Comment by mabshoff created at 2008-02-18 19:21:30

Resolution: fixed
