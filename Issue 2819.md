# Issue 2819: edge_style option for directed graphs

Issue created by migration from https://trac.sagemath.org/ticket/2819

Original creator: jason

Original creation time: 2008-04-06 03:46:46

Assignee: rlm

This adds an edge_style option for passing options to the arrow() command that draws edges of directed graphs.  It is a (small) step towards #2817.  In order for more to be done, we have to write graph-drawing (really, vertex and edge-drawing) code, since now we just pass everything off to networkx.



---

Attachment


---

Comment by mhansen created at 2008-04-06 04:50:47

Looks good to me.


---

Comment by mabshoff created at 2008-04-06 05:06:06

Resolution: fixed


---

Comment by mabshoff created at 2008-04-06 05:06:06

Merged in Sage 3.0.alpha2
