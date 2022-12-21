# Issue 1328: 2.8.14/Solaris: partitions_c.h compile fix - unclean

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-11-28 22:26:23

Assignee: mabshoff

On Solaris we need to apply the attached patch to make the partition code compile. This version breaks on non-Solaris, so it needs some trivial cleanup.

Cheers,

Michael


---

Attachment


---

Comment by mabshoff created at 2008-01-30 03:19:02

There is a new unified patch at #1329. Do not apply this patch here.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-30 03:19:02

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-01-30 07:09:29

Patch passes compile test and testall on non-Solaris.

Cheers,

Michael


---

Comment by jkantor created at 2008-01-30 07:30:20

tested that it doesn't break anyting on linux


---

Comment by mabshoff created at 2008-01-30 07:55:44

Merged Sage-2.10.1.rc2-Solaris-build-fixes-for-sage.spkg.patch from #1329 in Sage 2.10.1.rc3


---

Comment by mabshoff created at 2008-01-30 07:55:44

Resolution: fixed
