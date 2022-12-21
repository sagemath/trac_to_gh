# Issue 1229: 2.8.13.rc1: sage/calculus/calculus.py doctest failure

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-11-20 23:06:20

Assignee: was


```
File "calculus.py", line 209:
     sage: expand((x+y)^3)
Expected:
     y^3 + 3*x*y^2 + 3*x^2*y + x^3
Got:
     x^6 + 3*x^5 + 3*x^4 + x^3
```

This is likely fallout from #1215.


Cheers,

Michael


---

Attachment


---

Comment by mabshoff created at 2007-11-21 13:00:38

Changing status from new to assigned.


---

Comment by mabshoff created at 2007-11-21 13:00:38

Merged in 2.8.13.rc2.


---

Comment by mabshoff created at 2007-11-21 13:00:38

Changing assignee from was to mabshoff.


---

Comment by mabshoff created at 2007-11-21 13:01:01

Resolution: fixed


---

Comment by mabshoff created at 2007-11-21 13:01:01

Merged in 2.8.13.rc2.
