# Issue 6783: Doctest failure in sage-4.1.1/devel/sage/doc/en/constructions/linear_algebra.rst

Issue created by migration from https://trac.sagemath.org/ticket/6783

Original creator: drkirkby

Original creation time: 2009-08-20 21:34:42

Assignee: was

On Solaris (SPARC), the following test failed. Both ECL and Maxima were updated - ECL version 9.8.4, Maxima version 5.19.1


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
sage -t  "devel/sage/doc/en/constructions/linear_algebra.rst"
**********************************************************************
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/doc/en/constructions/linear_algebra.rst", line 276:
    sage: eig
Expected:
    [[[-sqrt(3)*%i,sqrt(3)*%i],[1,1]],[1,(sqrt(3)*%i+1)/4],[1,-(sqrt(3)*%i-1)/4]]
Got:
    [[[-sqrt(3)*%i,sqrt(3)*%i],[1,1]],[[[1,(sqrt(3)*%i+1)/4]],[[1,-(sqrt(3)*%i-1)/4]]]]
**********************************************************************
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/doc/en/constructions/linear_algebra.rst", line 291:
    sage: A.eigenvectors()
Expected:
    [[[2,11],[1,2]],[0,0,1],[0,1,1/3]]
Got:
    [[[2,11],[1,2]],[[[0,0,1]],[[0,1,1/3]]]]
**********************************************************************
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/doc/en/constructions/linear_algebra.rst", line 294:
    sage: A.eigenvectors()
Expected:
     [[[-1,2],[2,1]],[0,1,-1],[0,0,1]]
Got:
    [[[-1,2],[2,1]],[[[0,1,-1]],[[0,0,1]]]]
**********************************************************************
2 items had failures:
   1 of   5 in __main__.example_11
   2 of   6 in __main__.example_12
***Test Failed*** 3 failures.
For whitespace errors, see the file /export/home/drkirkby/sage/sage-4.1.1/tmp/.doctest_linear_algebra.py
         [19.2 s]
sage -t  "devel/sage/doc/en/constructions/number_theory.rst"
```



---

Comment by AlexGhitza created at 2009-08-20 23:27:53

Changing keywords from "" to "maxima".


---

Comment by AlexGhitza created at 2009-08-20 23:27:53

This is due to changes in Maxima's formatting of the output for eigenvectors.  See attached patch.


---

Attachment

apply after the spkg's at #6564 and #6699


---

Comment by AlexGhitza created at 2009-08-20 23:29:04

Changing assignee from was to AlexGhitza.


---

Comment by AlexGhitza created at 2009-08-20 23:29:04

Changing status from new to assigned.


---

Comment by mvngu created at 2009-09-02 10:57:53

This is fixed by #6699.


---

Comment by mvngu created at 2009-09-02 10:57:53

Resolution: fixed
