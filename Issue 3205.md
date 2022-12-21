# Issue 3205: when the notebook scrolls to a new cell that is created, the jsmath box obscures the bottom cell

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-05-14 21:55:56

Assignee: boothby

When scrolling through the notebook with the cursor keys (i.e., moving from cell to cell), if you move to a cell below the currently visible ones, the browser automatically scrolls down to let you see the new cell, but the jsmath box is sitting right there at the start of the cell, so you can't see what is in the start of the cell.

Fix 1: scroll a bit more than we do now

Fix 2: move the jsmath box to the bottom right instead of the bottom left

Fix 3: Get rid of the jsmath box and instead just make a menu option or some other way to access the jsmath controls.  Once the jsmath controls are set, they are very rarely accessed, at least for me.



---

Attachment


---

Comment by boothby created at 2008-06-15 00:32:28

Works for me in FF and Opera.  Need review from IE / Safari.


---

Comment by craigcitro created at 2008-06-15 21:43:49

Changing keywords from "" to "editor_mhansen".


---

Comment by mhansen created at 2008-06-19 19:58:23

I tested this in IE and Safari and everything looks good.


---

Comment by mabshoff created at 2008-06-23 12:55:15

Merged in Sage 3.0.4.alpha0


---

Comment by mabshoff created at 2008-06-23 12:55:15

Resolution: fixed
