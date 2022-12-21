# Issue 1548: Sage 2.9: calculus/calculus.py numerical noise doctest

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-12-17 13:32:31

Assignee: mabshoff


```
sage -t  devel/sage-main/sage/calculus/calculus.py
**********************************************************************
File "calculus.py", line 2460:
    sage: v.find_root(0, 0.002)
Expected:
    0.0015403270679114178
Got:
    0.0015403270679114176
**********************************************************************
File "calculus.py", line 2473:
    sage: a.find_root(0,0.002)
Expected:
    0.00041105140493493411
Got:
    0.00041105140493493417
**********************************************************************
```



---

Attachment


---

Comment by rlm created at 2007-12-18 21:24:27

Merged in 2.9.1.alpha1


---

Comment by rlm created at 2007-12-18 21:24:27

Resolution: fixed
