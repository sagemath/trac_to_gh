# Issue 6086: [with patch, needs review] fixed laplacian_matrix in graph.py

Issue created by migration from Trac.

Original creator: dperkinson

Original creation time: 2009-05-19 19:51:13

Assignee: dperkinson

CC:  ekirkman

Keywords: kirchhoff laplacian matrix

The kirchhoff_matrix/laplacian_matrix did not handle graphs with loops correctly.

The patch fixes the bug and adds a doctest that fails without the patch.


---

Attachment


---

Comment by ekirkman created at 2009-05-19 20:13:27

Passes doctests and fixes bug.  Good job!


---

Comment by mabshoff created at 2009-05-19 20:24:54

Resolution: fixed


---

Comment by mabshoff created at 2009-05-19 20:24:54

Merged in Sage 4.0.rc0.

Cheers,

Michael
