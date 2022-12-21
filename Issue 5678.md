# Issue 5678: LaTeX typesetting for two letters phi and Phi

Issue created by migration from Trac.

Original creator: gmhossain

Original creation time: 2009-04-04 01:34:08

Assignee: cwitty

Keywords: Latex,

In the list "common_varnames" (in sage/misc/latex.py) two
Greek letters "phi" and "Phi" are missing. So LaTeX typesetting
for them doesn't work unlike other Greek letters.

This issue has been discussed in the thread

http://groups.google.com/group/sage-devel/browse_thread/thread/a51f269f057d8223

A patch (created on top of sage-3.4) to fix this issue is attached.


---

Attachment


---

Comment by jhpalmieri created at 2009-04-06 23:06:01

Looks good to me: a trivial fix.

(gmhossain: your subject should have been: "[with patch, needs review] LaTeX typesetting for two letters phi and Phi")


---

Comment by mabshoff created at 2009-04-09 09:42:51

Resolution: fixed


---

Comment by mabshoff created at 2009-04-09 09:42:51

Merged in Sage 3.4.1.rc2.

Cheers,

Michael
