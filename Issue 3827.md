# Issue 3827: finance.TimeSeries -- missng docstring input option

Issue created by migration from https://trac.sagemath.org/ticket/3827

Original creator: cswiercz

Original creation time: 2008-08-12 23:44:08

Assignee: cswiercz

CC:  cswiercz

Keywords: finance, timeseries

TimeSeries.randomize has a lognormal distribution generator built in along with uniform, normal, and semicircle. However, there is no docstring that says so! Simply need to add a line that looks like


```
INPUT:
    distribution -- 'lognormal': mean loc and standard deviation scale
```


See patch below.


---

Attachment


---

Comment by cswiercz created at 2008-08-12 23:44:35

Changing status from new to assigned.


---

Comment by aginiewicz created at 2008-08-14 17:48:39

That's one trivial to review, patch works with 3.1-alpha2 (with 71 lines offset)...


---

Comment by mabshoff created at 2008-08-15 06:14:33

Resolution: fixed


---

Comment by mabshoff created at 2008-08-15 06:14:33

Merged in Sage 3.1.rc0
