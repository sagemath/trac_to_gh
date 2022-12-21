# Issue 2643: [with patch; needs review] Fix Debian Sections

Issue created by migration from Trac.

Original creator: tabbott

Original creation time: 2008-03-22 03:40:43

Assignee: tabbott

I failed to correctly setup the Section fields of some of the Debian control files.  Attached are a series of patches to fix these problems.


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment

Merged eclib.patch in eclib-20080310.p1.


---

Comment by tabbott created at 2008-04-10 16:13:23

I should note that missing sections cause failures when trying to upload to a repository, so we should try to be sure these get merged sometime before the 3.0 release.


---

Comment by mabshoff created at 2008-04-11 22:12:18

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-04-11 22:12:18

Changing priority from major to blocker.


---

Comment by mabshoff created at 2008-04-11 22:12:18

All these will go in before 3.0.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-11 22:12:18

Changing assignee from tabbott to mabshoff.


---

Comment by mabshoff created at 2008-04-12 17:29:11

Merged flint.patch, givaro.patch, libm4ri.patch and singular.patch into Sage 3.0.alpha4. I did not increment the patch level of the spkgs to avoid unneeded rebuilds on upgrade.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-12 17:29:11

Resolution: fixed
