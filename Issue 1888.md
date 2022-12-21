# Issue 1888: 3d graphics -- cool plots of space curves (examples for docstrings)

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-01-23 01:49:19

Assignee: was

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



---

Comment by was created at 2008-01-23 01:53:15

Remark: using the thickness=10 parameter makes some of these look much nicer.


---

Comment by mabshoff created at 2008-03-16 08:42:39

Mmh, maybe this has been merged already.

Cheers,

Michael


---

Comment by wdj created at 2008-03-16 10:56:25

I not so sure about that. The surfaces are at
http://www.sagemath.org/doc/html/ref/module-sage.plot.plot3d.parametric-plot3d.html
but if you go to the bottom of that page, you see 


```

parametric_plot3d_curve(  	f, urange, plot_points)

    This function is used internally by the parametric_plot3d command. 
```

with no examples.


---

Comment by was created at 2008-03-16 11:07:28

Hi,

Type


```
sage: parametric_plot3d?
```


If you don't see the examples above (I don't), then this isn't in Sage yet.


---

Comment by mabshoff created at 2008-10-10 19:03:26

Is this code still not in Sage? It should be trivial to add those curves to the plot3d.py docstring somewhere.

Cheers,

Michael


---

Comment by AlexGhitza created at 2009-01-22 18:27:20

Changing type from defect to enhancement.


---

Comment by mhansen created at 2009-10-19 18:25:57

There are already a ton of examples (almost annoyingly many) in the docstring for parametric_plot3d.  I don't think that adding the few listed here is helpful at this point.

If someone really wants to add them, then they can repoen this ticket.


---

Comment by mhansen created at 2009-10-19 18:25:57

Resolution: invalid
