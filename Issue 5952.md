# Issue 5952: Worksheet downloading blocks the entire server

Issue created by migration from https://trac.sagemath.org/ticket/5952

Original creator: robertwb

Original creation time: 2009-05-01 04:58:18

Assignee: tbd

#2740 is great to have, but we need to have a way to disable it, at least on the public server, until the blocking issue gets resolved


---

Attachment

When accounts=True, downloading is disabled.


---

Comment by mabshoff created at 2009-05-04 05:28:19

The patch applies, reads good and passes doctests, but I would prefer if someone with more knowledge about the notebook would take this for a spin also.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-04 10:05:19

Positive review. Works as advertised and passes doctests.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-04 10:12:04

Merged in Sage 3.4.2.final.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-04 10:12:04

Resolution: fixed


---

Comment by mabshoff created at 2009-05-04 10:12:28

And this ain't algebra, so fix it.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-04 10:12:28

Changing component from algebra to notebook.
