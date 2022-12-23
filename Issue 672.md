# Issue 672: Solaris 10: rings/complex_double.pyx doctests failure: nan vs. NaN

Issue created by migration from https://trac.sagemath.org/ticket/672

Original creator: mabshoff

Original creation time: 2007-09-17 00:33:34

Assignee: was

Keywords: Solaris 10, doctest, complex double


```
sage -t  rings/complex_double.pyx                           **********************************************************************
File "complex_double.pyx", line 621:
    sage: ~(0*CDF(0,1))
Expected:
    nan + nan*I
Got:
    -NaN + NaN*I
**********************************************************************
File "complex_double.pyx", line 1470:
    sage: z^2 - z + 1
Expected:
    2.22044604925e-16 + 1.11022302463e-16*I
Got:
    2.22044604925e-16 + 2.22044604925e-16*I
**********************************************************************
```



---

Comment by mabshoff created at 2007-09-17 01:24:09

Changing component from packages to doctest.


---

Comment by mabshoff created at 2007-09-17 01:24:09

Changing assignee from was to failure.


---

Comment by mabshoff created at 2009-04-17 10:54:06

This has been fixed in Sage 3.4.1.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-17 10:54:06

Resolution: fixed
