# Issue 6786: 4 doctest failures in sage-4.1.1/devel/sage/doc/en/tutorial/tour_algebra.rst

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2009-08-20 21:55:52

Assignee: tbd

On Solaris 10 update 7 (SPARC), the following test failed. Both ECL and Maxima were updated - ECL version 9.8.4, Maxima version 5.19.1. Sage was built with gcc 4.4.1

```
----------------------------------------------------------------------
----------------------------------------------------------------------
Thu Aug 20 20:02:37 BST 2009
dsage-trial tmp directory doesn't exist - creating ...
This script will run the unit tests for DSage
```

<SNIP>

```
sage -t  "devel/sage/doc/en/tutorial/tour_algebra.rst"
**********************************************************************
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/doc/en/tutorial/tour_algebra.rst", line 205:
    sage: lde1 = de1.laplace("t","s"); lde1
Expected:
    2*(-?%at('diff(x(t),t,1),t=0)+s^2*?%laplace(x(t),t,s)-x(0)*s)-2*?%laplace(y(t),t,s)+6*?%laplace(x(t),t,s)
Got:
    2*(-?%at('diff(x(t),t,1),t=0)+s^2*'laplace(x(t),t,s)-x(0)*s)-2*'laplace(y(t),t,s)+6*'laplace(x(t),t,s)
**********************************************************************
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/doc/en/tutorial/tour_algebra.rst", line 220:
    sage: lde2 = de2.laplace("t","s"); lde2
Expected:
    -?%at('diff(y(t),t,1),t=0)+s^2*?%laplace(y(t),t,s)+2*?%laplace(y(t),t,s)-2*?%laplace(x(t),t,s)-y(0)*s
Got:
    -?%at('diff(y(t),t,1),t=0)+s^2*'laplace(y(t),t,s)+2*'laplace(y(t),t,s)-2*'laplace(x(t),t,s)-y(0)*s
**********************************************************************
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/doc/en/tutorial/tour_algebra.rst", line 410:
    sage: maxima.eval("f:bessel_y(v, w)")
Expected:
    '?%bessel_y(v,w)'
Got:
    'bessel_y(v,w)'
**********************************************************************
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/doc/en/tutorial/tour_algebra.rst", line 412:
    sage: maxima.eval("diff(f,w)")
Expected:
    '(?%bessel_y(v-1,w)-?%bessel_y(v+1,w))/2'
Got:
    '(bessel_y(v-1,w)-bessel_y(v+1,w))/2'
**********************************************************************
3 items had failures:
   1 of   4 in __main__.example_11
   1 of   4 in __main__.example_12
   2 of   4 in __main__.example_20
***Test Failed*** 4 failures.
For whitespace errors, see the file /export/home/drkirkby/sage/sage-4.1.1/tmp/.doctest_tour_algebra.py
| Sage Version 4.1.1, Release Date: 2009-08-14                       |
| Type notebook() for the GUI, and license() for information.        |
```



---

Comment by AlexGhitza created at 2009-08-20 23:49:47

Changing assignee from tbd to AlexGhitza.


---

Comment by AlexGhitza created at 2009-08-20 23:49:47

Simple changes to Maxima formatting.  See attached patch.


---

Comment by AlexGhitza created at 2009-08-20 23:49:47

Changing keywords from "" to "maxima".


---

Comment by AlexGhitza created at 2009-08-20 23:49:47

Changing status from new to assigned.


---

Comment by drkirkby created at 2009-08-22 02:06:44

I don't see any patch attached.


---

Comment by mvngu created at 2009-09-02 11:00:00

This is fixed by #6699.


---

Comment by mvngu created at 2009-09-02 11:00:00

Resolution: fixed
