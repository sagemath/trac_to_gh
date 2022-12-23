# Issue 6784: Doctest failure in sage-4.1.1/devel/sage/doc/en/constructions/interface_issues.rst

Issue created by migration from https://trac.sagemath.org/ticket/6784

Original creator: drkirkby

Original creation time: 2009-08-20 21:43:53

Assignee: was

On Solaris 10 update 7 (SPARC), the following test failed. Both ECL and Maxima were updated - ECL version 9.8.4, Maxima version 5.19.1. Sage was built with gcc 4.4.1


```

----------------------------------------------------------------------
----------------------------------------------------------------------
Thu Aug 20 20:02:37 BST 2009
dsage-trial tmp directory doesn't exist - creating ...
This script will run the unit tests for DSage
```

| Sage Version 4.1.1, Release Date: 2009-08-14                       |
| Type notebook() for the GUI, and license() for information.        |
<SNIP>

```
sage -t  "devel/sage/doc/en/constructions/interface_issues.rst"
**********************************************************************
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/doc/en/constructions/interface_issues.rst", line 478:
    sage: maxima.eval("f:bessel_y (v, w)")
Expected:
    '?%bessel_y(v,w)'
Got:
    'bessel_y(v,w)'
**********************************************************************
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/doc/en/constructions/interface_issues.rst", line 480:
    sage: maxima.eval("diff(f,w)")
Expected:
    '(?%bessel_y(v-1,w)-?%bessel_y(v+1,w))/2'
Got:
    '(bessel_y(v-1,w)-bessel_y(v+1,w))/2'
**********************************************************************
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/doc/en/constructions/interface_issues.rst", line 482:
    sage: maxima.eval("diff (jacobi_sn (u, m), u)")
Expected:
    '?%jacobi_cn(u,m)*?%jacobi_dn(u,m)'
Got:
    'jacobi_cn(u,m)*jacobi_dn(u,m)'
**********************************************************************
1 items had failures:
   3 of   9 in __main__.example_3
***Test Failed*** 3 failures.
For whitespace errors, see the file /export/home/drkirkby/sage/sage-4.1.1/tmp/.doctest_interface_issues.py
         [19.8 s]

```



---

Comment by AlexGhitza created at 2009-08-20 23:34:50

Changing status from new to assigned.


---

Comment by AlexGhitza created at 2009-08-20 23:34:50

Changing keywords from "" to "maxima".


---

Comment by AlexGhitza created at 2009-08-20 23:34:50

Changing assignee from was to AlexGhitza.


---

Comment by AlexGhitza created at 2009-08-20 23:34:50

Simply due to new Maxima de-uglifying its output.  See attached patch.


---

Attachment

apply after spkg's at #6564 and #6699


---

Comment by mvngu created at 2009-09-02 10:58:36

Resolution: fixed


---

Comment by mvngu created at 2009-09-02 10:58:36

This is fixed by #6699.
