# Issue 1020: squash warning from decl.pxi emitted by cython

Issue created by migration from https://trac.sagemath.org/ticket/1020

Original creator: mabshoff

Original creation time: 2007-10-28 09:52:05

Assignee: mabshoff

With 2.8.10.alpha1 every file that includes decl.pxi cython emits the following warnings:

```
warning: /tmp/Work-mabshoff/sage-2.8.10.alpha1/devel/sage-main/sage/libs/ntl/decl.pxi:33:18: Function signature does not match previous declaration
warning: /tmp/Work-mabshoff/sage-2.8.10.alpha1/devel/sage-main/sage/libs/ntl/decl.pxi:34:18: Function signature does not match previous declaration
warning: /tmp/Work-mabshoff/sage-2.8.10.alpha1/devel/sage-main/sage/libs/ntl/decl.pxi:244:27: Function signature does not match previous declaration
```


Cheers,

Michael


---

Comment by cwitty created at 2007-10-28 16:54:21

Changing assignee from mabshoff to cwitty.


---

Attachment


---

Comment by cwitty created at 2007-10-28 17:46:20

The attached patches fix these warnings, as well as several others.


---

Comment by cwitty created at 2007-10-28 17:46:20

Resolution: fixed
