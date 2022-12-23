# Issue 1412: creating directory in notebook cell #x makes evaluation of cell #x hang

Issue created by migration from https://trac.sagemath.org/ticket/1412

Original creator: boothby

Original creation time: 2007-12-06 19:25:23

Assignee: was

Executing the following in a notebook cell works exactly once.  If one tries to re-evaluate the cell, an OSError is hit by the server, the evaluation never terminates nor does any work.


```
os.mkdir("tmp")
```



---

Attachment

patch works for me


---

Comment by mabshoff created at 2007-12-09 15:08:36

Resolution: fixed


---

Comment by mabshoff created at 2007-12-09 15:08:36

Merged in 2.9.alpha2.
