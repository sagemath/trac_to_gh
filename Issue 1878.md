# Issue 1878: [with patch] add new function from mpfr-2.3.0

Issue created by migration from Trac.

Original creator: zimmerma

Original creation time: 2008-01-21 07:12:06

Assignee: somebody

This patch completes #1716. Some new functions are added, also some functions already available
in SAGE are replaced by their exact mpfr flavour. For example sec(x) was defined as 1/cos(x),
it now calls directly mpfr_sec.


---

Attachment


---

Comment by ncalexan created at 2008-01-21 20:06:42

Excellent docs and tests.  Apply.


---

Comment by mabshoff created at 2008-01-21 23:55:02

Resolution: fixed


---

Comment by mabshoff created at 2008-01-21 23:55:02

Merged in Sage 2.10.1.alpha1
