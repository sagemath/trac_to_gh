# Issue 6150: numerical noise issues in 4.0.rc1

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2009-05-28 15:30:24

Assignee: tbd


```

       sage -t  "devel/sage/sage/matrix/matrix2.pyx"
       sage -t  "devel/sage/sage/symbolic/expression.pyx"

sage -t  "devel/sage/sage/matrix/matrix2.pyx"
**********************************************************************
File "/home/jaap/Download/sage-4.0.alpha0/devel/sage/sage/matrix/matrix2.pyx", line 4964:
    sage: m.change_ring(CDF).eigenvalues() # again for display purposes
Expected:
    [10.463115298 - 4.98835989975e-16*I, 7.42365754809 - 5.05298436852e-16*I, 3.36964641458 + 5.59670199836e-17*I, 1.25904669699 + 4.34508443713e-17*I,
0.00689184179485 - 5.75358699674e-17*I, 0.330700789655 + 5.1816322259e-16*I]
Got:
    [10.463115298 - 4.46500755169e-16*I, 7.42365754809 + 1.02246204259e-16*I, 3.36964641458 - 2.25910315504e-16*I, 1.25904669699 + 7.13217318887e-17*I,
0.00689184179485 - 3.00110164897e-16*I, 0.330700789655 + 1.23712186398e-16*I]
**********************************************************************
1 items had failures:
   1 of  36 in __main__.example_81

sage -t  "devel/sage/sage/symbolic/expression.pyx"
**********************************************************************
File "/home/jaap/Download/sage-4.0.alpha0/devel/sage/sage/symbolic/expression.pyx", line 4395:
    sage: maxima('atanh(0.5)')
Expected:
    .5493061443340548
Got:
    .5493061443340549
**********************************************************************
File "/home/jaap/Download/sage-4.0.alpha0/devel/sage/sage/symbolic/expression.pyx", line 946:
    sage: hash(x^y)
Expected:
    4043309056
Got:
    -251658240
**********************************************************************
2 items had failures:
   1 of   9 in __main__.example_115
   1 of  14 in __main__.example_33
***Test Failed*** 2 failures.
```



---

Comment by mhansen created at 2009-05-28 16:49:05

Changing status from new to assigned.


---

Comment by mhansen created at 2009-05-28 16:49:05

Changing assignee from tbd to mhansen.


---

Comment by mhansen created at 2009-05-28 16:49:05

I've attached a patch which fixes the above issues.


---

Attachment


---

Comment by mhansen created at 2009-05-28 19:12:06

Merged in 4.0.rc2.


---

Comment by mhansen created at 2009-05-28 19:12:06

Resolution: fixed
