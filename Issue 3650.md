# Issue 3650: [with patch, needs review] Infinite recursion in pbuild by recursive pxd imports

Issue created by migration from Trac.

Original creator: gfurnish

Original creation time: 2008-07-13 11:22:50

Assignee: gfurnish

In some cases, having pxds with recursive imports may cause pbuild to use recursion to go to infinity.  This patch fixes this issue.  In many cases this will just cause Cython to throw an error later, but pbuild should still behave better.


---

Attachment


---

Comment by mabshoff created at 2008-07-15 23:37:50

Positive review. What could go wrong? ;)

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-15 23:38:02

Resolution: fixed


---

Comment by mabshoff created at 2008-07-15 23:38:02

Merged in Sage 3.0.6.alpha0
