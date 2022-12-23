# Issue 5708: [with patch; needs review] solaris -- fix heilbronn.pyx (it turns out that our roundf is wrong)

Issue created by migration from https://trac.sagemath.org/ticket/5708

Original creator: was

Original creation time: 2009-04-08 00:24:34

Assignee: craigcitro




---

Attachment


---

Comment by mabshoff created at 2009-04-09 05:53:20

Positive review. The faulty roundf() substitute was for Solaris 9 and my fault :(

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-09 06:09:57

Merged in Sage 3.4.1.rc2.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-09 06:09:57

Resolution: fixed
