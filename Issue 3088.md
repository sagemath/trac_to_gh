# Issue 3088: [with patch; needs review] Fixes for Debian gfan build

Issue created by migration from Trac.

Original creator: tabbott

Original creation time: 2008-05-03 05:02:38

Assignee: tabbott

Attached is a patch that makes gfan build correctly for the Debian package.  I'm not sure why it stopped working in the first place, but this version is more Debian policy compliant than the old one anyway.


---

Attachment

Patch looks good to me. The solution is correct as discussed on sage-devel. Positive review. Slipped into gfan-0.3.p3.spkg without bumping the release number.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-03 14:16:37

Merged in Sage 3.0.1.final


---

Comment by mabshoff created at 2008-05-03 14:16:37

Resolution: fixed
