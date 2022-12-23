# Issue 6549: reinstate some doctests in schemes/plane_curves/affine_curve.py

Issue created by migration from https://trac.sagemath.org/ticket/6549

Original creator: AlexGhitza

Original creation time: 2009-07-17 14:12:32

Assignee: tbd

Some doctests in `schemes/plane_curves/affine_curve.py` are marked "not tested" with the comment that they crash on OS X intel.  This appears to not be the case any more:


```
aghitza@192-168-1-2:~/opt/sage-4.1$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: x, y = (GF(17)['x,y']).gens()
sage: C = Curve(x^2+y^5+x*y-19)
sage: v = C.rational_points(algorithm='bn')
sage: w = C.rational_points(algorithm='enum')
sage: len(v)
20
sage: v == w
True
sage: 
Exiting SAGE (CPU time 0m0.23s, Wall time 1m59.83s).
Exiting spawned Singular process.
aghitza@192-168-1-2:~/opt/sage-4.1$ uname -a
Darwin 192-168-1-2.tpgi.com.au 9.7.0 Darwin Kernel Version 9.7.0: Tue Mar 31 22:52:17 PDT 2009; root:xnu-1228.12.14~1/RELEASE_I386 i386
```



---

Comment by AlexGhitza created at 2009-07-17 14:20:59

Changing status from new to assigned.


---

Comment by AlexGhitza created at 2009-07-17 14:20:59

Changing assignee from tbd to AlexGhitza.


---

Comment by craigcitro created at 2009-08-17 06:15:56

Looks good. Works fine on my MacBook Pro, and also seems to work fine on sage.math. My one potential complaint: I think there's a missing level of nesting in the docstring. That is, I think the three bullets after "algorithm" should be in a sub-list. (I recognize that this patch doesn't touch the docstring other than the doctests, but I still think they should be fixed since we're here.)


---

Attachment


---

Comment by AlexGhitza created at 2009-08-17 12:05:09

Docstring fixed, new patch replaces the old.


---

Comment by craigcitro created at 2009-08-17 18:37:23

Nice.


---

Comment by mvngu created at 2009-08-25 04:12:07

Resolution: fixed
