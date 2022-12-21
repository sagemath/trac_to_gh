# Issue 3308: [with patch; needs review] Update sage-sbuildhack to work with new sbuild in Debian

Issue created by migration from Trac.

Original creator: tabbott

Original creation time: 2008-05-26 05:16:12

Assignee: tabbott

One of the two patches to sbuild that we're using was accepted in Debian upstream sbuild, so we no longer need a big piece of SbuildHack.pm.  The other has not yet been accepted, so we don't get to get rid of SbuildHack.pm entirely yet.

I've attached a patch to sage-sbuildhack and SbuildHack.pm to work with current sbuild.


---

Attachment


---

Comment by mabshoff created at 2008-05-28 06:38:11

Patch applies cleanly. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-28 06:38:32

Merged in Sage 3.0.3.alpha0


---

Comment by mabshoff created at 2008-05-28 06:38:32

Resolution: fixed
