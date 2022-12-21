# Issue 7281: numerical noise issue on fedora32 for 4.2.alpha1

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2009-10-24 03:35:08

Assignee: tbd


```
sage -t -long "devel/sage/doc/en/tutorial/tour_algebra.rst" 
**********************************************************************
File "/tmp/wstein/farm/sage-4.2.alpha1/devel/sage/doc/en/tutorial/tour_algebra.rst", line 87:
    sage: find_root(cos(phi)==sin(phi),0,pi/2)
Expected:
    0.78539816339744839
Got:
    0.78539816339744828
**********************************************************************
1 items had failures:
   1 of   4 in __main__.example_5
***Test Failed*** 1 failures.
```



---

Comment by mhansen created at 2009-10-24 03:40:43

Resolution: duplicate


---

Comment by mhansen created at 2009-10-24 03:40:43

Duplicate of #7275
