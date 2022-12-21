# Issue 6785: Doctest failure in sage-4.1.1/devel/sage/doc/en/constructions/plotting.rst

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2009-08-20 21:48:32

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
**********************************************************************
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/doc/en/constructions/plotting.rst", line 209:
    sage: maxima.eval('load("plotdf");')
Expected:
    '".../local/share/maxima/5.16.3/share/dynamics/plotdf.lisp"'
Got:
    '"/export/home/drkirkby/sage/sage-4.1.1/local/share/maxima/5.19.1/share/dynamics/plotdf.lisp"'
**********************************************************************
1 items had failures:
   1 of   3 in __main__.example_11
***Test Failed*** 1 failures.
For whitespace errors, see the file /export/home/drkirkby/sage/sage-4.1.1/tmp/.doctest_plotting.py
```



---

Comment by AlexGhitza created at 2009-08-20 23:40:03

Changing status from new to assigned.


---

Comment by AlexGhitza created at 2009-08-20 23:40:03

Trivial: the Maxima version changed.  See attached patch.


---

Comment by AlexGhitza created at 2009-08-20 23:40:03

Changing assignee from was to AlexGhitza.


---

Comment by AlexGhitza created at 2009-08-20 23:40:03

Changing keywords from "" to "maxima".


---

Attachment

apply after the spkg's at #6564 and #6699


---

Comment by mvngu created at 2009-09-02 10:59:07

This is fixed by #6699.


---

Comment by mvngu created at 2009-09-02 10:59:29

Resolution: fixed
