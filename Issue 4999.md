# Issue 4999: Solaris 10/Sparc: numerical noise doctest failure in sage/gsl/integration.pyx

Issue created by migration from https://trac.sagemath.org/ticket/4999

Original creator: mabshoff

Original creation time: 2009-01-17 16:02:24

Assignee: mabshoff


```
sage -t  "devel/sage/sage/gsl/integration.pyx"              
**********************************************************************
File "/home/mabshoff/build-3.2.3/sage-3.2.3-mark/devel/sage/sage/gsl/integration.pyx", line 163:
    sage: numerical_integral(exp(-1/x), 1, 2)
Expected:
    (0.50479221787318407, 5.6043194293440744e-15)
Got:
    (0.50479221787318396, 5.6043194293440728e-15)
**********************************************************************
```



---

Comment by mabshoff created at 2009-01-17 16:02:40

Changing status from new to assigned.


---

Attachment


---

Comment by mabshoff created at 2009-01-18 14:06:54

Merged in Sage 3.3.alpha0


---

Comment by mabshoff created at 2009-01-18 14:06:54

Resolution: fixed
