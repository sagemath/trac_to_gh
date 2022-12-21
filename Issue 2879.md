# Issue 2879: [with patch, needs review] Bug fix in totallyreal_rel

Issue created by migration from Trac.

Original creator: jvoight

Original creation time: 2008-04-11 18:09:32

Assignee: citro

There was an bug in the enumeration of relative totally real fields: if the extension was constant (coming from Q), it was ignored by a resultant calculation.  Also, some exceptional cases were unintentionally ignored.  The fix is attached.


---

Attachment


---

Attachment


---

Comment by craigcitro created at 2008-04-15 10:48:38

Patch looks good. I'm attaching a new version of the patch, since I had merge troubles.


---

Attachment


---

Comment by mabshoff created at 2008-04-15 10:57:54

Resolution: fixed


---

Comment by mabshoff created at 2008-04-15 10:57:54

Merged trac-2879.patch in Sage 3.0.alpha5
