# Issue 1329: 2.8.14/Solaris: real_rqdf.pyx compile fixes

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-11-28 22:28:35

Assignee: mabshoff

On Solaris we need some of the following two patches to make it compile. Those aren't clean and would break compilation on other platforms.

Cheers,

Michael


---

Attachment


---

Attachment


---

Comment by mabshoff created at 2008-01-30 03:20:11

The patch Sage-2.10.1.rc2-Solaris-build-fixes-for-sage.spkg.patch includes all fixes from #1328 and #1329 in a cleaned up for. Apply that patch only.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-30 03:20:18

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-01-30 07:09:36

Patch passes compile test and testall on non-Solaris.

Cheers,

Michael


---

Comment by jkantor created at 2008-01-30 07:29:26

Tested that it doesn't break anything on linux.


---

Comment by mabshoff created at 2008-01-30 07:55:25

Resolution: fixed


---

Comment by mabshoff created at 2008-01-30 07:55:25

Merged Sage-2.10.1.rc2-Solaris-build-fixes-for-sage.spkg.patch in Sage 2.10.1.rc3
