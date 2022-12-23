# Issue 2580: [with patch, needs review] Implement backends for graphs

Issue created by migration from https://trac.sagemath.org/ticket/2580

Original creator: rlm

Original creation time: 2008-03-18 01:56:35

Assignee: rlm

This abstracts the layer between NetworkX and Sage.


---

Attachment


---

Attachment

Make sure to apply both patches before building. :)


---

Comment by rlm created at 2008-03-18 02:10:10

Also,
`./sage -t -long sage/graphs`
passes all tests after these patches...


---

Comment by mhansen created at 2008-03-18 10:34:37

Applies, passes tests, and looks good to me.  I'm not too concerned about the doctests in the new file.


---

Comment by mabshoff created at 2008-03-18 11:04:05

Resolution: fixed


---

Comment by mabshoff created at 2008-03-18 11:04:05

Merged in Sage 2.11.alpha0
