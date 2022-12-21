# Issue 1335: [with patch] 2.8.14/Linux PPC: lcalc doctest failure

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-11-29 09:40:03

Assignee: mabshoff

On my Linux PPC 32 bit box I got the following doctest failure due to numerical noise:

```
File "lcalc.py", line 188:
    sage: E.Lseries().values_along_line(0.5, 3, 5)
Expected:
    lcalc:  1.5 0 WARNING- we don't have enough Dirichlet coefficients.
    lcalc:  Will use the maximum possible, though the output will not necessarily be accurate.
    lcalc:  nan nan
    [(0, 0.209951303),
     (0.500000000, -2...e-16),
     (1.00000000, 0.133768433),
     (2.00000000, 0.552975867)]
Got:
    lcalc:  1.5 0 WARNING- we don't have enough Dirichlet coefficients.
    lcalc:  Will use the maximum possible, though the output will not necessarily be accurate.
    lcalc:  nan nan
    [(0, 0.209951303), (0.500000000, -3.16949699e-16), (1.00000000, 0.133768433), (2.00000000, 0.552975867)]
```


The attached patch fixes that.

Cheers,

Michael


---

Attachment


---

Comment by mabshoff created at 2007-11-29 09:42:45

Changing status from new to assigned.


---

Comment by cwitty created at 2007-12-01 02:23:55

Looks good to me.


---

Comment by mabshoff created at 2007-12-01 11:25:01

Merged in 2.8.15.alpha0.


---

Comment by mabshoff created at 2007-12-01 11:25:01

Resolution: fixed
