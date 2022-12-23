# Issue 1330: [with patch] 2.8.14/Solaris: fix sympy doctest - numerical noise

Issue created by migration from https://trac.sagemath.org/ticket/1330

Original creator: mabshoff

Original creation time: 2007-11-28 23:17:59

Assignee: failure

On Solaris I get the following doctest failures due to numerical noise:

```
sage -t  devel/sage-main/sage/calculus/test_sympy.py        **********************************************************************
File "test_sympy.py", line 23:
    : float(pi + exp(1))
Expected:
    5.8598744820488378
Got:
    5.8598744820488387
```


The attached patch fixes that.

Cheers,

Michael


---

Comment by mabshoff created at 2007-11-28 23:18:26

Changing status from new to assigned.


---

Comment by mabshoff created at 2007-11-28 23:18:26

Changing assignee from failure to mabshoff.


---

Attachment


---

Comment by cwitty created at 2007-12-01 02:20:37

Looks good to me.


---

Comment by mabshoff created at 2007-12-01 11:27:49

Merged in 2.8.15.alpha0.


---

Comment by mabshoff created at 2007-12-01 11:27:49

Resolution: fixed
