# Issue 4273: Failure on Jordan form transformation matrices

Issue created by migration from https://trac.sagemath.org/ticket/4273

Original creator: mhampton

Original creation time: 2008-10-13 11:59:45

Assignee: was

CC:  jason

Keywords: jordan form, matrix

Getting the change of basis matrix for Jordan forms fails if there are multiple blocks with the same eigenvalue, e.g.:

```
m = matrix(QQ,[[0,1,0], [0,0,0], [0,0,0]])
m.jordan_form(base_ring=QQ, transformation=True) 
```

gives 

```
ValueError: cannot compute the basis of the Jordan block of size 2 with eigenvalue 0
```

This was reported on sage-support by Rob Beezer, subject line is: "Transformation to Jordan form for tame 6x6 integer matrix".


---

Comment by mhampton created at 2008-10-15 03:36:09

Changing assignee from was to mhampton.


---

Attachment


---

Comment by jason created at 2008-11-18 04:32:06

Tests pass in matrix2.pyx.


---

Comment by jason created at 2008-11-18 04:32:06

Changing assignee from mhampton to jason.


---

Comment by jason created at 2008-11-18 04:32:06

Changing status from new to assigned.


---

Comment by mhampton created at 2008-11-18 15:53:03

Seems to work very well.  I tested it on some tough random cases of size 12x12 to 30x30 and it seems correct, and reasonably fast.  Nice work.


---

Comment by mabshoff created at 2008-11-21 08:21:09

Resolution: fixed


---

Comment by mabshoff created at 2008-11-21 08:21:09

Merged in Sage 3.2.1.alpha0
