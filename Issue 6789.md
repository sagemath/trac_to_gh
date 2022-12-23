# Issue 6789: 2 doctest failures in devel/sage/sage/symbolic/expression.pyx

Issue created by migration from https://trac.sagemath.org/ticket/6789

Original creator: drkirkby

Original creation time: 2009-08-20 22:21:10

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
| Sage Version 4.1.1, Release Date: 2009-08-14                       |
| Type notebook() for the GUI, and license() for information.        |

```
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/sage/symbolic/expression.pyx", line 5541:
    sage: solve(Q*sqrt(Q^2 + 2) - 1,Q)
Expected:
    [Q == 1/sqrt(-sqrt(2) + 1), Q == 1/sqrt(sqrt(2) + 1)]
Got:
/ailures
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
For whitespace errors, see the file /export/home/drkirkby/sage/sage-4.1.1/tmp/.doctest_expression.py
         [116.1 s]

```



---

Comment by AlexGhitza created at 2009-08-20 23:55:46

Changing keywords from "" to "maxima".


---

Comment by mvngu created at 2009-09-02 11:02:50

This is fixed by #6699.


---

Comment by mvngu created at 2009-09-02 11:02:50

Resolution: fixed
