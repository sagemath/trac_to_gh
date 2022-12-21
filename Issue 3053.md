# Issue 3053: notebook -- new cell_resize doesn't respect %hide at the beginning of a cell

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-04-29 06:23:58

Assignee: boothby

If a cell starts with %hide, it should not be shown unless it is in focus.  The new cell_resize code doesn't respect this.  To see this:

1. Load a fresh worksheet with %hide's -- none of them are hidden.  Click on input cells then out  hide them.

2. Resize a web browser window with %hides -- suddenly all %hide inputs are shown.


---

Attachment


---

Comment by was created at 2008-05-11 01:59:27

Attached patch does this:

trac #3053 --  new cell_resize doesn't respect %hide at the beginning of a cell
  1. Fix the listed problem. 
  2. Fix the %hide styling a bit; make %hide be grey
  3. Make %hide work consistently on new page refresh versus in a running worksheet
  4. Make cell be resized when clicking on an input area.  This makes editing
     a %hide much more natural.


---

Comment by boothby created at 2008-05-12 06:01:27

nice!


---

Comment by mabshoff created at 2008-05-12 11:06:35

Merged in Sage 3.0.2.alpha1


---

Comment by mabshoff created at 2008-05-12 11:06:35

Resolution: fixed
