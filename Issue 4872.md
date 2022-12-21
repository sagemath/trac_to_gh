# Issue 4872: [with patch; needs review] latex typesetting using dvipng is broken on OS X unless unless one uses the dvipng spkg; also the optional filename argument is broken if the file isn't in the current directory; finally, there area  lot of dangerous tmp files created in the current directory

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-12-24 18:12:42

Assignee: cwitty




---

Attachment


---

Comment by abergeron created at 2008-12-25 04:31:31

This works as advertised.

The no space thing bothers me but is non-trivial to fix so it can stay as-is for now.


---

Comment by mabshoff created at 2008-12-26 22:50:59

Merged in Sage 3.2.3.final


---

Comment by mabshoff created at 2008-12-26 22:50:59

Resolution: fixed
