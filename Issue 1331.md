# Issue 1331: [with patch] 2.8.14/Solaris: fix complex_double doctest  - numerical noise

Issue created by migration from https://trac.sagemath.org/ticket/1331

Original creator: mabshoff

Original creation time: 2007-11-28 23:20:10

Assignee: mabshoff

On Solaris I get the following doctest failures due to numerical noise:

```
sage -t  devel/sage-main/sage/rings/complex_double.pyx      **********************************************************************
File "complex_double.pyx", line 1496:
    sage: z^2 - z + 1
Expected:
    2.22044604925e-16 + 1.11022302463e-16*I
Got:
    2.22044604925e-16 + 2.22044604925e-16*I
```

The attached patch fixes that.

Cheers,

Michael


---

Attachment


---

Comment by mabshoff created at 2007-11-28 23:20:34

Changing status from new to assigned.


---

Comment by cwitty created at 2007-12-01 02:23:05

We need another approach for this... what if on another machine, the imaginary component is exactly zero?

But let's cross that bridge when we come to it.

Looks good to me.


---

Comment by mabshoff created at 2007-12-01 11:27:34

Merged in 2.8.15.alpha0.


---

Comment by mabshoff created at 2007-12-01 11:27:34

Resolution: fixed
