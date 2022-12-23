# Issue 6791: 2 doctest failures in devel/sage/sage/symbolic/expression.pyx

Issue created by migration from https://trac.sagemath.org/ticket/6791

Original creator: drkirkby

Original creation time: 2009-08-20 22:45:07

Assignee: tbd

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
**********************************************************************
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/sage/symbolic/expression.pyx", line 5541:
    sage: solve(Q*sqrt(Q^2 + 2) - 1,Q)
Expected:
    [Q == 1/sqrt(-sqrt(2) + 1), Q == 1/sqrt(sqrt(2) + 1)]
Got:
    [Q == 1/sqrt(sqrt(2) + 1)]
**********************************************************************
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/sage/symbolic/expression.pyx", line 2467:
    sage: sin(x/2).expand_trig(half_angles=True)
Expected:
    1/2*sqrt(-cos(x) + 1)*sqrt(2)
Got:
    1/2*sqrt(-cos(x) + 1)*sqrt(2)*(-1)^floor(1/2*x/pi)
**********************************************************************
2 items had failures:
   1 of   6 in __main__.example_138
   1 of  13 in __main__.example_61
***Test Failed*** 2 failures.
```



---

Comment by AlexGhitza created at 2009-08-20 23:59:24

Duplicate of #6789.


---

Comment by kcrisman created at 2009-09-15 13:11:05

To release manager: Sounds like this should be closed, then.


---

Comment by was created at 2009-10-05 14:17:50

Resolution: duplicate
