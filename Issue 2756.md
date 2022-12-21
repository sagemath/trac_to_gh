# Issue 2756: [with patch; needs review] Debianize GAP spkg

Issue created by migration from Trac.

Original creator: tabbott

Original creation time: 2008-04-01 18:41:37

Assignee: tabbott

I've attached a patch to add Debian build support to the GAP spkg (it only builds the Guava GAP package).


---

Attachment


---

Attachment


---

Comment by mabshoff created at 2008-04-01 22:54:59

Patch looks good to me. One slight issue is that Guava has been updated to Guava 3.4. So let's merge this in alpha0 and if it doesn't work we can fix it later.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-01 23:06:58

Merged in gap-4.4.10.p5 in Sage 3.0.alpha0


---

Comment by mabshoff created at 2008-04-01 23:06:58

Resolution: fixed
