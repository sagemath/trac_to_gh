# Issue 1511: Export 3d objects in jmol format

Issue created by migration from https://trac.sagemath.org/ticket/1511

Original creator: robertwb

Original creation time: 2007-12-14 19:58:09

Assignee: was

http://jmol.sourceforge.net/ may be a promising answer to 3d graphics in Sage. 


---

Comment by robertwb created at 2007-12-14 19:58:15

Changing status from new to assigned.


---

Comment by robertwb created at 2007-12-14 19:58:15

Changing assignee from was to robertwb.


---

Comment by robertwb created at 2007-12-15 00:36:23

Bundle also contains #1473


---

Comment by robertwb created at 2007-12-15 00:39:28


```
    sage: from sage.plot.plot3d.shapes import *
    sage: from sage.plot.plot3d.plot3d import plot3d
    sage: S = Sphere(.5, color='yellow')
    sage: S += Cone(.5, .5, color='red').translate(0,0,.3)
    sage: S += Sphere(.1, color='white').translate(.45,-.1,.15) + Sphere(.05, color='black').translate(.51,-.1,.17)
    sage: S += Sphere(.1, color='white').translate(.45, .1,.15) + Sphere(.05, color='black').translate(.51, .1,.17)
    sage: S += Sphere(.1, color='yellow').translate(.5, 0, -.2)
    sage: def f(x,y): return math.exp(x/5)*math.cos(y)
```


```
    sage: P = plot3d(f,(-5,5),(-5,5), ['red','yellow'], max_depth=10)
    sage: cape_man = P.scale(.2)+S.translate(1,0,0)
    sage: cape_man.export_jmol('/path/to/a.script')
```

Then, after downloading jmol, do 

```
./jmol /path/to/a.script
```



---

Attachment


---

Comment by was created at 2007-12-15 01:59:38

It works perfectly!!! Of course, it needs some doctests...

Try this out, it's awesome:

```
 sage: from sage.plot.plot3d.shapes import *
    sage: from sage.plot.plot3d.plot3d import plot3d
    sage: S = Sphere(.5, color='yellow')
    sage: S += Cone(.5, .5, color='red').translate(0,0,.3)
    sage: S += Sphere(.1, color='white').translate(.45,-.1,.15) + Sphere(.05, color='black').translate(.51,-.1,.17)
    sage: S += Sphere(.1, color='white').translate(.45, .1,.15) + Sphere(.05, color='black').translate(.51, .1,.17)
    sage: S += Sphere(.1, color='yellow').translate(.5, 0, -.2)
    sage: def f(x,y): return math.exp(x/5)*math.cos(y)
    sage: P = plot3d(f,(-200,20),(-200,20), ['red','yellow'], max_depth=10)
    sage: cape_man = P.scale(.2)+S.translate(1,0,0)
    sage: cape_man.export_jmol('/Users/was/sage-2.9.alpha7/jmol/a.script')
```



---

Comment by robertwb created at 2007-12-15 02:19:30

See #1516 for future work.


---

Comment by was created at 2007-12-15 23:54:13

Positi


---

Comment by mabshoff created at 2007-12-16 00:56:33

Resolution: fixed


---

Attachment

Merged in 2.9.rc2.
