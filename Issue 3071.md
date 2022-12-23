# Issue 3071: Using pbuild does not create site-packages sage symlink

Issue created by migration from https://trac.sagemath.org/ticket/3071

Original creator: gfurnish

Original creation time: 2008-05-01 10:26:22

Assignee: mabshoff

Keywords: pbuild

If you use pbuild during the initial setup, it does not create the sage symlink in site-packages.  This can be fixed by performing:
ln -s devel/sage/build/sage/ local/lib/python/site-packages/sage
during the install process.  


---

Comment by gfurnish created at 2008-05-02 00:18:06

Changing status from new to assigned.


---

Comment by gfurnish created at 2008-05-02 00:18:06

The attached patch should fix this issue and the linking issues reported on the mailing list.  It also fixes the banner.


---

Comment by gfurnish created at 2008-05-02 00:18:06

Changing assignee from mabshoff to gfurnish.


---

Attachment


---

Attachment


---

Comment by mabshoff created at 2008-05-02 12:02:16

Merged in Sage 3.0.1.rc0


---

Comment by mabshoff created at 2008-05-02 12:02:16

Resolution: fixed
