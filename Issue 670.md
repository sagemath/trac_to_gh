# Issue 670: Solaris 10: functions/piecewise.py doctests failure (numerical)

Issue created by migration from https://trac.sagemath.org/ticket/670

Original creator: mabshoff

Original creation time: 2007-09-17 00:30:48

Assignee: was


```
sage -t  functions/piecewise.py                             **********************************************************************
File "piecewise.py", line 514:
    sage: f(2.5)
Expected:
    12.18249396070347
Got:
    12.18249396070348
**********************************************************************
1 items had failures:
   1 of   8 in __main__.example_13
***Test Failed*** 1 failures.
For whitespace errors, see the file .doctest_piecewise.py
         [10.0 s]
sage -t  functions/special.py                               **********************************************************************
File "special.py", line 689:
    sage: float(inverse_jacobi("sn",0.47,1/2))
Expected:
    0.4990982313222197
Got:
    0.49909823132221959
**********************************************************************
File "special.py", line 691:
    sage: float(inverse_jacobi("sn",0.4707504,0.5))
Expected:
    0.49999991146655459
Got:
    0.49999991146655481
**********************************************************************
```



---

Comment by mabshoff created at 2007-09-17 01:23:52

Changing component from packages to doctest.


---

Comment by mabshoff created at 2007-09-17 01:23:52

Changing assignee from was to failure.


---

Attachment


---

Comment by rlm created at 2007-12-22 01:08:35

Resolution: fixed


---

Comment by rlm created at 2007-12-22 01:08:35

merged in 2.9.1 alpha3
