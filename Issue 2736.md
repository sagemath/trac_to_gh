# Issue 2736: [with patch, needs review] fix for dsage doctest failures in sage-2.11.rc0

Issue created by migration from https://trac.sagemath.org/ticket/2736

Original creator: yi

Original creation time: 2008-03-30 21:45:12

Assignee: yi

Attached is a patch which fixes the annoying exceptions thrown by the doctest runner at the end of the dsage doctests. 

This patch does the following:
1) Explicitly call .wait() on subprocess.Popen instances
2) Explicitly delete the reference to the Popen instances before letting the interpreter exit
3) Explicitly join the dsage thread before letting the interpreter exit in the doctest.


---

Attachment

Tested on OS X.


---

Comment by mabshoff created at 2008-03-30 22:05:41

Resolution: fixed


---

Comment by mabshoff created at 2008-03-30 22:05:41

Merged in Sage 2.11.final
