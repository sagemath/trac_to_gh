# Issue 3110: [with patch, needs review] rare pbuild dependency bug

Issue created by migration from https://trac.sagemath.org/ticket/3110

Original creator: gfurnish

Original creation time: 2008-05-06 04:33:11

Assignee: gfurnish

Keywords: pbuild

This patch corrects a bug in pbuild dependency checking that does not correctly register the pxd file dependency for a pyx file if no other files cimport the file (rare).


---

Attachment


---

Comment by gfurnish created at 2008-05-06 04:35:28

This patch also modifies -ba to clean the build directory.


---

Comment by gfurnish created at 2008-05-06 04:35:28

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-05-06 20:01:27

Path looks good to me. One thing: This patch also contains unrelated changes [besides the clean option] which are uncontroversial. I would suggest that you also add some release number that you increment on changes so we do not end up having to poke around for the exact version of pbuild when we need to debug some problem remotely.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-06 20:02:16

Merged in Sage 3.0.2.alpha0


---

Comment by mabshoff created at 2008-05-06 20:02:16

Resolution: fixed
