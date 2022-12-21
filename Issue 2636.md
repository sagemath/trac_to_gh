# Issue 2636: notebook -- changing a cell without evaluate should put the red line back to the left

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-03-21 19:27:08

Assignee: boothby

If you enter text in a cell but do *not* evaluate, then move the cursor out of the cell, the red line to the left should be put back, to emphasize that the cell has not been evaluated. 


---

Attachment

this fixes the bug


---

Comment by was created at 2008-05-10 20:28:02

This is a very simple/short patch.


---

Comment by was created at 2008-05-10 20:32:06

WARNING: This patch might depend on the one for #336.


---

Comment by boothby created at 2008-05-12 05:44:58

Excellent!


---

Comment by mabshoff created at 2008-05-12 10:59:25

Merged in Sage 3.0.2.alpha1


---

Comment by mabshoff created at 2008-05-12 10:59:25

Resolution: fixed
