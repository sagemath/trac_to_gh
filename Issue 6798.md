# Issue 6798: fix doctest timeout in modules/vector_double_dense.pyx

Issue created by migration from https://trac.sagemath.org/ticket/6798

Original creator: drkirkby

Original creation time: 2009-08-21 08:16:12

Assignee: tbd

On Solaris 10 update 7 (SPARC), the following tests timed out. Both ECL and Maxima were updated - ECL version 9.8.4 (see trac #6564); Maxima version 5.19.1 (see trac #6699). Updated spkgs can be found here. I'm not sure if this is new or not since updating Maxima + ECL, so it may or may not be related to that. 

http://sage.math.washington.edu/home/kirkby/Solaris-fixes/ecl-9.8.4/

http://sage.math.washington.edu/home/kirkby/Solaris-fixes/maxima-5.19.1/


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
sage -t  "devel/sage/sage/modules/vector_double_dense.pyx"
         [71.4 s]

sage -t  "devel/sage/sage/lfunctions/sympow.py"
*** *** Error: TIMED OUT! PROCESS KILLED! *** ***
*** *** Error: TIMED OUT! *** ***
*** *** Error: TIMED OUT! *** ***
         [361.1 s]
sage -t  "devel/sage/sage/lfunctions/all.py"
         [1.2 s]
```




---

Comment by drkirkby created at 2009-11-09 14:05:41

Changing component from algebra to solaris.


---

Comment by jdemeyer created at 2013-12-02 20:52:09

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2013-12-02 20:52:16

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-12-05 08:07:53

Resolution: invalid
