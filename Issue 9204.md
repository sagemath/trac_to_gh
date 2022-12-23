# Issue 9204: %hide weirdness

Issue created by migration from https://trac.sagemath.org/ticket/9204

Original creator: malb

Original creation time: 2010-06-10 14:10:24

Assignee: jason, was

CC:  iandrus chapoton

Say we have a cell like this:


```
%hide
1+1
```


after Shift+Enter it would grey out the input but would *not* collapse the input cell to one line. If I click on the cell and then click somewhere else %hide works as expected and actually reduces the size of the input cell to one line.


---

Comment by mkoeppe created at 2020-08-18 00:36:52

Proposing to close all sagenb tickets as outdated, so that all remaining open tickets in the notebook component are about the Jupyter notebook.


---

Comment by mkoeppe created at 2020-08-18 00:36:52

Changing status from new to needs_review.


---

Comment by chapoton created at 2020-09-10 08:10:25

Resolution: invalid
