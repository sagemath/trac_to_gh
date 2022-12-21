# Issue 6203: numerical noise on sparc solaris (trivial to fix)

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-06-03 23:11:19

Assignee: tbd


```
sage -t  devel/sage/sage/symbolic/expression.pyx
**********************************************************************
File "/home/wstein/build-4.4.0/mark/sage-4.0.1.alpha0/devel/sage-main/sage/symbolic/expression.pyx", line 5486:
    sage: f.find_minimum_on_interval(1, 5, tol=1e-3)
Expected:
    (-3.288371361890984, 3.42575079030572)
Got:
    (-3.2883713618909844, 3.42575079030572)
**********************************************************************
1 items had failures:
   1 of   8 in __main__.example_141
***Test Failed*** 1 failures.
```



---

Comment by mhansen created at 2009-06-04 06:34:26

Changing assignee from tbd to mhansen.


---

Comment by mhansen created at 2009-06-04 06:34:26

Changing status from new to assigned.


---

Attachment


---

Comment by mhansen created at 2009-06-04 09:05:26

Resolution: fixed


---

Comment by mhansen created at 2009-06-04 09:05:26

Merged in 4.0.1.rc0.
