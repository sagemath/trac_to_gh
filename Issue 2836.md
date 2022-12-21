# Issue 2836: [with patch, needs review] twisted.conch.ssh deprecated functions

Issue created by migration from Trac.

Original creator: yi

Original creation time: 2008-04-07 00:11:07

Assignee: yi

Patch attached which uses the new twisted.conch.ssh.keys.Key object instead of the old helper functions. If we don't apply this patch we'll get a bunch of annoying deprecated API warnings :-) 


---

Attachment


---

Comment by mhansen created at 2008-04-07 01:03:00

Looks good to me.  Passes on alpha1 + new twisted spkg.


---

Comment by mabshoff created at 2008-04-07 01:22:00

Resolution: fixed


---

Comment by mabshoff created at 2008-04-07 01:22:00

Merged in Sage 3.0.alpha2
