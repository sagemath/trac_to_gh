# Issue 646: plot3d error on itanium

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2007-09-13 05:42:53

Assignee: was


```
---------- Forwarded message ----------
From: Kate Minola <kate01123`@`gmail.com>
Date: Sep 12, 2007 7:27 AM
Subject: [sage-support] sage-2.8.4.1 build report
To: sage-support`@`googlegroups.com



William,

sage-2.8.4.1 built and successfully passed all
tests on the following architectures:

  x86-Linux (pentium4-fc6)
  x86_64-Linux (fc6)

On ia64-Linux, sage-2.8.4.1 only failed one test:
      sage -t  devel/sage-main/sage/plot/plot3d/plot3d.py
      [...]
      File "base.pyx", line 274, in base.TransformGroup.get_transformation
        self.T = Transformation(self._scale, self._rot, self._trans)
      File "transform.pyx", line 37, in transform.Transformation.__init__
        t = atan2(vy,vz) + pi/2
    ValueError: math domain error

```



---

Attachment


---

Comment by robertwb created at 2007-09-13 05:47:07

Changing status from new to assigned.


---

Comment by robertwb created at 2007-09-13 05:47:07

Looks like itanium sets errno on atan2(0,0), whereas other processors
return 0. Here's a fix.

I am going to rewrite the function to be cleaner and avoid all use of atan.


---

Comment by robertwb created at 2007-09-13 05:47:07

Changing assignee from was to robertwb.


---

Comment by was created at 2007-09-13 06:20:36

Resolution: fixed


---

Comment by was created at 2007-09-13 15:52:26

Still broken:

```
William,

The patch as written gives the same error.  However if you
change line 37 of the patch from
    if vx == vy == 0:
to
    if vy == vz == 0:
(since atan2() is taking arguments vy and vz) then
I get a different error on ia64-Linux:

sage -t  devel/sage-main/sage/plot/plot3d/plot3d.py
**********************************************************************
File "plot3d.py", line 19:
   sage: S.show()
Expected nothing
Got:
   6.0
   <type 'sage.rings.real_double.RealDoubleElement'>
   0.0
   0.0
**********************************************************************
```



---

Comment by was created at 2007-09-13 15:52:26

Resolution changed from fixed to 


---

Comment by was created at 2007-09-13 15:52:26

Changing status from closed to reopened.


---

Attachment

Hopefully this is not fixed (it's in 2.8.4.2)


---

Comment by was created at 2007-09-13 18:20:18

Resolution: fixed
