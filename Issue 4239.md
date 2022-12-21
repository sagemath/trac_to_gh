# Issue 4239: [with patch, needs review] fix for problems with zero kernel and images

Issue created by migration from Trac.

Original creator: fwclarke

Original creation time: 2008-10-03 07:17:57

Assignee: tbd

Keywords: kernel, image

Computation of kernels and images of linear transformations over `GF(p)` (`p` odd) and `CC` fails when the result is zero.
The patch solves the problem by adjusting `FreeModule_submodule_with_basis_pid` so that a `tuple` of generators gets changed into a `list` (something that happens anyway if `check == True`).  New doctests have been included.


---

Attachment

Thumbs up!

Letting the new doctests run without the patch shows horrible behaviour indeed.

Please get this patch into 3.1.3.


---

Comment by mabshoff created at 2008-10-07 21:00:14

Merged in Sage 3.1.3.alpha3


---

Comment by mabshoff created at 2008-10-07 21:00:14

Resolution: fixed
