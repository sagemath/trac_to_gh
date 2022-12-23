# Issue 4634: Sage 3.2.1.a1: numerical noise in sage/schemes/ elliptic_curves/ell_rational_field.py

Issue created by migration from https://trac.sagemath.org/ticket/4634

Original creator: mabshoff

Original creation time: 2008-11-27 03:43:14

Assignee: mabshoff

CC:  jhpalmieri


```
File "/Applications/sage-3.2.1.alpha1/devel/sage/sage/schemes/
elliptic_curves/ell_rational_field.py", line 4071:
   sage: a = E.integral_points([P1,P2,P3], verbose=True)
Expected:
   Using mw_basis  [(2 : 0 : 1), (3 : -4 : 1), (8 : -22 : 1)]
   e1,e2,e3:  -3.01243037259331 1.0658205476962... 1.94660982489710
   Minimal eigenvalue of height pairing matrix:  0.63792081458500...
   x-coords of points on compact component with  -3 <=x<= 1
   [-3, -2, -1, 0, 1]
   x-coords of points on non-compact component with  2 <=x<= 6
   [2, 3, 4]
   starting search of remaining points using coefficient bound  5
   x-coords of extra integral points:
   [2, 3, 4, 8, 11, 14, 21, 37, 52, 93, 342, 406, 816]
   Total number of integral points: 18
Got:
   Using mw_basis  [(2 : 0 : 1), (3 : -4 : 1), (8 : -22 : 1)]
   e1,e2,e3:  -3.01243037259330 1.06582054769621 1.94660982489710
   Minimal eigenvalue of height pairing matrix:  0.637920814585007
   x-coords of points on compact component with  -3 <=x<= 1
   [-3, -2, -1, 0, 1]
   x-coords of points on non-compact component with  2 <=x<= 6
   [2, 3, 4]
   starting search of remaining points using coefficient bound  5
   x-coords of extra integral points:
   [2, 3, 4, 8, 11, 14, 21, 37, 52, 93, 342, 406, 816]
   Total number of integral points: 18
```



---

Attachment


---

Comment by mabshoff created at 2008-11-27 04:09:01

The problem is this:

```
   e1,e2,e3:  -3.01243037259331 1.0658205476962... 1.94660982489710
   e1,e2,e3:  -3.01243037259330 1.06582054769621 1.94660982489710
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-11-27 04:09:31

Changing status from new to assigned.


---

Comment by ncalexan created at 2008-11-27 04:10:42

Fine by me.


---

Comment by mabshoff created at 2008-11-27 04:19:50

Merged in Sage 3.2.1.alpha2


---

Comment by mabshoff created at 2008-11-27 04:19:50

Resolution: fixed
