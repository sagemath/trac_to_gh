# Issue 3077: pbuild does not return properly on failure

Issue created by migration from https://trac.sagemath.org/ticket/3077

Original creator: gfurnish

Original creation time: 2008-05-02 10:06:58

Assignee: gfurnish

Keywords: pbuild

pbuild does not return an exceptional value to the operating system on failure.



---

Attachment


---

Comment by gfurnish created at 2008-05-02 10:22:51

Changing status from new to assigned.


---

Comment by gfurnish created at 2008-05-02 10:22:51

The easy test case for this is to create a cython failure and try to sage -br.  Prepatch it runs sage and postpatch it does not.


---

Comment by mabshoff created at 2008-05-02 12:00:41

Resolution: fixed


---

Comment by mabshoff created at 2008-05-02 12:00:41

Merged in Sage 3.0.1.rc0
