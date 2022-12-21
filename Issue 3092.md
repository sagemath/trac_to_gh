# Issue 3092: [with patch; needs review] Debian Singular permissions fixes

Issue created by migration from Trac.

Original creator: tabbott

Original creation time: 2008-05-03 08:21:36

Assignee: tabbott

I've attached a patch that fixes the permissions issues with libsingular.so (and the oddly executable stuff in /usr/lib/singular).


---

Attachment


---

Comment by mabshoff created at 2008-05-03 14:26:15

Patch looks good to me. Positive review. Slipped into singular-3-0-4-2-20080405.p1.spkg without increasing the release version.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-03 14:26:27

Resolution: fixed


---

Comment by mabshoff created at 2008-05-03 14:26:27

Merged in Sage 3.0.1.final


---

Comment by tabbott created at 2008-05-03 18:40:27

That patch didn't actually work.  I've attached a patch on top of that one that fixes the real problem: dh_fixperms removing the executable bit.


---

Comment by tabbott created at 2008-05-03 18:40:27

Changing status from closed to reopened.


---

Comment by tabbott created at 2008-05-03 18:40:27

Resolution changed from fixed to 


---

Attachment


---

Comment by mabshoff created at 2008-05-03 19:14:04

Ops, merged singular-permissions.2.patch in Sage 3.0.1.final.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-03 19:14:04

Resolution: fixed
