# Issue 668: Solaris 10: calculus/calculus.py doctests failure (numerical)

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-09-17 00:29:00

Assignee: was

Keywords: Solaris 10, doctest


```
sage -t  calculus/calculus.py                               **********************************************************************
File "calculus.py", line 1695:
    sage: f.nintegral(x, 0, 1)
Expected:
    (0.52848223531423055, 4.1633141378838452e-11, 231, 0)
Got:
    (0.52848223531423055, 4.163291933423352e-11, 231, 0)
**********************************************************************
1 items had failures:
   1 of   3 in __main__.example_35
***Test Failed*** 1 failures.
```



---

Comment by mabshoff created at 2007-09-17 01:23:34

Changing component from packages to doctest.


---

Comment by mabshoff created at 2007-09-17 01:23:34

Changing assignee from was to failure.


---

Attachment


---

Comment by rlm created at 2007-12-22 01:06:49

Resolution: fixed


---

Comment by rlm created at 2007-12-22 01:06:49

merged in 2.9.1 alpha3
