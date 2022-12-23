# Issue 1455: 2.9.alpha4: numerical noise doctest failure on OSX 10.4

Issue created by migration from https://trac.sagemath.org/ticket/1455

Original creator: mabshoff

Original creation time: 2007-12-10 22:40:47

Assignee: mabshoff

Rishikesh reported:

```
sage -t  devel/sage-main/sage/numerical/optimize.py
**********************************************************************
File "optimize.py", line 93:
    sage: find_maximum_on_interval(f, 0,5)
Expected:
    (0.561096338191, 0.860333589015)
Got:
    (0.561096338191, 0.860333589074)
**********************************************************************

sage -t  devel/sage-main/sage/calculus/calculus.py
********************
**************************************************
File "calculus.py", line 2446:
    sage: f.find_maximum_on_interval(0,5)
Expected:
    (0.5610963381910451, 0.860333589015)
Got:
    (0.5610963381910451, 0.860333589074)
********************************************************************** 
```


Cheers,
Michael



---

Comment by mabshoff created at 2007-12-10 22:41:35

Changing status from new to assigned.


---

Comment by mabshoff created at 2007-12-11 01:01:26

Merged in 2.9.alpha5.


---

Comment by mabshoff created at 2007-12-11 01:01:26

Resolution: fixed
