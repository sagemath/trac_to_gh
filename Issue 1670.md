# Issue 1670: jmol / 3d -- my latest bundle

Issue created by migration from https://trac.sagemath.org/ticket/1670

Original creator: was

Original creation time: 2008-01-03 16:06:53

Assignee: was

Hi,

This is the latest 3d bundle.

There will still be some doctest failures in 3d -- just put nodoctest in the files.

This can be included in Sage, but much work remains before it is released. 


---

Attachment


---

Attachment


---

Attachment

Figured out how to display text in jmol, got rid of logo, implemented "ruler" function for displaying tick marks, ...


---

Attachment


---

Attachment

This replaces one of the same name and merges cleanly (but doctests will fail)


---

Comment by mabshoff created at 2008-01-04 11:15:12

Resolution: fixed


---

Comment by mabshoff created at 2008-01-04 11:15:12

Merged jmol-jan4.hg into 2.9.2.rc0, resolved some small merge conflict introduced #1671. Loads of doctests will fail, but William has assured me that those will be fixed tomorrow.

Cheers,

Michael
