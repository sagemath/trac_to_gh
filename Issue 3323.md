# Issue 3323: [with patch, needs review] Enhanced error reporting for dependency errors in pbuild

Issue created by migration from Trac.

Original creator: gfurnish

Original creation time: 2008-05-28 15:49:04

Assignee: gfurnish

Keywords: pbuild

This patch adds some better error handeling to pbuild - instead of dieing with a mysterious error, it will tell you the file from which a dependency that is missing is being imported from (if foo.pyx is trying to cimport bar and there is no bar.pxd, it will tell you that foo.pyx is missing bar.pxd).  It will also tell you if foo.pyx imports some file which imports bar.



---

Attachment


---

Comment by gfurnish created at 2008-05-28 15:49:47

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-05-28 23:36:16

Patch looks good to me. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-29 01:10:16

Merged in Sage 3.0.3.alpha1


---

Comment by mabshoff created at 2008-05-29 01:10:16

Resolution: fixed
