# Issue 3010: Numerical noise doctest failure in rings/complex_double.pyx

Issue created by migration from https://trac.sagemath.org/ticket/3010

Original creator: mabshoff

Original creation time: 2008-04-23 21:07:14

Assignee: failure

Andrzej Giniewicz reported:

```
sage -t  devel/sage-main/sage/rings/complex_double.pyx
**********************************************************************
File "/opt/sage-3.0.rc1/tmp/complex_double.py", line 1659:
    sage: z^2 - z + 1
Expected:
    2.22044604925e-16 + ...e-16*I
Got:
    2.22044604925e-16
**********************************************************************
1 items had failures:
   1 of   7 in __main__.example_93
***Test Failed*** 1 failures.
For whitespace errors, see the file /opt/sage-3.0.rc1/
tmp/.doctest_complex_double.py
         [4.1 s]
exit code: 1024
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-05-03 15:37:29

Changing priority from major to blocker.


---

Attachment


---

Comment by mabshoff created at 2008-05-03 15:54:22

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-05-03 15:54:22

Changing assignee from failure to mabshoff.


---

Comment by aginiewicz created at 2008-05-03 16:29:37

After applying that patch, doctest pass without problem


---

Comment by mabshoff created at 2008-05-03 16:33:59

Resolution: fixed


---

Comment by mabshoff created at 2008-05-03 16:33:59

Merged in Sage 3.0.1.final
