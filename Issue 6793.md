# Issue 6793: 1 doctest timed out in devel/sage/sage/schemes/elliptic_curves/ell_point.py

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2009-08-20 23:03:45

Assignee: davidloeffler

On Solaris 10 update 7 (SPARC), the following tests failed. Both ECL and Maxima were updated - ECL version 9.8.4, Maxima version 5.19.1. Sage was built with gcc 4.4.1

```
----------------------------------------------------------------------
----------------------------------------------------------------------
Thu Aug 20 20:02:37 BST 2009
dsage-trial tmp directory doesn't exist - creating ...
This script will run the unit tests for DSage
```

<SNIP>

```
sage -t  "devel/sage/sage/schemes/elliptic_curves/ell_point.py"
*** *** Error: TIMED OUT! PROCESS KILLED! *** ***
*** *** Error: TIMED OUT! *** ***
*** *** Error: TIMED OUT! *** ***
         [361.6 s]
```

| Sage Version 4.1.1, Release Date: 2009-08-14                       |
| Type notebook() for the GUI, and license() for information.        |


---

Comment by AlexGhitza created at 2009-08-21 00:01:03

Changing keywords from "" to "maxima".


---

Comment by davidloeffler created at 2009-10-09 09:09:45

Remove assignee davidloeffler.


---

Comment by AlexGhitza created at 2009-11-28 04:37:42

Changing component from elliptic curves to solaris.


---

Comment by jdemeyer created at 2013-12-02 20:51:18

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2013-12-02 20:51:24

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-12-05 08:07:36

Resolution: invalid
