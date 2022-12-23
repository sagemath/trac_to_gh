# Issue 1388: failure in calculus/wester.py

Issue created by migration from https://trac.sagemath.org/ticket/1388

Original creator: jsp

Original creation time: 2007-12-03 21:13:08

Assignee: was


```

sage -t  devel/sage-main/sage/calculus/wester.py            **********************************************************************
File "wester.py", line 399:
    : print d.factor()
Expected:
    (-1) * (a - d) * (-a + b) * (b - d) * (a - c) * (b - c) * (c - d)
Got:
    (-1) * (-a + b) * (a - c) * (b - c) * (a - d) * (b - d) * (c - d)
**********************************************************************
1 items had failures:
   1 of 188 in __main__.example_0
***Test Failed*** 1 failures.
For whitespace errors, see the file .doctest_wester.py
         [9.5 s]
exit code: 256
 

```



This seems to be a 32 bits issue!?


---

Comment by mabshoff created at 2007-12-03 21:24:10

Changing assignee from was to failure.


---

Comment by mabshoff created at 2007-12-03 21:24:10

Changing component from algebraic geometry to doctest.


---

Comment by mabshoff created at 2007-12-03 21:26:44

This only happens on Linux 32 bit, but not on OSX PPC 32 bit. So adding special `#32` and `#64` flags won't work.

Cheers,

Michael


---

Comment by mabshoff created at 2007-12-04 14:29:20

Fixed by #1392.

Cheers,

Michael


---

Comment by mabshoff created at 2007-12-04 14:29:20

Resolution: fixed
