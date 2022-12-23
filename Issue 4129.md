# Issue 4129: [with patch, needs review] add support for ntl.mat_GF2

Issue created by migration from https://trac.sagemath.org/ticket/4129

Original creator: malb

Original creation time: 2008-09-15 18:42:12

Assignee: was

We wrapped `ntl.GF2` so there is no reason not to wrap `ntl.mat_GF2`. Also, I needed it for comparison.


---

Attachment


---

Comment by malb created at 2008-09-20 15:59:44

Changing status from new to assigned.


---

Comment by malb created at 2008-09-20 15:59:44

Changing assignee from was to malb.


---

Comment by robertwb created at 2008-09-24 05:09:19

I've tested it out and it works well for me. Code is nice and clean and fully doctested.


---

Comment by mabshoff created at 2008-09-24 06:41:16

Resolution: fixed


---

Comment by mabshoff created at 2008-09-24 06:41:16

Merged in Sage 3.1.3.alpha1
