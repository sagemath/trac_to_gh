# Issue 1794: Gram-Schmidt typo

Issue created by migration from https://trac.sagemath.org/ticket/1794

Original creator: wjp

Original creation time: 2008-01-16 17:59:01

Assignee: was

Sage calls Gram-Schmidt Gramm-Schmidt in some places (including function names). The attached patch fixes the ones I found.


---

Attachment


---

Comment by ncalexan created at 2008-01-20 06:55:09

Apply this, but there may be other instances in libs/ntl/ntl_mat_ZZ.pyx.


---

Comment by mabshoff created at 2008-01-21 06:08:06

Merged in Sage 2.10.1.alpha1


---

Comment by mabshoff created at 2008-01-21 06:08:06

Resolution: fixed
