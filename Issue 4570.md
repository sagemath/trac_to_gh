# Issue 4570: change the numpy include to the standard place

Issue created by migration from https://trac.sagemath.org/ticket/4570

Original creator: jason

Original creation time: 2008-11-20 21:54:40

Assignee: mabshoff

CC:  robertwb

The standard numpy cython include is "numpy/arrayobject.h".  This changes Sage to use the standard include.


---

Attachment


---

Comment by robertwb created at 2008-11-20 22:08:07

Looks good to me, but I don't have a recent enough sage to try it out (merge conflicts). I guess it's time to download 3.2 now.


---

Comment by mabshoff created at 2008-11-21 10:28:36

Resolution: fixed


---

Comment by mabshoff created at 2008-11-21 10:28:36

Merged in Sage 3.2.1.alpha0
