# Issue 1336: [with patch] 2.8.14/Linux PPC: rings/polynomial/polynomial_element.pyx doctest failure

Issue created by migration from https://trac.sagemath.org/ticket/1336

Original creator: mabshoff

Original creation time: 2007-11-29 09:42:06

Assignee: mabshoff

On Linux PPC the following doctest fails due to numerical noise:

```
File "polynomial_element.pyx", line 2371:
    sage: f.roots(multiplicities=False)
Expected:
    [-1.6772670339941..., 0.199954796285..., 0.200045306115..., 1.5763035161844...]
Got:
    [-1.67726703399418, 0.199954796284890, 0.200045306115409, 1.57630351618444]
```


The attached patch fixes that.

Cheers,

Michael


---

Comment by mabshoff created at 2007-11-29 09:42:40

Changing status from new to assigned.


---

Attachment


---

Comment by cwitty created at 2007-12-01 02:26:56

Looks good to me.


---

Comment by mabshoff created at 2007-12-01 11:23:28

Resolution: fixed


---

Comment by mabshoff created at 2007-12-01 11:23:28

Merged in 2.8.15.alpha0.
