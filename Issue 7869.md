# Issue 7869: cylindrical plot

Issue created by migration from https://trac.sagemath.org/ticket/7869

Original creator: olazo

Original creation time: 2010-01-07 19:11:51

Assignee: was

Keywords: cylindric,plot

I've made a clone of Mathematicas SphericalPlot3d . Only that the 3d seemed redundant to me.

The code is

```
def cylindrical_plot(f,phiran,zran,**kwds):
   phi=phiran[0]
   z=zran[0]
   Rho=(f*cos(phi),f*sin(phi),z)
   return parametric_plot3d(Rho,phiran,zran,**kwds) 
```


Several examples can be found in [http://www.sagenb.org/home/pub/1325/](http://www.sagenb.org/home/pub/1325/)

For simplicity's sake I have not added default values for the ploting domain, that tends to produce undesired results.


---

Comment by olazo created at 2010-01-07 19:13:21

Changing assignee from was to olazo.


---

Comment by olazo created at 2010-01-08 17:55:22

Changing status from new to needs_work.


---

Attachment

a proposal for a docstring


---

Comment by olazo created at 2010-01-17 21:23:38

some corrections made


---

Attachment


---

Comment by olazo created at 2010-01-24 19:36:29

Resolution: invalid
