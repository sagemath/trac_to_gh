# Issue 2944: [with patch, needs review] add E2 parameter to padic_height_via_multiply

Issue created by migration from https://trac.sagemath.org/ticket/2944

Original creator: dmharvey

Original creation time: 2008-04-16 22:32:27

Assignee: was

This patch adds an optional E2 parameter to `padic_height_via_multiply`. The idea is to make it possible to use a precomputed value of E2. Since the E2 computation is very expensive relative to the p-adic height computation, this makes it easier to do profiling work on the p-adic height portion of the computation.



---

Attachment


---

Comment by ncalexan created at 2008-04-17 05:12:24

Fine by me.


---

Comment by mabshoff created at 2008-04-17 06:13:04

Resolution: fixed


---

Comment by mabshoff created at 2008-04-17 06:13:04

Merged in Sage 3.0.alpha6
