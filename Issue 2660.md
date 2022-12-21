# Issue 2660: copy work around stdint.h on Solaris 9

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-03-24 12:40:10

Assignee: mabshoff

Solaris 9 only supports a draft standard of the C99 spec, so it is missing stdint.h. This patch adds a workaround fix that for now is 32 bits only.



---

Comment by mabshoff created at 2008-03-24 12:42:39

Changing status from new to assigned.


---

Attachment


---

Comment by jkantor created at 2008-03-24 12:57:18

Patch applies cleanly. Looked at the changes, seems good. Not tested since it is sun only.


---

Comment by mabshoff created at 2008-03-24 12:58:42

Resolution: fixed


---

Comment by mabshoff created at 2008-03-24 12:58:42

Merged in Sage 2.11.alpha2
